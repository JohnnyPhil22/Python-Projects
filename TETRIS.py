import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SIDEBAR_WIDTH = 200

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

COLORS = [BLACK, LIGHT_BLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDEBAR_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()


class Shape:
    def __init__(self):
        self.x = 3
        self.y = 0
        self.color = random.randint(1, 7)

        # Tetromino shapes
        square = [[1, 1], [1, 1]]

        i_shape = [[1, 1, 1, 1]]

        t_shape = [[1, 1, 1], [0, 1, 0]]

        l_shape = [[1, 0], [1, 0], [1, 1]]

        j_shape = [[0, 1], [0, 1], [1, 1]]

        s_shape = [[0, 1, 1], [1, 1, 0]]

        z_shape = [[1, 1, 0], [0, 1, 1]]

        shapes = [square, i_shape, t_shape, l_shape, j_shape, s_shape, z_shape]
        self.shape = random.choice(shapes)
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def rotate(self, grid):
        # Don't rotate square
        if self.shape == [[1, 1], [1, 1]]:
            return

        # Rotate 90 degrees clockwise
        rotated = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape) - 1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated.append(new_row)

        # Check if rotation is valid
        new_height = len(rotated)
        new_width = len(rotated[0])

        if self.x + new_width <= GRID_WIDTH and self.y + new_height <= GRID_HEIGHT:
            # Check for collisions
            valid = True
            for y in range(new_height):
                for x in range(new_width):
                    if rotated[y][x] == 1:
                        if grid[self.y + y][self.x + x] != 0:
                            valid = False
                            break
                if not valid:
                    break

            if valid:
                self.shape = rotated
                self.height = new_height
                self.width = new_width

    def can_move(self, grid, dx, dy):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    new_x = self.x + x + dx
                    new_y = self.y + y + dy

                    # Check boundaries
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False

                    # Check collision (only if not at top)
                    if new_y >= 0 and grid[new_y][new_x] != 0:
                        return False
        return True

    def lock(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    if self.y + y >= 0:
                        grid[self.y + y][self.x + x] = self.color


def create_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def draw_grid(surface, grid, current_shape):
    # Draw the grid background
    grid_surface = pygame.Surface((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
    grid_surface.fill(BLACK)

    # Draw locked blocks
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] != 0:
                color = COLORS[grid[y][x]]
                pygame.draw.rect(
                    grid_surface,
                    color,
                    (
                        x * GRID_SIZE + 1,
                        y * GRID_SIZE + 1,
                        GRID_SIZE - 2,
                        GRID_SIZE - 2,
                    ),
                )

    # Draw current shape
    if current_shape:
        for y in range(current_shape.height):
            for x in range(current_shape.width):
                if current_shape.shape[y][x] == 1:
                    screen_y = current_shape.y + y
                    screen_x = current_shape.x + x
                    if screen_y >= 0:  # Only draw if visible
                        color = COLORS[current_shape.color]
                        pygame.draw.rect(
                            grid_surface,
                            color,
                            (
                                screen_x * GRID_SIZE + 1,
                                screen_y * GRID_SIZE + 1,
                                GRID_SIZE - 2,
                                GRID_SIZE - 2,
                            ),
                        )

    # Draw grid lines
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(
            grid_surface,
            GRAY,
            (x * GRID_SIZE, 0),
            (x * GRID_SIZE, GRID_HEIGHT * GRID_SIZE),
        )
    for y in range(GRID_HEIGHT + 1):
        pygame.draw.line(
            grid_surface,
            GRAY,
            (0, y * GRID_SIZE),
            (GRID_WIDTH * GRID_SIZE, y * GRID_SIZE),
        )

    surface.blit(grid_surface, (0, 0))


def check_lines(grid):
    lines_cleared = 0
    y = GRID_HEIGHT - 1

    while y >= 0:
        if all(grid[y][x] != 0 for x in range(GRID_WIDTH)):
            lines_cleared += 1
            # Remove the line
            del grid[y]
            # Add new empty line at top
            grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        else:
            y -= 1

    return lines_cleared


def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    grid = create_grid()
    current_shape = Shape()
    score = 0
    game_over = False

    fall_time = 0
    fall_speed = 0.5  # Seconds between automatic falls
    move_delay = 0

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_LEFT:
                    if current_shape.can_move(grid, -1, 0):
                        current_shape.x -= 1

                elif event.key == pygame.K_RIGHT:
                    if current_shape.can_move(grid, 1, 0):
                        current_shape.x += 1

                elif event.key == pygame.K_DOWN:
                    if current_shape.can_move(grid, 0, 1):
                        current_shape.y += 1
                        score += 1

                elif event.key == pygame.K_UP:
                    current_shape.rotate(grid)

                elif event.key == pygame.K_SPACE:
                    # Hard drop
                    while current_shape.can_move(grid, 0, 1):
                        current_shape.y += 1
                        score += 2
                    fall_time = fall_speed  # Force immediate lock

        if not game_over:
            # Automatic falling
            fall_time += dt
            if fall_time >= fall_speed:
                fall_time = 0

                if current_shape.can_move(grid, 0, 1):
                    current_shape.y += 1
                else:
                    # Lock the piece
                    current_shape.lock(grid)

                    # Check for cleared lines
                    lines = check_lines(grid)
                    score += lines * 100

                    # Create new shape
                    current_shape = Shape()

                    # Check game over
                    if not current_shape.can_move(grid, 0, 0):
                        game_over = True

        # Drawing
        screen.fill(BLACK)
        draw_grid(screen, grid, current_shape)

        # Draw sidebar
        sidebar_x = SCREEN_WIDTH + 20
        draw_text(screen, "TETRIS", 48, sidebar_x + 80, 20, CYAN)
        draw_text(screen, f"Score: {score}", 32, sidebar_x + 80, 100)
        draw_text(screen, "Controls:", 28, sidebar_x + 80, 200, YELLOW)
        draw_text(screen, "< / > - Move Left or Right", 24, sidebar_x + 80, 240)
        draw_text(screen, "^ - Rotate", 24, sidebar_x + 80, 270)
        draw_text(screen, "v - Soft Drop", 24, sidebar_x + 80, 300)
        draw_text(screen, "Space - Hard Drop", 24, sidebar_x + 80, 330)

        if game_over:
            # Draw game over overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))
            draw_text(
                screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED
            )
            draw_text(
                screen,
                f"Final Score: {score}",
                36,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 20,
            )
            draw_text(
                screen,
                "Close window to exit",
                24,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 70,
            )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
