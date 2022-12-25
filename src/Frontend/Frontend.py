import streamlit as st
import requests
import matplotlib.pyplot as plt
import json
import pandas as pd


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
view_world_data = st.sidebar.button("View world data")
view_country_data = st.sidebar.button("View data for a specific country")
view_pie_chart = st.sidebar.button("5M and above")

# If the user wants to view the world data, call the get_world_data function and display the data
if view_world_data:
    world_data = get_world_data()
    st.title("World data")
    st.json(world_data)
    
    countries = get_countries_data()
    labels = [country['Country'] for country in countries]
    cases = [country['TotalCases'] for country in countries]
    plt.pie(cases, labels=labels)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot() 
    
# If the user wants to view data for a specific country, display a dropdown menu to select the country

if view_country_data:
    st.title("Country data")
    countries = get_countries_data()
    country_names = [Country['Country'] for Country in countries]
    selected_country = st.selectbox("Select a country", country_names)
    country_data = get_country_data(selected_country)

    # Convert the country data dictionary into a Pandas DataFrame
    df = pd.DataFrame.from_dict(country_data, orient='index', columns=['Value'])

    # Display the table using st.table
    st.table(df)



if view_pie_chart:
    st.title("Pie chart of different countries with 5M cases and above!")
    countries = get_countries_data()
    # Filter the countries list to only include countries with more than 5,000,000 cases
    countries_filtered = [country for country in countries if country['TotalCases'] > 5000000]
    labels = [country['Country'] for country in countries_filtered]
    cases = [country['TotalCases'] for country in countries_filtered]
    plt.pie(cases, labels=labels)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot() 

   