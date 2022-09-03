from livewires import games, color
from Numbers import *
import MainMenu


def call_menu():
    global the_menu
    the_menu = Menu()
    games.screen.add(the_menu)
    Menu.create(the_menu)


def kill_menu():
    Menu.kill(the_menu)
    the_menu.destroy()


def level_map():
    for i in range(len(Variables.Chart)):
        for j in range(len(Variables.Chart)):
            if Variables.Chart[i][j][0] not in (0, 10, 11) and Variables.Chart[i][j][-1] != 0:
                if Variables.Stage == 0:
                    Space = 11
                    if Variables.Chart[i][j][-1] == 1:
                        image = games.load_image("GUI/map_0_1.png", False)
                    elif Variables.Chart[i][j][-1] == 2:
                        image = games.load_image("GUI/map_0_2.png", False)
                    elif Variables.Chart[i][j][-1] == 10:
                        image = games.load_image("GUI/map_0_10.png", False)
                    elif Variables.Chart[i][j][-1] == 11:
                        image = games.load_image("GUI/map_0_11.png", False)
                    else:
                        image = games.load_image("GUI/map_0_3.png", False)
                elif Variables.Stage == 1:
                    Space = 7
                    if Variables.Chart[i][j][-1] == 1:
                        image = games.load_image("GUI/map_1_1.png", False)
                    elif Variables.Chart[i][j][-1] == 2:
                        image = games.load_image("GUI/map_1_2.png", False)
                    elif Variables.Chart[i][j][-1] == 10:
                        image = games.load_image("GUI/map_1_10.png", False)
                    elif Variables.Chart[i][j][-1] == 11:
                        image = games.load_image("GUI/map_1_11.png", False)
                    else:
                        image = games.load_image("GUI/map_1_3.png", False)
                elif Variables.Stage == 2:
                    Space = 5
                    if Variables.Chart[i][j][-1] == 1:
                        image = games.load_image("GUI/map_2_1.png", False)
                    elif Variables.Chart[i][j][-1] == 2:
                        image = games.load_image("GUI/map_2_2.png", False)
                    elif Variables.Chart[i][j][-1] == 10:
                        image = games.load_image("GUI/map_2_10.png", False)
                    elif Variables.Chart[i][j][-1] == 11:
                        image = games.load_image("GUI/map_2_11.png", False)
                    else:
                        image = games.load_image("GUI/map_2_3.png", False)
                else:
                    Space = 4
                    if Variables.Chart[i][j][-1] == 1:
                        image = games.load_image("GUI/map_3_1.png", False)
                    elif Variables.Chart[i][j][-1] == 2:
                        image = games.load_image("GUI/map_3_2.png", False)
                    elif Variables.Chart[i][j][-1] == 10:
                        image = games.load_image("GUI/map_3_10.png", False)
                    elif Variables.Chart[i][j][-1] == 11:
                        image = games.load_image("GUI/map_3_11.png", False)
                    else:
                        image = games.load_image("GUI/map_3_3.png", False)

                games.screen.add(games.Sprite(image, x=1100+Space*(1+j*2), y=Space*(1+i*2)))


class LevelBar(games.Sprite):
    def __init__(self, x, level):
        super().__init__(games.load_image("GUI/XP_frame.png"), x=x, y=20) # x 350/390/430
        games.screen.add(games.Text(str(level), 30, color.pink, x=self.x, y=self.y))


class GoldBar(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("GUI/Gold.png"), x=200, y=28)
        self.cur_gold = games.Text(str(Variables.Gold), 30, color.yellow, left=self.right, y=self.y)
        games.screen.add(self.cur_gold)

    def update(self):
        self.cur_gold.destroy()
        self.cur_gold.value = str(int(Variables.Gold))
        games.screen.add(self.cur_gold)


def create_gui(ab, jb, sb, hb):
    games.screen.add(ab)
    games.screen.add(jb)
    if sb is not None:
        games.screen.add(sb)
    games.screen.add(hb)


class HealthBar(games.Sprite):
    def __init__(self, health):
        super().__init__(image=games.load_image("GUI/heart.png"), x=35, y=32)

        self.HP = games.Text(value=str(int(health)), size=32, color=color.red, left=70, top=0)
        games.screen.add(self.HP)

    def health_bar_update(self, health):
        self.HP.destroy()
        self.HP = games.Text(value=health, size=32, color=color.red, left=70, top=0)
        games.screen.add(self.HP)


class SpellBar(games.Sprite):
    def __init__(self, count):
        image = 0
        if count == 0:
            image = games.load_image("GUI/Status_bar_0.png")
        elif count == 1:
            image = games.load_image("GUI/Spell_bar_1.png")
        elif count == 2:
            image = games.load_image("GUI/Spell_bar_2.png")
        elif count == 3:
            image = games.load_image("GUI/Spell_bar_3.png")
        elif count == 4:
            image = games.load_image("GUI/Spell_bar_4.png")
        elif count == 5:
            image = games.load_image("GUI/Spell_bar_5.png")
        elif count == 6:
            image = games.load_image("GUI/Spell_bar_6.png")
        elif count == 7:
            image = games.load_image("GUI/Spell_bar_7.png")
        elif count == 8:
            image = games.load_image("GUI/Spell_bar_8.png")
        super().__init__(image=image, x=1075, y=25)


class JumpBar(games.Sprite):
    def __init__(self, jump_cooldown):
        super().__init__(image=games.load_image("GUI/Jump_bar_8.png"), x=1015, y=25)
        self.time = -1
        self.jump_cooldown = jump_cooldown

    def jump(self):
        self.time = self.jump_cooldown * Constants.FPS
        self.image = games.load_image("GUI/Status_bar_0.png")

    def update(self):
        if self.time <= 0:
            self.image = games.load_image("GUI/Jump_bar_8.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 1:
            self.image = games.load_image("GUI/Jump_bar_7.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 2:
            self.image = games.load_image("GUI/Jump_bar_6.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 3:
            self.image = games.load_image("GUI/Jump_bar_5.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 4:
            self.image = games.load_image("GUI/Jump_bar_4.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 5:
            self.image = games.load_image("GUI/Jump_bar_3.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 6:
            self.image = games.load_image("GUI/Jump_bar_2.png")
        elif self.time <= self.jump_cooldown * Constants.FPS / 8 * 7:
            self.image = games.load_image("GUI/Jump_bar_1.png")
        if self.time >= 0 and not Variables.Pause:
            self.time -= 1


class AttackBar(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("GUI/Attack_bar_8.png"), x=955, y=25)
        self.time = -1
        self.Attack_cooldown = 0

    def attack(self, attack_cooldown):
        self.time = attack_cooldown
        self.image = games.load_image("GUI/Status_bar_0.png")
        self.Attack_cooldown = attack_cooldown

    def update(self):
        if self.time <= 0:
            self.image = games.load_image("GUI/Attack_bar_8.png")
        elif self.time <= self.Attack_cooldown / 8 * 1:
            self.image = games.load_image("GUI/Attack_bar_7.png")
        elif self.time <= self.Attack_cooldown / 8 * 2:
            self.image = games.load_image("GUI/Attack_bar_6.png")
        elif self.time <= self.Attack_cooldown / 8 * 3:
            self.image = games.load_image("GUI/Attack_bar_5.png")
        elif self.time <= self.Attack_cooldown / 8 * 4:
            self.image = games.load_image("GUI/Attack_bar_4.png")
        elif self.time <= self.Attack_cooldown / 8 * 5:
            self.image = games.load_image("GUI/Attack_bar_3.png")
        elif self.time <= self.Attack_cooldown / 8 * 6:
            self.image = games.load_image("GUI/Attack_bar_2.png")
        elif self.time <= self.Attack_cooldown / 8 * 7:
            self.image = games.load_image("GUI/Attack_bar_1.png")
        if self.time > 0 and not Variables.Pause:
            self.time -= 1


class Menu(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("GUI/Pause_menu.png"), x=600, y=400)
        self.size = 50
        self.AUS0 = AUSure(0)
        self.AUS1 = AUSure(1)
        self.Restart = games.Text(x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2 - 100,
                                  value="Стереть прогресс", size=self.size, color=color.red)
        # self.Sound = games.Text(x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2, value="Громкость",
        #                         size=self.size, color=color.green)
        self.Sound = games.Text(x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2, value="Настроек нет",
                                size=self.size, color=color.green)
        self.Quit = games.Text(x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2 + 100, value="Выйти",
                               size=self.size, color=color.blue)
        self.time = 0

    def create(self):
        games.screen.add(self.Restart)
        games.screen.add(self.Sound)
        games.screen.add(self.Quit)

    def kill(self):
        self.Restart.destroy()
        self.Sound.destroy()
        self.Quit.destroy()

    def update(self):
        if games.mouse.is_pressed(0) and not Variables.YN and self.time == 0:
            if Constants.WindowWidth / 2 - 330 < games.mouse.x < Constants.WindowWidth / 2 + 330 and \
                    games.mouse.y > Constants.WindowHeight / 2 - 150:
                if games.mouse.y < Constants.WindowHeight / 2 - 50:
                    games.screen.add(self.AUS0)
                    self.AUS0.create()
                elif games.mouse.y < Constants.WindowHeight / 2 + 50:
                    Variables.Gold += 1
                elif games.mouse.y < Constants.WindowHeight / 2 + 150:
                    games.screen.add(self.AUS1)
                    self.AUS1.create()
        if self.time > 0:
            self.time -= 1

    def killaus(self, action):
        if action == 0:
            self.AUS0.destroy()
            self.AUS0.kill()
        else:
            self.AUS1.destroy()
            self.AUS1.kill()
        self.time = Constants.FPS


class AUSure(games.Sprite):
    def __init__(self, action):
        super().__init__(image=games.load_image("GUI/Pause_menu_ask.png"), x=Constants.WindowWidth / 2,
                         y=Constants.WindowHeight / 2)
        self.Sure = games.Text(value="Вы уверены?", size=50, color=color.green, x=Constants.WindowWidth / 2,
                               y=Constants.WindowHeight / 2 - 50)
        self.Y = games.Text(value="Да", size=50, color=color.red, x=Constants.WindowWidth / 2 - 200,
                            y=Constants.WindowHeight / 2 + 50)
        self.N = games.Text(value="Нет", size=50, color=color.blue, x=Constants.WindowWidth / 2 + 200,
                            y=Constants.WindowHeight / 2 + 50)
        self.action = action
        self.time = 0

    def create(self):
        games.screen.add(self.Sure)
        games.screen.add(self.Y)
        games.screen.add(self.N)
        Variables.YN = True
        self.time = Constants.FPS

    def kill(self):
        self.Sure.destroy()
        self.Y.destroy()
        self.N.destroy()

    def update(self):
        if games.mouse.is_pressed(0) and self.time == 0:
            if Constants.WindowHeight / 2 < games.mouse.y < Constants.WindowHeight / 2 + 100 and \
                    Constants.WindowWidth / 2 - 400 < games.mouse.x < Constants.WindowWidth / 2 + 400:
                Variables.YN = False
                if games.mouse.x < Constants.WindowWidth / 2:
                    if self.action == 0:
                        Variables.Pause = False
                        Variables.YN = False
                        load_to_default()
                        save()
                        games.music.load("sound/MM/pred_intro.wav")
                        games.music.play()
                        games.screen.clear()
                        games.screen.background = games.load_image("Locations/MM/MM_location.png", transparent=False)
                        games.screen.add(MainMenu.MainMenuDoor())
                        games.screen.add(
                            MainMenu.MainCharacter(Constants.WindowWidth / 2, Constants.WindowHeight / 2, 0))
                    else:
                        games.screen.clear()
                        games.screen.background = games.load_image("GUI/Black.png")
                        games.screen.quit()
                else:
                    Menu.killaus(the_menu, self.action)
        if self.time > 0:
            self.time -= 1
