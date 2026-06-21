import streamlit as st
from datetime import datetime, date
import pandas as pd
from PyJHora import Panchanga, Place

st.set_page_config(page_title="📅 తెలుగు పంచాంగం", layout="wide")
st.title("🌟 తెలుగు పంచాంగం - రోజువారీ ముహూర్తాలు")

# Sidebar Inputs
st.sidebar.header("📍 స్థలం & తేదీ")
city = st.sidebar.text_input("నగరం / స్థలం", value="Hyderabad, India")
date_input = st.sidebar.date_input("తేదీ", value=date.today())

# Place object
place = Place(city)

# Calculate Panchangam
panchang = Panchanga(date_input.year, date_input.month, date_input.day, place)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 ఈ రోజు పంచాంగం")
    st.write(f"**తేదీ:** {date_input}")
    st.write(f"**వారం:** {panchang.weekday_name_te}")
    st.write(f"**తిథి:** {panchang.tithi_name_te}")
    st.write(f"**నక్షత్రం:** {panchang.nakshatra_name_te}")
    st.write(f"**యోగం:** {panchang.yoga_name_te}")
    st.write(f"**కరణం:** {panchang.karana_name_te}")

with col2:
    st.subheader("🌅 సూర్యోదయ & సూర్యాస్తమయం")
    st.write(f"**సూర్యోదయం:** {panchang.sunrise.strftime('%I:%M %p')}")
    st.write(f"**సూర్యాస్తమయం:** {panchang.sunset.strftime('%I:%M %p')}")

# Rahukalam, Yamagandam, Gulika
st.subheader("⏰ కాలాలు (అశుభ సమయాలు)")

data = {
    "కాలం": ["రాహుకాలం", "యమగండం", "గులిక కాలం"],
    "సమయం": [
        panchang.rahu_kalam,
        panchang.yama_gandam,
        panchang.gulika_kalam
    ]
}
df = pd.DataFrame(data)
st.table(df)

# Good Lagnas (Auspicious Lagnas)
st.subheader("🕉️ ఈ రోజు శుభ లగ్నాలు")

good_lagnas = panchang.shubha_lagnas  # PyJHora provides this

if good_lagnas:
    for lagna in good_lagnas:
        st.success(f"**{lagna['name_te']}** - {lagna['time_range']}")
        st.write(f"**చేయగలిగిన పనులు:** {lagna['suitable_activities_te']}")
else:
    st.info("ఈ రోజు శుభ లగ్నాలు లెక్కించబడుతున్నాయి...")

# What to do during Good Lagnas
st.subheader("✅ శుభ లగ్నాల్లో చేయదగిన పనులు")
activities = """
- గృహ ప్రవేశం, వివాహం, ఉపనయనం  
- కొత్త వ్యాపారం ప్రారంభం  
- ఇంటి నిర్మాణం, గ్రహారంభం  
- మంత్ర జపం, హోమాలు, దానాలు  
- ప్రయాణాలు, ముఖ్య నిర్ణయాలు  
- ఔషధాలు ప్రారంభించడం
"""
st.markdown(activities)

# Footer Note
st.caption("⚠️ ఇది సాధారణ సమాచారం. సంపూర్ణ ఖచ్చితత్వం కోసం స్థానిక పంచాంగం లేదా జ్యోతిష్యుల సలహా తీసుకోండి.")

# Run the app
if __name__ == "__main__":
    st.info("అప్లికేషన్ రన్ అవుతోంది...")
