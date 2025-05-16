# Import necessary libraries
import pygame
import time 
import random           
pygame.font.init()

# Define game WINDOWdow dimensions
WIDTH = 800
HEIGHT = 600
# Create game WINDOWdow

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Set game WINDOWdow title
pygame.display.set_caption("Space Dodge")

# Load background image and scale it to game window size
BG = pygame.transform.scale(pygame.image.load("beg.jpg"), (WIDTH, HEIGHT))

# Function to draw game elements
def draw(player, elapsed_time, stars, score):
    # Draw background image
    WINDOW.blit(BG, (0, 0))
     #Initial start from left (0,0) to right (0, increase y position)
    
    # Render time text
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # Draw time text
    WINDOW.blit(time_text, (10, 10))

    # Render score text
    score_text = FONT.render(f"Score: {score}", 1, "white")
    # Draw score text
    WINDOW.blit(score_text, (10, 40))

    # Draw player rectangle
    pygame.draw.rect(WINDOW, "red", player)
    
    # Draw star rectangles
    for star in stars:
        pygame.draw.rect(WINDOW, "white", star)

    # Update game WINDOWdow
    pygame.display.update()

# Define player properties
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 10  
# Define font for text rendering
FONT = pygame.font.SysFont("timenewromans", 50)
# Define star properties
STAR_WIDTH = 10
STAR_HEIGHT = 30
STAR_VEL = 7

# Main game function
def main():
    # Initialize game loop
    run = True
    # Create player rectangle
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    # Create clock object to control game speed
    clock = pygame.time.Clock()

    # Record start time
    start_time = time.time()

    # Initialize game variables
    elapsed_time = 0
    star_add_increment = 1000
    star_count = 0
    stars = []
    hit = False
    score = 0

    # Game loop
    while run:
        # Increment star count and control game speed
        star_count += clock.tick(60)
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        # Increment score each second
        score = int(elapsed_time)

        # Add stars to game
        if star_count > star_add_increment:
            for _ in range(3):  #  for i in range 
                # Randomly generate star x position
                star_i = random.randint(0, WIDTH - STAR_WIDTH)
                # Create star rectangle
                star = pygame.Rect(star_i, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                # Add star to list
                stars.append(star)
            # Decrease star add increment
            star_add_increment = max(200, star_add_increment - 50)
            # Reset star count
            star_count = 0

        # Handle events
        for event in pygame.event.get():
            # Quit game if WINDOWdow is closed
            if event.type == pygame.QUIT:
                run = False
                break

        # Get pressed keys
        keys = pygame.key.get_pressed()
        # Move player left
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        # Move player right
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Update star positions
        for star in stars[:]:  #stars[:] creates a shallow copy of the list   // array = [1,2,3] // array[:] = [1,2,3]
            star.y += STAR_VEL
            # Remove star if it goes off screen
            if star.y > HEIGHT:
                # Remove star from list
                stars.remove(star)
                # Increment score for avoiding star
                score += 10
            # Check for collision with player
            elif star.y + star.height >= player.y and star.colliderect(player):
                # Remove star from list
                stars.remove(star)
                # Set hit flag to True
                hit = True
                break

        # Handle game over
        if hit:
            # Draw background image
            WINDOW.blit(BG, (0, 0))
            # Render game over text
            lost_text = FONT.render("You Lost!", 1, "white")
            # Render final score text
            score_text = FONT.render(f"Final Score: {score}", 1, "white")
            # Draw game over text
            WINDOW.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2 - 20))
            # Draw final score text
            WINDOW.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, HEIGHT / 2 - score_text.get_height() / 2 + 20))
            # Update game WINDOWdow
            pygame.display.update()
            # Delay for 2 seconds
            pygame.time.delay(2000)
            # Break game loop
            break

        # Draw game elements
        draw(player, elapsed_time, stars, score)

    # Quit Pygame
    pygame.quit()

# Run main function
if __name__ == "__main__":
    main()