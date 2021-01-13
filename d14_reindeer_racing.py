class ReindeerRacing:
    def __init__(self, filename):
        self.reindeer = dict()
        self.reindeer_names = []
        with open(filename, "r") as file:
            raw_reindeer_list = file.readlines()
        for raw_reindeer in raw_reindeer_list:
            raw_parts = raw_reindeer.split()
            self.reindeer[raw_parts[0]] = (
                int(raw_parts[3]),
                int(raw_parts[6]),
                int(raw_parts[13])
            )
            self.reindeer_names.append(raw_parts[0])
        # print(self.reindeer)

    def race_reindeer(self, time_of_race):
        best_reindeer = None
        best_distance = 0
        for reindeer in self.reindeer.items():
            name = reindeer[0]
            values = reindeer[1]
            speed = values[0]
            speed_time = values[1]
            rest_time = values[2]
            # print(f"{name} can reach {speed}km/s for {speed_time} seconds before resting for {rest_time} seconds")
            cycle_time = speed_time + rest_time
            no_cycles = time_of_race // cycle_time
            distance = speed * speed_time * no_cycles
            rest_of_cycle = time_of_race % cycle_time
            distance += min(speed_time, rest_of_cycle) * speed
            # print(f"{no_cycles} cycles and {rest_time} seconds")
            print(f"{name} reaches {distance}km")
            if distance > best_distance:
                best_reindeer = name
                best_distance = distance
        print()
        print(f"{best_reindeer} wins with a distance of {best_distance}")


reindeer_racing = ReindeerRacing("InputData/d14.txt")
reindeer_racing.race_reindeer(2503)
