__author__ = 'ohodegaa'

from sys import stdin

Inf = 1000000000


def min_coins_greedy(coins, value):
    num_of_coins = 0
    amount = 0
    i = 0
    while amount != value:
        if amount + coins[i] <= value:
            amount += coins[i]
            num_of_coins += 1
            if amount + coins[i] > value:
                i += 1
        else:
            i += 1

    return num_of_coins


def min_coins_dynamic(coins, value):
    # SKRIV DIN KODE HER
    pass


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    pass

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))