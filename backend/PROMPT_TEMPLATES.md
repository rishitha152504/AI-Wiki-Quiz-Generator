# LangChain Prompt Templates Documentation

This document describes the prompt templates used for quiz generation in the Wiki Quiz App.

## Overview

The quiz generation system uses LangChain's `ChatPromptTemplate` to structure prompts for the Google Gemini API. The prompts are designed to:

1. Generate high-quality, factual quiz questions
2. Minimize hallucination by grounding questions in article content
3. Ensure consistent output format (JSON)
4. Create diverse questions across article sections
5. Assign appropriate difficulty levels

## Prompt Structure

### System Message

The system message defines the role and requirements:

```
You are an expert quiz generator. Generate high-quality quiz questions based on the provided Wikipedia article content.

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
{
  "quiz": [
    {
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Correct answer text",
      "difficulty": "easy|medium|hard",
      "explanation": "Brief explanation of why this is correct"
    }
  ],
  "related_topics": ["Topic 1", "Topic 2", "Topic 3"]
}

Important: Return ONLY valid JSON, no additional text before or after.
```

### Human Message Template

The human message provides the article content:

```
Article Title: {title}

Article Sections: {sections}

Article Content:
{content}

Generate a quiz based on this article. Return the JSON response as specified.
```

## Prompt Design Principles

### 1. Content Grounding
- **Principle**: Questions must be answerable from provided content
- **Implementation**: Explicit instruction to avoid external knowledge
- **Result**: Reduces hallucination and ensures factual accuracy

### 2. Output Format Control
- **Principle**: Consistent JSON structure for parsing
- **Implementation**: Detailed JSON schema in system message
- **Result**: Reliable parsing and structured data

### 3. Question Diversity
- **Principle**: Cover different sections of the article
- **Implementation**: Instruction to distribute questions across sections
- **Result**: Comprehensive quiz coverage

### 4. Difficulty Distribution
- **Principle**: Mix of easy, medium, and hard questions
- **Implementation**: Explicit difficulty level requirement
- **Result**: Appropriate challenge levels

### 5. Plausible Distractors
- **Principle**: Wrong answers should be believable
- **Implementation**: Instruction for "plausible distractors"
- **Result**: More challenging and educational quizzes

## Content Truncation

To manage token limits:
- Article content is truncated to 6000 characters
- This ensures the prompt stays within API limits
- First paragraphs (most important) are prioritized

## Error Handling

If JSON parsing fails:
- Fallback quiz with a single generic question
- Error logged for debugging
- User receives a basic quiz instead of an error

## Optimization Strategies

### Current Optimizations

1. **Token Management**: Content truncation to 6000 chars
2. **Temperature Setting**: 0.7 for balanced creativity/consistency
3. **Model Selection**: Gemini Pro for quality and free tier
4. **Structured Output**: JSON format for reliable parsing

### Potential Improvements

1. **Few-shot Examples**: Add example questions in prompt
2. **Section-specific Prompts**: Generate questions per section
3. **Difficulty Calibration**: Use article complexity to guide difficulty
4. **Entity-based Questions**: Generate questions about extracted entities

## Example Prompt Execution

### Input
- Title: "Alan Turing"
- Sections: ["Early life", "World War II", "Legacy"]
- Content: "Alan Turing was a British mathematician..." (truncated)

### Expected Output
```json
{
  "quiz": [
    {
      "question": "Where did Alan Turing study?",
      "options": ["Harvard University", "Cambridge University", "Oxford University", "Princeton University"],
      "answer": "Cambridge University",
      "difficulty": "easy",
      "explanation": "Mentioned in the 'Early life' section."
    },
    {
      "question": "What was Alan Turing's main contribution during World War II?",
      "options": ["Atomic research", "Breaking the Enigma code", "Inventing radar", "Developing jet engines"],
      "answer": "Breaking the Enigma code",
      "difficulty": "medium",
      "explanation": "Detailed in the 'World War II' section."
    }
  ],
  "related_topics": ["Cryptography", "Enigma machine", "Computer science history"]
}
```

## Testing Prompts

To test prompt effectiveness:

1. **Factual Accuracy**: Verify answers are in article content
2. **Difficulty Distribution**: Check mix of easy/medium/hard
3. **Section Coverage**: Ensure questions span multiple sections
4. **Distractor Quality**: Verify wrong answers are plausible
5. **Explanation Clarity**: Check explanations are informative

## References

- LangChain Documentation: https://python.langchain.com/
- Google Gemini API: https://ai.google.dev/
- Prompt Engineering Best Practices: https://platform.openai.com/docs/guides/prompt-engineering
