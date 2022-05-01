from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        if self.value is not None:
            v = self.values[self.value] +\
                " of " + \
                self.suits[self.suit]
        else:
            v = self.suit
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

        # insert 4 joker cards
        for i in range(4):
            self.cards.append(Card(None, "joker"))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.joker_count = 0

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)

            if p1c.suit == "joker":
                self.joker_count += 1
                if self.joker_count < 3:
                    p1c = self.process_joker_card()
                elif self.joker_count == 3:
                    print("Round drawn due to {}'s joker card".format(p1n))
                    continue
                else:
                    print("Game ended due to {}'s joker card".format(p1n))
                    break

            if p2c.suit == "joker":
                if self.joker_count < 2:
                    p2c = self.process_joker_card()
                elif self.joker_count == 2:
                    print("Round drawn due to {}'s joker card".format(p2n))
                    continue
                else:
                    print("Game ended due to {}'s joker card".format(p2n))
                    break
                self.joker_count += 1

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

    def process_joker_card(self):
        if self.joker_count == 1:
            return Card(14, 3) # highest card
        elif self.joker_count == 2:
            return Card(2, 0) # lowest card

if __name__ == '__main__':
    game = Game()
    game.play_game()