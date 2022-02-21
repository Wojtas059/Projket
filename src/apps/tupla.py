Optimal_Route = [(1, 5), (2, 3), (3, 1), (4, 2), (5, 4)]
Route = []
depotList = [1,2]
affectedAreaList = [3,4,5]

legs = dict(Optimal_Route)
routes = {}
for start in depotList :
    place = start
    routes[start] = []
    end_places = [ i for i in depotList if i != start ]
    while place not in end_places :
        routes[start].append((place,legs[place]))
        place = legs[place]

for i in routes.keys() :
    print(i,routes[i])

print([ i for i in routes.values()])