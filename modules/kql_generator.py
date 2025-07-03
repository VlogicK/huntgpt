import ollama

def generate_kql(natural_language_query: str) -> str:
    prompt = f"""
You are a cybersecurity analyst using Microsoft Defender XDR for threat hunting.
Generate a KQL query using appropriate Defender XDR tables such as:

- DeviceEvents, DeviceProcessEvents, DeviceNetworkEvents, DeviceLogonEvents
- IdentityLogonEvents, IdentityQueryEvents
- EmailEvents, EmailAttachmentInfo, EmailUrlInfo
- CloudAppEvents, AppFileEvents

Request: {natural_language_query}

KQL:
"""
    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()
