import itertools,random
deck = list(itertools.product((range(1,14)),['hearts','diamonds','clubs','spades']))
random.shuffle(deck)
print("your combination cards are:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])