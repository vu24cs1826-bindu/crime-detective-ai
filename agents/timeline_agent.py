from llm import ask_llm

def create_timeline(text):

    prompt = f"""
You are a crime investigation timeline analyst.

Create a chronological timeline.

Return ONLY a markdown table.

| Time/Date | Event |
|------------|--------|

Arrange all events in chronological order.

Evidence:
{text}
"""

    return ask_llm(prompt)