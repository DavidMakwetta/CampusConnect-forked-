
import os

from google import genai

MODEL = "gemini-3.6-flash"

SYSTEM_PROMPT = """
You are a Software Engineering QA Agent.

Your task is to analyze software engineering requirements, user stories,
and code snippets from a quality assurance perspective.

For requirements and user stories:
- Identify ambiguity and missing information.
- Identify functional and non-functional requirements.
- Identify edge cases.
- Suggest test scenarios.
- Identify missing or unclear acceptance criteria.

For code:
- Identify possible bugs and defects.
- Identify edge cases.
- Identify security, performance, and maintainability concerns.
- Suggest appropriate tests.

Structure your response using:

1. QA Analysis
2. Issues Found
3. Test Scenarios
4. Recommendations

Be concise, practical, and specific.
"""


def analyze(text: str) -> str:
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    interaction = client.interactions.create(
        model=MODEL,
        system_instruction=SYSTEM_PROMPT,
        input=text,
    )

    return interaction.output_text


def main():
    print("Software Engineering QA Agent — Week 2")
    print(f"Model: {MODEL}")
    print("Enter a requirement, user story, or code snippet. Type 'exit' to quit.\n")

    while True:
        text = input("Input: ").strip()

        if text.lower() == "exit":
            break

        if not text:
            print("Please provide an input.\n")
            continue

        try:
            print("\n" + analyze(text) + "\n")
        except Exception as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
