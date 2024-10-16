import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 40

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Define the maze grid (1 is a wall, 0 is a path)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Starting position of the player
player_pos = [1, 1]

# Goal position
goal_pos = [7, 14]

# Function to draw the maze
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to move the player
def move_player(dx, dy):
    new_pos = [player_pos[0] + dx, player_pos[1] + dy]
    if maze[new_pos[0]][new_pos[1]] == 0:
        player_pos[0] += dx
        player_pos[1] += dy

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw maze
    draw_maze()

    # Draw the player (blue square)
    pygame.draw.rect(screen, BLUE, pygame.Rect(player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the goal (green square)
    pygame.draw.rect(screen, GREEN, pygame.Rect(goal_pos[1] * CELL_SIZE, goal_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(-1, 0)
            if event.key == pygame.K_DOWN:
                move_player(1, 0)
            if event.key == pygame.K_LEFT:
                move_player(0, -1)
            if event.key == pygame.K_RIGHT:
                move_player(0, 1)

    # Check if player reached the goal
    if player_pos == goal_pos:
        print("You win!")
        running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
