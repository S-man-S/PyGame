import json
from livewires import games


# class Names:
#     # Sprites:
#     ## Character
#     skin0_base = games.load_image("Character/Done/base.png")
#     skin1_base = games.load_image("Character/Done/warrior_sword.png")
#     skin1_damaged = games.load_image("Character/Done/warrior_sword_damaged.png")
#     skin2_base =
#     skin2_damaged =
#     skin3_base =
#     skin3_damaged =
#     skin4_base =
#     skin4_damaged =
#     skin5_base =
#     skin5_damaged =
#     skin6_base =
#     skin6_damaged =
#     skin7_base =
#     skin7_damaged =
#     skin8_base =
#     skin8_damaged =
#     skin9_base =
#     skin9_damaged =

class Constants:
    FPS = 60
    WindowWidth = 1200
    WindowHeight = 800


def load_to_max():
    file_handler = open("Settings/max_variables.json", encoding="cp1251")
    important_variables = json.load(file_handler)
    Variables.Edu_complete = important_variables["Edu_complete"]
    Variables.Intro = important_variables["Intro"]
    Variables.Shop = important_variables["Shop"]
    Variables.Gold = important_variables["Gold"]
    Variables.Boss_dead = important_variables["Boss_dead"]
    Variables.Special_played = important_variables["Special_played"]
    Variables.Stage = important_variables["Stage"]
    Variables.Floor = important_variables["Floor"]
    Variables.Chart = important_variables["Chart"]
    Variables.Prev_position = important_variables["Prev_position"]
    Variables.Position = important_variables["Position"]
    Variables.HP = important_variables["HP"]
    Variables.charges = important_variables["charges"]
    Variables.Character = important_variables["Character"]
    file_handler = open("Settings/max_trains.json", encoding="cp1251")
    Characteristics.Trains = json.load(file_handler)
    file_handler = open("Settings/max_upgrades.json", encoding="cp1251")
    Characteristics.UpgradesDict = json.load(file_handler)
    file_handler = open("Settings/max_XP.json", encoding="cp1251")
    Characteristics.XP_characters = json.load(file_handler)
    file_handler.close()


def load_to_default():
    file_handler = open("Settings/default_variables.json", encoding="cp1251")
    important_variables = json.load(file_handler)
    Variables.Edu_complete = important_variables["Edu_complete"]
    Variables.Intro = important_variables["Intro"]
    Variables.Shop = important_variables["Shop"]
    Variables.Gold = important_variables["Gold"]
    Variables.Boss_dead = important_variables["Boss_dead"]
    Variables.Special_played = important_variables["Special_played"]
    Variables.Stage = important_variables["Stage"]
    Variables.Floor = important_variables["Floor"]
    Variables.Chart = important_variables["Chart"]
    Variables.Prev_position = important_variables["Prev_position"]
    Variables.Position = important_variables["Position"]
    Variables.HP = important_variables["HP"]
    Variables.charges = important_variables["charges"]
    Variables.Character = important_variables["Character"]
    file_handler = open("Settings/default_trains.json", encoding="cp1251")
    Characteristics.Trains = json.load(file_handler)
    file_handler = open("Settings/default_upgrades.json", encoding="cp1251")
    Characteristics.UpgradesDict = json.load(file_handler)
    file_handler = open("Settings/default_XP.json", encoding="cp1251")
    Characteristics.XP_characters = json.load(file_handler)
    file_handler.close()


def save():
    important_variables = {"Edu_complete": Variables.Edu_complete,
                           "Intro": Variables.Intro,
                           "Shop": Variables.Shop,
                           "Gold": Variables.Gold,
                           "Boss_dead": Variables.Boss_dead,
                           "Special_played": Variables.Special_played,
                           "Stage": Variables.Stage,
                           "Floor": Variables.Floor,
                           "Chart": Variables.Chart,
                           "Prev_position": Variables.Prev_position,
                           "Position": Variables.Position,
                           "HP": Variables.HP,
                           "charges": Variables.charges,
                           "Character": Variables.Character}
    file_handler = open("Settings/variables.json", "w", encoding="cp1251")
    json.dump(important_variables, file_handler)
    file_handler = open("Settings/trains.json", "w", encoding="cp1251")
    json.dump(Characteristics.Trains, file_handler)
    file_handler = open("Settings/upgrades.json", "w", encoding="cp1251")
    json.dump(Characteristics.UpgradesDict, file_handler)
    file_handler = open("Settings/XP.json", "w", encoding="cp1251")
    json.dump(Characteristics.XP_characters, file_handler)
    file_handler.close()


def load():
    file_handler = open("Settings/variables.json", encoding="cp1251")
    important_variables = json.load(file_handler)
    Variables.Edu_complete = important_variables["Edu_complete"]
    Variables.Intro = important_variables["Intro"]
    Variables.Shop = important_variables["Shop"]
    Variables.Gold = important_variables["Gold"]
    Variables.Boss_dead = important_variables["Boss_dead"]
    Variables.Special_played = important_variables["Special_played"]
    Variables.Stage = important_variables["Stage"]
    Variables.Floor = important_variables["Floor"]
    Variables.Chart = important_variables["Chart"]
    Variables.Prev_position = important_variables["Prev_position"]
    Variables.Position = important_variables["Position"]
    Variables.HP = important_variables["HP"]
    Variables.charges = important_variables["charges"]
    Variables.Character = important_variables["Character"]
    file_handler = open("Settings/trains.json", encoding="cp1251")
    Characteristics.Trains = json.load(file_handler)
    file_handler = open("Settings/upgrades.json", encoding="cp1251")
    Characteristics.UpgradesDict = json.load(file_handler)
    file_handler = open("Settings/XP.json", encoding="cp1251")
    Characteristics.XP_characters = json.load(file_handler)
    file_handler.close()


class Variables:
    Edu_complete = [False, False, False, False]
    Intro = False
    Shop = False
    Gold = 0
    Boss_dead = False
    Special_played = False
    Stage = 0
    Floor = 0
    Chart = 0
    Prev_position = [0, 0]
    Position = []
    HP = None
    charges = None
    Character = 0

    map_unlocked = False
    Train_1_pressed = 0
    Train_1_opened = 0
    Train_2_opened = 0
    Num_of_enemies = 0
    X = Y = 0
    CutScene = False
    Pause = False
    YN = False
    Edu_pressed = [[False, False, False, False, False, False, False, False, False], 0, 0,
                   [False, False, False, False, False, False, False, False, False]]


class CurCharacteristics:
    def __init__(self):
        self.Health = Characteristics.UpgradesDict["Health"] * 100
        self.Damage = Characteristics.UpgradesDict["Damage"] * 10
        self.SpeedX = Constants.WindowWidth / 16 * Characteristics.UpgradesDict["SpeedX"]
        self.SpeedY = Constants.WindowHeight / 12 * Characteristics.UpgradesDict["SpeedY"]
        self.Attack_cooldown = 1.2 - Characteristics.UpgradesDict["Attack_cooldown"] * 0.2
        self.Attack_range = Constants.WindowWidth / 12 * Characteristics.UpgradesDict["Attack_range"]
        self.Jump_cooldown = 8 / (2 ** Characteristics.UpgradesDict["Jump_cooldown"])
        self.Jump_range = Constants.WindowWidth / 6 * Characteristics.UpgradesDict["Jump_range"]
        self.Strength = 10 + Characteristics.UpgradesDict["Strength"] + Characteristics.Trains["Strength"] + Characteristics.XP_stats["Strength"]
        self.Intelligence = 10 + Characteristics.UpgradesDict["Intelligence"] + Characteristics.Trains["Intelligence"] + Characteristics.XP_stats["Intelligence"]
        self.Agility = 10 + Characteristics.UpgradesDict["Agility"] + Characteristics.Trains["Agility"] + Characteristics.XP_stats["Agility"]
        self.Luck = 10 + Characteristics.UpgradesDict["Luck"] + Characteristics.Trains["Luck"] + Characteristics.XP_stats["Luck"]
        self.Spell = Characteristics.UpgradesDict["Spell"]
        self.Crit_chance = Characteristics.UpgradesDict["Crit_chance"] * Characteristics.UpgradesDict["Luck"] / 20
        self.Crit_damage = 1.25 + 0.25 * Characteristics.UpgradesDict["Crit_damage"]
        self.Invincibility = Characteristics.UpgradesDict["Invincibility"] * 0.25 + 1


class Characteristics:
    # max prokachka 5 5 4 3 3 6 2 3 30 30 30 30, 3, 5, 3, 4
    UpgradesDict = {"Health": 0, "Damage": 0, "SpeedX": 1, "SpeedY": 1, "Attack_cooldown": 0, "Attack_range": 2,
                    "Jump_cooldown": 0, "Jump_range": 1, "Strength": 0, "Agility": 0, "Intelligence": 0, "Luck": 0,
                    "Spell": 0, "Crit_chance": 2, "Crit_damage": 0, "Invincibility": 0}

    # max prokachka 10, 10, 10, 10
    Trains = {"Strength": 0, "Agility": 0, "Intelligence": 0, "Luck": 0}

    # max prokachka 50, 50, 50, 50
    XP_stats = {"Strength": 0, "Agility": 0, "Intelligence": 0, "Luck": 0}

    XP_characters = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    @staticmethod
    def xp_to_stats(skin):
        XP_characters = Characteristics.XP_characters
        Group_level = 0
        XP_groups = {"Warrior": XP_characters['1'] + XP_characters['2'] + XP_characters['3'],
                     "Mag": XP_characters['4'] + XP_characters['5'] + XP_characters['6'],
                     "Rogue": XP_characters['7'] + XP_characters['8'] + XP_characters['9'],
                     "All": XP_characters['1'] + XP_characters['2'] + XP_characters['3'] + XP_characters['4'] + XP_characters['5'] + XP_characters['6'] + XP_characters['7'] + XP_characters['8'] + XP_characters['9']}
        Characteristics.XP_stats["Strength"] = 0
        Characteristics.XP_stats["Intelligence"] = 0
        Characteristics.XP_stats["Agility"] = 0
        Characteristics.XP_stats["Luck"] = 0
        for i in range(1, 51):
            if skin in range(1, 4) and sum(list(range(1, 51))[:i]) * 3 <= XP_groups["Warrior"]:
                Group_level += 1
                Characteristics.XP_stats["Strength"] += 1
            if skin in range(4, 7) and sum(list(range(1, 51))[:i]) * 3 <= XP_groups["Mag"]:
                Group_level += 1
                Characteristics.XP_stats["Intelligence"] += 1
            if skin in range(7, 10) and sum(list(range(1, 51))[:i]) * 3 <= XP_groups["Rogue"]:
                Group_level += 1
                Characteristics.XP_stats["Agility"] += 1
            if sum(list(range(1, 51))[:i]) * 9 <= XP_groups["All"]:
                Characteristics.XP_stats["Luck"] += 1
        return Group_level, Characteristics.XP_stats["Luck"]
