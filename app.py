from fastapi import FastAPI  # importterar fastapi för att skapa api 
from weather_api import get_weather, fetch_multiple_cities # importterar funktionerna från weather.api

app = FastAPI() # skapar fastapi- applikation 

@app.get("/weather/{city}") #get- endspoint som hämtar väder för en stad 
def get_city_weather (sity:str): 
    result = get_weather(city) #anropar get_weather funktionen 

    if result: # kontrollerar om resut är något (ej none)
        temperature, city_name, date = result #packar upp de tre värderna från resultat 
        return {"city": city_name, "temperature": temperature, "date": date} #retunerar en dict med väderdata
    else:  # om result är none (något gick fel)
        return {"error": "Failed to fetch weather"} # retunerar fel medelande 



