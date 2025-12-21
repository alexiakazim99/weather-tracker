from fastapi import FastAPI  # importterar fastapi för att skapa api 
from weather_api import get_weather, fetch_multiple_cities # importterar funktionerna från weather.api
import uvicorn #importerar servern som lör fastapi 

app = FastAPI() # skapar fastapi- applikation 

@app.get("/weather/{city}") #get- endspoint som hämtar väder för en stad 
def get_city_weather (sity:str): 
    result = get_weather(city) #anropar get_weather funktionen, en turpe

    if result: # kontrollerar om resut är något (ej none)
        temperature, city_name, date = result #packar upp de tre värderna från resultat 
        return {"city": city_name, "temperature": temperature, "date": date} #retunerar en dict med väderdata
    else:  # om result är none (något gick fel)
        return {"error": "Failed to fetch weather"} # retunerar fel medelande 


@app.get("/weather-multiple") # get end-point för många städer 
def get_multiple_weather(cities: str): # definerar funktion som tar en string
    cities_list = cities.split(",") # konverterar städerna till lista 
    result = fetch_multiple_cities(cities_list) # anropar fetch_m_city
    return {"weather_data": result} # retunerar en dict med väderdata 

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) # startar srver 

    #app = din FastAPI-applikation
    #host="127.0.0.1" = localhost (min dator)
    #port=8000 = port 8000