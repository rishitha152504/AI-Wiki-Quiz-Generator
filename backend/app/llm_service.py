"""
LLM service using LangChain and Groq API
Generates quiz questions and related topics from Wikipedia article content
"""
import os
from typing import List, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import json


class LLMQuizGenerator:
    """Generate quiz questions using LLM"""

    def __init__(self, api_key: str):
        # Available Groq models:
        # - llama-3.1-8b-instant (fast, recommended)
        # - llama-3.1-70b-versatile (higher quality)
        # - mixtral-8x7b-32768 (good balance)
        # - gemma2-9b-it (alternative)
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",  # Fast and reliable
            groq_api_key=api_key,
            temperature=0.7
        )

    def generate_quiz(self, article_title: str, article_content: str, sections: List[str]) -> Dict:
        """
        Generate quiz questions and related topics from article content
        
        Returns:
            Dictionary with 'quiz' (list of questions) and 'related_topics' (list)
        """
        # Prompt template for quiz generation
        quiz_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert quiz generator. Generate high-quality quiz questions based on the provided Wikipedia article content.

Requirements:
1. Generate 5-10 questions (aim for 7-8 questions)
2. Each question must have exactly 4 options (A, B, C, D)
3. Include one correct answer and three plausible distractors
4. Assign difficulty levels: easy, medium, or hard
5. Provide a short explanation (1-2 sentences) for each answer
6. Questions should cover different sections of the article
7. Ensure questions are factual and can be answered from the provided content
8. Avoid questions that require external knowledge not in the article

Output format (JSON):
{{
  "quiz": [
    {{
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Correct answer text",
      "difficulty": "easy|medium|hard",
      "explanation": "Brief explanation of why this is correct"
    }}
  ],
  "related_topics": ["Topic 1", "Topic 2", "Topic 3"]
}}

Important: Return ONLY valid JSON, no additional text before or after."""),
            ("human", """Article Title: {title}

Article Sections: {sections}

Article Content:
{content}

Generate a quiz based on this article. Return the JSON response as specified.""")
        ])

        # Format the prompt
        formatted_prompt = quiz_prompt.format_messages(
            title=article_title,
            sections=", ".join(sections) if sections else "No specific sections",
            content=article_content[:6000]  # Limit content to avoid token limits
        )

        try:
            # Call LLM
            response = self.llm.invoke(formatted_prompt)
            
            # Extract JSON from response
            response_text = response.content.strip()
            
            # Try to parse JSON (handle markdown code blocks if present)
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            result = json.loads(response_text)
            
            # Validate and clean the result
            quiz = result.get("quiz", [])
            related_topics = result.get("related_topics", [])
            
            # Ensure quiz has required fields
            validated_quiz = []
            for q in quiz:
                if all(key in q for key in ["question", "options", "answer", "difficulty", "explanation"]):
                    if len(q["options"]) == 4:
                        validated_quiz.append(q)
            
            return {
                "quiz": validated_quiz[:10],  # Limit to 10 questions
                "related_topics": related_topics[:5]  # Limit to 5 topics
            }
            
        except json.JSONDecodeError as e:
            # Fallback: return minimal quiz if JSON parsing fails
            print(f"JSON parsing error: {e}")
            return {
                "quiz": [{
                    "question": f"What is the main topic of the article about {article_title}?",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "answer": article_title,
                    "difficulty": "medium",
                    "explanation": "Based on the article title and content."
                }],
                "related_topics": []
            }
        except Exception as e:
            error_msg = str(e)
            print(f"LLM generation error: {error_msg}")
            
            # Provide helpful error messages for common issues
            if "API key not valid" in error_msg or "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
                raise ValueError(
                    "Invalid Groq API key. Please check your .env file and ensure "
                    "GROQ_API_KEY is set correctly. Get your free key from: "
                    "https://console.groq.com/keys"
                )
            elif "not found" in error_msg.lower() and "model" in error_msg.lower():
                raise ValueError(
                    f"Model not found error: {error_msg}. "
                    "Available Groq models: llama-3.1-8b-instant, llama-3.1-70b-versatile, "
                    "mixtral-8x7b-32768, gemma2-9b-it"
                )
            elif "quota" in error_msg.lower() or "QUOTA" in error_msg or "rate limit" in error_msg.lower() or "429" in error_msg:
                raise ValueError(
                    "API quota/rate limit exceeded. This can happen if:\n"
                    "1. You've exceeded the free tier limit\n"
                    "2. You've hit the daily quota limit\n"
                    "3. Too many requests in a short time\n\n"
                    "Solutions:\n"
                    "- Wait 1-2 minutes and try again\n"
                    "- Check your usage at: https://console.groq.com/usage\n"
                    "- Try using a different article (cached articles don't use API)\n"
                    "- Groq free tier is generous, wait a few minutes and retry"
                )
            else:
                raise ValueError(f"Failed to generate quiz: {error_msg}")
