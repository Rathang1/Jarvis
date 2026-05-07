from strands import tool
import httpx


@tool
def geocode_location(location: str) -> str:
    """Convert a place name (city, address, landmark) into GPS coordinates (latitude and longitude).
    Use this whenever the user mentions a location by name instead of providing coordinates.
    Always use the best available match — never ask the user for clarification.
    If the specific place isn't found, fall back to the broader city or region.
    """
    def _search(query: str):
        resp = httpx.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": query, "count": 1, "format": "json"},
        )
        resp.raise_for_status()
        return resp.json().get("results")

    results = _search(location)

    # If exact query fails, retry with progressively broader terms
    # e.g. "The Domain, Austin, TX" -> "Austin, TX" -> "Austin"
    if not results:
        parts = [p.strip() for p in location.split(",")]
        for i in range(1, len(parts)):
            results = _search(", ".join(parts[i:]))
            if results:
                break

    if not results:
        return f"No location found for '{location}'."

    r = results[0]
    return f"latitude={r['latitude']}, longitude={r['longitude']}, name={r['name']}, country={r['country']}"
