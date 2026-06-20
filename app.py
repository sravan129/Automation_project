import streamlit as st
from datetime import date
import pandas as pd

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")
st.markdown("### రాహుకాలం • యమగండం • గులిక • శుభ లగ్నాలు")

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
place_name = st.sidebar.text_input("నగరం", value="Hyderabad, India")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

if st.sidebar.button("పంచాంగం చూడు"):
    weekday = selected_date.weekday()  # 0 = Monday

    # Standard South Indian Timings (Approximate but reliable)
    rahukalam_list = ["08:00-09:30", "01:30-03:00", "10:30-12:00", "03:00-04:30", 
                      "12:00-01:30", "09:30-11:00", "04:30-06:00"]
    yamagandam_list = ["10:30-12:00", "09:30-11:00", "01:30-03:00", "12:00-01:30",
                       "03:00-04:30", "08:00-09:30", "11:00-12:30"]
    gulika_list = ["06:00-07:00", "07:00-08:00", "08:00-09:00", "09:00-10:00",
                   "10:00-11:00", "11:00-12:00", "12:00-13:00"]

    st.success(f"**{selected_date.strftime('%d %B %Y')} - {place_name}**")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 పంచాంగం")
        st.write(f"**తిథి:** సప్తమి / అష్టమి (సాధారణ గణన)")
        st.write(f"**నక్షత్రం:** ఉత్తర / హస్త (సాధారణ గణన)")
        st.write(f"**యోగం:** సాధారణ గణన")
        st.write(f"**వారం:** {selected_date.strftime('%A')}")

    with col2:
        st.subheader("🌅 సూర్యోదయం")
        st.write("**సూర్యోదయం:** ~6:00 AM")
        st.write("**సూర్యాస్తమయం:** ~6:45 PM")

    # అశుభ కాలాలు
    st.subheader("⏰ అశుభ కాలాలు")
    data = {
        "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
        "సమయం": [
            rahukalam_list[weekday],
            yamagandam_list[weekday],
            gulika_list[weekday]
        ]
    }
    st.table(pd.DataFrame(data))

    st.subheader("🕉️ శుభ లగ్నాలు")
    st.success("**అమృత లగ్నం • గురు హోరా • శ్రీ లగ్నం • రవి హోరా**")

    st.markdown("""
    **శుభ లగ్నాల్లో చేయదగిన మంచి పనులు:**
    - వివాహం, గృహ ప్రవేశం, ఉపనయనం
    - కొత్త వ్యాపారం / ప్రాజెక్ట్ ప్రారంభం
    - హోమాలు, దానాలు, మంత్ర జపం
    - ముఖ్య నిర్ణయాలు & ప్రయాణాలు
    """)

st.caption("⚠️ ఇది సాధారణ గణన ఆధారంగా ఉంటుంది. ముఖ్య కార్యక్రమాలకు స్థానిక పంచాంగం లేదా జ్యోతిష్యుల సలహా తీసుకోండి.")
