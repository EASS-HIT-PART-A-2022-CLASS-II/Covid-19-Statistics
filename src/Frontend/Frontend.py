import streamlit as st
import requests
import matplotlib.pyplot as plt

# Set the base URL of the backend API
BASE_URL = "http://localhost:8000"

# Set the API key and host for the COVID API
API_KEY = "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c"
API_HOST = "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"

def get_world_data():
    # Call the get_all_world_covid_data endpoint to retrieve the world data
    response = requests.get(f"{BASE_URL}/get_all_world_covid_data", headers={
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    })
    return response.json()

def get_countries_data():
    # Call the get_all_countries_covid_data endpoint to retrieve the data for all countries
    response = requests.get(f"{BASE_URL}/get_all_countries_covid_data", headers={
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    })
    return response.json()

def get_country_data(country):
    # Call the get_specific_country_covid_data endpoint to retrieve the data for a specific country
    response = requests.get(f"{BASE_URL}/get_specific_country_covid_data/{country}", headers={
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    })
    return response.json()

# Create a side menu with options to view the world data or view data for a specific country
st.sidebar.title("Options")
view_world_data = st.sidebar.checkbox("View world data")
view_country_data = st.sidebar.checkbox("View data for a specific country")
view_pie_chart = st.sidebar.checkbox("View pie chart of cases in different countries")

# If the user wants to view the world data, call the get_world_data function and display the data
if view_world_data:
    world_data = get_world_data()
    st.title("World data")
    st.json(world_data)

# If the user wants to view data for a specific country, display a dropdown menu to select the country
if view_country_data:
    st.title("Country data")
    countries = get_countries_data()
    country_names = [country['Country'] for country in countries]
    selected_country = st.selectbox("Select a country", country_names)
    country_data = get_country_data(selected_country)
    st.json(country_data)

if view_pie_chart:
    st.title("Pie chart of cases in different countries")
    countries = get_countries_data()
    labels = [country['Country'] for country in countries]
    cases = [country['TotalCases'] for country in countries]
    plt.pie(cases, labels=labels)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot() 