import streamlit as st
from pypdf import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

def generate_pdf(report):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(temp_file.name, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "ClaimsIQ AI Analysis Report")

    y -= 40

    c.setFont("Helvetica", 11)

    for line in report.split("\n"):
        c.drawString(50, y, line)
        y -= 18

        if y < 50:
            c.showPage()
            y = 750

    c.save()

    return temp_file.name






    if st.button("Analyze Claim"):
     with st.spinner("Analyzing claim..."):
        result = analyze_claim(claim)

    st.success("Analysis Complete!")

    st.markdown(result)

    pdf_path = generate_pdf(result)

    with open(pdf_path, "rb") as pdf:
        st.download_button(
            label="📄 Download AI Report",
            data=pdf,
            file_name="ClaimsIQ_AI_Report.pdf",
            mime="application/pdf"
        )

def generate_pdf(report):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(temp_file.name, pagesize=letter)
    y = 750

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "ClaimsIQ AI Analysis Report")
    y -= 40

    c.setFont("Helvetica", 11)

    for line in report.split("\n"):
        c.drawString(50, y, line)
        y -= 18

        if y < 50:
            c.showPage()
            y = 750

    c.save()
    return temp_file.name
st.set_page_config(page_title="ClaimsIQ AI Assistant", layout="wide")

st.title("🛡️ ClaimsIQ AI Assistant")
st.write("Analyze insurance claims using Amazon Bedrock")

uploaded_file = st.file_uploader(
    "Upload Claim PDF",
    type=["pdf"]
)

claim = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            claim += text + "\n"

    st.subheader("📄 Extracted Claim")
    st.text_area(
        "Claim Content",
        claim,
        height=300
    )
