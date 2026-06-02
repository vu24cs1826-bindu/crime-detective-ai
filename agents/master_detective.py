from llm import ask_llm

def generate_report(
    evidence_analysis,
    timeline,
    contradictions
):

    prompt = f"""
Create a professional investigation report.

# Case Summary

# Timeline

# Key Evidence

# Contradictions

# Suspect Assessment

# Recommended Actions

Use professional report formatting.

Evidence Analysis:
{evidence_analysis}

Timeline:
{timeline}

Contradictions:
{contradictions}
"""

    return ask_llm(prompt)