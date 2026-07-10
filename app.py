import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Executive Tender Intelligence Suite",
    page_icon="🛡",
    layout="wide"
)

# ---------- SIDEBAR ----------

with st.sidebar:
    st.title("🛡")
    st.header("Executive")
    st.subheader("Security")
    st.caption("Tender Intelligence Suite")

    st.divider()

    st.checkbox("Sambad", value=True)
    st.checkbox("Samaja", value=True)
    st.checkbox("Dharitri", value=True)
    st.checkbox("Prameya", value=True)
    st.checkbox("Orissa Post", value=True)
    st.checkbox("Pioneer", value=True)
    st.checkbox("Times of India", value=True)
    st.checkbox("New Indian Express", value=True)

# ---------- HEADER ----------

st.title("Executive Tender Intelligence Suite")
st.subheader("Executive Security Service Pvt Ltd")

st.divider()

# ---------- DATE ----------

selected_date = st.date_input(
    "Newspaper Date",
    value=date.today()
)

# ---------- METRICS ----------

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Pages Scanned", 0)
c2.metric("Tender Found", 0)
c3.metric("Security", 0)
c4.metric("Housekeeping", 0)
c5.metric("Manpower", 0)

st.divider()

# ---------- BUTTON ----------

if st.button("🚀 START SCANNING", use_container_width=True):

    progress = st.progress(0)

    status = st.empty()

    for i in range(101):
        progress.progress(i)
        status.write(f"Scanning... {i}%")

    st.success("Scanning completed successfully.")

st.divider()

# ---------- RESULTS ----------

st.header("Today's Tenders")

st.info("No tenders found yet.")

st.divider()

# ---------- PLACEHOLDER TABLE ----------

df = pd.DataFrame(
    columns=[
        "Newspaper",
        "Page",
        "Category",
        "Image"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# ---------- WHATSAPP ----------

if st.button("📲 Send to WhatsApp", use_container_width=True):
    st.success("WhatsApp integration will be connected.")
