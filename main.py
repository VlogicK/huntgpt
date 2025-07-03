import streamlit as st
from modules.kql_generator import generate_kql

st.set_page_config(page_title="HUNTGPT", page_icon="🛡️")

st.title("🛡️ HUNTGPT – Ollama-based Threat Hunting Assistant")
st.subheader("🧠 Convert natural language into KQL")

query = st.text_area("Describe what you want to hunt:", height=150)

if st.button("Generate KQL"):
    with st.spinner("Thinking..."):
        try:
            kql = generate_kql(query)
            st.code(kql, language="kql")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
