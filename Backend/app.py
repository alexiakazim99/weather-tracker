from fastapi import FastAPI # importterar fastapi för att skapa api
from fastapi.middleware.cors import CORSMiddleware # Importera CORS-middleware för att tillåta förfrågningar från React
from weather_api import get_weather, fetch_multiple_cities # importterar funktionerna från weather.api
from database import get_all_weather # vi importerar denna funktion från bd 
import uvicorn # importerar servern som lör fastapi


app = FastAPI() # skapar fastapi-applikation

# === CORS CONFIGURATION ===
# CORS (Cross-Origin Resource Sharing) tillåter React på port 3000 att kommunicera med backend på port 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Tillåt förfrågningar från React på localhost:3000
    allow_credentials=True,  # Tillåt credentials (cookies, etc)
    allow_methods=["*"],  # Tillåt alla HTTP-metoder (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Tillåt alla headers
)


@app.get("/weather/{city}") # get-endpoint som hämtar väder för en stad
def get_city_weather(city: str): # denna funktion tar en stad som parameter
    result = get_weather(city) # anropar get_weather funktionen, returnerar en tupel [temp, city, date]
   
    if result: # kontrollerar om result är något (ej none)
        temperature, city_name, date = result # packar upp de tre värderna från resultat
        # Returnera samma format som weather-multiple för konsistens
        return {"weather_data": [[temperature, city_name, date]]} # retunerar weather_data med en lista innehållade väderdata
    else: # om result är none (något gick fel)
        return {"error": "Failed to fetch weather"} # retunerar fel medelande


@app.get("/weather-multiple") # get-endpoint för många städer
def get_multiple_weather(cities: str): # definerar funktion som tar en string med städer separerade med komma
    cities_list = cities.split(",") # konverterar städerna till lista (delad på komma)
    result = fetch_multiple_cities(cities_list) # anropar fetch_multiple_cities och passar listan
    # Returnerar väderdata i rätt format: {"weather_data": [[temp, city, date], [temp, city, date], ...]}
    return {"weather_data": result} # retunerar en dict med väderdata som en lista

@app.get("/weather-history")
def get_weather_history():
    data = get_all_weather()  # Anropar från database.py
    return {
        "total_searches": len(data),
        "weather_history": data
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) # startar server

    #app = din FastAPI-applikation
    #host="127.0.0.1" = localhost (min dator)
    #port=8000 = port 8000