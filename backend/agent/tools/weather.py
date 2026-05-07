from strands import tool
import httpx


@tool
def get_weather(latitude: float, longitude: float) -> str:
    """Fetch current weather conditions for given GPS coordinates.
    If the user provides a city or place name instead, call geocode_location first to get coordinates.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    }
    resp = httpx.get("https://api.open-meteo.com/v1/forecast", params=params)
    resp.raise_for_status()
    c = resp.json()["current"]
    return (
        f"Temp: {c['temperature_2m']}°C | "
        f"Humidity: {c['relative_humidity_2m']}% | "
        f"Wind: {c['wind_speed_10m']} km/h"
    )
