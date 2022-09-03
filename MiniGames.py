from livewires import games, color
from random import *
from Numbers import *
import MainMenu


class Exit(games.Sprite):
    def __init__(self):
        super().__init__(games.load_image("Minigames/EXIT.png"), x=1120, y=610)

    def update(self):
        if self.left < games.mouse.x < self.right and self.top < games.mouse.y < self.bottom and games.mouse.is_pressed(0):
            save()
            games.load_sound("sound/sfx/Doors_MM.wav").play()
            MainMenu.MainMenu.create()


class Choose(games.Text):
    def __init__(self):
        super().__init__("Судоку", 50, color.red, x=400, y=99)
        if Characteristics.Trains["Intelligence"] < 10:
            games.screen.add(games.Text("Повышает интеллект на 1", 30, color.blue, x=400, y=139))
        else:
            games.screen.add(games.Text("Даёт 3 золота и опыта", 30, color.blue, x=400, y=139))
            games.screen.add(games.Text("случайному магу", 30, color.blue, x=400, y=169))
        games.screen.add(games.Text("ЛКМ по правой цифре - выбор цифры", 30, color.green, x=750, y=84))
        games.screen.add(games.Text("ЛКМ по полю - выбор цифры", 30, color.green, x=750, y=140))
        games.screen.add(games.Text("ПКМ по полю - возможная цифра", 30, color.green, x=750, y=196))

        games.screen.add(games.Text("Сапёр", 50, color.red, x=400, y=283))
        if Characteristics.Trains["Luck"] < 10:
            games.screen.add(games.Text("Повышает удачу на 1", 30, color.blue, x=400, y=323))
        else:
            games.screen.add(games.Text("Даёт 3 золота и опыта", 30, color.blue, x=400, y=323))
            games.screen.add(games.Text("случайному герою", 30, color.blue, x=400, y=353))
        games.screen.add(games.Text("ЛКМ открыть поле", 30, color.green, x=750, y=298))
        games.screen.add(games.Text("ПКМ поставить флаг", 30, color.green, x=750, y=350))

        games.screen.add(games.Text("Реакция", 50, color.red, x=400, y=467))
        if Characteristics.Trains["Agility"] < 10:
            games.screen.add(games.Text("Повышает ловкость на 1", 30, color.blue, x=400, y=507))
        else:
            games.screen.add(games.Text("Даёт 3 золота и опыта", 30, color.blue, x=400, y=507))
            games.screen.add(games.Text("случайному разбойнику", 30, color.blue, x=400, y=537))
        games.screen.add(games.Text("Быстро нажимай на кнопки,", 30, color.green, x=750, y=452))
        games.screen.add(games.Text("которые будут написаны на экране.", 30, color.green, x=750, y=508))
        games.screen.add(games.Text("Не успеешь - проиграешь", 30, color.green, x=750, y=564))

        games.screen.add(games.Text("Жми быстрее", 50, color.red, x=400, y=651))
        if Characteristics.Trains["Strength"] < 10:
            games.screen.add(games.Text("Повышает силу на 1", 30, color.blue, x=400, y=691))
        else:
            games.screen.add(games.Text("Даёт 3 золота и опыта ", 30, color.blue, x=400, y=691))
            games.screen.add(games.Text("случаному войну", 30, color.blue, x=400, y=721))
        games.screen.add(games.Text("Жми пробел, как можно чаще", 30, color.green, x=750, y=692))

        games.screen.add(Exit())

    def update(self):
        if games.mouse.is_pressed(0) and 232 < games.mouse.x < 968 and games.mouse.y > 32:
            if games.mouse.y < 216:
                Sudoku()
            elif games.mouse.y < 400:
                Sapper()
            elif games.mouse.y < 584:
                games.screen.add(Tapper(0))
            elif games.mouse.y < 768:
                games.screen.add(Smarttapper())


class Win(games.Text):
    def __init__(self):
        super().__init__(x=600, y=400, value="Победа!", size=100, color=color.red)
        self.timer = 180

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            games.screen.background = games.load_image("Minigames/BG.png", transparent=False)
            games.screen.clear()
            games.screen.add(Choose())


class Lose(games.Text):
    def __init__(self):
        super().__init__(x=600, y=400, value="Поражение!", size=100, color=color.red)
        self.timer = 180

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            games.screen.background = games.load_image("Minigames/BG.png", transparent=False)
            games.screen.clear()
            games.screen.add(Choose())


class CellSudoku(games.Sprite):
    def __init__(self, num, unlocked, x, y, misstake):
        if not unlocked:
            self.path = "Minigames/Cell.png"
        elif num == 1:
            self.path = "Minigames/cell_1.png"
        elif num == 2:
            self.path = "Minigames/cell_2.png"
        elif num == 3:
            self.path = "Minigames/cell_3.png"
        elif num == 4:
            self.path = "Minigames/cell_4.png"
        elif num == 5:
            self.path = "Minigames/cell_5.png"
        elif num == 6:
            self.path = "Minigames/cell_6.png"
        elif num == 7:
            self.path = "Minigames/cell_7.png"
        elif num == 8:
            self.path = "Minigames/cell_8.png"
        elif num == 9:
            self.path = "Minigames/cell_9.png"
        super().__init__(image=games.load_image(self.path, transparent=False), x=x, y=y)
        self.small_nums = [False, False, False, False, False, False, False, False, False]
        self.small_num = [games.Sprite(games.load_image("Minigames/cell_1_small.png"), x=self.x - 27, y=self.y - 27),
                          games.Sprite(games.load_image("Minigames/cell_2_small.png"), x=self.x, y=self.y - 27),
                          games.Sprite(games.load_image("Minigames/cell_3_small.png"), x=self.x + 27, y=self.y - 27),
                          games.Sprite(games.load_image("Minigames/cell_4_small.png"), x=self.x - 27, y=self.y),
                          games.Sprite(games.load_image("Minigames/cell_5_small.png"), x=self.x, y=self.y),
                          games.Sprite(games.load_image("Minigames/cell_6_small.png"), x=self.x + 27, y=self.y),
                          games.Sprite(games.load_image("Minigames/cell_7_small.png"), x=self.x - 27, y=self.y + 27),
                          games.Sprite(games.load_image("Minigames/cell_8_small.png"), x=self.x, y=self.y + 27),
                          games.Sprite(games.load_image("Minigames/cell_9_small.png"), x=self.x + 27, y=self.y + 27)]
        self.num = num
        self.unlocked = unlocked
        self.timer = 30
        self.misstake = misstake

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        if self.left < games.mouse.x < self.right and self.top < games.mouse.y < self.bottom and self.timer == 0:
            if games.mouse.is_pressed(0):
                self.timer = 30
                if self.x > 1100:
                    Variables.Train_1_pressed = self.num
                elif not self.unlocked:
                    if self.num == Variables.Train_1_pressed:
                        Variables.Train_1_opened += 1
                        games.screen.add(CellSudoku(self.num, True, self.x, self.y, self.misstake))
                        if Variables.Train_1_opened == 81:
                            if Characteristics.Trains["Intelligence"] < 10:
                                Characteristics.Trains["Intelligence"] += 1
                            else:
                                Variables.Gold += 3
                                Characteristics.XP_characters[str(randint(4, 6))] += 3
                            games.screen.clear()
                            games.screen.background = games.load_image("GUI/Black.png")
                            games.screen.add(Win())
                        self.destroy()
                    elif Variables.Train_1_pressed != 0:
                        MisstakesSudoku.miss(self.misstake)
            if games.mouse.is_pressed(2) and not self.unlocked:
                self.timer = 30
                if not self.small_nums[Variables.Train_1_pressed - 1]:
                    games.screen.add(self.small_num[Variables.Train_1_pressed - 1])
                    self.small_nums[Variables.Train_1_pressed - 1] = True
                else:
                    self.small_num[Variables.Train_1_pressed - 1].destroy()
                    self.small_nums[Variables.Train_1_pressed - 1] = False


class MisstakesSudoku:
    def __init__(self):
        self.max = int(11 - Characteristics.Trains["Intelligence"]) // 2
        self.count = 0
        for i in range(self.max):
            games.screen.add(games.Sprite(image=games.load_image('GUI/heart.png'), left=100, y=160 + 120 * i))

    def miss(self):
        self.count += 1
        games.screen.add(
            games.Sprite(image=games.load_image('GUI/broken_heart.png'), left=100, y=40 + 120 * self.count))
        if self.count == self.max:
            games.screen.clear()
            games.screen.background = games.load_image("GUI/Black.png")
            games.screen.add(Lose())


class Sudoku:
    def __init__(self):
        games.screen.clear()
        games.screen.add(games.Sprite(games.load_image("Minigames/Sudoku_setka.png"), x=600, y=400))
        self.MT = MisstakesSudoku()
        mass = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        for _ in range(3):
            for i in range(3):
                a = b = c = d = randint(i * 3, i * 3 + 2)
                while a == b:
                    b = randint(i * 3, i * 3 + 2)
                while c == d:
                    d = randint(i * 3, i * 3 + 2)
                mass[a], mass[b] = mass[b], mass[a]
                for j in range(9):
                    mass[j][c], mass[j][d] = mass[j][d], mass[j][c]
            a = b = c = d = randint(0, 2)
            while a == b:
                b = randint(0, 2)
            while c == d:
                d = randint(0, 2)
            for i in range(3):
                mass[a * 3 + i], mass[b * 3 + i] = mass[b * 3 + i], mass[a * 3 + i]
                for j in range(9):
                    mass[j][c * 3 + i], mass[j][d * 3 + i] = mass[j][d * 3 + i], mass[j][c * 3 + i]
        transparent = choice([True, False])
        Variables.Train_1_opened = start = 36
        maximum = 81
        for i in range(9):
            for j in range(9):
                unlocked = False
                if randint(1, maximum) <= start:
                    unlocked = True
                    start -= 1
                maximum -= 1
                if transparent:
                    games.screen.add(CellSudoku(mass[j][i], unlocked, 272 + i * 82, 72 + j * 82, self.MT))
                else:
                    games.screen.add(CellSudoku(mass[i][j], unlocked, 272 + i * 82, 72 + j * 82, self.MT))
            games.screen.add(CellSudoku(1, True, 1110, 40, self.MT))
            games.screen.add(CellSudoku(2, True, 1110, 130, self.MT))
            games.screen.add(CellSudoku(3, True, 1110, 220, self.MT))
            games.screen.add(CellSudoku(4, True, 1110, 310, self.MT))
            games.screen.add(CellSudoku(5, True, 1110, 400, self.MT))
            games.screen.add(CellSudoku(6, True, 1110, 490, self.MT))
            games.screen.add(CellSudoku(7, True, 1110, 580, self.MT))
            games.screen.add(CellSudoku(8, True, 1110, 670, self.MT))
            games.screen.add(CellSudoku(9, True, 1110, 760, self.MT))


class BombsCount(games.Text):
    def __init__(self):
        super().__init__(16, 50, color.black, x=1150, y=400)


class CellSapper(games.Sprite):
    def __init__(self, bomb, form, x, y, bombscount):
        if form == 0:
            self.path = "Minigames/cell.png"
        elif form == 1:
            self.path = "Minigames/cell_flag.png"
        elif bomb == 0:
            self.path = "Minigames/cell_0.png"
        elif bomb == 1:
            self.path = "Minigames/cell_1.png"
        elif bomb == 2:
            self.path = "Minigames/cell_2.png"
        elif bomb == 3:
            self.path = "Minigames/cell_3.png"
        elif bomb == 4:
            self.path = "Minigames/cell_4.png"
        elif bomb == 5:
            self.path = "Minigames/cell_5.png"
        elif bomb == 6:
            self.path = "Minigames/cell_6.png"
        elif bomb == 7:
            self.path = "Minigames/cell_7.png"
        elif bomb == 8:
            self.path = "Minigames/cell_8.png"
        else:
            self.path = "Minigames/cell_bomb.png"

        super().__init__(image=games.load_image(self.path, transparent=False), x=x, y=y)
        self.bomb = bomb
        self.form = form
        self.timer = 30
        self.bombscount = bombscount

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        if self.left < games.mouse.x < self.right and self.top < games.mouse.y < self.bottom and self.form != 2 and self.timer == 0:
            if games.mouse.is_pressed(2):
                if self.form == 1:
                    games.screen.add(CellSapper(self.bomb, 0, self.x, self.y, self.bombscount))
                    self.bombscount.value += 1
                else:
                    games.screen.add(CellSapper(self.bomb, 1, self.x, self.y, self.bombscount))
                    self.bombscount.value -= 1
                self.destroy()
            elif games.mouse.is_pressed(0) and self.form == 0:
                Variables.Train_2_opened += 1
                games.screen.add(CellSapper(self.bomb, 2, self.x, self.y, self.bombscount))
                if Variables.Train_2_opened == 81:
                    if Characteristics.Trains["Luck"] < 10:
                        Characteristics.Trains["Luck"] += 1
                    else:
                        Variables.Gold += 3
                        Characteristics.XP_characters[str(randint(1, 9))] += 3
                    games.screen.clear()
                    games.screen.background = games.load_image("GUI/Black.png")
                    games.screen.add(Win())
                if self.bomb == 9:
                    games.screen.clear()
                    games.screen.background = games.load_image("GUI/Black.png")
                    games.screen.add(Lose())
                self.destroy()


class Sapper:
    def __init__(self):
        games.screen.clear()
        mass = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        maximum = 81
        Variables.Train_2_opened = mines = 16
        games.screen.add(games.Sprite(image=games.load_image("Minigames/cell_bomb.png", transparent=True), x=1050, y=400))
        bombscount = BombsCount()
        games.screen.add(bombscount)
        for i in range(9):
            for j in range(9):
                if mines >= randint(1, maximum):
                    mass[i][j] = 9
                    mines -= 1
                maximum -= 1
        for i in range(9):
            for j in range(9):
                if mass[i][j] != 9:
                    for z in range(i - 1, i + 2):
                        for k in range(j - 1, j + 2):
                            if 0 <= z < 9 and 0 <= k < 9 and mass[z][k] == 9:
                                mass[i][j] += 1
                games.screen.add(CellSapper(mass[i][j], 0, 272 + i * 82, 72 + j * 82, bombscount))


class Tapper(games.Text):
    def __init__(self, tries):
        games.screen.clear()
        self.time = (20 - Characteristics.Trains["Agility"]) * 6
        self.key = randint(97, 122)
        self.tries = tries
        super().__init__("Нажми " + chr(self.key), 100, x=600, y=400, color=color.green)

    def update(self):
        if self.time > 0:
            if games.keyboard.is_pressed(self.key):
                self.tries += 1
                if self.tries == 10:
                    if Characteristics.Trains["Agility"] < 10:
                        Characteristics.Trains["Agility"] += 1
                    else:
                        Variables.Gold += 3
                        Characteristics.XP_characters[str(randint(7, 9))] += 3
                    games.screen.clear()
                    games.screen.background = games.load_image("GUI/Black.png")
                    games.screen.add(Win())
                else:
                    games.screen.add(Tapper(self.tries))
                    self.destroy()
            self.time -= 1
        else:
            games.screen.clear()
            games.screen.background = games.load_image("GUI/Black.png")
            games.screen.add(Lose())


class Smarttapper(games.Text):
    def __init__(self):
        games.screen.clear()
        self.cooldown = 0
        self.time = 600
        self.taps = 0
        self.need_taps = Characteristics.Trains["Strength"] * 4
        super().__init__("Нажимай пробел", 100, x=600, y=200, color=color.green)
        games.screen.add(games.Text("как можно чаще!", 100, x=600, y=400, color=color.green))
        self.taps_count = games.Text(str(self.taps), 100, x=600, y=600, color=color.green)
        games.screen.add(self.taps_count)

    def update(self):
        if self.time > 0:
            if games.keyboard.is_pressed(games.K_SPACE) and self.cooldown <= 0:
                self.cooldown = 1
                self.taps += 1
                self.taps_count.destroy()
                self.taps_count.value = str(self.taps)
                games.screen.add(self.taps_count)
            self.time -= 1
            if not games.keyboard.is_pressed(games.K_SPACE):
                self.cooldown -= 1
        else:
            if self.taps >= self.need_taps:
                if Characteristics.Trains["Strength"] < 10:
                    Characteristics.Trains["Strength"] += 1
                else:
                    Variables.Gold += 3
                    Characteristics.XP_characters[str(randint(1, 3))] += 3
                games.screen.clear()
                games.screen.background = games.load_image("GUI/Black.png")
                games.screen.add(Win())
            else:
                games.screen.clear()
                games.screen.background = games.load_image("GUI/Black.png")
                games.screen.add(Lose())
