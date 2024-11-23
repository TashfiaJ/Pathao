from services.ride_service import rides

drivers = [{"id": 1, "name": "Abir", "rating": 4, "location": "Badda", "coordinate_x": 5, "coordinate_y": 10},
           {"id": 1, "name": "Fahmid", "rating": 4, "location": "Badda", "coordinate_x": 5, "coordinate_y": 10},
           {"id": 1, "name": "Tarek", "rating": 4, "location": "Badda", "coordinate_x": 5, "coordinate_y": 10}
           ]

def get_all_available_rides():
    result = []
    for ride in rides:
        if ride.status == "pending":
            result.append(ride)

    return result

def ride_request_process(ride_id: int):
    for ride in rides:
        if ride.id == ride_id:
            ride.status = "Accepted"
            return {"message": "Request has been accepted"}
        
    return {"err": "An error has occured"}

def ride_mark_completed(ride_id: int):
    for ride in rides:
        if ride.id == ride_id:
            ride.status = "Completed"
            return {"message": "Request has been completed"}
        
    return {"err": "An error has occured"}

