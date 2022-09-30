from random import randint


class Fighting:
    def __init__(self, player, xp=100):
        self.player = player
        self.xp = xp
        print('Вы создали игрока {} с количеством хп 100'.format(self.player))

    def hit(self, damage):
        if type(self) == type(damage):
            damage.xp -= randint(0, 25)


print('Введите имя первого игрока ')
player_1 = input()
hero_1 = Fighting(player_1, 100)

print('Введите имя второго игрока ')
player_2 = input()
hero_2 = Fighting(player_2, 100)

print('Чтобы начать нажмите Enter')
enter = input()
while (hero_1.xp > 0) and (hero_2.xp > 0):
    fight = randint(1, 2)
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
