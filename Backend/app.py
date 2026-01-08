from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from weather_api import get_weather, fetch_multiple_cities 
from database import get_all_weather
import uvicorn 

app = FastAPI() 

# === CORS CONFIGURATION ===
# CORS (Cross-Origin Resource Sharing) tillåter React på port 3000 att kommunicera med backend på port 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Tillåt förfrågningar från React på localhost:3000
    allow_credentials=True,  # Tillåt credentials (cookies, etc)
    allow_methods=["*"],  # Tillåt alla HTTP-metoder (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Tillåt alla headers
)


@app.get("/weather/{city}") 
def get_city_weather(city: str): 
    result = get_weather(city) 
   
    if result: 
        temperature, city_name, date = result 
    
        return {"weather_data": [[temperature, city_name, date]]} 
    else: 
        return {"error": "Failed to fetch weather"} 

@app.get("/weather-multiple") 
def get_multiple_weather(cities: str): 
    cities_list = cities.split(",") 
    result = fetch_multiple_cities(cities_list) 
    return {"weather_data": result} 

@app.get("/weather-history")
def get_weather_history():
    data = get_all_weather()  
    return {
        "total_searches": len(data),
        "weather_history": data
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 

