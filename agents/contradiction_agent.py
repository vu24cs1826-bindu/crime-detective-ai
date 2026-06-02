from llm import ask_llm

def find_contradictions(text):

    prompt = f"""
You are a forensic investigation expert.

Analyze witness statements and reports.

Return:

# Contradictions Found

| Statement A | Statement B | Issue |
|-------------|-------------|-------|

# Missing Information

- List missing details.

# Suspicious Observations

- List suspicious findings.

Evidence:
{text}
"""

    return ask_llm(prompt)