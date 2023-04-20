import sys
import pygame
from src.components.Backend import *
from src.components.music import MusicService
from typing import Tuple, Any


def main_menu_phase(Screen) -> None:
    MusicService.start_menu_music()
    BackGround.IMAGE = Background('assets/mm_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    LEVEL_SELECT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 250), 
                        text_input="Level Select", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), 
                         text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                        text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    Screen.blit(MENU_TEXT, MENU_RECT)

    for button in [LEVEL_SELECT_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if LEVEL_SELECT_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.LEVEL_SELECT
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.COS_MENU
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()


def level_select_phase(Screen):
    BackGround.IMAGE = Background('assets/level_select_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    LEVEL_SELECT_TEXT = get_font(50).render("Level Select", True, "#b68f40")
    

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 720), 
                        text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    LEADERBOARD_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/leaderboard_button.webp"),(75,75)), pos=(750, 50), 
                        text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
                                
    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/back_arrow.png"),(75,75)), pos=(50, 50), 
                        text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"),(100,100)), pos=(725, 400),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"),(100,100)), pos=(75, 400),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    

    match CurrentLevel.num:
                    case 1:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 1", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/space_background.jpg"),(500,500)), [150,150])
                    case 2:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 2", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/2.jpg"),(500,500)), [150,150])#REPLACE WITH LEVEL 2 BACKGROUND
                    case 3:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 3", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/haunted_background.jpeg"),(500,500)), [150,150])
                    case 4:
                        LEVEL_SELECT_TEXT = get_font(50).render("Level 4", True, "#b68f40")
                        Screen.blit(pygame.transform.scale(pygame.image.load("assets/4.jpg"),(500,500)), [150,150])#REPLACE WITH LEVEL 4 BACKGROUND

    LEVEL_SELECT_RECT = LEVEL_SELECT_TEXT.get_rect(center=(400, 100))
    Screen.blit(LEVEL_SELECT_TEXT, LEVEL_SELECT_RECT)

    for button in [PLAY_BUTTON, LEADERBOARD_BUTTON, RIGHT_BUTTON, LEFT_BUTTON, BACK_BUTTON]: 
        button.changeColor(MENU_MOUSE_POS)
        button.update(Screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                match CurrentLevel.num:
                    case 1:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_1
                    case 2:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_2
                    case 3:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_3
                    case 4:
                        GlobalState.GAME_STATE = GameStatus.LEVEL_4
            elif BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            elif LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                pass
            elif RIGHT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 4:
                    CurrentLevel.num = CurrentLevel.num + 1
            elif LEFT_BUTTON.checkForInput(MENU_MOUSE_POS):
                if CurrentLevel.num != 1:
                    CurrentLevel.num = CurrentLevel.num - 1

def level_one() -> None:
    # Background Image Setup
    # The background image will eventually become a global variable dependent on cosmetics
    MusicService.stop_music()
    MusicService.start_level_1_music()
    BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.05)
    PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.05)
    BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)

def level_two() -> None:
    MusicService.stop_music()
    MusicService.start_level_2_music()
    BackGround.IMAGE = Background('assets/2.jpg', [0, 0], 1.5)


def level_three() -> None:
    MusicService.stop_music()
    MusicService.start_level_3_music()
    BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
    BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
    PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)


def level_four() -> None:
    MusicService.stop_music()
    MusicService.start_level_4_music()
    BackGround.IMAGE = Background('assets/4.jpg', [0, 0], 1.5)


def cos_menu(Screen):
    BackGround.IMAGE = Background('assets/level_select_background.jpg', [0, 0], 1.5)
    Screen.blit(BackGround.IMAGE.image, BackGround.IMAGE.rect)
    COS_MOUSE_POS = pygame.mouse.get_pos()
    COS_TEXT = get_font(50).render("Cosmetics", True, "#b68f40")
    BACKGROUND_TEXT = get_font(33).render("Background", True, "#b68f40")
    PEG_TEXT = get_font(50).render("Peg", True, "#b68f40")
    BALL_TEXT = get_font(50).render("Ball", True, "#b68f40")

    RIGHT_BUTTON1 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"),(100,100)), pos=(725, 200),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON1 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"),(100,100)), pos=(400, 200),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON2 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"),(100,100)), pos=(725, 350),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON2 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"),(100,100)), pos=(400, 350),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    RIGHT_BUTTON3 = Button(image=pygame.transform.scale(pygame.image.load("assets/right_button.png"),(100,100)), pos=(725, 500),
                          text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    LEFT_BUTTON3 = Button(image=pygame.transform.scale(pygame.image.load("assets/left_button.png"),(100,100)), pos=(400, 500),
                         text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 625), 
                        text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 750), 
                        text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    
    COS_RECT = COS_TEXT.get_rect(center=(400, 50))
    BACKGROUND_RECT = BACKGROUND_TEXT.get_rect(center=(175, 200))
    PEG_RECT = PEG_TEXT.get_rect(center=(200, 350))
    BALL_RECT = BALL_TEXT.get_rect(center=(200, 500))
    Screen.blit(COS_TEXT, COS_RECT)
    Screen.blit(BACKGROUND_TEXT, BACKGROUND_RECT)
    Screen.blit(PEG_TEXT, PEG_RECT)
    Screen.blit(BALL_TEXT, BALL_RECT)

    for button in [RIGHT_BUTTON1, LEFT_BUTTON1, RIGHT_BUTTON2, LEFT_BUTTON2, RIGHT_BUTTON3, LEFT_BUTTON3, PLAY_BUTTON, BACK_BUTTON]: 
        button.changeColor(COS_MOUSE_POS)
        button.update(Screen)

    match CurrentBackground.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/space_background.jpg"),(150,150)), [500,125])
            BackGround.IMAGE = Background('assets/space_background.jpg', [0, 0], 1.0)
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/2.jpg"),(150,150)), [500,125])#REPLACE WITH LEVEL 2 BACKGROUND
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/haunted_background.jpeg"),(150,150)), [500,125])
            BackGround.IMAGE = Background('assets/haunted_background.jpeg', [-8, 0], 0.56)
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/4.jpg"),(150,150)), [500,125])#REPLACE WITH LEVEL 4 BACKGROUND

    match CurrentPeg.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/space_peg.png"),(150,150)), [500,275])
            PegSurface.SURFACE = ball_look('assets/space_peg.png', 0.1)
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/2.jpg"),(150,150)), [500,275])#REPLACE WITH LEVEL 2 PEG
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/haunted_peg.png"),(150,150)), [500,275])
            PegSurface.SURFACE = ball_look('assets/haunted_peg.png', 0.40)
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/4.jpg"),(150,150)), [500,275])#REPLACE WITH LEVEL 4 PEG
    
    match CurrentBall.num:
        case 1:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/space_ball.png"),(150,150)), [500,425])
            BallSurface.SURFACE = ball_look('assets/space_ball.png', 0.075)
        case 2:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/2.jpg"),(150,150)), [500,425])#REPLACE WITH LEVEL 2 BALL
        case 3:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/haunted_ball.png"),(150,150)), [500,425])
            BallSurface.SURFACE = ball_look('assets/haunted_ball.png', 0.15)
        case 4:
            Screen.blit(pygame.transform.scale(pygame.image.load("assets/4.jpg"),(150,150)), [500,425])#REPLACE WITH LEVEL 4 BALL


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(COS_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.COS_LEVEL
            elif BACK_BUTTON.checkForInput(COS_MOUSE_POS):
                GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            elif RIGHT_BUTTON1.checkForInput(COS_MOUSE_POS):
                if CurrentBackground.num != 4:
                    CurrentBackground.num = CurrentBackground.num + 1
            elif LEFT_BUTTON1.checkForInput(COS_MOUSE_POS):
                if CurrentBackground.num != 1:
                    CurrentBackground.num = CurrentBackground.num - 1
            elif RIGHT_BUTTON2.checkForInput(COS_MOUSE_POS):
                if CurrentPeg.num != 4:
                    CurrentPeg.num = CurrentPeg.num + 1
            elif LEFT_BUTTON2.checkForInput(COS_MOUSE_POS):
                if CurrentPeg.num != 1:
                    CurrentPeg.num = CurrentPeg.num - 1
            elif RIGHT_BUTTON3.checkForInput(COS_MOUSE_POS):
                if CurrentBall.num != 4:
                    CurrentBall.num = CurrentBall.num + 1
            elif LEFT_BUTTON3.checkForInput(COS_MOUSE_POS):
                if CurrentBall.num != 1:
                    CurrentBall.num = CurrentBall.num - 1