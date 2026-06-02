from llm import ask_llm

def analyze_evidence(text):

    prompt =  f"""
    You are a professional crime investigator.

    Analyze the case and provide only the important findings.

    Do not repeat information.
    Do not generate long summaries.
    Keep the response concise.

    Case Information:
    {text}
    """

    return ask_llm(prompt)