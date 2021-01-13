from itertools import permutations

class TravelingSanta:
    def __init__(self, filename):
        self.places = list()
        self.distances = dict()
        self.read_file(filename)
        self.travel()

    def read_file(self, filename):
        with open(filename, "r") as file:
            raw_distances = file.readlines()
        for raw_distance in raw_distances:
            distance_parts = raw_distance.strip("\n").split()
            if distance_parts[0] in self.distances.keys():
                start_dict = self.distances[distance_parts[0]]
                start_dict[distance_parts[2]] = int(distance_parts[4])
                self.distances[distance_parts[0]] = start_dict
            else:
                start_dict = dict()
                start_dict[distance_parts[2]] = int(distance_parts[4])
                self.distances[distance_parts[0]] = start_dict
            if distance_parts[2] in self.distances.keys():
                start_dict = self.distances[distance_parts[2]]
                start_dict[distance_parts[0]] = int(distance_parts[4])
                self.distances[distance_parts[2]] = start_dict
            else:
                start_dict = dict()
                start_dict[distance_parts[0]] = int(distance_parts[4])
                self.distances[distance_parts[2]] = start_dict
            if distance_parts[0] not in self.places:
                self.places.append(distance_parts[0])
            if distance_parts[2] not in self.places:
                self.places.append(distance_parts[2])
        print("Places:", self.places)

    def travel(self):
        best_route_length = 99999
        worst_route_length = 0
        best_route = []
        worst_route = []
        for possible_route in permutations(self.places, len(self.places)):
            route_length = 0
            current_position = None
            for place in possible_route:
                if not current_position:
                    current_position = place
                else:
                    position_dict = self.distances[current_position]
                    if place in position_dict.keys():
                        route_length += position_dict[place]
                    else:
                        route_length = 99999
                        break
                    current_position = place
            if route_length < best_route_length:
                best_route_length = route_length
                best_route = possible_route
            if route_length > worst_route_length:
                worst_route_length = route_length
                worst_route = possible_route
        print("Best route:")
        print(best_route)
        print("Distance:", best_route_length)
        print("Worst route:")
        print(worst_route)
        print("Distance:", worst_route_length)


TravelingSanta("InputData/d9.txt")
