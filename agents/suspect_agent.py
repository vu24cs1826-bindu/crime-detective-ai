from llm import ask_llm

def rank_suspects(text):

    prompt = f"""
You are a senior detective.

Rank suspects based on available evidence.

Return a markdown table:

| Rank | Suspect | Risk Score (1-10) | Reason |
|-------|----------|------------------|---------|

Evidence:
{text}
"""

    return ask_llm(prompt)