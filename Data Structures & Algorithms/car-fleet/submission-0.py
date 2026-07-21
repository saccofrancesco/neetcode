class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: List[tuple[int, int]] = sorted(zip(position, speed), reverse=True)
        fleet_count: int = 0
        fleet_arrival_time = 0.0
        for car_position, car_speed in cars:
            arrival_time = (target - car_position) / car_speed
            if arrival_time > fleet_arrival_time:
                fleet_count += 1
                fleet_arrival_time = arrival_time
        return fleet_count