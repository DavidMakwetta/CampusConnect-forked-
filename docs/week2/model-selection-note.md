# Model Selection Note — Week 2

**Project:** Software Engineering QA Agent  
**Week:** 2 — Foundation-Model Engineering and Prompting  
**Date:** 7–11 September 2026

## Selected model

The Week 2 baseline uses **Google Gemini 3.6 Flash** through the Gemini API. The model was accessed from a Python application using the `google-genai` SDK. It was selected as the working baseline for the Software Engineering QA Agent because it supports prompt-based analysis of software requirements, user stories, and code snippets.

## Selection considerations

**Capability:** Gemini 3.6 Flash is used to analyze software engineering inputs from a quality assurance perspective. The system prompt instructs the model to identify ambiguities, missing requirements, edge cases, possible defects, security and performance concerns, test scenarios, and recommendations.

**Cost:** The project uses the Gemini API, where usage costs depend on the selected model and the number of input and output tokens. Actual project cost therefore depends on API usage during testing.

**Latency:** The Flash model family is intended for fast responses. However, actual latency for this project depends on network conditions, API response time, prompt length, and output size, so latency should be measured during evaluation rather than assumed.

**Privacy:** API requests are sent to Google's Gemini service for processing. The project should therefore avoid sending confidential, sensitive, or unnecessary personal information to the API and should follow the applicable Google API data-use and privacy requirements.

**Access:** The model is accessed programmatically through the `google-genai` Python SDK. The application requires a `GEMINI_API_KEY`, which is stored as an environment variable rather than being written directly in the source code.

## Baseline interaction

The baseline implementation uses a single model interaction. The Python application accepts a requirement, user story, or code snippet from the user and sends it to Gemini together with the QA system instruction. The model returns a structured response containing:

1. QA Analysis
2. Issues Found
3. Test Scenarios
4. Recommendations

The implementation deliberately focuses on a simple baseline interaction without adding RAG or multiple agents.

## Decision

**Gemini 3.6 Flash** was selected as the Week 2 working baseline because it could be integrated into the Python application using the Gemini API and provided the required model interaction for the QA Agent prototype.

## References

Google. *Gemini API documentation*. Google AI for Developers.

Google. *Google Gen AI SDK documentation*. Google AI for Developers.
