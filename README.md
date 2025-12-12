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

- **Python 3.x
- **FastAPI** - Web framework for building APIs
- **SQLite** - Database for storing weather data
- **Requests** - HTTP library for API calls
- **Uvicorn** - ASGI server

## Project Structure

weather-tracker/
├── weather_api.py      # Fetches weather data from WeatherAPI
├── database.py         # Database operations (create, save, retrieve)
├── main.py            # FastAPI application with endpoints
├── models.py          # Data models
├── requirements.txt   # Python dependencies
└── weather.db         # SQLite database (created automatically)


This project is for educational purposes.
