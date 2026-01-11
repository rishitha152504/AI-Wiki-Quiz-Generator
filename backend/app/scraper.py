"""
Wikipedia article scraper using BeautifulSoup
Extracts title, summary, sections, and key entities from Wikipedia articles
"""
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
import re


class WikipediaScraper:
    """Scrape and extract content from Wikipedia articles"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape_article(self, url: str) -> Dict:
        """
        Scrape Wikipedia article and extract structured data
        
        Returns:
            Dictionary containing:
            - title: Article title
            - summary: First paragraph summary
            - sections: List of section headings
            - key_entities: Dictionary with people, organizations, locations
            - raw_html: Full HTML content
            - content_text: Clean text content for LLM
        """
        try:
            # Clean and validate URL
            url = url.strip()  # Remove whitespace
            
            # Validate URL format - more flexible
            if not url.startswith('https://en.wikipedia.org/wiki/'):
                # Try to fix common issues
                if url.startswith('http://en.wikipedia.org/wiki/'):
                    url = url.replace('http://', 'https://')
                elif url.startswith('en.wikipedia.org/wiki/'):
                    url = 'https://' + url
                elif url.startswith('www.en.wikipedia.org/wiki/'):
                    url = url.replace('www.en.wikipedia.org', 'en.wikipedia.org')
                    url = 'https://' + url if not url.startswith('https://') else url
                else:
                    raise ValueError(
                        f"URL must be a valid English Wikipedia article URL. "
                        f"Received: {url}. "
                        f"Example: https://en.wikipedia.org/wiki/Alan_Turing"
                    )

            # Fetch the page with better headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
            }
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
            
            # Check if we got valid HTML
            if not response.text or len(response.text) < 1000:
                raise ValueError("Received invalid or empty response from Wikipedia")
            
            # Debug: Print response length
            print(f"Fetched {len(response.text)} characters from Wikipedia")

            # Parse HTML
            soup = BeautifulSoup(response.text, 'lxml')
            raw_html = response.text

            # Check for disambiguation pages
            disambiguation_indicators = [
                soup.find('div', id='disambigbox'),
                soup.find('div', class_='dablink'),
                soup.find('table', class_='dablink'),
                soup.find('div', id='disambiguation'),
            ]
            
            # Check title for disambiguation
            title_element = soup.find('h1', class_='firstHeading')
            title_text = title_element.get_text() if title_element else ""
            
            # Check if it's a disambiguation page
            is_disambiguation = (
                any(disambiguation_indicators) or 
                'disambiguation' in title_text.lower() or
                soup.find('div', class_=lambda x: x and 'dab' in ' '.join(x).lower() if isinstance(x, list) else 'dab' in str(x).lower())
            )
            
            if is_disambiguation:
                raise ValueError(
                    f"This is a disambiguation page (lists multiple topics with the same name). "
                    f"Please use a specific article URL instead. "
                    f"\n\nExample: Instead of 'https://en.wikipedia.org/wiki/Python', "
                    f"use 'https://en.wikipedia.org/wiki/Python_(programming_language)' "
                    f"or 'https://en.wikipedia.org/wiki/Pythonidae'"
                    f"\n\nExample: Instead of 'https://en.wikipedia.org/wiki/Java', "
                    f"use 'https://en.wikipedia.org/wiki/Java_(programming_language)' "
                    f"or 'https://en.wikipedia.org/wiki/Java_(island)'"
                )

            # Extract title
            title = soup.find('h1', class_='firstHeading')
            title = title.text.strip() if title else "Unknown Title"

            # Extract summary (first paragraph)
            summary_paragraph = soup.find('div', class_='mw-parser-output')
            summary = ""
            if summary_paragraph:
                # Try to find first meaningful paragraph
                for p in summary_paragraph.find_all('p', recursive=True):
                    # Check if paragraph is in unwanted containers
                    parent = p.parent
                    in_unwanted = False
                    depth = 0
                    while parent and depth < 5:
                        parent_classes = parent.get('class', [])
                        if any(x in str(parent_classes).lower() for x in ['infobox', 'navbox', 'thumb', 'toc', 'hatnote', 'reflist']):
                            in_unwanted = True
                            break
                        parent = parent.parent
                        depth += 1
                    
                    if not in_unwanted:
                        text = p.get_text().strip()
                        # Get first substantial paragraph (longer than 50 chars)
                        if len(text) > 50:
                            summary = text
                            break
                
                # Fallback: get any first paragraph
                if not summary:
                    first_p = summary_paragraph.find('p')
                    if first_p:
                        summary = first_p.get_text().strip()
                        # Clean up common Wikipedia artifacts
                        summary = re.sub(r'\[.*?\]', '', summary)  # Remove citations
                        summary = summary.strip()

            # Extract sections
            sections = []
            content_div = soup.find('div', class_='mw-parser-output')
            if content_div:
                for heading in content_div.find_all(['h2', 'h3']):
                    # Try multiple methods to get section text
                    section_text = None
                    
                    # Method 1: Look for span with mw-headline class
                    span = heading.find('span', class_='mw-headline')
                    if span:
                        section_text = span.get_text().strip()
                    else:
                        # Method 2: Get text directly from heading
                        section_text = heading.get_text().strip()
                        # Remove edit links and other noise
                        section_text = re.sub(r'\[edit\]', '', section_text).strip()
                    
                    if section_text:
                        # Skip common non-content sections
                        skip_sections = ['contents', 'see also', 'references', 'external links', 
                                        'notes', 'bibliography', 'navigation menu', 'edit']
                        if section_text.lower() not in skip_sections and len(section_text) > 1:
                            sections.append(section_text)

            # Extract key entities (simplified extraction)
            key_entities = self._extract_entities(soup)

            # Extract clean text content for LLM
            content_text = self._extract_text_content(soup)

            return {
                'title': title,
                'summary': summary,
                'sections': sections,
                'key_entities': key_entities,
                'raw_html': raw_html,
                'content_text': content_text
            }

        except requests.RequestException as e:
            error_msg = f"Failed to fetch Wikipedia article: {str(e)}"
            print(f"Scraping error: {error_msg}")
            raise ValueError(error_msg)
        except Exception as e:
            error_msg = f"Error scraping article: {str(e)}"
            print(f"Scraping error: {error_msg}")
            import traceback
            traceback.print_exc()
            raise ValueError(error_msg)

    def _extract_entities(self, soup: BeautifulSoup) -> Dict[str, List[str]]:
        """Extract key entities from the article"""
        entities = {
            'people': [],
            'organizations': [],
            'locations': []
        }

        # Extract from infobox
        infobox = soup.find('table', class_='infobox')
        if infobox:
            # Look for common entity patterns in infobox
            for row in infobox.find_all('tr'):
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    label = th.get_text().strip().lower()
                    value = td.get_text().strip()
                    
                    if 'born' in label or 'died' in label:
                        # Extract location from birth/death info
                        location_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', value)
                        if location_match:
                            entities['locations'].append(location_match.group(1))
                    
                    if 'alma mater' in label or 'education' in label:
                        entities['organizations'].extend(
                            [v.strip() for v in value.split(',') if v.strip()]
                        )

        # Extract from categories (people, organizations, locations)
        categories = soup.find('div', id='mw-normal-catlinks')
        if categories:
            for link in categories.find_all('a'):
                cat_text = link.get_text().lower()
                if 'people' in cat_text or 'person' in cat_text:
                    # Try to extract person name from article title
                    title = soup.find('h1', class_='firstHeading')
                    if title:
                        entities['people'].append(title.get_text().strip())

        return entities

    def _extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract clean text content from article for LLM processing"""
        # Try multiple selectors in order of preference
        content_div = None
        
        # Method 1: Standard Wikipedia content div
        content_div = soup.find('div', class_='mw-parser-output')
        
        # Method 2: Alternative Wikipedia structure
        if not content_div:
            content_div = soup.find('div', id='bodyContent')
        
        # Method 3: Generic content div
        if not content_div:
            content_div = soup.find('div', id='content')
        
        # Method 4: Main content area
        if not content_div:
            main_content = soup.find('main')
            if main_content:
                content_div = main_content
        
        # Method 5: Article tag
        if not content_div:
            article_tag = soup.find('article')
            if article_tag:
                content_div = article_tag
        
        # Method 6: Last resort - find any div with substantial content
        if not content_div:
            # Try to find div with most paragraphs
            all_divs = soup.find_all('div')
            max_paragraphs = 0
            for div in all_divs:
                p_count = len(div.find_all('p'))
                if p_count > max_paragraphs and p_count > 5:
                    max_paragraphs = p_count
                    content_div = div
        
        if not content_div:
            print("Warning: Could not find content div, trying to extract from body")
            content_div = soup.find('body')
        
        if not content_div:
            return ""

        # Get text from paragraphs directly (more reliable)
        text_parts = []
        
        # Find all paragraphs in the content div
        paragraphs = content_div.find_all('p')
        
        # Also try to get text from divs that might contain content
        content_divs = content_div.find_all('div', class_=lambda x: x and 'mw-content' in ' '.join(x) if isinstance(x, list) else 'mw-content' in str(x))
        
        if not paragraphs:
            # If no paragraphs found, try to get text directly
            all_text = content_div.get_text(separator='\n', strip=True)
            all_text = re.sub(r'\[.*?\]', '', all_text)  # Remove citations
            lines = [line.strip() for line in all_text.split('\n') 
                    if line.strip() and len(line.strip()) > 50]
            text_parts = lines[:50]  # Get first 50 meaningful lines
        else:
            for p in paragraphs:
                # Skip paragraphs that are in unwanted containers
                skip = False
                parent = p.parent
                depth = 0
                while parent and depth < 5:
                    parent_classes = parent.get('class', [])
                    parent_id = parent.get('id', '')
                    parent_str = ' '.join([str(parent_classes), str(parent_id)]).lower()
                    
                    # Skip navigation, infoboxes, sidebars, etc.
                    if any(x in parent_str for x in ['infobox', 'navbox', 'reflist', 'thumb', 'toc', 'hatnote', 'mw-jump', 'sidebar', 'navigation', 'mw-editsection', 'coordinates', 'metadata', 'ambox', 'dablink', 'disambig']):
                        skip = True
                        break
                    parent = parent.parent
                    depth += 1
                
                if not skip:
                    text = p.get_text().strip()
                    # Clean up citations and references
                    text = re.sub(r'\[.*?\]', '', text)  # Remove [1], [citation needed], etc.
                    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
                    # Get meaningful paragraphs (longer than 30 chars, but not too short)
                    if text and len(text) > 30 and len(text) < 5000:  # Avoid extremely long paragraphs
                        text_parts.append(text)
        
        # If we still don't have enough content, try extracting from list items (for structured pages)
        if len(text_parts) < 3:
            list_items = content_div.find_all('li')
            for li in list_items[:20]:  # Limit to first 20 list items
                text = li.get_text().strip()
                text = re.sub(r'\[.*?\]', '', text)
                text = re.sub(r'\s+', ' ', text)
                if text and len(text) > 50 and len(text) < 1000:
                    # Check if it's not in a navigation box
                    parent_str = ' '.join([str(li.parent.get('class', [])), str(li.parent.get('id', ''))]).lower()
                    if 'navbox' not in parent_str and 'sidebar' not in parent_str:
                        text_parts.append(text)
        
        # If we still don't have enough content, try getting text directly from content_div
        if len(text_parts) < 3:
            # Get all text from content div, but clean it
            all_text = content_div.get_text(separator='\n', strip=True)
            # Remove citations and clean up
            all_text = re.sub(r'\[.*?\]', '', all_text)
            all_text = re.sub(r'\s+', ' ', all_text)  # Normalize whitespace
            # Split into sentences/paragraphs
            lines = [line.strip() for line in all_text.split('\n') 
                    if line.strip() and len(line.strip()) > 50]
            if lines:
                text_parts = lines[:50]  # Limit to first 50 meaningful lines
        
        text_content = '\n\n'.join(text_parts)

        # Limit content length to avoid token limits (keep first 10000 characters for better context)
        result = text_content[:10000] if text_content else ""
        
        # Debug: Print extraction info
        if not result or len(result) < 100:
            print(f"Warning: Insufficient content extracted. Found {len(paragraphs)} paragraphs, {len(text_parts)} text parts")
            # Last resort: try to get ANY text from the page, excluding navigation
            if content_div:
                # Remove navigation and sidebar elements first
                for nav in content_div.find_all(['nav', 'div'], class_=lambda x: x and any(y in ' '.join(x).lower() for y in ['nav', 'sidebar', 'toc', 'infobox'])):
                    nav.decompose()
                
                all_text = content_div.get_text(separator=' ', strip=True)
                all_text = re.sub(r'\[.*?\]', '', all_text)  # Remove citations
                all_text = re.sub(r'\s+', ' ', all_text)  # Normalize whitespace
                # Remove common Wikipedia boilerplate
                all_text = re.sub(r'Jump to.*?hide', '', all_text, flags=re.IGNORECASE)
                all_text = re.sub(r'Main menu.*?hide', '', all_text, flags=re.IGNORECASE)
                
                if len(all_text) > 100:
                    result = all_text[:10000]
                    print(f"Extracted {len(result)} characters using fallback method")
        
        print(f"Final extracted content length: {len(result)} characters")
        
        # Final validation - check if result is meaningful
        if len(result) < 100:
            raise ValueError(
                f"Unable to extract sufficient content from this Wikipedia page. "
                f"This might be a disambiguation page, redirect page, or a page with very little content. "
                f"Please try a different article URL. "
                f"Extracted only {len(result)} characters."
            )
        
        return result
