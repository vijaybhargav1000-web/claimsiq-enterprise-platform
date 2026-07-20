from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import streamlit as st
from pypdf import PdfReader
from bedrocks import analyze_claim
from prompts import CLAIM_ANALYSIS_PROMPT
def generate_pdf(report):

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(temp_file.name, pagesize=letter)

    y = 750

    for line in report.split("\n"):

        c.drawString(40, y, line[:100])

        y -= 20

        if y < 40:
            c.showPage()
            y = 750

    c.save()

    return temp_file.name
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
        pdf_file = generate_pdf(report)

        with open(pdf_file, "rb") as file:

            st.download_button(
        label="📥 Download AI Report",
        data=file,
        file_name="ClaimsIQ_AI_Report.pdf",
        mime="application/pdf"
    )
    else:
        st.warning("No text found in the uploaded PDF.")
