import ollama

def generate_kql(user_query: str, mode: str) -> str:
    if mode == "Microsoft Defender XDR":
        schema_reference = """Available Defender XDR tables and key columns:

- DeviceProcessEvents:
  Timestamp, FileName, FolderPath, ProcessCommandLine, InitiatingProcessFileName, InitiatingProcessParentFileName

- DeviceLogonEvents:
  Timestamp, DeviceName, AccountName, ActionType, LogonType, RemoteIP, RemoteDeviceName

- DeviceNetworkEvents:
  Timestamp, DeviceName, RemoteIP, RemotePort, LocalPort, InitiatingProcessFileName, InitiatingProcessCommandLine, Protocol

- DeviceFileEvents:
  Timestamp, DeviceName, FileName, FolderPath, SHA1, ActionType

- IdentityLogonEvents:
  Timestamp, AccountUpn, IPAddress, Application, ResultType, Location, ResourceDisplayName

- EmailEvents:
  Timestamp, SenderFromAddress, RecipientEmailAddress, Subject, NetworkMessageId, DeliveryAction, ThreatTypes

- EmailAttachmentInfo:
  Timestamp, FileName, SHA256, FileType, EmailNetworkMessageId

- CloudAppEvents:
  Timestamp, AppName, ActionType, AccountName, IPAddress, DeviceName
"""

        prompt = f"""
You are a Microsoft Defender XDR threat hunter.
Generate a KQL query using only the following schema:

{schema_reference}

Request: {user_query}

KQL:
"""
    else:
        schema_reference = """Available Microsoft Sentinel (Log Analytics) tables and key columns:

- SecurityEvent:
  TimeGenerated, EventID, AccountName, Computer, LogonType, Status, TargetUserName, SubjectUserName

- SigninLogs:
  TimeGenerated, UserPrincipalName, IPAddress, Location, ResultType, AppDisplayName, ConditionalAccessStatus

- OfficeActivity:
  TimeGenerated, Operation, UserId, Workload, ClientIP, Site_Url, ObjectId

- AzureDiagnostics:
  TimeGenerated, ResourceId, Category, ActivityStatus, Identity, ResultDescription

- AzureActivity:
  TimeGenerated, Caller, Category, OperationName, ActivityStatusValue, ResourceGroup

- AuditLogs:
  TimeGenerated, LoggedByService, OperationName, Result, TargetResources, InitiatedBy

- Heartbeat:
  TimeGenerated, Computer, IPAddress, RemoteIPCountry, OSType, OSName"""
        prompt = f"""
You are a security analyst working in Microsoft Sentinel. Use only tables like SecurityEvent, SigninLogs, OfficeActivity.

Request: {user_query}
KQL:
"""

    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()
