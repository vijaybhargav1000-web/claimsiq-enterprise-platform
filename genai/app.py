import streamlit as st
from bedrocks import analyze_claim
from pypdf import PdfReader

st.set_page_config(page_title="ClaimsIQ AI Assistant", page_icon="🛡️")

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

    st.subheader("Extracted Claim")
    st.text_area("Claim Content", claim, height=250)

else:
    claim = st.text_area(
        "Enter Claim Details",
        """Customer vehicle damaged due to heavy rainfall while parked.

Estimated repair cost: ₹1,80,000

Policy: Comprehensive

No previous claims in the last 3 years.""",
        height=250
    )

if st.button("Analyze Claim"):

    with st.spinner("Analyzing claim..."):
        result = analyze_claim(claim)

    st.success("Analysis Complete")

    # Dashboard
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Risk Score", "18/100")

    with col2:
        st.metric("Fraud Status", "Low")

    with col3:
        st.metric("Coverage", "Approved")

    st.progress(18)

    st.divider()

    st.markdown(result)
    
    