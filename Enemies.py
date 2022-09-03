from Character import *
from livewires import games, color
import Dungeon


class Shot(games.Sprite):
    def __init__(self, x, y, dx, dy, dmg):
        super().__init__(image=games.load_image("Enemies/Shot.png"), x=x, y=y)
        self.DX = dx
        self.DY = dy
        self.dmg = dmg
        self.timer = 60

    def update(self):
        if not Variables.Pause:
            self.y += self.DY
            self.x += self.DX
            if self.timer == 0:
                self.destroy()
            self.timer -= 1
            for hero in self.overlapping_sprites:
                try:
                    if hero.type == 0 and not hero.Jump and hero.Invincibilitytimer == -1:
                        games.screen.add(TakeDamage(hero, self.dmg))
                except AttributeError:
                    pass


class EnemyTest(games.Sprite):
    def __init__(self, boss, place, image):
        image = games.load_image("Enemies/Stage_2/1_zombie.png")
        self.type = 1
        self.boss = boss
        self.attack_type = 0
        self.attack_cooldown = 150
        self.Spell_timer = self.Attack_timer = self.Move_timer = 0
        x = y = 0
        if place == 0:
            x = 600
            y = 400
            while x in range(400, 801) or y in range(300, 501):
                x = randint(150, 1050)
                y = randint(150, 650)
        if place == 1:
            x = randint(200, 1000)
            y = randint(100, 400)
        elif place == 2:
            x = randint(200, 1000)
            y = randint(400, 700)
        elif place == 3:
            x = randint(600, 1100)
            y = randint(200, 600)
        elif place == 4:
            x = randint(100, 600)
            y = randint(200, 600)

        self.SpeedX /= 60
        self.SpeedY = self.SpeedX / 1.5
        if boss == 1:
            self.HP *= 5
            self.DMG *= 2
            self.SpeedX *= 1.5
            self.SpeedY *= 1.5
        super().__init__(image, 0, x, y)
        self.HPBar = games.Text(self.HP, 20, color.red, x=self.x, y=self.top)
        games.screen.add(self.HPBar)


class Zombie(EnemyTest):
    def __init__(self, boss, place):
        image = games.load_image("Enemies/Stage_2/1_zombie.png")
        self.HP = 275 #200
        self.DMG = 40 #20
        self.SpeedX = Constants.WindowWidth / 16 #17
        self.respawn = True
        if boss == 2:
            self.HP = 100
            self.DMG = 10
            self.SpeedX /= 1.5
            self.respawn = False
        super().__init__(boss, place, image)

class Enemy(games.Sprite):
    def __init__(self, var, boss, place):
        self.var = var
        self.type = 1
        self.boss = boss
        self.attack_type = 0
        self.attack_cooldown = 150
        self.Hp = self.DMG = self.SpeedX = self.SpeedY = self.Width = self.Height = 0
        self.Spell_timer = self.Attack_timer = self.Move_timer = 0
        image = x = y = angle = 0
        if place == 0:
            x = 600
            y = 400
            while x in range(400, 801) or y in range(300, 501):
                x = randint(150, 1050)
                y = randint(150, 650)
        if place == 1:
            x = randint(200, 1000)
            y = randint(100, 400)
        elif place == 2:
            x = randint(200, 1000)
            y = randint(400, 700)
        elif place == 3:
            x = randint(600, 1100)
            y = randint(200, 600)
        elif place == 4:
            x = randint(100, 600)
            y = randint(200, 600)
        if var == 6: # 1 * 1 * 1
            image = games.load_image("Enemies/stage_1/1_rat.png")
            self.HP = 100 #50
            self.DMG = 10 #5
            self.SpeedX = Constants.WindowWidth / 16 #/12
        elif var == 7: # 1.25 * 1.2 * 4/3
            image = games.load_image("Enemies/stage_1/2_spider.png")
            self.HP = 125 #100
            self.DMG = 12 #10
            self.SpeedX = Constants.WindowWidth / 12 #/14
        elif var == 8: # 1.5 * 1.5 * 4/3
            image = games.load_image("Enemies/stage_1/3_bee.png")
            self.HP = 150 #150
            self.DMG = 15 #15
            self.SpeedX = Constants.WindowWidth / 12 #/13
        elif var == 9: # 3 * 2 * 2/3
            image = games.load_image("Enemies/stage_1/4_bones_axe.png")
            self.HP = 300 #200
            self.DMG = 20 #20
            self.SpeedX = Constants.WindowWidth / 24 #/18
        elif var == 10: # 1.25 * 2 * 4/3 * 1.5
            image = games.load_image("Enemies/stage_1/5_bones_archer.png")
            self.HP = 125 #150
            self.DMG = 20 #15
            self.SpeedX = Constants.WindowWidth / 12 #18
            self.attack_type = 1
        elif var == 11: # 2.75 * 4 * 1
            image = games.load_image("Enemies/Stage_2/1_zombie.png")
            self.HP = 275 #200
            self.DMG = 40 #20
            self.SpeedX = Constants.WindowWidth / 16 #17
            self.respawn = True
            if boss == 2:
                self.HP = 100
                self.DMG = 10
                self.SpeedX /= 1.5
                self.respawn = False
        elif var == 12: # 3 * 2.5 * 2 * 0.8
            image = games.load_image("Enemies/Stage_2/2_leprecon.png")
            self.HP = 300 # 250
            self.DMG = 25 # 25
            self.SpeedX = Constants.WindowWidth / 8 # 12
        elif var == 13: # 1.5 * 6.5 * 4/3
            image = games.load_image("Enemies/Stage_2/3_thief.png")
            self.HP = 150 # 300
            self.DMG = 65 # 30
            self.SpeedX = Constants.WindowWidth / 12 # 16
            self.attack_type = 2
            self.steal = False
        elif var == 14: # Как это вообще балансить???
            image = games.load_image("Enemies/Stage_2/4_ball.png")
            self.HP = 3
            self.DMG = 100
            self.attack_type = 3
            self.type = 3
            self.run = False
            self.run_x = (Variables.X - x) / 30000
            self.run_y = (Variables.Y - y) / 30000
            self.run_stacks = 0
        elif var == 15: # 7.5 * 1 * 1 * 2
            image = games.load_image("Enemies/Stage_2/5_necromant.png")
            self.HP = 750 # 300
            self.attack_type = 4
            self.SpeedX = Constants.WindowWidth/16 # /20
        elif var == 16: # 6 * 3.5 * 1
            image = games.load_image("Enemies/Stage_3/1_satyr.png")
            self.HP = 600
            self.DMG = 35
            self.SpeedX = Constants.WindowWidth/16 #17
            self.cooldown = 180
        elif var == 17: # 6 * 5.5 * 2/3
            image = games.load_image("Enemies/Stage_3/2_robot.png")
            self.HP = 600 #400
            self.DMG = 55 #40
            self.SpeedX = Constants.WindowWidth/24 #18
            if Variables.Character in (1, 2, 3, 7, 8, 9):
                self.HP = self.HP * 2
        elif var == 18: # 2.3 * 5 * 1 * 1.5
            image = games.load_image("Enemies/Stage_3/3_elf.png")
            self.HP = 230 # 350
            self.DMG = 50 # 35
            self.SpeedX = Constants.WindowWidth/ 12 # 17
            if Variables.Character in (4, 5, 6):
                self.HP = self.HP * 2
            self.attack_type = 1
        elif var == 19: # 3 * 10 * (0.8)
            image = games.load_image("Enemies/Stage_3/4_ballista.png")
            self.HP = 300 # 300
            self.DMG = 100 # 100
            self.attack_type = 5
            y = randint(100, 700)
            if place in range(0, 2):
                place = choice((3, 4))
            if place == 3:
                x = 1100
            elif place == 4:
                x = 100
                angle = 180
        elif var == 20:
            image = games.load_image("Enemies/stage_3/5_demon.png")
            self.HP = 500 # 550
            self.DMG = 50 # 55
            self.SpeedX = Constants.WindowWidth / 16 # 20
            self.cooldown = 180
        elif var == 21: # 10 * 3.1 * 1
            image = games.load_image("Enemies/stage_4/1_sukkub.png")
            self.HP = 1000 # 500
            self.DMG = 31 # 50
            self.SpeedX = Constants.WindowWidth / 16 # /8
            self.MaxHP = 1000
            self.stage = 0
            if self.boss == 1:
                self.MaxHP *= 5
        elif var == 22: # 5 * 4 * 1.6
            image = games.load_image("Enemies/stage_4/2_robot.png")
            self.HP = 500 # 550
            self.DMG = 40 # 55
            self.SpeedX = Constants.WindowWidth / 10 # /10
            if Variables.Character in (1, 2, 3, 7, 8, 9):
                self.HP = self.HP * 3
        elif var == 23: # 3 * 5.5 * 4/3 * 1.5
            image = games.load_image("Enemies/stage_4/3_elf_dark.png")
            self.HP = 300 # 500
            self.DMG = 55 # 50
            self.SpeedX = Constants.WindowWidth / 12 # /12
            if Variables.Character in (4, 5, 6):
                self.HP = self.HP * 3
            self.attack_type = 1
        elif var == 24:
            image = games.load_image("Enemies/stage_4/4_werewolf.png")
            self.HP = 850 # 650
            self.DMG = 80 # 65
            self.SpeedX = Constants.WindowWidth / 32 # /15
        elif var == 25:
            image = games.load_image("Enemies/stage_4/5_vampire.png")
            self.HP = 875 # 700
            self.DMG = 100 # 70
            self.SpeedX = Constants.WindowWidth / 40 # /12

        self.SpeedX /= 60
        self.SpeedY = self.SpeedX / 1.5
        if boss == 1:
            self.HP *= 5
            self.DMG *= 2
            self.SpeedX *= 1.5
            self.SpeedY *= 1.5
        super().__init__(image, angle, x, y)
        self.HPBar = games.Text(self.HP, 20, color.red, x=self.x, y=self.top)
        games.screen.add(self.HPBar)

    def update(self):
        if not Variables.Pause:
            self.HPBar.destroy()
            if self.var == 16 and self.cooldown in range(300, 601):
                pass
            else:
                self.HPBar.value = int(self.HP)
                self.HPBar.x = self.x
                self.HPBar.y = self.top
                games.screen.add(self.HPBar)

            if self.HP <= 0:
                if self.var == 11 and self.respawn and self.Spell_timer == 0:
                    if self.boss == 0:
                        self.HP = 150
                        self.DMG = 20
                    else:
                        self.HP = 750
                        self.DMG = 40
                    self.SpeedX = self.SpeedX / 1.5
                    self.SpeedY = self.SpeedY / 1.5
                    self.respawn = False
                else:
                    if self.var == 12 and self.Spell_timer == 0:
                        Variables.Gold += 1
                    if self.var == 13 and self.steal:
                        Variables.Gold += 5
                    self.HPBar.destroy()
                    if self.boss == 0:
                        Variables.Num_of_enemies -= 1
                    elif self.boss == 1:
                        Variables.Boss_dead = True
                        games.screen.add(Dungeon.TrapDoor())
                    if self.var in (6, 7, 8):
                        games.load_sound("sound/sfx/Damage/insect_dead.wav").play()
                    elif self.var in (9, 10):
                        games.load_sound("sound/sfx/Damage/bones_dead.ogg").play()
                    elif self.var in (17, 22):
                        games.load_sound("sound/sfx/Damage/robot_dead.ogg").play()
                    elif self.var in (14, 19):
                        games.load_sound("sound/sfx/Damage/build_dead.ogg").play()
                    elif self.var in (16, 20, 21):
                        games.load_sound("sound/sfx/Damage/demon_dead.wav").play()
                    else:
                        games.load_sound("sound/sfx/Damage/human_dead.wav").play()
                    self.destroy()

            if self.var == 16:
                if self.cooldown == 300:
                    self._replace(games.load_image("Enemies/stage_3/1_satyr.png"))
                    self.cooldown -= 1
                elif self.cooldown == 0 and self.Spell_timer == 0:
                    self._replace(games.load_image("Enemies/stage_3/1_satyr_invis.png"))
                    self.cooldown = 600
                elif self.Spell_timer == 0:
                    self.cooldown -= 1

            if self.var == 20:
                if self.cooldown == 0 and self.Spell_timer == 0:
                    self.SpeedX = self.SpeedX * 2
                    self.SpeedY = self.SpeedY * 2
                    self.cooldown = 600
                elif self.cooldown == 300:
                    self.SpeedX = self.SpeedX / 2
                    self.SpeedY = self.SpeedY / 2
                    self.cooldown -= 1
                elif self.Spell_timer == 0:
                    self.cooldown -= 1

            if self.var == 21 and self.Spell_timer == 0:
                if self.HP <= self.MaxHP / 5 * 4 and self.stage == 0:
                    self.SpeedX *= 1.6
                    self.SpeedY *= 1.6
                    self.stage = 1
                if self.HP <= self.MaxHP / 5 * 3 and self.stage == 1:
                    self.DMG *= 2
                    self.stage = 2
                if self.HP <= self.MaxHP / 5 * 2 and self.stage == 2:
                    self.SpeedX *= 1.25
                    self.SpeedY *= 1.25
                    self.stage = 3
                if self.HP <= self.MaxHP / 5 and self.stage == 3:
                    self.DMG *= 1.5
                    self.stage = 4

            if self.var == 24 and self.Spell_timer == 0:
                if sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) > 300 and self.type == 1:
                    self.SpeedX = self.SpeedX * 4
                    self.SpeedY = self.SpeedY * 4
                    self._replace(games.load_image("Enemies/stage_4/4_wolf.png"))
                    self.type = 10
                elif sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) < 100 and self.type == 10:
                    self.SpeedX = self.SpeedX / 4
                    self.SpeedY = self.SpeedY / 4
                    self._replace(games.load_image("Enemies/stage_4/4_werewolf.png"))
                    self.type = 1

            if self.var == 25 and self.Spell_timer == 0:
                if sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) > 300 and self.type == 1:
                    self.SpeedX = self.SpeedX * 5
                    self.SpeedY = self.SpeedY * 5
                    self._replace(games.load_image("Enemies/stage_4/5_bat.png"))
                    self.type = 10
                elif sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) < 100 and self.type == 10:
                    self.SpeedX = self.SpeedX / 5
                    self.SpeedY = self.SpeedY / 5
                    self._replace(games.load_image("Enemies/stage_4/5_vampire.png"))
                    self.type = 1

            if self.Spell_timer > 0:
                self.Spell_timer -= 1

            if self.Attack_timer > 0:
                self.Attack_timer -= 1

            if self.Move_timer > 0:
                self.Move_timer -= 1

            if self.attack_type == 0:
                if self.Move_timer == 0:
                    if Variables.X > self.x:
                        self.x += self.SpeedX
                    else:
                        self.x -= self.SpeedX
                    if Variables.Y > self.y:
                        self.y += self.SpeedY
                    else:
                        self.y -= self.SpeedY

                if self.Attack_timer == 0:
                    for hero in self.overlapping_sprites:
                        try:
                            if hero.type == 0 and not hero.Jump and hero.Invincibilitytimer == -1:
                                if self.var == 25:
                                    self.HP += self.DMG
                                games.screen.add(TakeDamage(hero, self.DMG))
                        except AttributeError:
                            pass

            elif self.attack_type == 1:
                if self.Move_timer == 0:
                    if sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) > 300:
                        if Variables.X > self.x:
                            self.x += self.SpeedX
                        else:
                            self.x -= self.SpeedX
                        if Variables.Y > self.y:
                            self.y += self.SpeedY
                        else:
                            self.y -= self.SpeedY
                    else:
                        if Variables.X > self.x > 50:
                            self.x -= self.SpeedX
                        elif Variables.X < self.x < 1150:
                            self.x += self.SpeedX
                        if Variables.Y > self.y > 50:
                            self.y -= self.SpeedY
                        elif Variables.Y < self.y < 750:
                            self.y += self.SpeedY
                if self.attack_cooldown > 0:
                    self.attack_cooldown -= 1
                if sqrt((Variables.X - self.x) ** 2 + (
                        Variables.Y - self.y) ** 2) < 400 and self.Attack_timer == 0 and self.attack_cooldown == 0:
                    self.attack_cooldown = 150
                    k = sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) / 500
                    attack_x = (Variables.X - self.x) / k
                    attack_y = (Variables.Y - self.y) / k
                    dx = attack_x / Constants.FPS
                    dy = attack_y / Constants.FPS
                    games.screen.add(Shot(self.x, self.y, dx, dy, self.DMG))

            elif self.attack_type == 2:
                if not self.steal:
                    if self.Move_timer == 0:
                        if Variables.X > self.x:
                            self.x += self.SpeedX
                        else:
                            self.x -= self.SpeedX
                        if Variables.Y > self.y:
                            self.y += self.SpeedY
                        else:
                            self.y -= self.SpeedY

                    if self.Attack_timer == 0:
                        for hero in self.overlapping_sprites:
                            try:
                                if hero.type == 0 and not hero.Jump and hero.Invincibilitytimer == -1:
                                    games.screen.add(TakeDamage(hero, self.DMG))
                                    if self.Spell_timer == 0:
                                        self.steal = True
                                        if Variables.Gold > 5:
                                            Variables.Gold -= 5
                                        else:
                                            Variables.Gold = 0
                                        if self.x > Constants.WindowWidth/2:
                                            self.dx = self.SpeedX
                                        else:
                                            self.dx = -self.SpeedX
                                        if self.x > Constants.WindowHeight/2:
                                            self.dy = self.SpeedY
                                        else:
                                            self.dy = -self.SpeedY
                            except AttributeError:
                                pass
                else:
                    if self.x <= 50 or self.x >= 1150 or self.y <= 50 or self.y >= 750:
                        Variables.Num_of_enemies -= 1
                        self.destroy()

            elif self.attack_type == 3:
                if not self.run:
                    self.run_x = (Variables.X - self.x) / 30000
                    self.run_y = (Variables.Y - self.y) / 30000
                    self.run = True
                else:
                    self.x += self.run_x * self.run_stacks
                    self.y += self.run_y * self.run_stacks
                    self.run_stacks += 1
                    if self.Attack_timer == 0:
                        for hero in self.overlapping_sprites:
                            try:
                                if hero.type == 0 and not hero.Jump and hero.Invincibilitytimer == -1:
                                    games.screen.add(TakeDamage(hero, self.DMG))
                            except AttributeError:
                                pass
                    if self.x <= 50:
                        self.HP -= 1
                        self.run = False
                        self.x = 51
                    if self.x >= 1150:
                        self.HP -= 1
                        self.run = False
                        self.x = 1149
                    if self.y < 50:
                        self.HP -= 1
                        self.run = False
                        self.y = 51
                    if self.y > 750:
                        self.HP -= 1
                        self.run = False
                        self.y = 749

            elif self.attack_type == 4:
                if sqrt((Variables.X - self.x) ** 2 + (Variables.Y - self.y) ** 2) < 500 and self.Move_timer == 0:
                    if Variables.X > self.x > 60:
                        self.x -= self.SpeedX
                    elif Variables.X < self.x < 1140:
                        self.x += self.SpeedX
                    if Variables.Y > self.y > 60:
                        self.y -= self.SpeedY
                    elif Variables.Y < self.y < 740:
                        self.y += self.SpeedY
                if self.attack_cooldown > 0:
                    self.attack_cooldown -= 1
                else:
                    self.attack_cooldown = 300
                    if self.boss:
                        self.attack_cooldown /= 2
                        games.screen.add(Enemy(11, 0, 0))
                    else:
                        games.screen.add(Enemy(11, 2, 0))

            elif self.attack_type == 5:
                if self.attack_cooldown == 0 and self.Attack_timer == 0:
                    self.attack_cooldown = 60
                    if self.x < 600:
                        games.screen.add(Shot(self.x, self.y, 10, 0, self.DMG))
                    else:
                        games.screen.add(Shot(self.x, self.y, -10, 0, self.DMG))
                else:
                    self.attack_cooldown -= 1

            if self.attack_type in (0, 1, 2, 4):
                for sprite in self.overlapping_sprites:
                    try:
                        if sprite.type in (0, 1, 10) and Variables.X > sprite.x > self.x and self.SpeedX <= sprite.SpeedX:
                            self.x -= self.SpeedX*3/4
                        if sprite.type in (0, 1, 10) and Variables.X < sprite.x < self.x and self.SpeedX <= sprite.SpeedX:
                            self.x += self.SpeedX*3/4
                        if sprite.type in (0, 1, 10) and Variables.Y > sprite.y > self.y and self.SpeedY <= sprite.SpeedY:
                            self.y -= self.SpeedY*3/4
                        if sprite.type in (0, 1, 10) and Variables.Y < sprite.x < self.x and self.SpeedY <= sprite.SpeedY:
                            self.y += self.SpeedY*3/4
                    except AttributeError:
                        pass
            if self.x < 50:
                self.x = 50
            if self.x > 1150:
                self.x = 1150
            if self.y < 50:
                self.y = 50
            if self.y > 750:
                self.y = 750
