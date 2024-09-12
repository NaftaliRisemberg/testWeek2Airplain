from airplane import Airplane
from pilot import Pilot
from target import Target

class OfferAttack(Airplane, Target, Pilot):
    def __init__(self, target_city, priority, assigned_pilot, distance, weather_conditions,
                 pilot_skill, aircraft_speed, fuel_capacity, mission_fit_score):
        Airplane.__init__(self,aircraft_speed, fuel_capacity)
        Pilot.__init__(self, assigned_pilot, pilot_skill)
        Target.__init__(self, target_city, priority)
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.mission_fit_score = mission_fit_score

