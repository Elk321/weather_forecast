import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, select box, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

try:
    # Get temperatures and sky data
    if place:
        dates, filtered_data = get_data(place, days)
        st.subheader(f"{option} for the next {days} day(s) in {place.title()}")

        # Display temperatures
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        else:
            # Get the images
            images = {"Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png",
                      "Clear": "images/clear.png"}

            # Display sky
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths, caption=dates, width=200)
except KeyError:
    st.error("The city name is incorrect. Please try again.")
