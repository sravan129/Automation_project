import streamlit as st
from datetime import datetime, date
import pandas as pd
import swisseph as swe
import math

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
city = st.sidebar.text_input("నగరం", value="Hyderabad")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

# Basic calculations using Swiss Ephemeris
def get_panchangam(d):
    # Set Ephemeris path (Streamlit Cloud supports this)
    swe.set_ephe_path('/usr/share/swisseph')  # Default path in many environments
    
    year, month, day = d.year, d.month, d.day
    jd = swe.julday(year, month, day, 12.0)  # Noon for panchang
    
    # Simple Tithi & Nakshatra approximation (for demo)
    st.success(f"**తేదీ:** {d}")
    st.write("**తిథి & నక్షత్రం** - (పూర్తి లైబ్రరీతో అప్‌డేట్ చేస్తాను)")
    
    # Rahukalam, Yamagandam (Standard South Indian Timings - Approximate)
    weekday = d.weekday()  # 0=Mon ... 6=Sun
    
    rahukalam = ["8:00-9:30", "1:30-3:00", "10:30-12:00", "3:00-4:30", 
                 "12:00-1:30", "9:30-11:00", "4:30-6:00"][weekday]
    
    yamagandam = ["10:30-12:00", "9:30-11:00", "1:30-3:00", "12:00-1:30",
                  "3:00-4:30", "8:00-9:30", "11:00-12:30"][weekday]
    
    gulika = ["6:00-7:00", "7:00-8:00", "8:00-9:00", "9:00-10:00",
              "10:00-11:00", "11:00-12:00", "12:00-1:00"][weekday]
    
    return rahukalam, yamagandam, gulika

rahukalam, yamagandam, gulika = get_panchangam(selected_date)

st.subheader("⏰ అశుభ కాలాలు")
data = {
    "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
    "సమయం": [rahukalam, yamagandam, gulika]
}
st.table(pd.DataFrame(data))

st.subheader("🕉️ శుభ లగ్నాలు (ఉదాహరణలు)")
st.info("**అమృత లగ్నం, శ్రీ లగ్నం, గురు లగ్నం** - మంచి పనులకు ఉత్తమం")

st.markdown("""
**శుభ లగ్నాల్లో చేయదగిన పనులు:**
- వివాహం, గృహ ప్రవేశం, ఉపనయనం
- కొత్త వ్యాపారం ప్రారంభం
- హోమాలు, దానాలు, మంత్ర జపం
- ముఖ్య నిర్ణయాలు తీసుకోవడం
""")

st.caption("⚠️ ఇది సాధారణ గణన. పూర్తి ఖచ్చితత్వం కోసం స్థానిక పంచాంగం చూడండి.")
