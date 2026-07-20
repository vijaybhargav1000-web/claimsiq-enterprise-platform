import streamlit as st
from pypdf import PdfReader
from bedrocks import analyze_claim
from prompts import CLAIM_ANALYSIS_PROMPT

st.set_page_config(
    page_title="ClaimsIQ - AI Claim Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ClaimsIQ - AI Claim Analyzer")
st.write("Upload a claim PDF and analyze it using Amazon Bedrock.")

uploaded_file = st.file_uploader(
    "Upload Claim PDF",
    type=["pdf"]
)

claim_text = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            claim_text += text

    st.subheader("Extracted Claim Text")
    st.text_area(
        "Claim Content",
        claim_text,
        height=300
    )
    if st.button("Analyze Claim"):

     if claim_text.strip():

        with st.spinner("Analyzing claim using Amazon Bedrock..."):

            report = analyze_claim(
                CLAIM_ANALYSIS_PROMPT.format(claim=claim_text)
            )

        st.subheader("AI Claim Analysis")
        st.write(report)

    else:
        st.warning("No text found in the uploaded PDF.")
