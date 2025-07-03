import ollama

def generate_kql(user_query: str, mode: str) -> str:
    if mode == "Microsoft Defender XDR":
        prompt = f"""
You are a cybersecurity expert hunting in Microsoft Defender XDR using advanced KQL queries.

Here are some examples:

Request: Show all PowerShell executions in the last day  
KQL:
DeviceProcessEvents
| where FileName has "powershell.exe"
| where Timestamp > ago(1d)

Request: List failed RDP logins on endpoints  
KQL:
DeviceLogonEvents
| where LogonType == "RemoteInteractive"
| where ActionType == "LogonFailed"

Now generate a KQL query for the following request:

Request: {user_query}  
KQL:
"""
    else:
        prompt = f"""
You are a cybersecurity expert working in Microsoft Sentinel.

Examples:

Request: Show failed logons by admin accounts  
KQL:
SecurityEvent
| where EventID == 4625 and AccountType == "Administrator"

Request: Find logins from foreign IPs  
KQL:
SigninLogs
| where Location !in ("New Zealand", "Australia")

Now convert:
Request: {user_query}  
KQL:
"""

    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()
