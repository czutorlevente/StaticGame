class Calculator:
    @staticmethod
    def support_reactions(weight_unit, distance_unit):
        weight_number = int(input("How many point loads does this bridge hold? "))
        distributed_weight_number = int(input("How many distributed loads does this bridge hold? "))

        weights = [0] * (weight_number + distributed_weight_number)
        distances = [0] * (weight_number + distributed_weight_number)
        all_weights = 0

        for i in range(weight_number):
            weights[i] = float(input(f"Weight of point load {i + 1} in {weight_unit}: "))
            weights[i] = point_load
            distances[i] = float(input(f"Distance of point load {i + 1} from pillar 'A' in {distance_unit}\n(positive to the right, negative to the left): "))
            all_weights += weights[i]

        for i in range(distributed_weight_number):
            width_d = float(input(f"Width of distributed load {i + 1} in {distance_unit}: "))
            distance_d = float(input(f"Distance of closest end of distributed load {i + 1} from pillar 'A'\n in {distance_unit} (positive to the right, negative to the left): "))
            amount_d = float(input(f"Load amount of distributed load {i + 1} ({weight_unit}/{distance_unit}): "))

            distributed_results = Calculator.distributed_loads(width_d, amount_d, distance_d)
            weights[weight_number + i], distances[weight_number + i] = distributed_results
            all_weights += weights[weight_number + i]

        pillar_distance = float(input(f"Distance of pillar 'B' from pillar 'A' in {distance_unit}\n(positive to the right, negative to the left): "))

        weight_moments = weights[0] * distances[0]
        moments_A = f"B(y)*{pillar_distance} + {weights[0]}*({distances[0]})"

        for i in range(1, weight_number + distributed_weight_number):
            weight_moments += weights[i] * distances[i]
            moments_A += f" + {weights[i]}*{distances[i]}"

        support_B = (weight_moments / pillar_distance)
        support_A = all_weights - support_B

        end_line_1 = f"\nMoments on A = {moments_A} = 0. So based on that By = {support_B} {weight_unit}"
        end_line_2 = f"and because A(y) + B(y) = sum of all weights ({all_weights} {weight_unit}), A(y) = {support_A}"
        end_line_3 = f"\nSo the support reaction on pillar A is {support_A} {weight_unit} and on B is {support_B} {weight_unit}"
        end_line = end_line_1 + end_line_2 + end_line_3
        print(end_line)

    @staticmethod
    def distributed_loads(width, amount, distance):
        load_amount = width * amount

        if distance < 0:
            width = -width
        load_distance = (width / 2) + distance

        return load_amount, load_distance