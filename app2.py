import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_weather_info(city):
    # Perform a Google search for the weather
    search_query = f"Weather in {city}"
    google_url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(google_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the weather information from the search results
        weather_info_tag = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
        
        if weather_info_tag is not None:
            weather_info = weather_info_tag.get_text()
            
            if weather_info:
                # #Remove the non-numeric characters from the string
                # numeric_part = ''.join(c for c in weather_info if c.isdigit() or c == '.')
                # #convert float
                # temperature = float(numeric_part)
                # #convert Celsius to Fahrenheit 
                # fahrenheit = (temperature * 9/5) + 32
                # #convert Fahrenheit to Celsius
                # celsius = (fahrenheit - 32) * 5/9

                return weather_info
            else:
                return "No weather information found."
        else:
            return "Weather information not found on the page."
    else:
        return "Failed to retrieve weather information. Please try again."

# Streamlit UI
st.title("Weather App")

city = st.text_input("Enter the city:")
if st.button("Get Weather"):
    weather_result = get_weather_info(city)
    st.success(f"The weather in {city} is {weather_result}")
