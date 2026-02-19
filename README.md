# Event Hub API 🚀

A FastAPI based Event Aggregator backend that collects and serves tech events.

## Features
- Get all events
- Add new event
- Scrape events from website
- Seed demo events (10 sample events)
- REST API with Swagger docs

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- BeautifulSoup (Web Scraping)

## API Endpoints

### Home
GET /
Returns API status

### Get Events
GET /events

### Add Event
POST /events

### Scrape Events
GET /scrape

### Seed Demo Events
GET /seed

## Run Locally

```bash
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload
