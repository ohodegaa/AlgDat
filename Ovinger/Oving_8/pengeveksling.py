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

def show_table(c):
    for i in range(len(c[0])):
        for j in range(len(c)):
            print(c[j][i], end=" , ")
        print()
def min_coins_dynamic(coins, value):
    c = [[0 for v in range(value + 1)] for w in range(len(coins) + 1)]

    for v in range(value + 1):
        c[1][v] = v

    for w in range(2, len(coins) + 1):
        for v in range(1, value + 1):
            # dersom penge-verdien er lik verdien på coin
            if coins[w - 1] == v:
                c[w][v] = 1

            # dersom verdien på coin er større enn penge-verdien
            # dvs. at verdien på coin er for stor til å bruke som veksel

            elif coins[w - 1] > v:
                c[w][v] = c[w - 1][v]

            # dersom verdien på coin er mindre enn penge-verdien
            # dvs. vi må velge mellom å bruke det forrige brukte
            # antall mynter (c[w-1][v]) og verdien - mynt-verdien + 1 (altså legger til en mynt til)

            else: # elif coins[w - 1] < v:
                c[w][v] = min(c[w - 1][v], 1 + c[w][v - coins[w - 1]])

    #show_table(c)
    return c[-1][-1]



def can_use_greedy(coins):
    for i in range(len(coins) - 2):
        can_use = False
        for j in range(i+1, len(coins) - 1):
            if coins[i]%coins[j] == 0:
                can_use = True
        if not can_use:
            return False
    return True




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
        print(min_coins_dynamic(sorted(coins), int(line)))