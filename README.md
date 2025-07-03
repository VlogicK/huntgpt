# huntgpt
An AI-native security assistant that helps SOC analysts and threat hunters generate queries, enrich IOCs, analyze logs, and triage alerts — all via natural language.
![HUNTGPT Screenshot Placeholder](screenshot.png)

---

## 🚀 Features

- 💬 **Natural Language to KQL** – Describe your hunt, get ready-to-run queries.
- 🧠 **Log File Summarization** – Upload logs and get key anomalies and behavior insights.
- 🔎 **IOC Enrichment** – Get threat intelligence for IPs, domains, and hashes via VirusTotal and GreyNoise.
- ⚡ **Alert Summarizer** – Input raw alerts (e.g. Defender or Sentinel JSON) and get context, risks, and recommended steps.
- 🧭 **MITRE ATT&CK Integration** – Ask about techniques and get mapped references.

---

## 🛠️ Tech Stack

| Component       | Tech                         |
|----------------|------------------------------|
| Backend         | Python + FastAPI             |
| Frontend        | Streamlit                    |
| AI Engine       | OpenAI GPT-4 / Ollama LLM    |
| Log Analysis    | Pandas, regex, evtxtract     |
| Enrichment APIs | VirusTotal, GreyNoise, AbuseIPDB |
| Prompt Handling | LangChain / Custom Templates |

---

## 🧪 Demo

```bash
# Run the app
streamlit run main.py


Example Prompts
"Show me failed RDP logons from outside NZ in the past week."
"Summarize this Defender alert JSON for triage."
"List MITRE techniques used in ransomware campaigns."
