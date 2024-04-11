import pygame
import math

def draw_screen(W, AB, FA, FB, AL, PL, DL, message, weight_unit, length_unit):
    # Initialize Pygame
    pygame.init()

    # Set up screen
    screen_width = 900
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Load Visualization")

    # Calculate unit_1
    unit_1 = 0.8 * screen_width / W

    # Draw white screen
    screen.fill((255, 255, 255))

    # Draw lines
    line_length = W * unit_1
    line_thickness = 5
    line_x = (screen_width - line_length) / 2
    line_y = (screen_height / 7) * 2
    pygame.draw.line(screen, (0, 0, 0), (line_x, line_y), (line_x + line_length, line_y), line_thickness)

    line_2_y = (screen_height / 7) * 4
    pygame.draw.line(screen, (0, 0, 0), (line_x, line_2_y), (line_x + line_length, line_2_y), line_thickness)

    line_3_y = (screen_height / 7) * 6
    pygame.draw.line(screen, (0, 0, 0), (line_x, line_3_y), (line_x + line_length, line_3_y), line_thickness)

    # Initialize list that will be a list of touples containing x values, force values, and slope (for distributed loads)
    all_points = []

    # Step 1 to set up vertical scale:
    largest_vertical_value = FA
    if FB > largest_vertical_value:
        largest_vertical_value = FB

    # Draw distributed loads
    for dist_load in DL:
        distributed_x = AL * unit_1 + screen_width * 0.1 + dist_load.distance * unit_1
        distributed_y = line_y - 20
        dist_width = dist_load.width * unit_1
        dist_weight = dist_load.weight
        overall_w = dist_load.overall_weight

        # Add to point list
        all_points.append(["D1", distributed_x, dist_weight])
        all_points.append(["D2", distributed_x + dist_width])

        if overall_w > largest_vertical_value: # for vertical scale
            largest_vertical_value = overall_w

        if dist_weight % 1 == 0:
            dist_weight = int(dist_weight)
        pygame.draw.line(screen, (200, 180, 150), (distributed_x, distributed_y), (distributed_x + dist_width, distributed_y), 30)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(str(dist_weight) + " " + weight_unit + "/" + length_unit, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(distributed_x + dist_width / 2, distributed_y))
        screen.blit(text_surface, text_rect)



    # Draw arrow for FA
    arrow_color = (255, 0, 0)
    arrow_height = 50
    arrow_width = 20
    arrow_x = AL * unit_1 + (screen_width * 0.1)

    # Add to point list
    all_points.append(["P", arrow_x, -FA])

    #Make sure that arrow is pointing at the right location
    arrow_x = arrow_x - (arrow_width / 2)
    arrow_y = line_y + arrow_height
    pygame.draw.polygon(screen, arrow_color, [(arrow_x, arrow_y), (arrow_x + arrow_width / 2, arrow_y - arrow_height), (arrow_x + arrow_width, arrow_y)])
    font = pygame.font.Font(None, 36)
    text_surface = font.render(str(round(FA, 3)) + " " + weight_unit, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(arrow_x + arrow_width / 2, arrow_y + arrow_height / 2))
    screen.blit(text_surface, text_rect)

    # Draw arrow for FB
    arrow_x_ab = arrow_x + AB * unit_1
    arrow_y_ab = line_y + arrow_height
    pygame.draw.polygon(screen, arrow_color, [(arrow_x_ab, arrow_y_ab), (arrow_x_ab + arrow_width / 2, arrow_y_ab - arrow_height), (arrow_x_ab + arrow_width, arrow_y_ab)])
    text_surface_ab = font.render(str(round(FB, 3)) + " " + weight_unit, True, (0, 0, 0))
    text_rect_ab = text_surface_ab.get_rect(center=(arrow_x_ab + arrow_width / 2, arrow_y_ab + arrow_height / 2))
    screen.blit(text_surface_ab, text_rect_ab)

    # Add B to point list
    all_points.append(["P", arrow_x_ab + arrow_width / 2, -FB])

    
    # Draw longer text at the top of the screen
    font_m = pygame.font.Font(None, 20)  # Define font
    text = message  # Your longer text here
    lines = text.split('\n')  # Split text into lines
    line_height = font_m.get_linesize()  # Get height of each line

    y_pos = 10

    # Render and display each line
    for line in lines:
        text_surface = font_m.render(line, True, (0, 0, 0))  # Render line
        text_rect = text_surface.get_rect(center=(screen_width / 2, y_pos))  # Center line horizontally and set y position
        screen.blit(text_surface, text_rect)  # Blit line onto the screen
        y_pos += line_height  # Move to next line

    # Draw arrow pointing downward
    for point_load in PL:
        pl_distance = point_load.distance
        pl_weight = point_load.weight
        if pl_weight > largest_vertical_value: # For setting up vertical scale
            largest_vertical_value = pl_weight
        arrow_x_down = arrow_x + pl_distance * unit_1  # 3 unit_1 to the right of FA
        arrow_y_down = line_y - arrow_height  # Same height as the FA arrow
        pygame.draw.polygon(screen, (0, 255, 0), [(arrow_x_down, arrow_y_down), 
                                                (arrow_x_down + arrow_width / 2, arrow_y_down + arrow_height), 
                                                (arrow_x_down + arrow_width, arrow_y_down)])
        text_surface_load = font.render((str(pl_weight) + " " + weight_unit), True, (0, 0, 0))
        text_rect_load = text_surface_load.get_rect(center=(arrow_x_down + arrow_width / 2, arrow_y_down - arrow_height/2))
        screen.blit(text_surface_load, text_rect_load)

        # Add to point list
        all_points.append(["P", arrow_x_down + arrow_width / 2, pl_weight])

    # Vertical scale final setup:
    unit_2 = (screen_height/7.1) / largest_vertical_value

    def point_list_sort(item):
        # Sort by the second element (smaller_list[1])
        # If second elements are equal, prioritize "D1" or "D2" over "P"
        return (item[1], 0 if item[0] in ["D1", "D2"] else 1)
    
    all_points = sorted(all_points, key=point_list_sort)
    print(all_points)

    # Update the display
    pygame.display.flip()

    # Wait for user to close window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

