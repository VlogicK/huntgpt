import ollama

def generate_kql(natural_language_query: str) -> str:
    prompt = f"""
You are a security analyst skilled in Microsoft Sentinel and KQL.
Convert this natural language request into a KQL query:

Request: {natural_language_query}

KQL:
"""
    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()
