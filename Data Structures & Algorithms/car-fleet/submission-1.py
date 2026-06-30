class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        cars = list(zip(pos, speed))
        cars.sort(reverse=True)
        time = []
        fleet = 0
        fleet_time = 0
        
        for pos, speed in cars:
            time.append((target - pos) / speed)

        for i in time:
            if i > fleet_time:
                fleet += 1
                fleet_time = i

        return fleet