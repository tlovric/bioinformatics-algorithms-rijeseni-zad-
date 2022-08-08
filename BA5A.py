#Find the Minimum Number of Coins Needed to Make Change
def DPChange(money, coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        MinNumCoins.append(float("inf"))
        for i in range(1, len(coins)):
            if (m >= coins[i]):
                if MinNumCoins[m - coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coins[i]] + 1
    return MinNumCoins[money]


if __name__ == "__main__":
    x = '''40
1,5,10,20,25,50'''
    inlines = x.split('\n')
    money = int(inlines[0])
    coins = list(map(int, inlines[1].split(",")))
    res=DPChange(money, coins)
    print(res)
