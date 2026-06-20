import streamlit as st
from datetime import date
import pandas as pd
from vedastro import *

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
place_name = st.sidebar.text_input("నగరం", value="Hyderabad, India")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

if st.sidebar.button("పంచాంగం చూడు"):
    try:
        # Create Person for the day
        birth_time = f"{selected_date.year}-{selected_date.month:02d}-{selected_date.day:02d} 12:00:00"  # Noon for panchang
        
        # Get Panchangam
        panchang = Panchangam(birth_time, place_name)
        
        st.success(f"**{selected_date} - {place_name}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📌 పంచాంగం వివరాలు")
            st.write(f"**తిథి:** {panchang.Tithi}")
            st.write(f"**నక్షత్రం:** {panchang.Nakshatra}")
            st.write(f"**యోగం:** {panchang.Yoga}")
            st.write(f"**కరణం:** {panchang.Karana}")
            st.write(f"**వారం:** {panchang.Weekday}")
        
        with col2:
            st.subheader("🌅 సూర్యోదయం & సూర్యాస్తమయం")
            st.write(f"**సూర్యోదయం:** {panchang.Sunrise}")
            st.write(f"**సూర్యాస్తమయం:** {panchang.Sunset}")
        
        # Rahukalam, Yamagandam, Gulika
        st.subheader("⏰ అశుభ కాలాలు")
        data = {
            "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
            "సమయం": [panchang.RahuKalam, panchang.YamaGandam, panchang.GulikaKalam]
        }
        st.table(pd.DataFrame(data))
        
        # Good Lagnas
        st.subheader("🕉️ శుభ లగ్నాలు")
        st.info(panchang.ShubhaLagnas or "ఈ రోజు శుభ లగ్నాలు లెక్కించబడుతున్నాయి...")
        
        st.markdown("""
        **శుభ లగ్నాల్లో చేయదగిన మంచి పనులు:**
        - వివాహం, గృహ ప్రవేశం, ఉపనయనం
        - కొత్త వ్యాపారం / ప్రాజెక్ట్ ప్రారంభం
        - హోమాలు, దానాలు, మంత్ర జపం
        - ముఖ్య నిర్ణయాలు, ప్రయాణాలు
        """)
        
    except Exception as e:
        st.error(f"లోపం: {str(e)}")
        st.info("కొంత సమయం తర్వాత మళ్లీ ప్రయత్నించండి.")

st.caption("⚠️ ఇది ఖచ్చితమైన గణనల ఆధారంగా ఉంటుంది. ముఖ్య పనులకు స్థానిక జ్యోతిష్యుల సలహా తీసుకోండి.")
