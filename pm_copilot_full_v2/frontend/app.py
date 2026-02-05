
import streamlit as st
import requests

st.title("PM Copilot v2")

backend = "http://localhost:8000"

st.header("Upload Files")
files = st.file_uploader("Choose project docs", accept_multiple_files=True)

if st.button("Upload"):
    if files:
        mfiles = [("files", (f.name, f.getvalue())) for f in files]
        r = requests.post(f"{backend}/upload", files=mfiles)
        st.success(r.json())
    else:
        st.warning("No files selected")
