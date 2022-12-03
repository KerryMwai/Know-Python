class Planet:

    shape="Round"
    def __init__(self,name,radius,gravity,system):
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f"{self.name} is orbiting around the {self.system}"

    @classmethod
    def commons(cls):
        return f"All panets are {cls.shape} because of gravity"

    @staticmethod
    def spins(speed="40000 Km/Hr"):
        return f"The planet spins at {speed}"

