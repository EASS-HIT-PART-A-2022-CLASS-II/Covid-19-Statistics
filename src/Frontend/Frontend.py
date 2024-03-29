import streamlit as st
import requests
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://mongodb:27017/Covid19")

db = client["Covid19_database"]
collection = db["Covid19_collection"]


st.sidebar.title("Select Option")

st.markdown(
  """
  <style>
      .block-container.css-12oz5g7.egzxvld2 {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqCLzGHDCWbv-_VeSlCpw2ISxtfcrGtGYxA&usqp=CAU');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top left;
        }
      .css-1offfwp.e16nr0p34 {
            color: black;
            background-color: #FAEBD7;
      }
      .st-be.st-bf.st-by.st-bz.st-c0.st-b3.st-c1.st-c2.st-bg.st-c3.st-c4.st-c5.st-c6 {
            background-color: #FAEBD7;
            color: black;
      }
      css-163ttbj.e1fqkh3o11 {
            background-color: #F0F8FF;x
            color: black;
      }
      css-1ec096l.edw49t14 {
            background-color: #F0F8FF;
            color: black;
      }
      css-ltmqks.e1tzin5v0 {
            background-color: #F0F8FF;
            color: black; 
      }
  </style>
  """
,unsafe_allow_html=True)
option = st.sidebar.selectbox("Select data to display", ["World Wide" , "Single Country View",  "All Countries Charts"])

if option == "World Wide":
  # Call the /get_all_world_covid_data endpoint
  response = requests.get("http://backend:8000/get_all_world_covid_data")
  data = response.json()

elif option == "Single Country View":
  # Call the /get_specific_country_covid_data endpoint and pass the user-specified country name as a parameter
  country = st.sidebar.text_input("Enter a country name")
  if country == "":
    country = "USA"
  response = requests.get(f"http://backend:8000/get_specific_country_covid_data/{country}")
  data = response.json()

elif option == "All Countries Charts":
  # Call the /get_all_countries_covid_data endpoint
  response = requests.get("http://backend:8000/get_all_countries_covid_data")
  data = response.json()

if option == "Single Country View":
  st.write(f"Country: {data['Country']}")
  st.write(f"Three Letter Symbol: {data['ThreeLetterSymbol']}")
  st.write(f"Infection Risk: {data['Infection_Risk']}")
  st.write(f"Total Cases: {data['TotalCases']}")
  st.write(f"Total Deaths: {data['TotalDeaths']}")
  st.write(f"Total Recovered: {data['TotalRecovered']}")
  st.write(f"Total Tests: {data['TotalTests']}")
  st.write(f"Population: {data['Population']}")
    # Create the chart
  countries = [data['Country']]
  total_cases = [data['TotalCases']]
  total_deaths = [data['TotalDeaths']]

  fig = make_subplots(rows=1, cols=2)

  fig.add_trace(go.Bar(x=countries, y=total_cases, name="Total Cases"), row=1, col=1)
  fig.add_trace(go.Bar(x=countries, y=total_deaths, name="Total Deaths"), row=1, col=2)

  fig.update_layout(barmode='group')
  st.plotly_chart(fig)
  
  
  results = collection.find({"country":data['Country']})
  img = ""
  for result in results:
    img = result["country_image"]
  st.image(img , width=200)

if option == "World Wide" or option == "All Countries Charts":
  countries = [d['Country'] for d in data]
  total_cases = [d['TotalCases'] for d in data]
  total_deaths = [d['TotalDeaths'] for d in data]
  total_recovered = [d['TotalRecovered'] for d in data]

  fig = make_subplots(rows=1, cols=3)
  fig.add_trace(go.Bar(x=countries, y=total_cases, name="Total Cases"), row=1, col=1)
  fig.add_trace(go.Bar(x=countries, y=total_deaths, name="Total Deaths"), row=1, col=2)
  fig.add_trace(go.Bar(x=countries, y=total_recovered, name="Total Recovered"), row=1, col=3)
  fig.update_layout(barmode='group')
  
  # Create the table data with specific information
  table_data = [{'Country': country, 'Total Cases': total_cases, 'Total Deaths': total_deaths, 'Total Recovered': total_recovered} for country, total_cases, total_deaths, total_recovered in zip(countries, total_cases, total_deaths, total_recovered)]
  

  
  st.plotly_chart(fig)
  # Display the table
  st.table(table_data)