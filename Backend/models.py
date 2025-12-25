from pydantic import BaseModel
# Importerar BaseModel från pydantic för att skapa data-modeller
class Weather(BaseModel): # Modell för EN väder-data
    city: str  # Stad-namn måste vara text
    temperature: float # Temperatur måste vara ett decimaltal
    date: str  # Datum måste vara text

class MultipleWeather(BaseModel): # Modell för MÅNGA väder-data
    weather_data: list # En lista med väder-data

class WeatherResponse(BaseModel): # Modell för API-svar när du hämtar väder
    city: str  # Stad-namn
    temperature: float  # Temperatur
    date: str  # Datum

class ErrorResponse(BaseModel): # Modell för felmeddelanden
    error: str # Felmeddelande som text