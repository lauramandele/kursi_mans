import random
import itertools


def get_shuffled_cards():
    types = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
    signs = ("hearts ♥", "spades ♠", "diamonds ♦", "clubs ♣")
    my_cards = list(itertools.product(signs, types)) # var ģenerēt ar itertools - uztaisa listi ar katru no katra
    # var ģenerēt manuāli
    # my_cards = []
    # for t in types:
    #     for s in signs:
    #         my_cards += (t,s)
    #####
    # 3rd approach
    my_cards = [(t, s) for t in types for s in signs]
    random.shuffle(my_cards)
    print(my_cards)
    return my_cards

cards = get_shuffled_cards()
print(cards)



