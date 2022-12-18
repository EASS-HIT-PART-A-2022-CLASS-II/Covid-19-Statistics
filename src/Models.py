import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class singleCountry(BaseModel):
    Country:Optional[str]
    ThreeLetterSymbol:Optional[str]
    Infection_Risk:Optional[float]
    TotalCases:Optional[int]
    TotalDeaths:Optional[int]
    TotalRecovered:Optional[str]
    TotalTests:Optional[str]
    Population:Optional[str]
    ActiveCases:Optional[int]
    SeriousCritical:Optional[int]
    Message:Optional[str]
    class Config:
        orm_mode=True
    
    
