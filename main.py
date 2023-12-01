import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Sounds
        main_sound = pygame.mixer.Sound('audio/main.mp3')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Set the title of the window
        pygame.display.set_caption("Arandir")
        # Load the icon image
        icon = pygame.image.load('images/icon.png')
        pygame.display.set_icon(icon)

        # Pixel Menu setup
        font_path = "graphics/font/joystix.ttf"  # Replace with the path to your TTF font file
        arandir_font_size = 26  # Set the font size for "ARANDIR"
        story_font_size = 14  # Set the font size for the story and other text
        self.menu_font_arandir = pygame.font.Font(font_path, arandir_font_size)
        self.menu_font_story = pygame.font.Font(font_path, story_font_size)

        # Create separate surfaces for each line
        name_surface = self.menu_font_arandir.render("ARANDIR", True, GOLD)
        
        # Enhanced story text
        story_text = [
            "In the mystical realm of Arandir, a looming curse cast shadows upon the once vibrant land,",
            "As the curse tightened its grip, whispers of despair echoed through the enchanted forests and hills.",
            "In this darkened realm,",
            "a hero emerged—armed with a blade forged in determination and guided by ancient prophecies.",
            "The hero set forth to unravel the mysteries, the path treacherous with the weight of destiny.",
            "In the mystical realm of Arandir, a looming curse cast shadows upon the once vibrant land,",
            "Would they be the beacon to dispel shadows and rekindle hope?",
        ]

        story_surfaces = [self.menu_font_story.render(line, True, GOLD) for line in story_text]

        # Calculate positions for each line
        arandir_rect = name_surface.get_rect(center=(WIDTH // 2, HEIGTH // 2 - 80))
        story_rects = [surface.get_rect(center=(WIDTH // 2, HEIGTH // 2 + i * 30)) for i, surface in enumerate(story_surfaces)]

        # Draw each line onto the menu background
        self.screen.fill(BLACK)  # Fill the screen with black
        self.screen.blit(name_surface, arandir_rect)
        for surface, rect in zip(story_surfaces, story_rects):
            self.screen.blit(surface, rect)

        # "Press 'P' to start" message
        press_p_surface = self.menu_font_story.render("Press 'P' to start", True, GOLD)
        press_p_rect = press_p_surface.get_rect(center=(WIDTH // 2, HEIGTH // 2 + 250))
        self.screen.blit(press_p_surface, press_p_rect)

        # Combine all lines into a single surface
        self.menu_text = self.screen

        # Flag to check if the game is in the menu state
        self.in_menu = True

    def run(self):
        story_displayed = False  # Flag to check if the story is displayed
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and self.in_menu:
                        self.in_menu = False  # Start the game

                    story_displayed = True  # Set the flag to indicate the story is displayed

            if self.in_menu and not story_displayed:
                self.screen.blit(self.menu_text, (0, 0))
            else:
            # Start the game
                self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
