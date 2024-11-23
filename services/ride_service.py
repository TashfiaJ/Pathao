rides = []

def top_n_routes(n: int):
    ride_count = []

    for ride in rides:
        if ride.status == "completed":
            ride_count[ride["id"]] = ride_count.get(ride["id"], 0) + 1

    sorted_ride = sorted(ride_count.items(), key = lambda x: x[1], reverse = True)
    result = []
    for id, count in sorted_ride[:n]:
        result.append({"id": id, "count": count})
    return result


