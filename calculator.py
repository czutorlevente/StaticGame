import objects
import math

class Calculator:
    @staticmethod
    def support_reactions(weight_unit, distance_unit, weights, distances, ab_dist):

        print(f"Weights: {weights} Distances: {distances} AB Distance {ab_dist}")
        
        weight_moments = weights[0] * distances[0]
        moments_A = f"B(y)*{ab_dist} + {weights[0]}*({distances[0]})"

        for i in range(1, len(weights)):
            weight_moments += weights[i] * distances[i]
            moments_A += f" + {weights[i]}*{distances[i]}"

        all_weights = 0

        for weight in weights:
            all_weights += weight

        support_B = round(weight_moments / ab_dist, 3)
        support_A = round(all_weights - support_B, 3)
        all_weights = round(all_weights, 3)

        end_line_1 = f"\nMoments on A = {moments_A} = 0. \nSo based on that By = {support_B} {weight_unit} "
        end_line_2 = f"and because A(y) + B(y) = sum of all weights ({all_weights} {weight_unit}), \nA(y) = {support_A}"
        end_line_3 = f"\nSo the support reaction on pillar A is {support_A} {weight_unit} and on B is {support_B} {weight_unit}"
        end_line = end_line_1 + end_line_2 + end_line_3

        return support_A, support_B, end_line
    
    def calculate_width(point_loads, distributed_loads, ab_distance):

        full_width = 0
        positive_distance = 0
        negative_distance = 0

        for point_load in point_loads:
            if point_load.distance > 0:
                if point_load.distance > positive_distance:
                    positive_distance = point_load.distance
            elif point_load.distance < 0:
                if abs(point_load.distance) > negative_distance:
                    negative_distance = abs(point_load.distance)


        if ab_distance > full_width:
            full_width = ab_distance

        positive_d_d = 0
        negative_d_d = 0

        for distributed_load in distributed_loads:
            dist_distance = abs(distributed_load.distance) + distributed_load.width
            if distributed_load.distance > 0:
                if dist_distance > positive_d_d:
                    positive_d_d = dist_distance
            elif distributed_load.distance < 0:
                if dist_distance > negative_d_d:
                    negative_d_d = dist_distance
        
        if positive_d_d > positive_distance:
            positive_distance = positive_d_d

        if negative_d_d > negative_distance:
            negative_distance = negative_d_d

        if ab_distance > positive_distance:
            positive_distance = ab_distance

        full_width = positive_distance + negative_distance
        A_location = negative_distance

        return full_width, A_location


            

    