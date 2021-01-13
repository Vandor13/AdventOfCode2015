class ReindeerRacing:
    def __init__(self, filename):
        self.reindeer = []
        with open(filename, "r") as file:
            raw_reindeer_list = file.readlines()
        for raw_reindeer in raw_reindeer_list:
            raw_parts = raw_reindeer.split()
            self.reindeer.append((
                raw_parts[0],
                int(raw_parts[3]),
                int(raw_parts[6]),
                int(raw_parts[13])
            ))
        # print(self.reindeer)


    def race_by_second(self, time_of_race):
        distances = []
        scores = []
        for reindeer_number in range(len(self.reindeer)):
            distances.append(0)
            scores.append(0)
        for second in range(time_of_race):
            for reindeer_number in range(len(self.reindeer)):
                speed = self.reindeer[reindeer_number][1]
                speed_time = self.reindeer[reindeer_number][2]
                rest_time = self.reindeer[reindeer_number][3]
                cycle_time = speed_time + rest_time
                rest_of_cycle = second % cycle_time
                if rest_of_cycle < speed_time:
                    distances[reindeer_number] += speed
            # print(second, distances, scores)
            best_distance = max(distances)
            scores[distances.index(best_distance)] += 1
        for i in range(len(scores)):
            print(f"{self.reindeer[i][0]} has {scores[i]} points")


reindeer_racing = ReindeerRacing("InputData/d14.txt")
reindeer_racing.race_by_second(2503)
