import pygame

class Button:
    def __init__(self, x, y, width, height, text, font_size, color, glow_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.color = color
        self.glow_color = glow_color
        self.active = False

    def render(self, screen):
        if self.active:
            color = self.glow_color
        else:
            color = self.color

        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("monospace", self.font_size)
        text = font.render(self.text, 1, (255, 255, 255))
        screen.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def is_mouse_over(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        return False
    
# Modify button sizes and positions
button_s = Button(10, 10, 100, 30, "Save (S)", 20, (0, 0, 255), (0, 255, 0))
button_q = Button(10, 50, 100, 30, "Quit (Q)", 20, (0, 0, 255), (0, 255, 0))
button_a = Button(10, 90, 100, 30, "Axes (A)", 20, (0, 0, 255), (0, 255, 0))
button_r = Button(10, 130, 100, 30, "Reset (R)", 20, (0, 0, 255), (0, 255, 0))  # New reset button

# Add the new reset button to the list
buttons = [button_s, button_q, button_a, button_r]

    