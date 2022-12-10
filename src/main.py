import uvicorn
import http.client
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():

    conn = http.client.HTTPSConnection("imdb-top-100-movies.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "a463c18a92msha3eb294601ac463p198518jsna8e685091d4c",
        'X-RapidAPI-Host': "imdb-top-100-movies.p.rapidapi.com"
        }

    conn.request("GET", "/premiummovies/top17", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return {data.decode("utf-8")}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    