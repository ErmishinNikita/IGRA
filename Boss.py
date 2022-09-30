import random


class Fighting:
    def __init__(self, player, xp=100):
        self.player = player
        self.xp = xp
        print('Вы создали игрока {} с количеством хп 100'.format(self.player))

    def hit(self, opponent):
        if True:
            print('Игрок {} нанёс удар опоненту {}'.format(self.player, opponent.player))
            opponent.ostxp(
                opponent.polxp() - random.randint(0, 30)
            )

    def ostxp(self, xp):
        self.xp = xp
        if xp > 0:
            print('У игрока {} осталось {}'.format(self.player, self.xp))
        else:
            print('У игрока {} нет хп'.format(self.player))

    def polxp(self):
        try:
            return self.xp
            print('XP {} - {}'.format(self.player, self.xp))
        except:
            return 'ХП net'


print('Введите имя первого игрока ')
player_1 = input()
hero_1 = Fighting(player_1, 100)

print('Введите имя второго игрока ')
player_2 = input()
hero_2 = Fighting(player_2, 100)

print('Чтобы начать нажмите Enter')
enter = input()
while (hero_1.xp > 0) and (hero_2.xp > 0):
    fight = random.randint(1, 2)
    if fight == 1:
        hero_1.hit(hero_2)
    else:
        hero_2.hit(hero_1)

    if fight == 1:
        player = hero_1.player
        name = hero_2.player
    else:
        player = hero_2.player
        name = hero_1.player

print('{} Победил игрокa {}'.format(player, name))
print()