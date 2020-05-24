from Card import *
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
    def inHand(self):
        return self.N
    def addCard(self,c,f):
        self.cards.append([c,f])
        self.N += 1
        print(self.name, self.cards)
        return c
    def value(self):
        val=0
        for i in range(len(self.cards)):
            if int(self.cards[i][0])==1: #ace
                val+=11
            else:
                val+=int(self.cards[i][0])

        for i in range(len(self.cards)):
            if val>21 and int(self.cards[i][0])==1:
                val-=10

        return val

    def reset(self):
        self.cards.clear()
        self.N=0

#ace는 1혹은 11로 모두 사용 가능
#일단 11로 계산한 후 21이 넘어가면 1로 정정