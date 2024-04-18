class D_Calculator:

    def polygon_centroid(vertices):
        """
        Calculate the centroid (geometric center) of a polygon.
        
        Parameters:
            vertices (list of tuples): List of tuples containing (x, y) coordinates of polygon vertices.
        
        Returns:
            tuple: (x, y) coordinates of the centroid.
        """
        # Number of vertices
        n = len(vertices)
        
        # Initialize centroid coordinates
        cx = cy = 0
        
        # Calculate signed area and centroid coordinates
        signed_area = 0
        for i in range(n):
            x0, y0 = vertices[i]
            x1, y1 = vertices[(i + 1) % n]  # Wrap around to the first vertex
            
            # Calculate the cross product
            cross_product = (x0 * y1) - (x1 * y0)
            
            # Update signed area
            signed_area += cross_product
            
            # Update centroid coordinates
            cx += (x0 + x1) * cross_product
            cy += (y0 + y1) * cross_product
        
        # Finalize centroid coordinates
        signed_area *= 0.5
        cx /= (6 * signed_area)
        cy /= (6 * signed_area)
        
        return (cx, cy)
    
    # Calculate sub areas and slope for the creation of the moment diagram:
    def moment_creator(vertices, line_2_y, line_3_y):
        final_moment_points = []
        last_moment = 0
        for i in range(len(vertices)):
            final_moment_points_1 = []
            if i != 0:
                if vertices[i][0] != vertices[i-1][0]: # if x is not the same as x for the one before
                    if vertices[i][1] == vertices[i-1][1]: # if y is the same as y for the one before
                        x_coordinates = [vertices[i-1][0] + (vertices[i][0] - vertices[i-1][0]) * j / (200 - 1) for j in range(200)]
                        slope = 0
                        intercept = vertices[i-1][1] - line_2_y
                        moment_values = [(slope * (x - x_coordinates[0])**2 / 2 + intercept * (x - x_coordinates[0]) + last_moment) for x in x_coordinates]
                        final_moment_points_1 = [x_coordinates, moment_values]
                    else: # if it is sloping downward
                        x_coordinates = [vertices[i-1][0] + (vertices[i][0] - vertices[i-1][0]) * j / (200 - 1) for j in range(200)]
                        slope = (vertices[i][1] - vertices[i-1][1]) / (vertices[i][0] - vertices[i-1][0])
                        intercept = vertices[i-1][1] - line_2_y
                        moment_values = [(slope * (x - x_coordinates[0])**2 / 2 + intercept * (x - x_coordinates[0]) + last_moment) for x in x_coordinates]
                        final_moment_points_1 = [x_coordinates, moment_values]
                    last_moment = moment_values[-1]
            final_moment_points.append(final_moment_points_1)
        return final_moment_points
        
                        



