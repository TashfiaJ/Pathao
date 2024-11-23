from services.ride_service import rides
from services.driver_service import drivers
from datetime import datetime

users = [
    {"id": 1, "name": "Tash", "location": "Banani", "coordinate_x": 5, "coordinate_y": 10},
    {"id": 2, "name": "Fia", "location": "Uttara", "coordinate_x": 5, "coordinate_y": 10},
    {"id": 3, "name": "Anika", "location": "Mohakhali", "coordinate_x": 5, "coordinate_y": 10},
]

def request_ride(user_id: int, destination: str):
    current_location = None
    ride = None
    for user in users:
        if user.id == user_id:
            current_location = user.location
            break
    
    if current_location:
        ride_id = len(rides) + 1
        ride = {
            "id": ride_id,
            "pickup": current_location,
            "dropoff": destination,
            "user_id": user_id,
            "driver_id": "None",
            "status": "pending",
            "rating": 0,
            "ordered_time": datetime.now()
        }
        rides.append(ride)
        return ride
    
    return {"err": "Could not Process"}

def past_rides(user_id: int):
    ride_result = []

    for ride in rides:
        if ride.user_id == user_id:
            ride_result.append(ride)

    ride_result.sort(key = lambda x: x["ordered_time"], reverse = True)
    result = []
    for ride in ride_result:
        driver_name = None
        for driver in drivers:
            if driver.id == ride.driver_id:
                driver_name = driver.name
        result.append({"pickup": ride.pickup, "dropoff": ride.dropoff, "driver's name": driver_name, "rating": ride.rating})
    return result

def area_search(user_coordinate_x: float, user_coordinate_y: float, n: int):
    # I will measure distance between all drivers loaction and user location and then store it in a data structure and then sort them and based on that display only those where distance is less than or equal n

def rating(ride_id: int):
    # iterate through all the ride and if user_id and ride_id matches then user can add rating to that ride
    

        

    





