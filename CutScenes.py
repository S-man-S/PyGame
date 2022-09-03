from Character import *


class IntroCutScene(games.Sprite):
    def __init__(self, x, y, shop, gym, edu):
        super().__init__(image=games.load_image("Guys/U_shall_not_pass.png"), x=400, y=-50, dy=0.75)
        self.time = 0
        self.the_gg = MainCharacter(x, y, 0)
        self.shop = shop
        self.gym = gym
        self.edu = edu

        self.TextSize = 100
        self.TextColor = color.black
        self.TextY = 100

        self.U = games.Text(value="ТЫ", size=self.TextSize, color=self.TextColor, y=self.TextY, x=75)
        self.No = games.Text(value="НЕ", size=self.TextSize, color=self.TextColor, y=self.TextY, x=225)
        self.Pass = games.Text(value="ПРОЙДЁШЬ!", size=self.TextSize, color=self.TextColor, y=self.TextY, x=900)

    def update(self):
        Variables.CutScene = True
        if self.time == 0:
            games.screen.add(self.the_gg)
            self.the_gg.CanMove = False
            self.the_gg.dx = 1.15
            games.screen.add(self.U)
        if self.time == Constants.FPS:
            games.screen.add(self.No)
        if self.time == Constants.FPS * 3:
            self.the_gg.dx = 0
            games.screen.add(self.Pass)
        if self.time == Constants.FPS * 5:
            self.dy = 0
            self.U.destroy()
            self.No.destroy()
            self.Pass.destroy()
        if self.time == Constants.FPS * 7:
            games.screen.add(self.shop)
        if self.time == Constants.FPS * 8:
            self.shop.dy = 0
            games.screen.add(self.edu)
        if self.time == Constants.FPS * 9:
            self.edu.dy = 0
            games.screen.add(self.gym)
            games.load_sound("sound/sfx/Event_lose.ogg").play()
            self._replace(games.load_image("Enemies/super_boss/death.png"))
        if self.time == Constants.FPS * 10:
            self.gym.dy = 0
            self.destroy()
            self.the_gg.CanMove = True
            Variables.Intro = True
        self.time += 1
        Variables.CutScene = False
        save()
