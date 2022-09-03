from CutScenes import *
from MiniGames import *
from Dungeon import *


class TrainingDummy(games.Sprite):
    def __init__(self, x, y, target, tries, hero):
        self.HP = 1
        super().__init__(games.load_image("Guys/maneken.png"), x=x, y=y)
        self.type = 1
        self.target = target
        self.tries = tries
        self.hero = hero
        self.text1 = 0
        self.text2 = 0
        self.text3 = 0
        if target == 1:
            hero.Can_attack = False
            hero.Can_jump = False
            hero.Can_spell = False
            if tries != 0:
                games.screen.add(games.Text("Здоровье:" + str(self.hero.maxHP), 40, color.brown, left=0, top=160))
                games.screen.add(games.Text("Урон:" + str(self.hero.DMG), 40, color.brown, left=0, top=200))
                games.screen.add(
                    games.Text("Интервал между атаками:" + str(self.hero.Attack_cooldown), 40, color.brown, left=0,
                               top=240))
                if tries in (4, 5, 6, 8, 9):
                    games.screen.add(
                        games.Text("Дальность атаки:" + str(self.hero.Attack_range), 40, color.brown, left=0, top=280))
                games.screen.add(
                    games.Text("Перезарядка рывка:" + str(self.hero.Jump_cooldown), 40, color.brown, left=0, top=320))
                games.screen.add(
                    games.Text("Дистанция рывка:" + str(self.hero.Jump_range), 40, color.brown, left=0, top=360))
                games.screen.add(
                    games.Text("Скорость по горизонтали:" + str(self.hero.SpeedX), 40, color.brown, left=0, top=400))
                games.screen.add(
                    games.Text("Скорость по вертикали:" + str(self.hero.SpeedY), 40, color.brown, left=0, top=440))
                games.screen.add(games.Text("Вот он мой любимый интерефейс!", 40, color.brown, right=1200, top=160))
                games.screen.add(games.Text("Слева направо:", 40, color.brown, right=1200, top=200))
                games.screen.add(games.Text("здоровье,", 40, color.brown, right=1200, top=240))
                games.screen.add(games.Text("золото,", 40, color.brown, right=1200, top=280))
                games.screen.add(games.Text("уровень героя,", 40, color.brown, right=1200, top=320))
                games.screen.add(games.Text("уровень класса,", 40, color.brown, right=1200, top=360))
                games.screen.add(games.Text("уровень игрока,", 40, color.brown, right=1200, top=400))
                games.screen.add(games.Text("шкала атаки,", 40, color.brown, right=1200, top=440))
                games.screen.add(games.Text("шкала рывка,", 40, color.brown, right=1200, top=480))
                games.screen.add(games.Text("шкала способности.", 40, color.brown, right=1200, top=520))
                games.screen.add(games.Text("(и карта локации)", 40, color.brown, right=1200, top=560))
            if tries == 0:
                self.text1 = games.Text("Сначала тебе необходимо познакомиться с героями", 40, color.brown, left=100,
                                        top=20)
                self.text2 = games.Text("Нажимай на цифры 1-9, чтобы узнать информацию о герое", 40, color.brown,
                                        left=100, top=60)
                self.text3 = games.Text("Нажми на 0, чтобы выйти", 40, color.brown, left=100, top=100)
            elif tries == 1:
                games.screen.add(games.Text("'Баланс во плоти'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Воин - рыцарь", 40, color.brown, left=100, top=100))
                games.screen.add(games.Text("Размер оружия: 100x40", 40, color.brown, left=0, top=280))

            elif tries == 2:
                games.screen.add(
                    games.Text("'Больше урона - меньше скорости'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Воин - берсерк", 40, color.brown, left=100, top=100))
                games.screen.add(games.Text("Размер оружия: 80x50", 40, color.brown, left=0, top=280))

            elif tries == 3:
                games.screen.add(games.Text("'Зато его сложно убить'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Воин - защитник", 40, color.brown, left=100, top=100))
                games.screen.add(games.Text("Размер оружия: 80x32", 40, color.brown, left=0, top=280))
            elif tries == 4:
                games.screen.add(games.Text("'Стеклянная пушка'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Маг огня", 40, color.brown, left=100, top=100))
            elif tries == 5:
                games.screen.add(games.Text("'Был бы хорошим лекарем'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Маг льда", 40, color.brown, left=100, top=100))
            elif tries == 6:
                games.screen.add(games.Text("'Типичный маг'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Маг земли", 40, color.brown, left=100, top=100))
            elif tries == 7:
                games.screen.add(
                    games.Text("'Быстрый и слабый'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Разбойник - вор", 40, color.brown, left=100, top=100))
                games.screen.add(games.Text("Размер оружия: 40x16", 40, color.brown, left=0, top=280))
            elif tries == 8:
                games.screen.add(games.Text("'Ненавижу лучников'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Разбойник - лучник", 40, color.brown, left=100, top=100))
            elif tries == 9:
                games.screen.add(
                    games.Text("'Вомзожно, самый несбалансированный герой'", 40, color.brown, left=100, top=60))
                games.screen.add(games.Text("Разбойник - охотник", 40, color.brown, left=100, top=100))

        elif target == 2:
            hero.Can_spell = False
            hero.Can_jump = False
            self.text1 = games.Text("Настоло время познакомить тебя с атакой", 40, color.brown, left=100, top=60)
            self.text2 = games.Text("Для атаки нажми правую кнопку мыши", 40, color.brown, left=100, top=100)
            self.text3 = games.Text("Перезарядка атаки показана в первом круге (красном)", 40, color.brown, left=100,
                                    top=140)
        elif target == 3:
            hero.Can_spell = False
            hero.Can_attack = False
            self.text1 = games.Text("Теперь познакомим тебя с рывком", 40, color.brown, left=100, top=60)
            self.text2 = games.Text("Для рывка нажми правую кнопку мыши", 40, color.brown, left=100, top=100)
            self.text3 = games.Text("Перезарядка рывка показана во втором круге (зелёном)", 40, color.brown, left=100,
                                    top=140)
        else:
            hero.Can_jump = False
            if tries == 0:
                self.text1 = games.Text("Нажав кнопку 'R'('К'), вы используете способность(если вы не разбойник :))",
                                        40, color.brown, left=100, top=20)
                self.text2 = games.Text("Сила способности зависит от количества зарядов в третьем круге (жёлтом)", 40,
                                        color.brown, left=100, top=60)
                self.text3 = games.Text("Заряды получаются за прохождение комнат", 40,
                                        color.brown, left=100, top=100)
            elif tries == 1:
                self.text1 = games.Text("Воин получает неуязвимость и наносит урон врагам поблизости", 40, color.brown,
                                        left=100, top=60)
            elif tries == 2:
                self.text1 = games.Text("Следующая атака воина будет усилена", 40, color.brown, left=100, top=60)
            elif tries == 3:
                self.text1 = games.Text("Воин восстанавливает себе здоровье", 40, color.brown, left=100, top=60)
            elif tries == 4:
                self.text1 = games.Text("Маг уменьшает время между атаками и изменяет урон", 40, color.brown, left=100,
                                        top=60)
            elif tries == 5:
                self.text1 = games.Text("Маг восстанавливает себе здоровье и наносит удары во все стороны", 40,
                                        color.brown, left=100, top=60)
            elif tries == 6:
                self.text1 = games.Text("На месте вашего курсора через 2 секунды упадёт метеорит", 40, color.brown,
                                        left=100, top=60)
            elif tries == 7:
                self.text1 = games.Text("Разбойник имеет шанс на нанесение увеличенного урона и уворот", 40,
                                        color.brown, left=100, top=60)
            elif tries == 8:
                self.text1 = games.Text("Разбойник имеет шанс запустить несколько стрел", 40, color.brown, left=100,
                                        top=60)
            elif tries == 9:
                self.text1 = games.Text("Разбойник имеет шанс увеличить урон и наложить негативные эффекты", 40,
                                        color.brown, left=100, top=60)

        if target != 1 or tries == 0:
            games.screen.add(self.text1)
            if target != 4:
                games.screen.add(self.text2)
                games.screen.add(self.text3)

    def train_2_3(self):
        if self.tries < 9:
            trainings_begin(self.target, self.tries + 1)
        else:
            if not Variables.Edu_complete[self.target - 1]:
                Variables.Edu_complete[self.target - 1] = True
            save()
            games.screen.clear()
            games.screen.background = games.load_image("GUI/Black.png")
            games.screen.add(EduCenterIn(True))

    def train_1_4(self):
        if Variables.Edu_pressed[self.target - 1].count(True) == 9 and not Variables.Edu_complete[self.target - 1]:
            Variables.Edu_complete[self.target - 1] = True

        if games.keyboard.is_pressed(games.K_1) and self.tries != 1:
            Variables.Edu_pressed[self.target - 1][0] = True
            Variables.charges = 8
            trainings_begin(self.target, 1)

        elif games.keyboard.is_pressed(games.K_2) and self.tries != 2:
            Variables.Edu_pressed[self.target - 1][1] = True
            Variables.charges = 8
            trainings_begin(self.target, 2)

        elif games.keyboard.is_pressed(games.K_3) and self.tries != 3:
            Variables.Edu_pressed[self.target - 1][2] = True
            Variables.charges = 8
            trainings_begin(self.target, 3)

        elif games.keyboard.is_pressed(games.K_4) and self.tries != 4:
            Variables.Edu_pressed[self.target - 1][3] = True
            Variables.charges = 8
            trainings_begin(self.target, 4)

        elif games.keyboard.is_pressed(games.K_5) and self.tries != 5:
            Variables.Edu_pressed[self.target - 1][4] = True
            Variables.charges = 8
            trainings_begin(self.target, 5)

        elif games.keyboard.is_pressed(games.K_6) and self.tries != 6:
            Variables.Edu_pressed[self.target - 1][5] = True
            Variables.charges = 8
            trainings_begin(self.target, 6)

        elif games.keyboard.is_pressed(games.K_7) and self.tries != 7:
            Variables.Edu_pressed[self.target - 1][6] = True
            Variables.charges = 8
            trainings_begin(self.target, 7)

        elif games.keyboard.is_pressed(games.K_8) and self.tries != 8:
            Variables.Edu_pressed[self.target - 1][7] = True
            Variables.charges = 8
            trainings_begin(self.target, 8)

        elif games.keyboard.is_pressed(games.K_9) and self.tries != 9:
            Variables.Edu_pressed[self.target - 1][8] = True
            Variables.charges = 8
            trainings_begin(self.target, 9)

        elif games.keyboard.is_pressed(games.K_0):
            save()
            games.screen.clear()
            games.screen.background = games.load_image("GUI/Black.png")
            games.screen.add(EduCenterIn(True))

    def update(self):
        if not Variables.Pause:
            if self.target == 1 or self.target == 4:
                self.train_1_4()

            if self.target == 2:
                if self.HP < 0:
                    self.train_2_3()

            elif self.target == 3:
                for hero in self.overlapping_sprites:
                    try:
                        if hero.Jump:
                            self.train_2_3()
                    except AttributeError:
                        pass


def trainings_begin(target, tries):
    games.screen.clear()
    games.screen.background = games.load_image("Locations/MM/Edu_floor.jpg")
    x = randint(100, Constants.WindowWidth - 100)
    y = randint(100, Constants.WindowHeight - 100)
    if target == 1 or target == 4:
        x = Constants.WindowWidth / 2
        y = Constants.WindowHeight / 2
    the_gg = MainCharacter(Variables.X, Variables.Y, tries)
    games.screen.add(TrainingDummy(x, y, target, tries, the_gg))
    games.screen.add(the_gg)


class MainMenu:
    @staticmethod
    def create():
        games.screen.clear()
        games.screen.background = games.load_image("Locations/MM/MM_location.png")
        Locked = True
        if Variables.Edu_complete.count(True) == 4:
            Locked = False
        if randint(1, 2) == 1:
            games.music.load("sound/MM/post_intro_1.mp3")
        else:
            games.music.load("sound/MM/post_intro_2.mp3")
        games.music.play(-1)
        games.screen.add(MainMenuShop(MainMenuShop.Position, Locked))
        games.screen.add(MainMenuGym(MainMenuGym.Position, Locked))
        games.screen.add(MainMenuEducationCenter(MainMenuEducationCenter.Position))
        games.screen.add(MainMenuDoor())
        games.screen.add(MainCharacter(Constants.WindowWidth / 2, Constants.WindowHeight / 2, 0))


class MainMenuShop(games.Sprite):
    Position = 525

    def __init__(self, y, locked):
        self.Position = MainMenuShop.Position
        if locked:
            super().__init__(image=games.load_image("Locations/MM/MM_shop_locked.png"), x=900, y=y,
                             dy=(y - self.Position) / -Constants.FPS)
        else:
            super().__init__(image=games.load_image("Locations/MM/MM_shop.png"), x=900, y=y,
                             dy=(y - self.Position) / -Constants.FPS)
        self.locked = locked

    def update(self):
        for hero in self.overlapping_sprites:
            try:
                if not self.locked and hero.type == 0:
                    games.screen.background = games.load_image("Locations/MM/MM_shop_inside.png", transparent=False)
                    games.screen.clear()
                    games.load_sound("sound/sfx/Doors_MM.wav").play()
                    games.screen.add(ShopInside())
            except AttributeError:
                pass


class ShopInside(games.Sprite):
    def __init__(self):
        super().__init__(image=games.load_image("Guys/BlackSmith.png"), right=Constants.WindowWidth,
                         bottom=Constants.WindowHeight)
        rnd = randint(1, 5)
        if rnd == 1:
            games.music.load("sound/Somewhere/Shop_1.mp3")
        elif rnd == 2:
            games.music.load("sound/Somewhere/Shop_2.mp3")
        elif rnd == 3:
            games.music.load("sound/Somewhere/Shop_3.mp3")
        elif rnd == 4:
            games.music.load("sound/Somewhere/Shop_4.mp3")
        else:
            games.music.load("sound/Somewhere/Shop_5.ogg")
        games.music.play(-1)
        self.text1 = self.text2 = ""
        if not Variables.Shop:
            self.text1 = games.Text("Здравствуй путник, это магазин", 50, color.purple, x=Constants.WindowWidth / 2,
                                    y=Constants.WindowHeight / 2 - 50)
            self.text2 = games.Text("Здесь ты можешь усилить себя. За некоторую цену", 50, color.purple,
                                    x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2 + 50)
        else:
            self.text1 = games.Text("Вернулся, чтобы получить усиления?", 50, color.purple, x=Constants.WindowWidth / 2,
                                    y=Constants.WindowHeight / 2 - 50)
            self.text2 = games.Text("Надеюсь у тебя хватит монеток. Кхе-хе", 50, color.purple,
                                    x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2 + 50)
        games.screen.add(self.text1)
        games.screen.add(self.text2)
        self.board = games.Sprite(image=games.load_image("Locations/MM/Shop_choose.png", transparent=False),
                                  x=Constants.WindowWidth / 2, y=Constants.WindowHeight / 2)
        self.needbuy = games.Text("", 70, color.pink, x=600, y=385)
        self.Ok = games.Text("Ок", 30, color.green, x=600, y=435)
        self.Yes = games.Text("Да", 30, color.green, x=500, y=435)
        self.No = games.Text("Нет", 30, color.green, x=700, y=435)
        self.price = 0
        self.product = 0
        self.timer = Constants.FPS * 2
        self.choose = False
        self.notenought = False

    @staticmethod
    def create():
        Shop_cell_image = games.load_image("Locations/MM/MM_shop_cell_base.png", transparent=False)
        Gold = games.load_image("GUI/Gold.png", transparent=True)

        games.screen.add(games.Text("Атака", 30, color.green, x=383, y=290))
        games.screen.add(games.Text("Скачок", 30, color.green, x=817, y=290))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=275, y=225))
        if Characteristics.UpgradesDict["Health"] != 5:
            games.screen.add(games.Text("Здоровье", 30, color.dark_red, x=275, y=215))
            games.screen.add(games.Text("Увеличить на 100", 20, color.dark_blue, x=275, y=240))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Health"] * 10, 20, color.yellow, x=275, y=265))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=275, y=225))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=275, y=325))
        if Characteristics.UpgradesDict["Attack_cooldown"] != 3:
            games.screen.add(games.Text("Перезарядка", 30, color.dark_red, x=275, y=315))
            if Characteristics.UpgradesDict["Attack_cooldown"] == 0:
                games.screen.add(games.Text("Уменьшить в 1.2 раза", 20, color.dark_blue, x=275, y=340))
            elif Characteristics.UpgradesDict["Attack_cooldown"] == 1:
                games.screen.add(games.Text("Уменьшить в 1.25 раз", 20, color.dark_blue, x=275, y=340))
            else:
                games.screen.add(games.Text("Уменьшить в 4/3 раза", 20, color.dark_blue, x=275, y=340))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Attack_cooldown"] * 10, 20, color.yellow, x=275, y=365))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=275, y=325))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=275, y=425))
        if Characteristics.UpgradesDict["Strength"] != 30:
            games.screen.add(games.Text("Сила", 30, color.dark_red, x=275, y=415))
            games.screen.add(games.Text("Увеличить на 1", 20, color.dark_blue, x=275, y=440))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Strength"] * 10, 20, color.yellow, x=275, y=465))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=275, y=425))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=275, y=525))
        if Characteristics.UpgradesDict["Spell"] != 3:
            games.screen.add(games.Text("Усилить", 30, color.dark_red, x=275, y=515))
            games.screen.add(games.Text("способность", 20, color.dark_blue, x=275, y=540))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Spell"] * 10, 20, color.yellow, x=275, y=565))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=275, y=525))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=491, y=225))
        if Characteristics.UpgradesDict["Damage"] != 5:
            games.screen.add(games.Text("Урон", 30, color.dark_red, x=491, y=215))
            games.screen.add(games.Text("Увеличить на 10", 20, color.dark_blue, x=491, y=240))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Damage"] * 10, 20, color.yellow, x=491, y=265))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=491, y=225))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=491, y=325))
        if Characteristics.UpgradesDict["Attack_range"] != 6:
            games.screen.add(games.Text("Дальность", 30, color.dark_red, x=491, y=315))
            if Characteristics.UpgradesDict["Attack_range"] == 2:
                games.screen.add(games.Text("Увеличить в 2 раза", 20, color.dark_blue, x=491, y=340))
            elif Characteristics.UpgradesDict["Attack_range"] == 3:
                games.screen.add(games.Text("Увеличить в 1.5 раза", 20, color.dark_blue, x=491, y=340))
            elif Characteristics.UpgradesDict["Attack_range"] == 4:
                games.screen.add(games.Text("Увеличить в 4/3 раза", 20, color.dark_blue, x=491, y=340))
            else:
                games.screen.add(games.Text("Увеличить в 1.25 раз", 20, color.dark_blue, x=491, y=340))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Attack_range"] * 10, 20, color.yellow, x=491, y=365))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=491, y=325))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=491, y=425))
        if Characteristics.UpgradesDict["Agility"] != 30:
            games.screen.add(games.Text("Ловкость", 30, color.dark_red, x=491, y=415))
            games.screen.add(games.Text("Увеличить на 1", 20, color.dark_blue, x=491, y=440))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Agility"] * 10, 20, color.yellow, x=491, y=465))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=491, y=425))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=491, y=525))
        if Characteristics.UpgradesDict["Crit_chance"] != 5:
            games.screen.add(games.Text("Шанс крита", 30, color.dark_red, x=491, y=515))
            if Characteristics.UpgradesDict["Crit_chance"] == 2:
                games.screen.add(games.Text("Увеличить в 1.5 раза", 20, color.dark_blue, x=491, y=540))
            elif Characteristics.UpgradesDict["Crit_chance"] == 3:
                games.screen.add(games.Text("Увеличить в 4/3 раза", 20, color.dark_blue, x=491, y=540))
            else:
                games.screen.add(games.Text("Увеличить в 1.25 раз", 20, color.dark_blue, x=491, y=540))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Crit_chance"] * 10, 20, color.yellow, x=491, y=565))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=491, y=525))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=709, y=225))
        if Characteristics.UpgradesDict["SpeedX"] != 4:
            games.screen.add(games.Text("Скорость (x)", 30, color.dark_red, x=709, y=215))
            if Characteristics.UpgradesDict["SpeedX"] == 1:
                games.screen.add(games.Text("Увеличить в 2 раза", 20, color.dark_blue, x=709, y=240))
            elif Characteristics.UpgradesDict["SpeedX"] == 2:
                games.screen.add(games.Text("Увеличить в 1.5 раза", 20, color.dark_blue, x=709, y=240))
            else:
                games.screen.add(games.Text("Увеличить в 1.33 раза", 20, color.dark_blue, x=709, y=240))
            games.screen.add(games.Text(Characteristics.UpgradesDict["SpeedX"] * 10, 20, color.yellow, x=709, y=265))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=709, y=225))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=709, y=325))
        if Characteristics.UpgradesDict["Jump_cooldown"] != 2:
            games.screen.add(games.Text("Перезарядка", 30, color.dark_red, x=709, y=315))
            games.screen.add(games.Text("Уменьшить в 2 раза", 20, color.dark_blue, x=709, y=340))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Jump_cooldown"] * 10, 20, color.yellow, x=709, y=365))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=709, y=325))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=709, y=425))
        if Characteristics.UpgradesDict["Intelligence"] != 30:
            games.screen.add(games.Text("Интеллект", 30, color.dark_red, x=709, y=415))
            games.screen.add(games.Text("Увеличить на 1", 20, color.dark_blue, x=709, y=440))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Intelligence"] * 10, 20, color.yellow, x=709, y=465))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=709, y=425))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=709, y=525))
        if Characteristics.UpgradesDict["Crit_damage"] != 3:
            games.screen.add(games.Text("Крит урон", 30, color.dark_red, x=709, y=515))
            if Characteristics.UpgradesDict["Crit_damage"] == 0:
                games.screen.add(games.Text("Увеличить в 1.2 раза", 20, color.dark_blue, x=709, y=540))
            elif Characteristics.UpgradesDict["Crit_damage"] == 1:
                games.screen.add(games.Text("Увеличить в 7/6 раз", 20, color.dark_blue, x=709, y=540))
            else:
                games.screen.add(games.Text("Увеличить в 8/7 раз", 20, color.dark_blue, x=709, y=540))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Crit_damage"] * 10, 20, color.yellow, x=709, y=565))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=709, y=525))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=925, y=225))
        if Characteristics.UpgradesDict["SpeedY"] != 3:
            games.screen.add(games.Text("Скорость (y)", 30, color.dark_red, x=925, y=215))
            if Characteristics.UpgradesDict["SpeedY"] == 1:
                games.screen.add(games.Text("Увеличить в 2 раза", 20, color.dark_blue, x=925, y=240))
            else:
                games.screen.add(games.Text("Увеличить в 1.5 раза", 20, color.dark_blue, x=925, y=240))
            games.screen.add(games.Text(Characteristics.UpgradesDict["SpeedY"] * 10, 20, color.yellow, x=925, y=265))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=925, y=225))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=925, y=325))
        if Characteristics.UpgradesDict["Jump_range"] != 3:
            games.screen.add(games.Text("Дальность", 30, color.dark_red, x=925, y=315))
            if Characteristics.UpgradesDict["Jump_range"] == 1:
                games.screen.add(games.Text("Увеличить в 2 раза", 20, color.dark_blue, x=925, y=340))
            else:
                games.screen.add(games.Text("Увеличить в 1.5 раза", 20, color.dark_blue, x=925, y=340))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Jump_range"] * 10, 20, color.yellow, x=925, y=365))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=925, y=325))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=925, y=425))
        if Characteristics.UpgradesDict["Luck"] != 30:
            games.screen.add(games.Text("Удача", 30, color.dark_red, x=925, y=415))
            games.screen.add(games.Text("Увеличить на 1", 20, color.dark_blue, x=925, y=440))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Luck"] * 10, 20, color.yellow, x=925, y=465))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=925, y=425))

        games.screen.add(games.Sprite(image=Shop_cell_image, x=925, y=525))
        if Characteristics.UpgradesDict["Invincibility"] != 4:
            games.screen.add(games.Text("Неуязвимость", 30, color.dark_red, x=925, y=515))
            games.screen.add(games.Text("Увеличить на 0,25", 20, color.dark_blue, x=925, y=540))
            games.screen.add(games.Text(Characteristics.UpgradesDict["Invincibility"] * 10, 20, color.yellow, x=925, y=565))
        else:
            games.screen.add(games.Text("Куплено", 50, color.black, x=925, y=525))

        games.screen.add(games.Sprite(image=Gold, x=550, y=720))
        games.screen.add(games.Text(Variables.Gold, 50, color.yellow, x=650, y=720))

    def menu(self, enought):
        games.screen.add(self.board)
        if enought:
            self.needbuy.value = "Вам необходимо " + str(self.price) + " , покупаете?"
            games.screen.add(self.needbuy)
            games.screen.add(self.Yes)
            games.screen.add(self.No)
            self.choose = True
        else:
            self.needbuy.value = "Вам нехватает " + str(self.price)
            games.screen.add(self.needbuy)
            games.screen.add(self.Ok)
            self.notenought = True

    def upgrade(self):
        if self.product == 1:
            Characteristics.UpgradesDict["Health"] += 1
        elif self.product == 2:
            Characteristics.UpgradesDict["Damage"] += 1
        elif self.product == 3:
            Characteristics.UpgradesDict["SpeedX"] += 1
        elif self.product == 4:
            Characteristics.UpgradesDict["SpeedY"] += 1
        elif self.product == 5:
            Characteristics.UpgradesDict["Attack_cooldown"] += 1
        elif self.product == 6:
            Characteristics.UpgradesDict["Attack_range"] += 1
        elif self.product == 7:
            Characteristics.UpgradesDict["Jump_cooldown"] += 1
        elif self.product == 8:
            Characteristics.UpgradesDict["Jump_range"] += 1
        elif self.product == 9:
            Characteristics.UpgradesDict["Strength"] += 1
        elif self.product == 10:
            Characteristics.UpgradesDict["Agility"] += 1
        elif self.product == 11:
            Characteristics.UpgradesDict["Intelligence"] += 1
        elif self.product == 12:
            Characteristics.UpgradesDict["Luck"] += 1
        elif self.product == 13:
            Characteristics.UpgradesDict["Spell"] += 1
        elif self.product == 14:
            Characteristics.UpgradesDict["Crit_chance"] += 1
        elif self.product == 15:
            Characteristics.UpgradesDict["Crit_damage"] += 1
        else:
            Characteristics.UpgradesDict["Invincibility"] += 1

    def update(self):
        if self.timer == Constants.FPS:
            self.text1.destroy()
            self.text2.destroy()
            self.create()
        if self.timer > 0:
            self.timer -= 1
        else:
            if games.mouse.is_pressed(0):
                x = games.mouse.x
                y = games.mouse.y
                self.timer = Constants.FPS / 2
                if self.notenought and 420 < y < 450 and 550 < x < 650:
                    self.board.destroy()
                    self.needbuy.destroy()
                    self.Ok.destroy()
                    self.notenought = False
                elif self.choose and 420 < y < 450 and (650 < x < 750 or 450 < x < 550):
                    self.board.destroy()
                    self.needbuy.destroy()
                    self.Yes.destroy()
                    self.No.destroy()
                    self.choose = False
                    if x < 550:
                        Variables.Gold -= self.price
                        games.load_sound("sound/sfx/Event_9.ogg").play()
                        self.upgrade()
                        self.create()
                elif not self.choose and not self.notenought:
                    self.product = 0
                    if 200 < x < 350 and 200 < y < 250 and Characteristics.UpgradesDict["Health"] < 5:
                        self.price = Characteristics.UpgradesDict["Health"] * 10
                        self.product = 1
                    elif 416 < x < 566 and 200 < y < 250 and Characteristics.UpgradesDict["Damage"] < 5:
                        self.price = Characteristics.UpgradesDict["Damage"] * 10
                        self.product = 2
                    elif 634 < x < 784 and 200 < y < 250 and Characteristics.UpgradesDict["SpeedX"] < 4:
                        self.price = Characteristics.UpgradesDict["SpeedX"] * 10
                        self.product = 3
                    elif 850 < x < 1000 and 200 < y < 250 and Characteristics.UpgradesDict["SpeedY"] < 3:
                        self.price = Characteristics.UpgradesDict["SpeedY"] * 10
                        self.product = 4
                    elif 200 < x < 350 and 300 < y < 350 and Characteristics.UpgradesDict["Attack_cooldown"] < 3:
                        self.price = Characteristics.UpgradesDict["Attack_cooldown"] * 10
                        self.product = 5
                    elif 416 < x < 566 and 300 < y < 350 and Characteristics.UpgradesDict["Attack_range"] < 6:
                        self.price = Characteristics.UpgradesDict["Attack_range"] * 10
                        self.product = 6
                    elif 634 < x < 784 and 300 < y < 350 and Characteristics.UpgradesDict["Jump_cooldown"] < 2:
                        self.price = Characteristics.UpgradesDict["Jump_cooldown"] * 10
                        self.product = 7
                    elif 850 < x < 1000 and 300 < y < 350 and Characteristics.UpgradesDict["Jump_range"] < 3:
                        self.price = Characteristics.UpgradesDict["Jump_range"] * 10
                        self.product = 8
                    elif 200 < x < 350 and 400 < y < 450 and Characteristics.UpgradesDict["Strength"] < 30:
                        self.price = Characteristics.UpgradesDict["Strength"] * 10
                        self.product = 9
                    elif 416 < x < 566 and 400 < y < 450 and Characteristics.UpgradesDict["Agility"] < 30:
                        self.price = Characteristics.UpgradesDict["Agility"] * 10
                        self.product = 10
                    elif 634 < x < 784 and 400 < y < 450 and Characteristics.UpgradesDict["Intelligence"] < 30:
                        self.price = Characteristics.UpgradesDict["Intelligence"] * 10
                        self.product = 11
                    elif 850 < x < 1000 and 400 < y < 450 and Characteristics.UpgradesDict["Luck"] < 30:
                        self.price = Characteristics.UpgradesDict["Luck"] * 10
                        self.product = 12
                    elif 200 < x < 350 and 500 < y < 550 and Characteristics.UpgradesDict["Spell"] < 3:
                        self.price = Characteristics.UpgradesDict["Spell"] * 10
                        self.product = 13
                    elif 416 < x < 566 and 500 < y < 550 and Characteristics.UpgradesDict["Crit_chance"] < 5:
                        self.price = Characteristics.UpgradesDict["Crit_chance"] * 10
                        self.product = 14
                    elif 634 < x < 784 and 500 < y < 550 and Characteristics.UpgradesDict["Crit_damage"] < 3:
                        self.price = Characteristics.UpgradesDict["Crit_damage"] * 10
                        self.product = 15
                    elif 850 < x < 1000 and 500 < y < 550 and Characteristics.UpgradesDict["Invincibility"] < 4:
                        self.price = Characteristics.UpgradesDict["Invincibility"] * 10
                        self.product = 16
                    if self.product != 0:
                        if Variables.Gold >= self.price:
                            self.menu(True)
                        else:
                            self.price = self.price - Variables.Gold
                            self.menu(False)
                if 0 < x < 200 and 500 < y < 800:
                    save()
                    games.load_sound("sound/sfx/Doors_MM.wav").play()
                    MainMenu.create()


class MainMenuGym(games.Sprite):
    Position = 280

    def __init__(self, y, locked):
        self.Position = MainMenuGym.Position
        if locked:
            super().__init__(image=games.load_image("Locations/MM/MM_gym_locked.png"), x=200, y=y,
                             dy=(y - self.Position) / -Constants.FPS)
        else:
            super().__init__(image=games.load_image("Locations/MM/MM_gym.png"), x=200, y=y,
                             dy=(y - self.Position) / -Constants.FPS)
        self.locked = locked

    def update(self):
        for hero in self.overlapping_sprites:
            try:
                if not self.locked and hero.type == 0:
                    games.screen.clear()
                    games.screen.background = games.load_image("Minigames/BG.png", transparent=False)
                    games.load_sound("sound/sfx/Doors_MM.wav").play()
                    rnd = randint(1, 5)
                    if rnd == 1:
                        games.music.load("sound/Somewhere/Train_1.mp3")
                    elif rnd == 2:
                        games.music.load("sound/Somewhere/Train_2.mp3")
                    elif rnd == 3:
                        games.music.load("sound/Somewhere/Train_3.mp3")
                    elif rnd == 4:
                        games.music.load("sound/Somewhere/Train_4.mp3")
                    else:
                        games.music.load("sound/Somewhere/Train_5.mp3")
                    games.music.play(-1)
                    games.screen.add(Choose())
            except AttributeError:
                pass


class MainMenuEducationCenter(games.Sprite):
    Position = 615

    def __init__(self, y):
        self.Position = MainMenuEducationCenter.Position
        super().__init__(image=games.load_image("Locations/MM/MM_education.png"), x=325, y=y,
                         dy=(y - self.Position) / -Constants.FPS)

    def update(self):
        for hero in self.overlapping_sprites:
            try:
                if hero.type == 0:
                    games.screen.clear()
                    games.screen.background = games.load_image("GUI/Black.png")
                    games.load_sound("sound/sfx/Doors_MM.wav").play()
                    games.screen.add(EduCenterIn(False))
            except AttributeError:
                pass


class EduCenterIn(games.Sprite):
    def __init__(self, after_edu):
        Variables.HP = 100
        Variables.charges = 8
        self.time = 0
        self.Text_size = 50
        self.Text_unactive_color = color.red
        self.Text_undone_color = color.yellow
        self.Text_done_color = color.green
        self.Text_x = 240
        self.Text_y = 100
        self.Text_width = 240
        self.Text_height = 100
        self.Exit_text_x = 900
        self.Exit_text_y = 700
        super().__init__(image=games.load_image("Guys/Expirience_guy.png"), x=100, y=700)
        self.Hello_Warrior = games.Text(value="Приветсвую, воин. Перед боями нужно пройти обучение, не так ли?",
                                        size=self.Text_size, color=self.Text_undone_color, left=0, y=550)
        if Variables.Edu_complete.count(True) == 4:
            self.Hello_Warrior = games.Text(value="Приветсвую, воин. Решил повторить пройденный материал?",
                                            size=self.Text_size, color=self.Text_undone_color, left=0, y=550)
        self.Characters_train = games.Text(value="Знакомство", size=self.Text_size, color=self.Text_undone_color,
                                           x=self.Text_x, y=self.Text_y)
        self.Attack_train = games.Text(value="Атака", size=self.Text_size, color=self.Text_undone_color,
                                       x=self.Text_x + self.Text_width, y=self.Text_y + self.Text_height)
        self.Jump_train = games.Text(value="Рывок", size=self.Text_size, color=self.Text_undone_color,
                                     x=self.Text_x + self.Text_width * 2, y=self.Text_y + self.Text_height * 2)
        self.Spells_train = games.Text(value="Способность", size=self.Text_size, color=self.Text_undone_color,
                                       x=self.Text_x + self.Text_width * 3, y=self.Text_y + self.Text_height * 3)
        self.Exit = games.Text(value="Выход", size=self.Text_size, color=self.Text_undone_color,
                               x=self.Exit_text_x, y=self.Exit_text_y)
        if Variables.Edu_complete[0]:
            self.Characters_train.color = self.Text_done_color
        else:
            self.Attack_train.color = self.Text_unactive_color
            self.Jump_train.color = self.Text_unactive_color
            self.Spells_train.color = self.Text_unactive_color
        if Variables.Edu_complete[1]:
            self.Attack_train.color = self.Text_done_color
        if Variables.Edu_complete[2]:
            self.Jump_train.color = self.Text_done_color
        if Variables.Edu_complete[3]:
            self.Spells_train.color = self.Text_done_color
        self.after_edu = after_edu

    def update(self):
        if self.time == 0 and not self.after_edu:
            games.screen.add(self.Hello_Warrior)
            games.music.load("sound/Education/Edu.mp3")
            games.music.play(-1)
        if self.time == 3 * Constants.FPS:
            self.Hello_Warrior.destroy()
            Variables.X = 600
            Variables.Y = 400
            games.screen.add(self.Characters_train)
            games.screen.add(self.Attack_train)
            games.screen.add(self.Jump_train)
            games.screen.add(self.Spells_train)
            games.screen.add(self.Exit)
        if self.time == 5 * Constants.FPS and games.mouse.is_pressed(0):
            if self.Text_x - self.Text_width * 0.5 < games.mouse.x < self.Text_x + self.Text_width * 0.5 and \
                    self.Text_y - self.Text_height * 0.5 < games.mouse.y < self.Text_y + self.Text_height * 0.5:
                trainings_begin(1, 0)
            elif self.Text_x + self.Text_width * 0.5 < games.mouse.x < self.Text_x + self.Text_width * 1.5 and \
                    self.Text_y + self.Text_height * 0.5 < games.mouse.y < self.Text_y + self.Text_height * 1.5 and \
                    Variables.Edu_complete[0]:
                trainings_begin(2, 1)
            elif self.Text_x + self.Text_width * 1.5 < games.mouse.x < self.Text_x + self.Text_width * 2.5 and \
                    self.Text_y + self.Text_height * 1.5 < games.mouse.y < self.Text_y + self.Text_height * 2.5 and \
                    Variables.Edu_complete[0]:
                trainings_begin(3, 1)
            elif self.Text_x + self.Text_width * 2.5 < games.mouse.x < self.Text_x + self.Text_width * 3.5 and \
                    self.Text_y + self.Text_height * 2.5 < games.mouse.y < self.Text_y + self.Text_height * 3.5 and \
                    Variables.Edu_complete[0]:
                trainings_begin(4, 0)
            elif self.Exit_text_x - 100 < games.mouse.x < self.Exit_text_x + 100 and \
                    self.Exit_text_y - 100 < games.mouse.y < self.Exit_text_y + 100:
                games.load_sound("sound/sfx/Doors_MM.wav").play()
                MainMenu.create()
        if self.time < 5 * Constants.FPS:
            self.time += 1


class MainMenuDoor(games.Sprite):
    def __init__(self):
        if Variables.Edu_complete.count(True) == 0 and not Variables.Intro or Variables.Edu_complete.count(
                True) == 4 and Variables.Intro:
            super().__init__(image=games.load_image("Locations/MM/MM_door.png", transparent=False), x=600, y=75)
        elif Variables.Intro and Variables.Edu_complete.count(True) < 4:
            super().__init__(image=games.load_image("Locations/MM/MM_door_locked.png", transparent=False), x=600, y=75)

    def update(self):
        try:
            for hero in self.overlapping_sprites:
                if hero.type == 0 and Variables.Edu_complete.count(True) == 0 and not Variables.Intro:
                    super().__init__(image=games.load_image("Locations/MM/MM_door_locked.png", transparent=False),
                                     x=600,
                                     y=75)
                    hero.destroy()
                    games.screen.add(
                        IntroCutScene(hero.x, hero.y, MainMenuShop(0, True), MainMenuGym(0, True),
                                      MainMenuEducationCenter(0)))
                    Variables.Intro = True
                if Variables.Edu_complete.count(True) == 4 and Variables.Intro:
                    games.load_sound("sound/sfx/Door_dungeon.wav").play()
                    games.screen.add(EnterTheDungeon())
        except AttributeError:
            pass
