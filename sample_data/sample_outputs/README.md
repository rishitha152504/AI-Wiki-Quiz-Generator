# Sample API Outputs

This folder contains example JSON responses from the API for different Wikipedia articles.

## Structure

Each sample file follows the naming convention: `{article_title_slug}.json`

Example: `alan_turing.json`, `quantum_computing.json`

## Output Format

All outputs follow the same structure as defined in the API documentation:

```json
{
  "id": 1,
  "url": "https://en.wikipedia.org/wiki/Article_Title",
  "title": "Article Title",
  "summary": "First paragraph summary...",
  "key_entities": {
    "people": [],
    "organizations": [],
    "locations": []
  },
  "sections": ["Section 1", "Section 2"],
  "quiz": [
    {
      "question": "Question text?",
      "options": ["A", "B", "C", "D"],
      "answer": "Correct answer",
      "difficulty": "easy|medium|hard",
      "explanation": "Explanation text"
    }
  ],
  "related_topics": ["Topic 1", "Topic 2"]
}
```

## Generating Sample Data

To generate sample outputs:

1. Start the backend server
2. Use the API to generate quizzes for URLs in `example_urls.txt`
3. Save the JSON responses to this folder
4. Name files appropriately (e.g., `alan_turing.json`)

## Notes

- Actual outputs may vary due to LLM generation
- Questions and related topics are generated dynamically
- Entity extraction may differ based on article structure
- Quiz difficulty distribution may vary
