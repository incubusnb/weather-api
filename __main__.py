import json
import requests

# from src.location import Location


def main():
    endpoint = "https://api.open-meteo.com/v1/forecast"
    lat = 52.52
    long = 13.41
    tz = "America/Edmonton"
    time_format = "iso8601"  # "unixtime"
    temp_unit = "celsius"

    payload = {
        "latitude": lat,
        "longitude": long,
        "temperature_unit": temp_unit,
        "timezone": tz,
        "timeformat": time_format,
        "current_weather": True
        # "hourly": "temperature_2m",
    }
    r = requests.get(endpoint, params=payload)
    print(r.url)
    print(r.status_code)
    content = json.loads(r.text)
    print(json.dumps(content, indent=4))


if __name__ == "__main__":
    main()
