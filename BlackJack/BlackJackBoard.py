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
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0
        self.playerMoney = 1000
        self.nCardsDealer = 0 #딜러가 뽑은 카드 수?
        self.nCardsPlayer = 0 #플레이어가 뽑은 카드 수?
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.deckN = 0
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
        self.player.reset()
        self.dealer.reset()  # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN =0
        #self.hitPlayer(0)
        #self.hitDealerDown()
        #self.hitPlayer(1)

        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'

    def hitPlayer(self, n): #n은 카드의 위치
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="Resources/cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250 + n * 30, y=350)
        self.LplayerPts.configure(text=str(self.player.value()))
        PlaySound('Resources/sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealerDown(self): #딜러는 히트없이 초반 카드 그대로임!
        #딜러도 한 판에 52장 중 두개를 뽑아야 할 것 같아서 self.cardDeck 배열을 같이 사용하도록 함
        #틀린것같다면 알려주세얌
        self.nCardsDealer = 2
        self.deckN += 1 #가려진 카드(찐카드)
        DealerCard1= Card(self.cardDeck[self.deckN])  # 카드 덱에 저장되어잇는 0부터 52까지의 랜덤 숫자를 넘김
        self.deckN += 1#공개된카드
        DealerCard2 = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(DealerCard1)#self.dealer.cards[0]
        self.dealer.addCard(DealerCard2)#self.dealer.cards[1]

        #딜러의 첫 째 카드는 안 보여야 하므로 나오는 사진은 뒷면 사진으로 보이게 함
        #뽑은 두장 카드도 출력하지만 그 위에 백 카드를 덮어 그리는 식으로 일단 짰습니다.
        p1=PhotoImage(file='Resources/cards/b2fv.png')
        p2 = PhotoImage(file='Resources/cards/' + DealerCard2.filename())
        
        self.LcardsDealer.append(Label(self.window, image=p1))
        self.LcardsDealer.append(Label(self.window, image=p2))
        self.LcardsDealer[0].image = p1
        self.LcardsDealer[0].place(x=250 + 30, y=150)
        self.LcardsDealer[1].image = p2
        self.LcardsDealer[1].place(x=250 + 60, y=150)

    def pressedStay(self):
        #딜러의 카드를 공개함
        pass

    def pressedDeal(self):
        #딜 버튼이 눌렸을때 할 일
        #플레이어와 딜러에게 카드 두 장씩 나눠주기(플레이어는 오픈된 채로, 딜러는 한 장 뒤집은 채로)
        self.deal()

        #첫번째카드뽑기!

        self.deckN+= 1
        startCard1=Card(self.cardDeck[self.deckN]) #카드 덱에 저장되어잇는 0부터 52까지의 랜덤 숫자를 넘김
        self.player.addCard(startCard1)
        p1 = PhotoImage(file='Resources/cards/' + startCard1.filename())
        self.LcardsPlayer.append(Label(self.window, image=p1))
        self.LcardsPlayer[self.player.inHand() - 1].image = p1
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250 + 30, y=350)

        self.deckN+=1
        startCard2= Card(self.cardDeck[self.deckN])
        self.player.addCard(startCard2)
        p2 = PhotoImage(file='Resources/cards/' + startCard2.filename())
        self.LcardsPlayer.append(Label(self.window, image=p2))
        self.LcardsPlayer[self.player.inHand() - 1].image = p2
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250 + 60, y=350)

        self.nCardsPlayer = 2  # 플레이어가 뽑은 카드 수?
        self.hitDealerDown()

    def pressedAgain(self):
        pass

    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value() > 21:
            self.checkWinner()

    def checkWinner(self):
        self.betMoney = 0
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
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LdealerPts.configure(text=str(self.dealer.value()))
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

BlackJack()