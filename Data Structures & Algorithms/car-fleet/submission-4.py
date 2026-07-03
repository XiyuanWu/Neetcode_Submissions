class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        times = sorted(list(zip(pos, speed)), reverse=True)
        fleet = 0
        fleet_time = 0

        for pos, speed in times:
            time = (target - pos) / speed

            if time > fleet_time:
                fleet += 1
                fleet_time = time

        return fleet


