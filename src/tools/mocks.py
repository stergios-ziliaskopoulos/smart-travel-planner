from langchain_core.tools import tool
import random

@tool
def search_flights(origin: str, destination: str, date: str) -> list:
    """Search for flights between origin and destination on a specific date."""
    # Mock data
    airlines = ["Ryanair", "EasyJet", "Lufthansa", "British Airways"]
    return [
        {
            "airline": random.choice(airlines),
            "price": random.randint(50, 300),
            "departure_time": "08:00 AM",
            "arrival_time": "10:30 AM",
            "origin": origin,
            "destination": destination,
            "date": date
        },
        {
            "airline": random.choice(airlines),
            "price": random.randint(50, 300),
            "departure_time": "02:00 PM",
            "arrival_time": "04:30 PM",
            "origin": origin,
            "destination": destination,
            "date": date
        }
    ]

@tool
def search_hotels(location: str) -> list:
    """Search for hotels in a specific location."""
    # Mock data
    hotel_names = ["Artemide", "Hilton", "Marriott", "Ibis", "The Plaza"]
    return [
        {
            "name": f"Hotel {random.choice(hotel_names)}",
            "price_per_night": random.randint(80, 500),
            "rating": round(random.uniform(3.5, 5.0), 1),
            "location": location
        },
        {
            "name": f"Hotel {random.choice(hotel_names)}",
            "price_per_night": random.randint(80, 500),
            "rating": round(random.uniform(3.5, 5.0), 1),
            "location": location
        }
    ]

@tool
def search_activities(location: str) -> list:
    """Search for activities and attractions in a specific location."""
    activities = ["Museum Tour", "City Walk", "Food Tasting", "Boat Ride"]
    return [
        {"name": f"{location} {act}", "price": random.randint(10, 50)} 
        for act in random.sample(activities, 2)
    ]
