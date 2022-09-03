from Enemies import *


class Win(games.Text):
    def __init__(self):
        games.screen.clear()
        games.screen.background = games.load_image("GUI/Black.png")
        Variables.Stage = 0
        Variables.Floor = 0
        Variables.Character = 0
        super().__init__("Победа!", 100, color.red, x=600, y=400)
        games.screen.add(games.Text("(ждите следующего обновления)", 50, color.blue, x=600, y=600))
        self.timer = 180

    def update(self):
        if self.timer == 0:
            save()
            MainMenu.MainMenu.create()
        else:
            self.timer -= 1


class Event(games.Text):
    def __init__(self, type_):
        Variables.Special_played = True
        self.timer = -1
        games.screen.background = games.load_image("GUI/Black.png")
        games.screen.clear()
        if type_ in (3, 6, 7):
            value = "Хотите ли вы проверить свою удачу?"
            games.screen.add(games.Text("Да", 30, color.green, x=300, y=600))
            games.screen.add(games.Text("Нет", 30, color.green, x=900, y=600))
        elif type_ in (4, 9):
            value = "Вам повезло!"
        else:
            value = "Хотите ли вы"
            games.screen.add(games.Text("Да", 30, color.green, x=300, y=600))
            games.screen.add(games.Text("Нет", 30, color.green, x=900, y=600))
        if type_ == 3:
            games.screen.add(games.Text("(Потерять " + str(Variables.Gold/2) + "золота или получить " + str(Variables.Gold) + " золота)", 50, color.yellow, x=600, y=400))
        elif type_ == 4:
            if Variables.Character not in (7, 8, 9):
                games.screen.add(games.Text("Восстановлено " + str(Variables.HP/4) + " здоровья и 2 заряда!", 50, color.yellow, x=600, y=400))
                Variables.HP = Variables.HP * 1.25
                if Variables.charges < 7:
                    Variables.charges += 2
            else:
                games.screen.add(games.Text("Восстановлено " + str(Variables.HP/3) + " здоровья!", 50, color.yellow, x=600, y=400))
                Variables.HP = Variables.HP * 4 / 3
                games.load_sound("sound/sfx/Event_4.ogg").play()
            self.timer = 180
        elif type_ == 5:
            games.screen.add(games.Text("пропустить следующий этаж?", 50, color.yellow, x=600, y=400))
        elif type_ == 6:
            games.screen.add(games.Text("Восстановить" + str(Variables.HP/2) + " или потерять " + str(Variables.HP/4) + " здоровья?", 50, color.yellow, x=600, y=400))
        elif type_ == 7:
            games.screen.add(games.Text("Убить босса или умереть", 50, color.yellow, x=600, y=400))
        elif type_ == 8:
            games.screen.add(games.Text("потерять " + str(Variables.HP/2) + " здоровья и получить " + str(Variables.HP/4) + "золота", 50, color.yellow, x=600, y=400))
        elif type_ == 9:
            games.screen.add(games.Text("Вы получили 5 монет!", 50, color.yellow, x=600, y=400))
            Variables.Gold += 5
            self.timer = 180
            games.load_sound("sound/sfx/Event_9.ogg").play()
        self.type = type_

        super().__init__(value, 70, color.pink, x=600, y=200)

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        elif self.timer == 0:
            Variables.Position[0], Variables.Prev_position[0] = Variables.Prev_position[0], Variables.Position[0]
            Variables.Position[1], Variables.Prev_position[1] = Variables.Prev_position[1], Variables.Position[1]
            room()
        elif self.type in (3, 5, 6, 7, 8) and games.mouse.is_pressed(0) and 500 < games.mouse.y < 700:
            if 150 < games.mouse.x < 450:
                rnd = randint(0, 1)
                if self.type in (3, 6, 7):
                    if rnd == 0:
                        if self.type == 7:
                            games.load_sound("sound/sfx/Event_7_death.wav").play()
                        else:
                            games.load_sound("sound/sfx/Event_lose.ogg").play()
                    else:
                        games.load_sound("sound/sfx/Event_win.ogg").play()
                if self.type == 3:
                    if rnd == 0:
                        Variables.Gold = Variables.Gold / 2
                    else:
                        Variables.Gold = Variables.Gold * 2
                elif self.type == 5:
                    if Variables.Floor == 0:
                        Variables.Floor += 1
                    else:
                        Variables.Floor = 0
                        Variables.Stage += 1
                elif self.type == 6:
                    if rnd == 0:
                        Variables.HP = Variables.HP * 3 / 4
                    else:
                        Variables.HP = Variables.HP * 3 / 2
                elif self.type == 7:
                    if rnd == 0:
                        games.screen.add(Lose())
                    else:
                        Variables.Boss_dead = True
                else:
                    Variables.Gold += Variables.HP / 4
                    Variables.HP -= Variables.HP / 2
                self.timer = 1

            elif 750 < games.mouse.x < 1050:
                Variables.Position[0], Variables.Prev_position[0] = Variables.Prev_position[0], Variables.Position[0]
                Variables.Position[1], Variables.Prev_position[1] = Variables.Prev_position[1], Variables.Position[1]
                room()


class TrapDoor(games.Sprite):
    def __init__(self):
        super().__init__(games.load_image("Locations/Doors/TrapDoor_locked.png"), x=600, y=400)
        self.can_go = False

    def update(self):
        if Variables.X < self.left or Variables.X > self.right or Variables.Y < self.top or Variables.Y > self.bottom:
            self.can_go = True
            self._replace(games.load_image("Locations/Doors/TrapDoor_unlocked.png"))
        if self.can_go:
            for hero in self.overlapping_sprites:
                try:
                    if hero.type == 0:
                        print(Variables.Stage)
                        if Variables.Floor == 0:
                            Variables.Floor += 1
                        else:
                            Variables.Floor = 0
                            Variables.Stage += 1
                        print(Variables.Stage)
                        if Variables.Stage == 4:
                            games.screen.add(Win())
                        else:
                            Variables.Gold += (Variables.Stage + 1 + Variables.Floor)
                            Characteristics.XP_characters[str(Variables.Character)] += (Variables.Stage + 1 + Variables.Floor)
                            map_generate()
                            map_visualisation()
                            map_filling()
                            room()
                except AttributeError:
                    pass


class Doors(games.Sprite):
    def __init__(self, place, type_, locked):
        image = x = y = None
        if place == 4:
            if locked or (type_ == 3 and Variables.Special_played):
                image = games.load_image("Locations/Doors/door(right)_close.png")
            elif type_ == 1:
                image = games.load_image("Locations/Doors/door(right)_normal.png")
            elif type_ == 2:
                image = games.load_image("Locations/Doors/door(right)_boss.png")
            elif type_ == 3:
                image = games.load_image("Locations/Doors/door(right)_special.png")
            x = 1177
            y = 400
        elif place == 3:
            if locked or (type_ == 3 and Variables.Special_played):
                image = games.load_image("Locations/Doors/door(left)_close.png")
            elif type_ == 1:
                image = games.load_image("Locations/Doors/door(left)_normal.png")
            elif type_ == 2:
                image = games.load_image("Locations/Doors/door(left)_boss.png")
            elif type_ == 3:
                image = games.load_image("Locations/Doors/door(left)_special.png")
            x = 22
            y = 400
        elif place == 2:
            if locked or (type_ == 3 and Variables.Special_played):
                image = games.load_image("Locations/Doors/door(bottom)_close.png")
            elif type_ == 1:
                image = games.load_image("Locations/Doors/door(bottom)_normal.png")
            elif type_ == 2:
                image = games.load_image("Locations/Doors/door(bottom)_boss.png")
            elif type_ == 3:
                image = games.load_image("Locations/Doors/door(bottom)_special.png")
            x = 600
            y = 766
        elif place == 1:
            if locked or (type_ == 3 and Variables.Special_played):
                image = games.load_image("Locations/Doors/door(top)_close.png")
            elif type_ == 1:
                image = games.load_image("Locations/Doors/door(top)_normal.png")
            elif type_ == 2:
                image = games.load_image("Locations/Doors/door(top)_boss.png")
            elif type_ == 3:
                image = games.load_image("Locations/Doors/door(top)_special.png")
            x = 600
            y = 27
        self.type_ = type_
        self.locked = locked
        self.place = place
        super().__init__(image, x=x, y=y)

    def update(self):
        if Variables.Chart[Variables.Position[0]][Variables.Position[1]][0] == 2:
            if Variables.Boss_dead and self.locked:
                games.screen.add(Doors(self.place, self.type_, False))
                save()
                self.destroy()
        elif Variables.Num_of_enemies == 0 and self.locked:
            if Variables.Chart[Variables.Position[0]][Variables.Position[1]][-2] == 1:
                Variables.Chart[Variables.Position[0]][Variables.Position[1]][-2] = 0
                if Variables.charges < 8 and Variables.Character not in (7, 8, 9):
                    Variables.charges += 1
                    SpellBar(Variables.charges)
            games.screen.add(Doors(self.place, self.type_, False))
            save()
            self.destroy()

        if not self.locked:
            for hero in self.overlapping_sprites:
                try:
                    if hero.type == 0:
                        if self.place == 1:
                            Variables.Prev_position[0] = Variables.Position[0]
                            Variables.Prev_position[1] = Variables.Position[1]
                            Variables.Position[0] -= 1
                        elif self.place == 2:
                            Variables.Prev_position[0] = Variables.Position[0]
                            Variables.Prev_position[1] = Variables.Position[1]
                            Variables.Position[0] += 1
                        elif self.place == 3:
                            Variables.Prev_position[0] = Variables.Position[0]
                            Variables.Prev_position[1] = Variables.Position[1]
                            Variables.Position[1] -= 1
                        elif self.place == 4:
                            Variables.Prev_position[0] = Variables.Position[0]
                            Variables.Prev_position[1] = Variables.Position[1]
                            Variables.Position[1] += 1
                        room()
                except AttributeError:
                    pass


class EnterTheDungeon(games.Text):
    def __init__(self):
        games.music.stop()
        Variables.Stage = Variables.Floor = 0
        games.screen.clear()
        games.screen.background = games.load_image("GUI/Black.png")
        super().__init__("Выбери класс", 100, color.purple, x=600, y=50)
        games.screen.add(games.Text("Воин", 80, color.red, x=600, y=150))
        games.screen.add(games.Text("рыцарь", 60, color.red, x=300, y=220))
        games.screen.add(games.Text("берсерк", 60, color.red, x=600, y=220))
        games.screen.add(games.Text("защитник", 60, color.red, x=900, y=220))
        games.screen.add(games.Text("Маг", 80, color.blue, x=600, y=350))
        games.screen.add(games.Text("огня", 60, color.blue, x=300, y=420))
        games.screen.add(games.Text("льда", 60, color.blue, x=600, y=420))
        games.screen.add(games.Text("земли", 60, color.blue, x=900, y=420))
        games.screen.add(games.Text("Разбойник", 80, color.green, x=600, y=550))
        games.screen.add(games.Text("вор", 60, color.green, x=300, y=620))
        games.screen.add(games.Text("лучник", 60, color.green, x=600, y=620))
        games.screen.add(games.Text("охотник", 60, color.green, x=900, y=620))

    def update(self):
        if games.mouse.is_pressed(0):
            character = type_ = None
            if 190 < games.mouse.y < 250:
                character = 0
            elif 390 < games.mouse.y < 450:
                character = 1
            elif 590 < games.mouse.y < 650:
                character = 2
            if 200 < games.mouse.x < 400:
                type_ = 1
            elif 500 < games.mouse.x < 700:
                type_ = 2
            elif 800 < games.mouse.x < 1000:
                type_ = 3
            if character is not None and type_ is not None:
                map_generate()
                map_visualisation()
                map_filling()
                Variables.Character = character * 3 + type_
                room()


def map_generate():
    Variables.Boss_dead = Variables.Special_played = False
    Variables.HP = Variables.charges = None
    rnd = randint(1, 7)
    if Variables.Stage == 0:
        chart = [[0, 0, 0],
                 [0, 11, 0],
                 [1, 0, 0]]
        if rnd == 1:
            games.music.load("sound/Dungeon/Stage_1/1.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_1/2.mp3")
        elif rnd == 3:
            games.music.load("sound/Dungeon/Stage_1/3.mp3")
        elif rnd == 4:
            games.music.load("sound/Dungeon/Stage_1/4.mp3")
        elif rnd == 5:
            games.music.load("sound/Dungeon/Stage_1/5.mp3")
        elif rnd == 6:
            games.music.load("sound/Dungeon/Stage_1/6.mp3")
        else:
            games.music.load("sound/Dungeon/Stage_1/7.mp3")
    elif Variables.Stage == 1:
        chart = [[0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0],
                 [1, 0, 0, 0, 0]]
        if rnd == 1:
            games.music.load("sound/Dungeon/Stage_2/1.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_2/2.mp3")
        elif rnd == 3:
            games.music.load("sound/Dungeon/Stage_2/3.mp3")
        elif rnd == 4:
            games.music.load("sound/Dungeon/Stage_2/4.mp3")
        elif rnd == 5:
            games.music.load("sound/Dungeon/Stage_2/5.mp3")
        elif rnd == 6:
            games.music.load("sound/Dungeon/Stage_2/6.mp3")
        else:
            games.music.load("sound/Dungeon/Stage_2/7.mp3")
    elif Variables.Stage == 2:
        chart = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0],
                 [1, 0, 0, 0, 0, 0, 0]]
        if rnd == 1:
            games.music.load("sound/Dungeon/Stage_3/1.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_3/2.mp3")
        elif rnd == 3:
            games.music.load("sound/Dungeon/Stage_3/3.mp3")
        elif rnd == 4:
            games.music.load("sound/Dungeon/Stage_3/4.mp3")
        elif rnd == 5:
            games.music.load("sound/Dungeon/Stage_3/5.mp3")
        elif rnd == 6:
            games.music.load("sound/Dungeon/Stage_3/6.mp3")
        else:
            games.music.load("sound/Dungeon/Stage_3/7.mp3")
    else:
        chart = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 11, 0, 11, 0, 11, 0, 11, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        if rnd == 1:
            games.music.load("sound/Dungeon/Stage_4/1.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_4/2.ogg")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_4/3.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_4/4.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_4/5.mp3")
        elif rnd == 2:
            games.music.load("sound/Dungeon/Stage_4/6.ogg")
        else:
            games.music.load("sound/Dungeon/Stage_4/7.mp3")
    games.music.play(-1)
    Variables.Position = cur = [len(chart) - 1, 0]
    Variables.Prev_position[0] = Variables.Position[0]
    Variables.Prev_position[1] = Variables.Position[1]
    prev = []
    nxt = []
    length = 1
    boss = 0
    special = 0
    while True:
        nxt.clear()
        var = 0
        extra_dead_end = 0
        for i in range(cur[0] - 1, cur[0] + 2, 2):
            if -1 < i < len(chart) and chart[i][cur[1]] == 10:
                extra_dead_end += 1
            if -1 < i < len(chart) and chart[i][cur[1]] == 0:
                var += 1
                nxt.append([i, cur[1]])
        for j in range(cur[1] - 1, cur[1] + 2, 2):
            if -1 < j < len(chart) and chart[cur[0]][j] == 10:
                extra_dead_end += 1
            if -1 < j < len(chart) and chart[cur[0]][j] == 0:
                var += 1
                nxt.append([cur[0], j])
        if var > 0:
            prev.append(cur)
            rnd = randint(0, var - 1)
            cur = nxt[rnd]
            if length < len(chart):
                chart[cur[0]][cur[1]] = 1
                length += 1
            elif length == len(chart):
                if boss == 0:
                    chart[cur[0]][cur[1]] = 2
                    boss = 1
                elif special == 0:
                    rnd = randint(3, 9)
                    chart[cur[0]][cur[1]] = rnd
                    special = 1
                else:
                    chart[cur[0]][cur[1]] = 1
                for i in range(cur[0] - 1, cur[0] + 2, 2):
                    if -1 < i < len(chart) and chart[i][cur[1]] == 0:
                        if chart[i][cur[1]] == 0:
                            chart[i][cur[1]] = 10
                for j in range(cur[1] - 1, cur[1] + 2, 2):
                    if -1 < j < len(chart) and chart[cur[0]][j] == 0:
                        if chart[cur[0]][j] == 0:
                            chart[cur[0]][j] = 10
                cur = prev.pop()
        elif extra_dead_end == 1:
            chart[cur[0]][cur[1]] = 1
            for i in range(cur[0] - 1, cur[0] + 2, 2):
                if -1 < i < len(chart) and chart[i][cur[1]] == 0:
                    if chart[i][cur[1]] == 0:
                        chart[i][cur[1]] = 10
            for j in range(cur[1] - 1, cur[1] + 2, 2):
                if -1 < j < len(chart) and chart[cur[0]][j] == 0:
                    if chart[cur[0]][j] == 0:
                        chart[cur[0]][j] = 10
            cur = prev.pop()
        else:
            try:
                cur = prev.pop()
            except IndexError:
                break
            length -= 1
    Variables.Chart = chart


def map_visualisation():
    if Variables.Stage == 0:
        chart_2 = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
    elif Variables.Stage == 1:
        chart_2 = [[[0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0]]]
    elif Variables.Stage == 2:
        chart_2 = [[[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0]]]
    else:
        chart_2 = [[[0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
                   [[0], [0], [0], [0], [0], [0], [0], [0], [0]]]

    for i in range(len(Variables.Chart)):
        for j in range(len(Variables.Chart)):
            ij = [Variables.Chart[i][j]]
            if Variables.Chart[i][j] in range(1, 10):
                if i > 0 and Variables.Chart[i - 1][j] in range(1, 10):
                    if Variables.Chart[i - 1][j] == 1:
                        ij.append(1)
                    elif Variables.Chart[i - 1][j] == 2:
                        ij.append(2)
                    else:
                        ij.append(3)
                else:
                    ij.append(0)
                if i < len(Variables.Chart) - 1 and Variables.Chart[i + 1][j] in range(1, 10):
                    if Variables.Chart[i + 1][j] == 1:
                        ij.append(1)
                    elif Variables.Chart[i + 1][j] == 2:
                        ij.append(2)
                    else:
                        ij.append(3)
                else:
                    ij.append(0)
                if j > 0 and Variables.Chart[i][j - 1] in range(1, 10):
                    if Variables.Chart[i][j - 1] == 1:
                        ij.append(1)
                    elif Variables.Chart[i][j - 1] == 2:
                        ij.append(2)
                    else:
                        ij.append(3)
                else:
                    ij.append(0)
                if j < len(Variables.Chart) - 1 and Variables.Chart[i][j + 1] in range(1, 10):
                    if Variables.Chart[i][j + 1] == 1:
                        ij.append(1)
                    elif Variables.Chart[i][j + 1] == 2:
                        ij.append(2)
                    else:
                        ij.append(3)
                else:
                    ij.append(0)
            chart_2[i][j] = ij

    for i in range(len(Variables.Chart)):
        for j in range(len(Variables.Chart)):
            Variables.Chart[i][j] = chart_2[i][j]


def map_filling():
    for i in range(len(Variables.Chart)):
        for j in range(len(Variables.Chart)):
            if Variables.Chart[i][j][0] == 1:
                rnd = randint(1, 100)
                if rnd <= 25 - 8 * Variables.Stage:
                    num_of_enemies = 0
                elif rnd <= 47 - 7 * Variables.Stage:
                    num_of_enemies = 1
                elif rnd <= 65 - 6 * Variables.Stage:
                    num_of_enemies = 2
                elif rnd <= 80 - 5 * Variables.Stage:
                    num_of_enemies = 3
                elif rnd <= 92 - 4 * Variables.Stage:
                    num_of_enemies = 4
                elif rnd <= 100 - 3 * Variables.Stage:
                    num_of_enemies = 5
                else:
                    num_of_enemies = 6
                Variables.Chart[i][j].append(num_of_enemies)
                enemy_pool = [0, 0, 0, 0, 0]
                for _ in range(num_of_enemies):
                    rnd = randint(1, 100)
                    if rnd <= 30 - 20 * Variables.Floor:
                        enemy_pool[0] += 1
                    elif rnd <= 55 - 30 * Variables.Floor:
                        enemy_pool[1] += 1
                    elif rnd <= 75 - 30 * Variables.Floor:
                        enemy_pool[2] += 1
                    elif rnd <= 90 - 20 * Variables.Floor:
                        enemy_pool[3] += 1
                    elif rnd <= 100:
                        enemy_pool[4] += 1
                for z in range(4):
                    if z == Variables.Stage:
                        for k in range(5):
                            Variables.Chart[i][j].append(enemy_pool[k])
                    else:
                        for k in range(5):
                            Variables.Chart[i][j].append(0)
                Variables.Chart[i][j].append(1)

            elif Variables.Chart[i][j][0] == 2:
                if Variables.Stage == 1:
                    rnd = randint(1 + Variables.Floor * 3, 2 + Variables.Floor * 3)
                elif Variables.Stage == 2:
                    if Variables.Floor == 0:
                        rnd = randint(1, 3)
                    else:
                        rnd = choice((1, 5))
                elif Variables.Stage == 3:
                    if Variables.Floor == 0:
                        rnd = randint(1, 3)
                    else:
                        rnd = randint(3, 5)
                        if rnd == 3:
                            rnd = 1
                else:
                    rnd = randint(1 + Variables.Floor * 2, 3 + Variables.Floor * 2)
                for z in range(4):
                    if z == Variables.Stage:
                        Variables.Chart[i][j].append(rnd)
                    else:
                        Variables.Chart[i][j].append(0)
            if not Variables.map_unlocked:
                Variables.Chart[i][j].append(0)
            else:
                Variables.Chart[i][j].append(Variables.Chart[i][j][0])


def map_drawing():
    cur = Variables.Chart[Variables.Position[0]][Variables.Position[1]]
    cur[-1] = 11
    try:
        top = Variables.Chart[Variables.Position[0] - 1][Variables.Position[1]]
        if cur[1] not in (0, 10, 11):
            if top[-1] == 0:
                top[-1] = 10
            elif top[-1] == 11:
                top[-1] = top[0]
    except IndexError:
        pass
    try:
        bottom = Variables.Chart[Variables.Position[0] + 1][Variables.Position[1]]
        if cur[2] not in (0, 10, 11):
            if bottom[-1] == 0:
                bottom[-1] = 10
            elif bottom[-1] == 11:
                bottom[-1] = bottom[0]
    except IndexError:
        pass
    try:
        left = Variables.Chart[Variables.Position[0]][Variables.Position[1] - 1]
        if cur[3] not in (0, 10, 11):
            if left[-1] == 0:
                left[-1] = 10
            elif left[-1] == 11:
                left[-1] = left[0]
    except IndexError:
        pass
    try:
        right = Variables.Chart[Variables.Position[0]][Variables.Position[1] + 1]
        if cur[4] not in (0, 10, 11):
            if right[-1] == 0:
                right[-1] = 10
            elif right[-1] == 11:
                right[-1] = right[0]
    except IndexError:
        pass
    level_map()


def room():
    games.screen.background = games.load_image("Locations/Dungeon/Location_first.png")
    games.screen.clear()
    cur_location = Variables.Chart[Variables.Position[0]][Variables.Position[1]]
    place = 0
    map_drawing()
    if Variables.Prev_position == Variables.Position:
        games.screen.add(MainCharacter(600, 400, Variables.Character))
    elif Variables.Prev_position[0] > Variables.Position[0]:
        games.screen.add(MainCharacter(600, 600, Variables.Character))
        place = 1
    elif Variables.Prev_position[0] < Variables.Position[0]:
        games.screen.add(MainCharacter(600, 200, Variables.Character))
        place = 2
    elif Variables.Prev_position[1] < Variables.Position[1]:
        games.screen.add(MainCharacter(200, 400, Variables.Character))
        place = 3
    elif Variables.Prev_position[1] > Variables.Position[1]:
        games.screen.add(MainCharacter(1000, 400, Variables.Character))
        place = 4
    if cur_location[0] == 1:
        if cur_location[-2] == 1:
            Variables.Num_of_enemies = cur_location[5]
            for i in range(1, 5):
                if cur_location[i] != 0:
                    games.screen.add(Doors(i, cur_location[i], True))

            for i in range(6, 26):
                if cur_location[i] != 0:
                    for j in range(cur_location[i]):
                        games.screen.add(Enemy(i, 0, place))
        else:
            for i in range(1, 5):
                if cur_location[i] != 0:
                    games.screen.add(Doors(i, cur_location[i], False))
    elif cur_location[0] == 2:
        if not Variables.Boss_dead:
            for i in range(1, 5):
                if cur_location[i] != 0:
                    games.screen.add(Doors(i, cur_location[i], True))
            for i in range(5, 9):
                if cur_location[i] != 0:
                    games.screen.add(Enemy((i - 4) * 5 + cur_location[i], 1, place))
                    break
        else:
            games.screen.add(TrapDoor())
            for i in range(1, 5):
                if cur_location[i] != 0:
                    games.screen.add(Doors(i, cur_location[i], False))
    else:
        games.screen.add(Event(cur_location[0]))
