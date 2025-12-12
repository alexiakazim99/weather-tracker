# Weather Tracker

A Python application that collects, stores, and provides access to weather data through a REST API.

## Project Overview

This project fetches weather data from WeatherAPI, stores it in a SQLite database, and provides API endpoints to query the stored data.

## Features

- Fetch real-time weather data for any city
- Store weather history in SQLite database
- REST API to access stored weather data
- Error handling for API calls and database operations

## Tech Stack

- **Python 3.x**
- **FastAPI** - Web framework for building APIs
- **SQLite** - Database for storing weather data
- **Requests** - HTTP library for API calls
- **Uvicorn** - ASGI server

## Project Structure
```
weather-tracker/
├── weather_api.py      # Fetches weather data from WeatherAPI
├── database.py         # Database operations (create, save, retrieve)
├── main.py            # FastAPI application with endpoints
├── models.py          # Data models
├── requirements.txt   # Python dependencies
└── weather.db         # SQLite database (created automatically)
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/weather-tracker.git
cd weather-tracker
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /weather` - Retrieve all weather data
- `GET /weather/{city}` - Get weather for specific city
- `POST /weather` - Save new weather data

## Database Schema

**Table: weather**
- `id` - Primary key (auto-increment)
- `city` - City name (TEXT)
- `temperature` - Temperature in Celsius (REAL)
- `date` - Date of record (TEXT)

## Usage Example
```python
# Fetch weather for Stockholm
get_weather("Stockholm")

# Save to database
save_weather("Stockholm", 5.2, "2024-12-08")

# Retrieve all data
get_all_weather()
```

## Author

Alexia kazim

## License

This project is for educational purposes.
