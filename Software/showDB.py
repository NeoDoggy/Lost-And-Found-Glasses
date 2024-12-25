import pygame
import json
import time
from datetime import datetime

# Function to read JSON data from file
def read_json_file():
    with open("./db.json", "r") as file:
        return json.load(file)

labels = {
    "0": "Bottle",
    "1": "Key",
    "2": "Phone",
    "3": "Umbrella",
    "4": "Wallet"
}

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSON Data Viewer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (100, 100, 100)

# Fonts
title_font = pygame.font.Font(None, 48)
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Running state
running = True

# Function to format timestamp
def format_timestamp(raw_timestamp):
    try:
        dt = datetime.fromisoformat(raw_timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "Invalid time"

# Main loop
while running:
    screen.fill(WHITE)

    # Read JSON data
    json_data = read_json_file()

    # Display JSON data
    y_offset = 70  # Starting Y position
    x_label = 50   # X position for labels
    x_time = 300   # X position for timestamps

    # Render title
    title_text = title_font.render("Last Seen Object", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))

    for key, timestamp in json_data.items():
        label = labels.get(key, "Unknown")
        formatted_time = format_timestamp(timestamp)

        # Render label and formatted timestamp
        label_text = font.render(f"{label}:", True, BLACK)
        time_text = small_font.render(formatted_time, True, LIGHT_GRAY)

        # Display on screen
        screen.blit(label_text, (x_label, y_offset))
        screen.blit(time_text, (x_time, y_offset + 5))

        y_offset += 50  # Move to the next line

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    # Add a small delay to prevent excessive file reads
    time.sleep(0.5)

pygame.quit()
