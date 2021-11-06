# example of proxy pattern - athlete (Real Subject) and coach (Proxy)
## https://youtu.be/KU3svHBrfiU
from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.majors = True
        self.injured = False
        self.pay = randint(1200000, 6000000)
        self.injury = ''

    def recovered(self):
        self.injured = False


class Coach:
    def __init__(self, name):
        self.name = name

    def gotHurt(self, player, injury):
        player.injured = True
        self.player = player
        self.injury = injury 

    def sendtoAAA(self, player):
        if player.injured == True:
            player.majors = False
            print(f'sending {player.name} down to AAA to recover from a {self.injury} injury')
        else:
            print(f'{player.name} is good and healthy. Let\'s keep him up here.')


if __name__ == '__main__':
    
    rizz = Player('Anthony Rizzo')
    boone = Coach('Aaron Boone')

    print(rizz.majors)
    boone.gotHurt(rizz, 'hamstring')
    boone.sendtoAAA(rizz)
    print(rizz.majors)

    