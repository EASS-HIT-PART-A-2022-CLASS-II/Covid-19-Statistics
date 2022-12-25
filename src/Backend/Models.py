import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class singleCountry(BaseModel):
    Country:str
    ThreeLetterSymbol:Optional[str]
    Infection_Risk:Optional[float]
    TotalCases:Optional[int]
    TotalDeaths:Optional[int]
    TotalRecovered:Optional[int]
    TotalTests:Optional[int]
    Population:Optional[int]
    Message:Optional[str]
    class Config:
        orm_mode=True
    
class AllWorld(BaseModel):
    TotalDeath:Optional[int]
    
    class config:
        orm_mode=True
