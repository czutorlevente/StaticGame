import pygame
import math

# Define PointLoad and DistributedLoad classes (assuming they're defined elsewhere)

class PointLoad:
    def __init__(self, magnitude, location):
        self.magnitude = magnitude
        self.location = location

class DistributedLoad:
    def __init__(self, magnitude, start_location, end_location):
        self.magnitude = magnitude
        self.start_location = start_location
        self.end_location = end_location

def draw_screen(W, AB, FA, FB, AL, PL, DL, message, weight_unit, length_unit):
    # Initialize Pygame
    pygame.init()

    # Set up screen
    screen_width = 800
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Load Visualization")

    # Calculate unit_1
    unit_1 = 0.8 * screen_width / W

    # Draw white screen
    screen.fill((255, 255, 255))

    # Draw black line
    line_length = W * unit_1
    line_thickness = 5
    line_x = (screen_width - line_length) / 2
    line_y = screen_height / 2
    pygame.draw.line(screen, (0, 0, 0), (line_x, line_y), (line_x + line_length, line_y), line_thickness)

    # Draw arrow for FA
    arrow_color = (255, 0, 0)
    arrow_height = 50
    arrow_width = 20
    arrow_x = AL * unit_1 + (screen_width * 0.1)  # 10% from the left edge of the black line
    arrow_y = line_y + arrow_height
    pygame.draw.polygon(screen, arrow_color, [(arrow_x, arrow_y), (arrow_x + arrow_width / 2, arrow_y - arrow_height), (arrow_x + arrow_width, arrow_y)])
    font = pygame.font.Font(None, 36)
    text_surface = font.render(str(round(FA, 3)), True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(arrow_x + arrow_width / 2, arrow_y + arrow_height / 2))
    screen.blit(text_surface, text_rect)

    # Draw arrow for AB
    arrow_x_ab = arrow_x + AB * unit_1
    arrow_y_ab = line_y + arrow_height
    pygame.draw.polygon(screen, arrow_color, [(arrow_x_ab, arrow_y_ab), (arrow_x_ab + arrow_width / 2, arrow_y_ab - arrow_height), (arrow_x_ab + arrow_width, arrow_y_ab)])
    text_surface_ab = font.render(str(round(FB, 3)), True, (0, 0, 0))
    text_rect_ab = text_surface_ab.get_rect(center=(arrow_x_ab + arrow_width / 2, arrow_y_ab + arrow_height / 2))
    screen.blit(text_surface_ab, text_rect_ab)

    
    # Draw longer text at the top of the screen
    font = pygame.font.Font(None, 24)  # Define font
    text = message  # Your longer text here
    lines = text.split('\n')  # Split text into lines
    line_height = font.get_linesize()  # Get height of each line

    # Calculate total height of multiline text
    total_height = len(lines) * line_height

    y_pos = 30

    # Render and display each line
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))  # Render line
        text_rect = text_surface.get_rect(center=(screen_width / 2, y_pos))  # Center line horizontally and set y position
        screen.blit(text_surface, text_rect)  # Blit line onto the screen
        y_pos += line_height  # Move to next line

    # Update the display
    pygame.display.flip()

    # Wait for user to close window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

# Example usage:
#draw_screen(10, 5, -7.5, 8.3, 3, [PointLoad(5, 2)], [DistributedLoad(2, 1, 4)], "hi", "#", "feet")
