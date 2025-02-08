import streamlit as st

st.set_page_config(
    page_title="About DermaScan",
    page_icon="🩺",
    layout="centered"
)

st.title("About DermaScan")
st.write("""
DermaScan is an interactive tool that allows users to input images of their skin and using a deep learning algorithm we here at DeepSeek will
         help identify any potential skin diseases or conditions you may possibly have from here users can simply enter in their location
         and we will show you the specialists for your condition in the area!

### Features:
- Identify Potential Skin Conditions/Diseases
- Find nearby dermatology clinics
- Interactive map
- Simple and fast location search
""")