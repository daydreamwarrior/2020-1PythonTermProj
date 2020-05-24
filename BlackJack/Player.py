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
        return c
    def value(self):
        val=0
        for i in range(len(self.cards)):
            val+=int(self.cards[i][0])
        return val
    def reset(self):
        self.cards.clear()
        self.N=0
        print(self.name,'카드 클리어')
        print("self.n:",self.N)

#ace는 1혹은 11로 모두 사용 가능
#일단 11로 계산한 후 21이 넘어가면 1로 정정