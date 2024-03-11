import pygame
import math

w = 800
h = 600

window = pygame.display.set_mode((w, h))

bg_color = (255, 255, 255)
items_color = (150, 100, 255)
window.fill(bg_color)

first_click = False
drawn_circle = False
drawn_line = False
start_drawn_line = False
circle = []
start_line = (0, 0)
end_line = (0, 0)
radio = 0
x1, y1, x2, y2 = 0, 0, 0, 0


def calculate_radio(ca, co):
    return math.sqrt(ca ** 2 + co ** 2)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            first_click = True

        if event.type == pygame.MOUSEMOTION:
            if first_click:
                window.fill(bg_color)
                x2, y2 = event.pos
                if len(circle) > 0:
                    pygame.draw.circle(window, items_color, (circle[0], circle[1]), circle[2], 4)
                    start_drawn_line = True
                if drawn_circle:
                    start_line = (x1, y1)
                    pygame.draw.line(window, items_color, (x1, y1), (x2, y2), 4)

                else:
                    radio = calculate_radio(x2 - x1, y2 - y1)
                    pygame.draw.circle(window, items_color, (x1, y1), radio, 4)
                    pygame.draw.circle(window, bg_color, (x1, y1), radio - 0.09 * radio)

        if event.type == pygame.MOUSEBUTTONUP:
            drawn_circle = True
            first_click = False
            circle = [x1, y1, radio]

        if event.type == pygame.MOUSEBUTTONUP and start_drawn_line:
            drawn_line = True
            end_line = (x2, y2)

        pygame.display.update()

        if drawn_line:
            window.fill(bg_color)
            pygame.draw.circle(window, items_color, start_line, circle[2], 4)

            for i in range(0, 100):
                window.fill(bg_color)
                x = x1 + (x2 - x1) * i / 100
                y = y1 + (y2 - y1) * i / 100
                pygame.draw.circle(window, items_color, (int(x), int(y)), circle[2], 4)
                pygame.display.update()
                pygame.time.delay(50)

            first_click = False
            drawn_circle = False
            drawn_line = False
            start_drawn_line = False
            circle = []
            start_line = (0, 0)
            end_line = (0, 0)
            radio = 0
            x1, y1, x2, y2 = 0, 0, 0, 0


