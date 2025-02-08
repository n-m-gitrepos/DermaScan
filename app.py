import streamlit as st
import urllib.parse

# add icon here
st.set_page_config(
    page_title="DermaScan",  
    page_icon="🩺",  
    layout="centered" 
)

st.title("DermaScan")

st.title("Skin Disease Treatment Locator")

st.write("### Enter Location")
user_location = st.text_input("Enter your city (and state if needed)")

if user_location:
    formatted_location = urllib.parse.quote_plus(user_location.strip())
    try:
        with open("api_key.txt", "r") as file:
            api_key = file.readline().strip() 
    except Exception as e:
        st.error(f"Error reading API key: {e}")
        api_key = None

    if api_key:
        google_maps_url = f"https://www.google.com/maps/embed/v1/search?key={api_key}&q=dermatology+clinics+near+{formatted_location}"

        st.write("### Map Showing Treatment Centers Nearby")
        st.components.v1.html(
            f'<iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen '
            f'src="{google_maps_url}"></iframe>',
            height=450,
        )

        ##hi
    else:
        st.error("API Key is missing or incorrect.")