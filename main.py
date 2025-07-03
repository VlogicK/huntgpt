import streamlit as st
from modules.kql_generator import generate_kql

st.set_page_config(page_title="HUNTGPT", page_icon="🛡️")
st.title("🛡️ HUNTGPT – AI Threat Hunting Assistant")

# 👇 Sidebar dropdown for mode
st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Choose Query Type", ["Microsoft Defender XDR", "Azure Sentinel Logs"])

st.markdown(f"🎯 **Current Mode:** {mode}")

query = st.text_area("🔍 Describe what you want to hunt:", height=150)

if st.button("Generate KQL"):
    with st.spinner("Thinking..."):
        try:
            kql = generate_kql(query, mode)
            st.code(kql, language="kql")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
