from dataclasses import dataclass
@dataclass
class Location:
    Location:str
    Latitude:float
    Longitude:float
    numero:int
    def __hash__(self):
        return hash(self.Location)