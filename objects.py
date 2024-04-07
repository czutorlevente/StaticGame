class PointLoad:
    def __init__(self, weight, distance):
        self.weight = float(weight)
        self.distance = float(distance)

class DistributedLoad:
    def __init__(self, weight, distance, width):
        self.weight = float(weight)
        self.distance = float(distance)
        self.width = float(width)

        # Calculate the equivalent point weight of the distributed weight
        self.overall_weight = float(weight) * float(width)
        # Calculate the distance of this equivalent point load from pillar 'A'
        self.distance_point_eq = (float(width)/ 2) + float(distance)