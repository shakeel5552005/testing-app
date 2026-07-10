import streamlit as st
import requests

API_KEY = "15a0bdf79c5d8d99439ac1789ebc5756"


st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌦️ Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city == "":
        st.warning("Please enter a city name.")

    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            st.success(f"Weather in {city}")

            st.write(f"🌡 Temperature : {data['main']['temp']} °C")

            st.write(f"🤗 Feels Like : {data['main']['feels_like']} °C")

            st.write(f"💧 Humidity : {data['main']['humidity']} %")

            st.write(f"🌬 Wind Speed : {data['wind']['speed']} m/s")

            st.write(f"☁ Condition : {data['weather'][0]['description'].title()}")

        else:
            st.error("City not found.")
            st.error(f"Status Code: {response.status_code}")
            st.json(data)