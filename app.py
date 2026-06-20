import streamlit as st
from datetime import date
import pandas as pd
from vedastro import *

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")

Calculate.SetAPIKey('FreeAPIUser')

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
place_name = st.sidebar.text_input("నగరం", value="Hyderabad, India")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

if st.sidebar.button("పంచాంగం చూడు"):
    try:
        # Correct Format with Timezone (IST = +05:30)
        time_str = f"12:00 {selected_date.day:02d}/{selected_date.month:02d}/{selected_date.year} +05:30"
        
        geo = GeoLocation(place_name, 78.4867, 17.3850)  # Hyderabad
        birth_time = Time(time_str, geo)

        st.success(f"**{selected_date} - {place_name}**")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 పంచాంగం వివరాలు")
            st.write(f"**తిథి:** {Calculate.LunarDay(birth_time)}")
            st.write(f"**నక్షత్రం:** {Calculate.MoonConstellation(birth_time)}")
            st.write(f"**యోగం:** {Calculate.Yoga(birth_time)}")
            st.write(f"**కరణం:** {Calculate.Karana(birth_time)}")
            st.write(f"**వారం:** {Calculate.Weekday(birth_time)}")

        with col2:
            st.subheader("🌅 సూర్యోదయం & సూర్యాస్తమయం")
            st.write(f"**సూర్యోదయం:** {Calculate.Sunrise(birth_time)}")
            st.write(f"**సూర్యాస్తమయం:** {Calculate.Sunset(birth_time)}")

        # అశుభ కాలాలు
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

        st.subheader("🕉️ శుభ లగ్నాలు")
        st.success("అమృత లగ్నం, గురు హోరా, శ్రీ లగ్నం — మంచి పనులకు ఉత్తమం")

        st.markdown("""
        **శుభ లగ్నాల్లో చేయదగిన పనులు:**
        - వివాహం, గృహ ప్రవేశం, ఉపనయనం
        - కొత్త వ్యాపారం / ప్రాజెక్ట్ ప్రారంభం
        - హోమాలు, దానాలు, మంత్ర జపం
        - ముఖ్య నిర్ణయాలు
        """)

    except Exception as e:
        st.error(f"లోపం: {str(e)}")

st.caption("⚠️ VedAstro API ఉపయోగించి గణన చేయబడింది. ముఖ్య కార్యాలకు స్థానిక పంచాంగం చూడండి.")
