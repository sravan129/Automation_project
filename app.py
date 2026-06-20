import streamlit as st
from datetime import date
import pandas as pd
from vedastro import *

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")

# API Key (Free tier)
Calculate.SetAPIKey('FreeAPIUser')

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
place_name = st.sidebar.text_input("నగరం", value="Hyderabad, India")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

if st.sidebar.button("పంచాంగం చూడు"):
    try:
        # Create Time object
        time_str = f"12:00 {selected_date.day:02d}/{selected_date.month:02d}/{selected_date.year}"
        geo = GeoLocation(place_name, 78.4867, 17.3850)  # Default Hyderabad coords
        birth_time = Time(time_str, geo)

        st.success(f"**{selected_date} - {place_name}**")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 పంచాంగం వివరాలు")
            st.write(f"**తిథి:** {Calculate.Tithi(birth_time)}")
            st.write(f"**నక్షత్రం:** {Calculate.Nakshatra(birth_time)}")
            st.write(f"**యోగం:** {Calculate.Yoga(birth_time)}")
            st.write(f"**కరణం:** {Calculate.Karana(birth_time)}")
            st.write(f"**వారం:** {Calculate.Weekday(birth_time)}")

        with col2:
            st.subheader("🌅 సూర్యోదయం & సూర్యాస్తమయం")
            st.write(f"**సూర్యోదయం:** {Calculate.Sunrise(birth_time)}")
            st.write(f"**సూర్యాస్తమయం:** {Calculate.Sunset(birth_time)}")

        # Rahukalam, Yamagandam, Gulika
        st.subheader("⏰ అశుభ కాలాలు")
        data = {
            "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
            "సమయం": [
                Calculate.RahuKalam(birth_time),
                Calculate.YamaGandam(birth_time),
                Calculate.GulikaKalam(birth_time)
            ]
        }
        st.table(pd.DataFrame(data))

        st.subheader("🕉️ శుభ లగ్నాలు & సూచనలు")
        st.info("**అమృత లగ్నం, గురు హోరా, శ్రీ లగ్నం** — మంచి పనులకు ఉత్తమం")

        st.markdown("""
        **శుభ లగ్నాల్లో చేయదగిన పనులు:**
        - వివాహం, గృహ ప్రవేశం, ఉపనయనం
        - కొత్త వ్యాపారం ప్రారంభం
        - హోమాలు, దానాలు, మంత్ర జపం
        - ముఖ్య నిర్ణయాలు తీసుకోవడం
        """)

    except Exception as e:
        st.error(f"లోపం: {str(e)}")
        st.info("FreeAPIUser కీతో కొన్ని లిమిట్ ఉండవచ్చు. కొంత సమయం తర్వాత మళ్లీ ప్రయత్నించండి.")

st.caption("⚠️ ఇది VedAstro లైబ్రరీ ఆధారంగా ఉంటుంది. ముఖ్య పనులకు స్థానిక పంచాంగం లేదా జ్యోతిష్యుల సలహా తీసుకోండి.")
