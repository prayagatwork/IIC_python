import requests

def get_travel_time(api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode=driving&key={api_key}"
    response = requests.get(url)
    result = response.json()

    # Extracting travel time in seconds
    travel_time_seconds = result['rows'][0]['elements'][0]['duration']['value']
    travel_time_hours = travel_time_seconds / 3600
    return travel_time_hours

def adjust_time_for_load(travel_time, load):
    # Assuming speed decreases by 10% per ton over 5 tons
    adjustment_factor = 1 + 0.1 * (load - 5) if load > 5 else 1
    return travel_time * adjustment_factor

# Example usage
api_key = "YOUR_GOOGLE_MAPS_API_KEY"
origin = "Ahmedabad, India"
destination = "Mumbai, India"

travel_time = get_travel_time(api_key, origin, destination)
adjusted_time = adjust_time_for_load(travel_time, 10)

print(f"Estimated travel time: {adjusted_time:.2f} hours")
