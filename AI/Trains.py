trainline = {"Exeter": [("Exmouth",8),("Dawlish",8),("Plymouth",60)],
             "Exmouth":[("Exeter",8)],
             "Dawlish":[("Exeter",8),("Torquay",7)],
             "Torquay":[("Dawlish",7),("Plymouth",46)],
             "Plymouth":[("Torquay",45),("Exeter",60)]
             }

def get_connections(station, distance, routes, visited):
    journeys = trainline[station]
    for pair in journeys:
        if routes == []:
            routes = journeys.copy()
        else:
            if pair[0] in visited:
                print()
            else:
                routes.append((pair[0],distance + pair[1]))
                routepoint[(pair[0],distance + pair[1])] = visited.copy()
    return routes



def search(routes, visited):
    if routes[0][0] not in visited:
        working_distance = routes[0][1]
    else:
        working_distance = routes[1][1]
    for pair in routes:
        if pair[1] <= working_distance:
            if pair[0] not in visited:
                rroute = pair
                working_distance = pair[1]
                return_station = pair[0]
    distance = working_distance
    
    return return_station, distance, rroute

def purge(routes):
    for places in routes:
        for vplace in visited:
            if places[0] == vplace:
                routes.remove(places)

    return routes

possible = list(trainline.keys())
print("Possible train stations: ")
print(possible)
start_station = input("Enter start station (eg. Exmouth): ")
target_station = input("Enter target station (eg. Plymouth): ")
next_station = ""
last_station = ""
routes = []
visited = []
routepoint = {}
distance = 0
current_station = start_station
if current_station != target_station:
    while current_station != target_station:
        visited.append(current_station)
        routes = get_connections(current_station, distance, routes, visited)
        next_station, distance, rroute = search(routes, visited)
        last_station = current_station
        current_station = next_station
        routes = purge(routes)


    routepoint[rroute].append(rroute[0])
    print("Route taken: ")
    print(routepoint[rroute])
    print("Distance: ")
    print(distance)
else:
    print("Already at target station!")
