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