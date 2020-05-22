class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
    def inHand(self):
        return self.N
    def addCard(self,c):
        self.cards.append(c)
        self.N += 1
        return c
    def reset(self):
        self.N = 0
        self.cards.clear()
    def value(self):
        #점수를 계산하여 리턴하는 함수
        #밸류를 어떻게 받아올까?
        pass

#ace는 1혹은 11로 모두 사용 가능
#일단 11로 계산한 후 21이 넘어가면 1로 정정