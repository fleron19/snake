import pygame


class field():
    def __init__(self, width, height):
        self.height = height
        self.width = width


class snake():
    def __init__(self, x, y, length, dir):
        self.x = x
        self.y = y
        self.length = length
        self.dir = dir


if __name__ == '__main__':
    running = True
    pygame.init()
    line_width = 2
    Snake = snake([6, 7], [7, 7], 2, 'r')
    Snake_Field = field(15, 15)
    x = Snake_Field.width * 50 + line_width
    y = Snake_Field.height * 50 + line_width
    size = (x, y)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")
    speed = 4
    FPS = 60
    count_goal = FPS/speed
    count = 0
    clock = pygame.time.Clock()
    while running:
        # Handle events
        for event in pygame.event.get():
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and Snake.dir != "r":
                    Snake.dir = "l"
                elif event.key == pygame.K_RIGHT and Snake.dir != "l":
                    Snake.dir = "r"
                elif event.key == pygame.K_UP and Snake.dir != "d":
                    Snake.dir = "u"
                elif event.key == pygame.K_DOWN and Snake.dir != "u":
                    Snake.dir = "d"
            if event.type == pygame.QUIT:
                running = False

        # Draw shapes
        window.fill((0, 122, 122))
        for i in range(x):
            if i % 50 == 0:
                pygame.draw.line(window, (0, 0, 0), [i, 0], [i, y], line_width)
        for j in range(y):
            if j % 50 == 0:
                pygame.draw.line(window, (0, 0, 0), [0, j], [x, j], line_width)
        for i in range(Snake.length):
            pygame.draw.rect(window, (0, 255, 0),
                            (Snake.x[i] * 50 + 2, Snake.y[i] * 50 + 2, 50 - 2, 50 - 2))

        if count == count_goal:
            if Snake.dir == "u":
                for i in range(Snake.length):
                    Snake.y[i] -= 1
            elif Snake.dir == "d":
                for i in range(Snake.length):
                    Snake.y[i] += 1
            elif Snake.dir == "l":
                for i in range(Snake.length):
                    Snake.x[i] -= 1
            elif Snake.dir == "r":
                for i in range(Snake.length):
                    Snake.x[i] += 1
            count = 0
        count += 1
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
