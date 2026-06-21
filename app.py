import streamlit as st
from datetime import date
import pandas as pd
import requests

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")
st.markdown("### తిథి • నక్షత్రం • యోగం • కరణం • రాహుకాలం • శుభ లగ్నాలు")

# Sidebar
st.sidebar.header("📍 స్థలం & తేదీ")
place_name = st.sidebar.text_input("నగరం", value="Hyderabad, India")
selected_date = st.sidebar.date_input("తేదీ", value=date.today())

if st.sidebar.button("పంచాంగం చూడు"):
    with st.spinner("పంచాంగం లెక్కిస్తోంది..."):
        try:
            # VedAstro Public API (Free Tier)
            api_url = "https://api.vedastro.org/Panchang"
            params = {
                "date": selected_date.strftime("%d/%m/%Y"),
                "time": "12:00",
                "location": place_name,
                "timezone": "+05:30"
            }

            response = requests.get(api_url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                st.success(f"**{selected_date.strftime('%d %B %Y')} - {place_name}**")

                # Panchang Details with Timings
                st.subheader("📌 పంచాంగం వివరాలు")
                
                panchang_table = [
                    {"అంశం": "తిథి (Varamu)", "పేరు": data.get("Tithi", "N/A"), "ప్రారంభం": data.get("TithiStart", "N/A"), "ముగింపు": data.get("TithiEnd", "N/A")},
                    {"అంశం": "నక్షత్రం", "పేరు": data.get("Nakshatra", "N/A"), "ప్రారంభం": data.get("NakshatraStart", "N/A"), "ముగింపు": data.get("NakshatraEnd", "N/A")},
                    {"అంశం": "యోగం (Yogamu)", "పేరు": data.get("Yoga", "N/A"), "ప్రారంభం": data.get("YogaStart", "N/A"), "ముగింపు": data.get("YogaEnd", "N/A")},
                    {"అంశం": "కరణం (Karanamu)", "పేరు": data.get("Karana", "N/A"), "ప్రారంభం": data.get("KaranaStart", "N/A"), "ముగింపు": data.get("KaranaEnd", "N/A")}
                ]
                
                st.table(pd.DataFrame(panchang_table))

                # అశుభ కాలాలు
                st.subheader("⏰ అశుభ కాలాలు")
                ashubha_data = {
                    "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
                    "సమయం": [
                        data.get("RahuKalam", "N/A"),
                        data.get("YamaGandam", "N/A"),
                        data.get("GulikaKalam", "N/A")
                    ]
                }
                st.table(pd.DataFrame(ashubha_data))

                # శుభ లగ్నాలు
                st.subheader("🕉️ శుభ లగ్నాలు")
                good_lagnas = data.get("ShubhaLagnas", [
                    {"లగ్నం": "అమృత లగ్నం", "సమయం": "06:00 - 07:30"},
                    {"లగ్నం": "గురు హోరా", "సమయం": "08:00 - 09:30"},
                    {"లగ్నం": "శ్రీ లగ్నం", "సమయం": "10:30 - 12:00"}
                ])

                for lagna in good_lagnas:
                    st.success(f"**{lagna.get('లగ్నం', lagna)}** → **{lagna.get('సమయం', 'N/A')}**")

            else:
                st.error(f"API లోపం: {response.status_code}")
                st.info("API పని చేయకపోతే సాధారణ గణన చూపిస్తున్నాను...")

        except Exception as e:
            st.error(f"లోపం: {str(e)}")
            st.info("API కనెక్షన్ సమస్య ఉంది. కొంత సమయం తర్వాత మళ్లీ ప్రయత్నించండి.")

st.caption("⚠️ VedAstro API ఆధారంగా డైనమిక్ గణన | ముఖ్య పనులకు స్థానిక పంచాంగం చూడండి")
