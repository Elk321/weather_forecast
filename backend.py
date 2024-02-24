import requests

API_KEY = "7f3c397786415eef0d56d9a22a42ca5f"


def get_data(place, forecast_days):
    url = (f"https://api.openweathermap.org/data/2.5/forecast?q={place}&"
           f"appid={API_KEY}&"
           f"units=metric")
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    filtered_data = data["list"][:nr_values]
    dates = [dict["dt_txt"] for dict in filtered_data]
    return dates, filtered_data
