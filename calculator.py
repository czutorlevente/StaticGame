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

        support_B = (weight_moments / ab_dist)
        support_A = all_weights - support_B

        end_line_1 = f"\nMoments on A = {moments_A} = 0. \nSo based on that By = {support_B}{weight_unit} "
        end_line_2 = f"and because A(y) + B(y) = sum of all weights ({all_weights} {weight_unit}), \nA(y) = {support_A}"
        end_line_3 = f"\nSo the support reaction on pillar A is {support_A} {weight_unit} and on B is {support_B} {weight_unit}"
        end_line = end_line_1 + end_line_2 + end_line_3

        return support_A, support_B, end_line
    

    