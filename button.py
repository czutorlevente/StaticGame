import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Button:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, BLACK)
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

class TextInput:
    def __init__(self, rect):
        self.rect = rect
        self.text = ''
        self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        if self.active:
            pygame.draw.rect(surface, BLACK, self.rect, 2)
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, BLACK)
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Button and Text Input Example")

    # Create a button
    button_rect = pygame.Rect(300, 200, 200, 50)
    button = Button("Click Me", button_rect)

    # Create a text input field
    text_input_rect = pygame.Rect(300, 300, 200, 50)
    text_input = TextInput(text_input_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            text_input.handle_event(event)

        screen.fill(WHITE)
        button.draw(screen)
        text_input.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()