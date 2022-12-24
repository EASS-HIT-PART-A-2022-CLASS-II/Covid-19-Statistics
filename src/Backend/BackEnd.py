import uvicorn
import requests
from fastapi import FastAPI
from .Models import *

app = FastAPI()

# Set the API key and host for the COVID API
API_KEY = "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c"
API_HOST = "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"

@app.get("/get_all_world_covid_data") #  all world covid data
def World_Data():

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/world"

    headers = {
        "X-RapidAPI-Key": "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c",
        "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    response_data= response.json()
    return (response_data)

@app.get("/get_all_countries_covid_data") #  each country covid data
def index2():

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries"

    headers = {
        "X-RapidAPI-Key": "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c",
        "X-RapidAPI-Host":"vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    
    response_data= response.json()
    return (response_data)



@app.get("/get_specific_country_covid_data/{country}",response_model=singleCountry,response_model_exclude_unset=True) #  specific country covid data
def specicif_country(country):

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries"

    headers = {
        "X-RapidAPI-Key": "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c", 
        "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    
    response_data= response.json()
    for i in response_data:
        singleCountry.Country = "" # solve the saving last input problem
        singleCountry.ThreeLetterSymbol = ""
        singleCountry.Infection_Risk = 0
        singleCountry.TotalCases = 0
        singleCountry.TotalDeaths = 0
        singleCountry.TotalRecovered = ""
        singleCountry.TotalTests = ""
        singleCountry.Population = ""
        singleCountry.ActiveCases = 0
        if i['Country'] == country:  # search by country - user input
            singleCountry.Country=i['Country'] # value i want to show
            singleCountry.ThreeLetterSymbol=i['ThreeLetterSymbol'] # value i want to show
            singleCountry.Infection_Risk=i['Infection_Risk'] # value i want to show
            singleCountry.TotalCases=i['TotalCases'] # value i want to show
            singleCountry.TotalDeaths=i['TotalDeaths'] # value i want to show
            singleCountry.TotalRecovered=i['TotalRecovered'] # value i want to show
            singleCountry.TotalTests=i['TotalTests'] # value i want to show
            singleCountry.Population=i['Population'] # value i want to show
            singleCountry.ActiveCases=i['ActiveCases'] # value i want to show
            singleCountry.Message="OK"
            return singleCountry
        
    singleCountry.Message='Country not found' # if not found
    return singleCountry

if __name__ == "__BackEnd__":
    uvicorn.run("BackEnd:app", port=8000, reload=True)
    