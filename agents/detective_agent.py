from llm import ask_llm

def ask_detective(question, case_text):

    prompt = f"""
    You are a professional crime detective.

    Answer ONLY the user's question.

    Rules:
    - Maximum 2-3 sentences.
    - Do not generate investigation summaries.
    - Do not generate suspect tables.
    - Do not generate location lists.
    - Do not generate reports.
    - Give only the direct answer.

    Case:
    {case_text}

    Question:
    {question}
    """

    return ask_llm(prompt)