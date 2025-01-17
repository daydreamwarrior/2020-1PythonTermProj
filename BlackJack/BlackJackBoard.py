from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random
class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        # self.player = Player("player")
        # self.dealer = Player("dealer")
        self.betMoney = 0
        self.playerMoney = 1000
        #self.nCardsDealer = 0 #딜러가 뽑은 카드 수?
        self.nCardsPlayer = 0 #플레이어가 뽑은 카드 수?
        self.LcardsPlayer = []#플레이어가 뽑은 카드의 라벨 리스트
        self.LcardsDealer = []#딜러가 뽑은 카드의 라벨 리스트
        self.deckN = 0
        self.cardsphotoimage=[0 for _ in range (10)]
        self.window.mainloop()

    def setupButton(self):
        self.B50 = Button(self.window, text="Bet 50", width=6, height=1, font=self.fontstyle2, command=self.pressedB50)
        self.B50.place(x=50, y=500)
        self.B10 = Button(self.window, text="Bet 10", width=6, height=1, font=self.fontstyle2, command=self.pressedB10)
        self.B10.place(x=150, y=500)
        self.B1 = Button(self.window, text="Bet 1", width=6, height=1, font=self.fontstyle2, command=self.pressedB1)
        self.B1.place(x=250, y=500)
        self.Hit = Button(self.window, text="Hit", width=6, height=1, font=self.fontstyle2, command=self.pressedHit)
        self.Hit.place(x=400, y=500)
        self.Stay = Button(self.window, text="Stay", width=6, height=1, font=self.fontstyle2, command=self.pressedStay)
        self.Stay.place(x=500, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$0", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)

    def pressedB50(self):
        self.betMoney += 50

        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 50
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('Resources/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 50

    def pressedB10(self):
        self.betMoney += 10

        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 10
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('Resources/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 10
    def pressedB1(self):
        self.betMoney += 1

        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 1
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('Resources/sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1

    def deal(self): #딜 처음 시작 때 불리는 세팅 함수
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.cardsphotoimage=[0 for _ in range(10)]
        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        #딜을 시작하면 버튼 상태가 바뀌어야 하므로 관련 코드 추가
        #히트와 스테이는 액티브 나머지는 disabled

        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'

        self.Hit['state'] = 'active'
        self.Hit['bg'] = 'SystemButtonFace'
        self.Stay['state'] = 'active'
        self.Stay['bg'] = 'SystemButtonFace'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def hitPlayer(self, n): #n은 카드의 위치
        #이부분에서 플레이어 포인트가 21 이상일 때 게임오버 먼저 처리#
        self.deckN += 1
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.player.addCard(self.cardsphotoimage[self.deckN].getValue(),self.cardsphotoimage[self.deckN].filename())
        self.updatePlayerCards(self.player.inHand()-1)
        self.LplayerPts.configure(text=str(self.player.value()))
        PlaySound('Resources/sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self): #딜러는 히트없이 초반 카드 그대로임!
        #딜러도 한 판에 52장 중 두개를 뽑아야 할 것 같아서 self.cardDeck 배열을 같이 사용하도록 함
        #self.dealer.reset()
        self.deckN += 1 #가려진 카드
        self.cardsphotoimage[self.deckN]= Card(self.cardDeck[self.deckN])
        self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(),self.cardsphotoimage[self.deckN].filename())
        p1 = PhotoImage(file='Resources/cards/b2fv.png')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
        self.LcardsDealer.append(Label(self.window, image=p1,bd=0,bg='green'))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p1
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=280, y=150)

        self.deckN += 1#공개된카드
        test = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(test.getValue(),test.filename())
        self.updateDealerCards(self.dealer.inHand()-1)
        #print(self.dealer.cards[0][0])
        self.LdealerPts.configure(text=str(self.dealer.value()-self.dealer.cards[0][0]))

    def pressedStay(self):
        self.afterStay()

    def pressedDeal(self):
        #딜 버튼이 눌렸을때 할 일
        #플레이어와 딜러에게 카드 두 장씩 나눠주기(플레이어는 오픈된 채로, 딜러는 한 장 뒤집은 채로)

        self.deal()
        #첫번째카드뽑기!
        self.cardsphotoimage[self.deckN]=Card(self.cardDeck[self.deckN]) #카드 덱에 저장되어있는 0부터 52까지의 랜덤 숫자를 넘김
        self.player.addCard(self.cardsphotoimage[self.deckN].getValue(),self.cardsphotoimage[self.deckN].filename())
        self.updatePlayerCards(self.player.inHand()-1)

        self.deckN+=1
        self.cardsphotoimage[self.deckN]= Card(self.cardDeck[self.deckN])
        self.player.addCard(self.cardsphotoimage[self.deckN].getValue(),self.cardsphotoimage[self.deckN].filename())
        self.updatePlayerCards(self.player.inHand()-1)

        self.nCardsPlayer = 2  # 플레이어가 뽑은 카드 수?
        self.hitDealer()
        #플레이어가 뽑은 카드에 따른 점수를 카드 위 라벨에 업데이트한다.
        self.LplayerPts.configure(text=str(self.player.value()))
        if self.player.value()==21: #블랙잭
            self.blackjack()

    def updatePlayerCards(self, i):
        p = PhotoImage(file='Resources/cards/' + self.player.cards[i][1])
        self.LcardsPlayer.append(Label(self.window, image=p,bd=0,bg='green'))
        self.LcardsPlayer[i].image = p
        self.LcardsPlayer[i].place(x=250 + (i+1)*30, y=350)

    def opendealercard(self):
        p = PhotoImage(file="Resources/cards/" + self.dealer.cards[0][1])
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LdealerPts.configure(text=str(self.dealer.value()))

    def updateDealerCards(self, i):
        p = PhotoImage(file='Resources/cards/' + self.dealer.cards[i][1])
        self.LcardsDealer.append(Label(self.window, image=p,bd=0,bg='green'))
        self.LcardsDealer[i].image = p
        self.LcardsDealer[i].place(x=250 + (i+1)*30, y=150)
    def blackjack(self):

        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'SystemButtonFace'
        self.opendealercard()
        self.Lstatus.configure(text="BlackJack!")
        PlaySound('Resources/sounds/win.wav', SND_FILENAME)
        self.playerMoney+=int(self.betMoney*3/2)
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))

    def pressedAgain(self):
        #사용한 변수 초기화 --> 세팅은 deal()에서
        #카드는 함수 안에서 할당되니 지울필요 x..?
        self.cardDeck.clear()
        self.deckN = 0
        self.nCardsPlayer=0

        #버튼 라벨 초기화는 정상 작동
        self.setupButton()
        self.LplayerPts.configure(text="")
        self.LdealerPts.configure(text="")
        self.Lstatus.configure(text="")
        self.Lstatus.configure(text="")

        for i in range (self.player.inHand()):
            self.player.cards[i][1]='clearcard.png'
            self.updatePlayerCards(i)

        for i in range (self.dealer.inHand()):
            self.dealer.cards[i][1]='clearcard.png'
            self.updateDealerCards(i)

        del self.player
        del self.dealer
        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()

    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value() > 21: #21점 초과?
            self.checkWinner()

    def afterStay(self):  #딜러의 카드 추가
        while self.dealer.value() < 17:
            self.deckN += 1  # 공개된카드
            test = Card(self.cardDeck[self.deckN])
            self.dealer.addCard(test.getValue(), test.filename())
            self.updateDealerCards(self.dealer.inHand() - 1)
            self.LdealerPts.configure(text=str(self.dealer.value()-self.dealer.cards[0][0]))
        self.checkWinner()

    def checkWinner(self):

        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

        # 뒤집힌 카드를 다시 그린다.

        self.opendealercard()
        #
        if self.player.value() > 21:
            self.Lstatus.configure(text="Player Busts")
            PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text="Dealer Busts")
            self.playerMoney += self.betMoney * 2
            PlaySound('Resources/sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text="Push")
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text="You won!!")
            self.playerMoney += self.betMoney * 2
            PlaySound('Resources/sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text="Sorry you lost!")
            PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)

        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.betMoney = 0
        self.LbetMoney.configure(text="$"+str(self.betMoney))

BlackJack()