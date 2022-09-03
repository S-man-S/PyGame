from MainMenu import *
from Character import *
from MiniGames import *
from Enemies import *


def startgame():
    games.screen.clear()
    games.screen.background = games.load_image("Locations/MM/MM_location.png", transparent=False)
    games.music.load("sound/MM/pred_intro.wav")
    games.music.play()
    games.screen.add(MainMenuDoor())
    games.screen.add(MainCharacter(Constants.WindowWidth / 2, Constants.WindowHeight / 2, 0))


games.init(Constants.WindowWidth, Constants.WindowHeight, Constants.FPS)
games.pygame.display.set_icon(games.pygame.image.load("Icon.png"))
games.pygame.display.set_caption("Hero path")


load()

if not Variables.Intro:
    startgame()
elif Variables.Character == 0:
    MainMenu.MainMenu.create()
else:
    games.music.load("sound/Education/Edu.mp3")
    games.music.play(-1)
    room()
games.screen.mainloop()
