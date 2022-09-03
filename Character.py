from GUI import *
from Numbers import *
from math import *
from random import *
import MainMenu


class Lose(games.Text):
    def __init__(self):
        games.screen.clear()
        games.screen.background = games.load_image("GUI/Black.png")
        Variables.Stage = 0
        Variables.Floor = 0
        Variables.Character = 0
        save()
        super().__init__("Поражение", 100, color.red, x=600, y=400)
        self.timer = 180

    def update(self):
        if self.timer == 0:
            MainMenu.MainMenu.create()
        if not Variables.Pause:
            self.timer -= 1


class Stone(games.Sprite):
    def __init__(self, x, y, dmg):
        super().__init__(image=games.load_image("Character/Done/Stone.png"), x=x, y=y)
        self.timer = Constants.FPS / 2
        self.DMG = dmg
        self.CanDMG = True
        self.crit_chance = self.crit_damage = 0

    def update(self):
        if self.CanDMG:
            self.CanDMG = False
            for sprite in self.overlapping_sprites:
                try:
                    if sprite.type == 1:
                        games.screen.add(Attack(self, sprite))
                except AttributeError:
                    pass

        if self.timer == 0:
            self.destroy()
        if not Variables.Pause:
            self.timer -= 1


class StoneAOE(games.Sprite):
    def __init__(self, x, y, dmg):
        super().__init__(image=games.load_image("Character/Done/Stone_area.png"), x=x, y=y)
        self.timer = 120
        self.DMG = dmg

    def update(self):
        if self.timer == 0:
            games.screen.add(Stone(self.x, self.y, self.DMG))
            self.destroy()
        if not Variables.Pause:
            self.timer -= 1


class TakeDamage(games.Text):
    def __init__(self, hero, damage):
        self.timer = Constants.FPS
        hero.Invincibilitytimer = hero.Invincibilitytime
        if hero.skin != 7 or randint(1, 100) > hero.Spell * 5 + hero.luck / 10:
            value = str(damage)
            Variables.HP -= damage
            HealthBar.health_bar_update(hero.HPBar, Variables.HP)
            if Variables.HP > 0:
                if Variables.HP > hero.maxHP / 10 > damage:
                    rnd = randint(1, 3)
                    if rnd == 1:
                        sound = games.load_sound("sound/sfx/Damage/Character_pain_1.wav")
                    elif rnd == 2:
                        sound = games.load_sound("sound/sfx/Damage/Character_pain_2.wav")
                    else:
                        sound = games.load_sound("sound/sfx/Damage/Character_pain_3.wav")
                else:
                    sound = games.load_sound("sound/sfx/Damage/Character_lowHP_1.wav")
            else:
                rnd = randint(1, 3)
                if rnd == 1:
                    sound = games.load_sound("sound/sfx/Damage/Character_death_1.ogg")
                elif rnd == 2:
                    sound = games.load_sound("sound/sfx/Damage/Character_death_2.wav")
                else:
                    sound = games.load_sound("sound/sfx/Damage/Character_death_3.wav")
            sound.play(fade_ms=10)
        else:
            value = "Уворот!"
        super().__init__(value=value, size=50, color=color.dark_red, x=hero.x, y=hero.y)

    def update(self):
        if self.timer == 0:
            self.destroy()
        if not Variables.Pause:
            self.timer -= 1


class Attack(games.Text):
    def __init__(self, hero, sprite):
        self.type = 2
        damage = hero.DMG
        if randint(1, 100) <= hero.crit_chance:
            damage *= hero.crit_damage
            text = str(int(damage*10)/10) + "Критический урон!"
            self.time = Constants.FPS * 2
        else:
            text = str(int(damage*10)/10)
            self.time = Constants.FPS
        sprite.HP -= damage
        super().__init__(value=text, size=50, color=color.red, x=sprite.x, y=sprite.y)

    def update(self):
        if self.time == 0:
            self.destroy()
        if not Variables.Pause:
            self.time -= 1


class Weapon(games.Sprite):
    def __init__(self, x, y, hero, angle, dx, dy, attacktime):
        self.type = 2
        games.load_sound("sound/sfx/Damage/melee_hit.wav").play()
        dx /= attacktime
        dy /= attacktime
        if hero.skin == 1:
            image = games.load_image("Character/Done/sword.png")
        elif hero.skin == 2:
            image = games.load_image("Character/Done/double_axe.png")
        elif hero.skin == 3:
            if angle == 0 and dx > 0 or angle == 90 and dy > 0 or angle == 180 and dx < 0 or angle == 270 and dy < 0:
                image = games.load_image("Character/Done/axe.png")
            else:
                image = games.load_image("Character/Done/axe_reversed.png")
        else:
            image = games.load_image("Character/Done/knife.png")
        if angle == 0:
            super().__init__(image=image, x=x, bottom=y, angle=angle)
        elif angle == 90:
            super().__init__(image=image, left=x, y=y, angle=angle)
        elif angle == 180:
            super().__init__(image=image, x=x, top=y, angle=angle)
        elif angle == 270:
            super().__init__(image=image, right=x, y=y, angle=angle)
        self.time = Constants.FPS * attacktime
        self.ddx = dx
        self.ddy = dy
        self.hero = hero

    def update(self):
        if self.time == 0:
            self.destroy()
        if not Variables.Pause:
            self.time -= 1
            self.x += self.ddx
            self.y += self.ddy
        for sprite in self.overlapping_sprites:
            try:
                if sprite.type == 1:
                    games.screen.add(Attack(self.hero, sprite))
                    self.destroy()
            except AttributeError:
                pass


class Bullet(games.Sprite):
    def __init__(self, hero, dx, dy):
        self.type = 2
        if hero.skin == 4:
            image = games.load_image("Character/Done/mage_fire_bullet.png")
        elif hero.skin == 5:
            image = games.load_image("Character/Done/mage_wind_bullet.png")
        elif hero.skin == 6:
            image = games.load_image("Character/Done/mage_earth_bullet.png")
        else:
            image = games.load_image("Character/Done/arrow.png")
            games.load_sound("sound/sfx/Damage/bow_hit.wav").play()

        if hero.skin in (4, 5, 6):
            sound = games.load_sound("sound/sfx/Damage/mag_hit.wav")
            sound.set_volume(0.2)
            sound.play()

        if dx == 0:
            if dy > 0:
                angle = 270
            else:
                angle = 90
        elif dx > 0:
            angle = degrees(atan(dy / dx)) + 180
        else:
            angle = degrees(atan(dy / dx))
        super().__init__(image=image, x=hero.x, y=hero.y, angle=angle)
        self.time = 0
        self.ddx = dx
        self.ddy = dy
        self.hero = hero

    def update(self):
        if self.time == Constants.FPS:
            self.destroy()
        if not Variables.Pause:
            self.time += 1
            self.x += self.ddx
            self.y += self.ddy
        for sprite in self.overlapping_sprites:
            try:
                if sprite.type == 1:
                    games.screen.add(Attack(self.hero, sprite))
                    self.destroy()
            except AttributeError:
                pass


class Kapkan(games.Sprite):
    def __init__(self, x, y, hero):
        super().__init__(image=games.load_image("Character/Done/kapkan.png"), x=x, y=y)
        self.debuff = -1
        if randint(1, 100) <= (hero.Spell + 1) * 5:
            self.debuff = hero.Spell
        self.hero = hero

    def update(self):
        for sprite in self.overlapping_sprites:
            try:
                if sprite.type == 1:
                    damage = self.hero.DMG
                    if self.debuff > -1:
                        self.hero.DMG *= 1.5
                    if self.debuff > 0:
                        self.hero.DMG *= 4/3
                        sprite.Spell_timer = Constants.FPS
                    if self.debuff > 1:
                        self.hero.DMG *= 1.25
                        sprite.Spell_timer = 2 * Constants.FPS
                        sprite.Attack_timer = 2 * Constants.FPS
                    if self.debuff > 2:
                        self.hero.DMG *= 1.2
                        sprite.Spell_timer = 3 * Constants.FPS
                        sprite.Attack_timer = 3 * Constants.FPS
                        sprite.Move_timer = 3 * Constants.FPS
                    games.screen.add(Attack(self.hero, sprite))
                    games.load_sound("sound/sfx/Damage/kapkan_hit.ogg").play()
                    self.hero.DMG = damage
                    self.destroy()
            except AttributeError:
                pass


class MainCharacter(games.Sprite):
    def __init__(self, x, y, skin):
        Group_level, Full_level = Characteristics.xp_to_stats(skin)
        self.Characteristics = CurCharacteristics()
        self.skin = skin
        HealthMultiply = DMGMultiply = MovementMultiply = ACMultiply = 1
        if skin == 0:
            self.imaged = games.load_image("Character/Done/base.png")

        elif skin == 1:
            self.imaged = games.load_image("Character/Done/warrior_sword.png")
            self.damaged = games.load_image("Character/Done/warrior_sword_damaged.png")
            HealthMultiply = 1.25 #1
            DMGMultiply = 1.2 #1
            MovementMultiply = 1 #1
            ACMultiply = 1 #1

        elif skin == 2:
            self.imaged = games.load_image("Character/Done/warrior_axe.png")
            self.damaged = games.load_image("Character/Done/warrior_axe_damaged.png")
            HealthMultiply = 1.2 #1
            DMGMultiply = 1.5 #1.35
            MovementMultiply = 1 #0.9
            ACMultiply = 1.2 #1.2

        elif skin == 3:
            self.imaged = games.load_image("Character/Done/warrior_axe+shield.png")
            self.damaged = games.load_image("Character/Done/warrior_axe+shield_damaged.png")
            HealthMultiply = 1.5 #1.5
            DMGMultiply = 1.2 #0.9
            MovementMultiply = 1 #0.9
            ACMultiply = 1.2 #1.2

        elif skin == 4:
            self.imaged = games.load_image("Character/Done/mage_fire.png")
            self.damaged = games.load_image("Character/Done/mage_fire_damaged.png")
            HealthMultiply = 0.9 #0.8
            DMGMultiply = 1
            MovementMultiply = 1
            ACMultiply = 0.9 #1

        elif skin == 5:
            self.imaged = games.load_image("Character/Done/mage_wind.png")
            self.damaged = games.load_image("Character/Done/mage_wind_damaged.png")
            HealthMultiply = 1
            DMGMultiply = 0.9 #0.8
            MovementMultiply = 1
            ACMultiply = 0.9 #1

        elif skin == 6:
            self.imaged = games.load_image("Character/Done/mage_earth.png")
            self.damaged = games.load_image("Character/Done/mage_earth_damaged.png")
            HealthMultiply = 1 #0.9
            DMGMultiply = 1 #0.9
            MovementMultiply = 1
            ACMultiply = 1 #1

        elif skin == 7:
            self.imaged = games.load_image("Character/Done/rogue_knife.png")
            self.damaged = games.load_image("Character/Done/rogue_knife_damaged.png")
            HealthMultiply = 0.75 #0.6
            DMGMultiply = 1 #0.75
            MovementMultiply = 1.2 #1.2
            ACMultiply = 0.6 #0.6

        elif skin == 8:
            self.imaged = games.load_image("Character/Done/rogue_bow.png")
            self.damaged = games.load_image("Character/Done/rogue_bow_damaged.png")
            HealthMultiply = 0.25 #0.8
            DMGMultiply = 2 #0.8
            MovementMultiply = 1.2 #1.1
            ACMultiply = 0.6 #0.8

        else:
            self.imaged = games.load_image("Character/Done/rogue_kapkan.png")
            self.damaged = games.load_image("Character/Done/rogue_kapkan_damaged.png")
            HealthMultiply = 0.5 #0.85
            DMGMultiply = 2 #2
            MovementMultiply = 1.2 #1.05
            ACMultiply = 1.2 #2

        super().__init__(image=self.imaged, x=x, y=y)

        if 0 < skin < 4:
            self.DMG_type = 0
            MainCharacteristic = self.Characteristics.Strength
        elif skin < 7:
            self.DMG_type = 1
            MainCharacteristic = self.Characteristics.Intelligence
        else:
            self.DMG_type = 0
            MainCharacteristic = self.Characteristics.Agility

        if skin == 9:
            self.Attack_type = 2
            self.Attack_range = 100
        elif 0 < skin < 4 or skin == 7:
            self.Attack_type = 0
            self.Attack_range = 0
        else:
            self.Attack_type = 1
            self.Attack_range = self.Characteristics.Attack_range

        self.type = 0
        self.maxHP = (self.Characteristics.Health + self.Characteristics.Strength * 10) * HealthMultiply
        self.DMG = (self.Characteristics.Damage + MainCharacteristic) * DMGMultiply
        self.SpeedX = int(self.Characteristics.SpeedX * MovementMultiply + self.Characteristics.Agility)
        self.SpeedY = int(self.Characteristics.SpeedY * MovementMultiply + self.Characteristics.Agility)
        self.Jump_range = int(self.Characteristics.Jump_range * MovementMultiply + self.Characteristics.Agility)
        self.Attack_cooldown = int(self.Characteristics.Attack_cooldown * ACMultiply * 100) / 100
        self.Jump_cooldown = self.Characteristics.Jump_cooldown
        if Variables.charges is None:
            Variables.charges = 8
        self.luck = self.Characteristics.Luck
        self.crit_chance = self.Characteristics.Crit_chance
        self.crit_damage = self.Characteristics.Crit_damage
        self.Attack_multiply = 1
        self.Spell = self.Characteristics.Spell
        self.Invincibilitytime = self.Characteristics.Invincibility * Constants.FPS
        self.Attack_no_cooldown = 0
        self.Can_attack = self.Can_jump = self.Can_spell = True

        if skin != 0:
            Level_bonus = 0
            for i in range(1, 51):
                if sum(list(range(1, 51))[:i]) <= Characteristics.XP_characters[str(skin)]:
                    Level_bonus += 1
            self.maxHP += Level_bonus * 5
            self.DMG += Level_bonus

            if Variables.HP is None:
                Variables.HP = self.maxHP

            self.HPBar = HealthBar(Variables.HP)
            self.ABar = AttackBar()
            self.JBar = JumpBar(self.Jump_cooldown)
            if self.skin not in (7, 8, 9):
                self.SBar = SpellBar(Variables.charges)
            else:
                self.SBar = None
            create_gui(self.ABar, self.JBar, self.SBar, self.HPBar)
            games.screen.add(LevelBar(350, Level_bonus))
            games.screen.add(LevelBar(390, Group_level))
            games.screen.add(LevelBar(430, Full_level))
            games.screen.add(GoldBar())

        self.damage = self.DMG
        self.pausetime = 0
        self.attacktime = 0
        self.jumptime = 0
        self.CanMove = True
        self.Jump = False
        self.Invincibilitytimer = -1
        self.spelltime = -1
        self.power_shards = 0
        self.timer = 0
        self.quit_timer = 0

    def update(self):
        if not Variables.Pause:
            Variables.X = self.x
            Variables.Y = self.y

            if games.keyboard.is_pressed(games.K_m) and games.keyboard.is_pressed(games.K_a) and games.keyboard.is_pressed(games.K_p):
                Variables.map_unlocked = True

            if Variables.Character != 0 and games.keyboard.is_pressed(games.K_q):
                self.quit_timer += 1
            else:
                self.quit_timer = 0
            if self.quit_timer == 180:
                MainMenu.MainMenu.create()
                Variables.Character = 0
                save()

            if self.timer > 0:
                self.timer -= 1
            elif self.timer == 0:
                self.power_shards = 0

            if self.power_shards == 0:
                if games.keyboard.is_pressed(games.K_1):
                    self.power_shards += 1
                    self.timer = 180
            elif self.power_shards in (1, 5):
                if games.keyboard.is_pressed(games.K_3):
                    self.power_shards += 1
                    self.timer = 180
            elif self.power_shards in (2, 3):
                if games.keyboard.is_pressed(games.K_2):
                    self.power_shards += 1
                    self.timer = 180
            elif self.power_shards == 4:
                if games.keyboard.is_pressed(games.K_8):
                    self.power_shards += 1
                    self.timer = 180
            elif self.power_shards == 6:
                if games.keyboard.is_pressed(games.K_7):
                    load_to_max()
                    save()
                    MainMenu.MainMenu.create()

            if self.skin != 0 and Variables.HP > self.maxHP:
                Variables.HP = self.maxHP
                HealthBar.health_bar_update(self.HPBar, Variables.HP)

            if self.skin != 0 and Variables.HP <= 0:
                games.screen.add(Lose())
            if self.Invincibilitytimer == 0:
                self._replace(self.imaged)
                self.Invincibilitytimer -= 1
            if self.Invincibilitytimer > 0:
                self._replace(self.damaged)
                self.Invincibilitytimer -= 1

            if self.CanMove:
                if self.x > 50 and games.keyboard.is_pressed(games.K_a):
                    self.x -= self.SpeedX / Constants.FPS
                if self.x < Constants.WindowWidth - 50 and games.keyboard.is_pressed(games.K_d):
                    self.x += self.SpeedX / Constants.FPS
                if self.y > 50 and games.keyboard.is_pressed(games.K_w):
                    self.y -= self.SpeedY / Constants.FPS
                if self.y < Constants.WindowHeight - 50 and games.keyboard.is_pressed(games.K_s):
                    self.y += self.SpeedY / Constants.FPS

            if games.mouse.is_pressed(0) and self.skin != 0 and self.attacktime <= 0 and self.Can_attack:
                if self.Attack_no_cooldown == 0:
                    self.attacktime = (self.Attack_cooldown + 1) * Constants.FPS
                else:
                    self.Attack_no_cooldown -= 1
                    self.attacktime = Constants.FPS
                    if self.Attack_no_cooldown == 0:
                        self.DMG /= 1.25 + 0.25 * self.Spell
                self.ABar.attack(self.attacktime)
                if self.Attack_multiply == 0:
                    self.DMG = self.damage
                    self.Attack_multiply = 1
                if self.Attack_type == 0:
                    if self.skin == 7 and randint(1, 100) <= self.Spell * 5 + self.luck / 10:
                        self.Attack_multiply = 4
                    if self.Attack_multiply != 1:
                        self.DMG *= self.Attack_multiply
                        self.Attack_multiply = 0
                    attack_x = (games.mouse.x - self.x) / 42
                    attack_y = (games.mouse.y - self.y) / 76
                    if abs(attack_x) > abs(attack_y):
                        if attack_x > 0:
                            if attack_y > 0:
                                games.screen.add(Weapon(self.right, self.bottom, self, 90, 0,
                                                        (self.top - self.bottom) / Constants.FPS, 1))
                            else:
                                games.screen.add(
                                    Weapon(self.right, self.top, self, 90, 0, (self.bottom - self.top) / Constants.FPS,
                                           1))
                        else:
                            if attack_y > 0:
                                games.screen.add(Weapon(self.left, self.bottom, self, 270, 0,
                                                        (self.top - self.bottom) / Constants.FPS, 1))
                            else:
                                games.screen.add(
                                    Weapon(self.left, self.top, self, 270, 0, (self.bottom - self.top) / Constants.FPS,
                                           1))
                    else:
                        if attack_y > 0:
                            if attack_x > 0:
                                games.screen.add(
                                    Weapon(self.right, self.bottom, self, 180, (self.left - self.right) / Constants.FPS,
                                           0, 1))
                            else:
                                games.screen.add(
                                    Weapon(self.left, self.bottom, self, 180, (self.right - self.left) / Constants.FPS,
                                           0, 1))
                        else:
                            if attack_x > 0:
                                games.screen.add(
                                    Weapon(self.right, self.top, self, 0, (self.left - self.right) / Constants.FPS, 0,
                                           1))
                            else:
                                games.screen.add(
                                    Weapon(self.left, self.top, self, 0, (self.right - self.left) / Constants.FPS, 0,
                                           1))

                elif self.Attack_type == 1:
                    Chance = randint(1, 100)
                    k = sqrt((games.mouse.x - self.x) ** 2 + (games.mouse.y - self.y) ** 2) / self.Attack_range
                    attack_x = (games.mouse.x - self.x) / k
                    attack_y = (games.mouse.y - self.y) / k
                    dx = attack_x / Constants.FPS
                    dy = attack_y / Constants.FPS
                    if Chance > self.luck / 2 or self.skin != 8:
                        games.screen.add(Bullet(self, dx, dy))
                    else:
                        if self.Spell % 2 == 0:
                            games.screen.add(Bullet(self, dx * 1.1, dy * 0.9))
                            games.screen.add(Bullet(self, dx * 0.9, dy * 1.1))
                        if self.Spell % 2 == 1:
                            games.screen.add(Bullet(self, dx, dy))
                            games.screen.add(Bullet(self, dx * 1.2, dy * 0.8))
                            games.screen.add(Bullet(self, dx * 0.8, dy * 1.2))
                        if self.Spell == 2:
                            games.screen.add(Bullet(self, dx * 1.3, dy * 0.7))
                            games.screen.add(Bullet(self, dx * 0.7, dy * 1.3))
                        if self.Spell == 3:
                            games.screen.add(Bullet(self, dx * 1.4, dy * 0.6))
                            games.screen.add(Bullet(self, dx * 0.6, dy * 1.4))
                else:
                    if sqrt((games.mouse.x - self.x) ** 2 + (games.mouse.y - self.y) ** 2) > self.Attack_range:
                        k = sqrt((games.mouse.x - self.x) ** 2 + (games.mouse.y - self.y) ** 2) / self.Attack_range
                        kapkan_x = self.x + (games.mouse.x - self.x) / k
                        kapkan_y = self.y + (games.mouse.y - self.y) / k
                    else:
                        kapkan_x = games.mouse.x
                        kapkan_y = games.mouse.y
                    games.screen.add(Kapkan(kapkan_x, kapkan_y, self))

            if games.mouse.is_pressed(2) and self.skin != 0 and self.jumptime == 0 and self.Can_jump:
                if sqrt((games.mouse.x - self.x) ** 2 + (games.mouse.y - self.y) ** 2) > self.Jump_range:
                    k = sqrt((games.mouse.x - self.x) ** 2 + (games.mouse.y - self.y) ** 2) / self.Jump_range
                    jump_x = (games.mouse.x - self.x) / k
                    jump_y = (games.mouse.y - self.y) / k

                else:
                    jump_x = games.mouse.x - self.x
                    jump_y = games.mouse.y - self.y

                self.dx = jump_x / Constants.FPS
                self.dy = jump_y / Constants.FPS
                self.CanMove = False
                self.Jump = True
                self.jumptime = self.Jump_cooldown * Constants.FPS
                self.JBar.jump()

            if games.keyboard.is_pressed(games.K_r) and self.skin != 0 and Variables.charges != 0 and self.Can_spell:
                if self.skin == 1:
                    self.spelltime = Variables.charges * 0.4 * Constants.FPS
                elif self.skin == 2:
                    self.Attack_multiply = 1 + Variables.charges * 0.5 * (1 + self.Spell)
                elif self.skin == 3:
                    Variables.HP += (20 + 10 * self.Spell) * Variables.charges
                    if Variables.HP > self.maxHP:
                        Variables.HP = self.maxHP
                    HealthBar.health_bar_update(self.HPBar, Variables.HP)
                elif self.skin == 4:
                    self.Attack_no_cooldown = Variables.charges
                    self.DMG *= 1.25 + 0.25 * self.Spell
                elif self.skin == 5:
                    Variables.HP += (5 * Variables.charges * (1 + self.Spell))
                    dc = self.Attack_range / Constants.FPS
                    self.DMG = self.DMG * 0.25 * Variables.charges
                    games.screen.add(Bullet(self, dc, 0))
                    games.screen.add(Bullet(self, -dc, 0))
                    games.screen.add(Bullet(self, 0, dc))
                    games.screen.add(Bullet(self, 0, -dc))
                    games.screen.add(Bullet(self, dc / sqrt(2), dc / sqrt(2)))
                    games.screen.add(Bullet(self, dc / sqrt(2), -dc / sqrt(2)))
                    games.screen.add(Bullet(self, -dc / sqrt(2), dc / sqrt(2)))
                    games.screen.add(Bullet(self, -dc / sqrt(2), -dc / sqrt(2)))
                    self.Attack_multiply = 0
                elif self.skin == 6:
                    games.screen.add(
                        StoneAOE(games.mouse.x, games.mouse.y, self.DMG * Variables.charges / 8 * (1 + self.Spell)))
                if self.skin != 1:
                    Variables.charges = 0
                games.screen.add(SpellBar(Variables.charges))

            if Variables.charges != 0 and self.spelltime == Variables.charges * 0.4 * Constants.FPS:
                self.DMG = self.DMG * (1.25 + 0.25 * self.Spell)
                Variables.charges = 0
            if self.spelltime == 0:
                self.DMG = self.damage

            if self.spelltime > 0:
                if self.spelltime / (0.1 * Constants.FPS) % 4 == 0:
                    games.screen.add(
                        Weapon(self.left, self.top, self, 0, (self.right - self.left) / Constants.FPS, 0, 0.1))
                elif self.spelltime / (0.1 * Constants.FPS) % 4 == 3:
                    games.screen.add(
                        Weapon(self.right, self.top, self, 90, 0, (self.bottom - self.top) / Constants.FPS, 0.1))
                elif self.spelltime / (0.1 * Constants.FPS) % 4 == 2:
                    games.screen.add(
                        Weapon(self.right, self.bottom, self, 180, (self.left - self.right) / Constants.FPS, 0, 0.1))
                elif self.spelltime / (0.1 * Constants.FPS) % 4 == 1:
                    games.screen.add(
                        Weapon(self.left, self.bottom, self, 270, 0, (self.top - self.bottom) / Constants.FPS, 0.1))
                self.spelltime -= 1

            if self.attacktime > 0:
                self.attacktime -= 1

            if self.jumptime > 0:
                self.jumptime -= 1

            if self.jumptime == Constants.FPS * (self.Jump_cooldown - 1):
                self.dx = 0
                self.dy = 0
                self.CanMove = True
                self.Jump = False

        if self.pausetime > 0:
            self.pausetime -= 1

        if games.keyboard.is_pressed(
                games.K_ESCAPE) and self.pausetime == 0 and not Variables.YN and not Variables.CutScene:
            if not Variables.Pause and not Variables.YN:
                Variables.Pause = True
                call_menu()
            else:
                Variables.Pause = False
                kill_menu()
            self.pausetime = Constants.FPS
