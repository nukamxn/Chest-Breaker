level = 1
basehealth = 10
chesthealth = 10
costcalculator = 10
swordnumber = 1
swordprice = (1 * pow(costcalculator, swordnumber))
coinbagnumber = 1
coinbagprice = 100
damage = 1
coins = 10
items = []
coinsearned = 100
coinmulti = 1
while True :
    print("""
    ---Chest Breaker---
    Type x after the > to do damage to the chest
    Everytime you break the chest it gets stronger
    Type shop to open the shop to buy items 
    
    """)
    print(f"""
    Chests health - {chesthealth}
    Your damage - {damage}
    your coins - {coins}
            """)
    playercommand = input("> ")
    if playercommand == ("shop"):
        print(f"""
    ---Shop--- ( will spoend all coins on item purchased)
    Sword {swordnumber} -- {swordprice} coins -- x2 damage each
    Coinbag {coinbagnumber} -- {coinbagprice} coins -- x2 coins from chest each
    ----------
    """)
        itembought = input("Which item do you want to buy>")
        if itembought == ("sword") and coins >= swordprice:
            print("Purchased")
            swordspurchased = int(coins / swordprice)
            coins -= (swordprice * swordspurchased)
            swordnumber += swordspurchased
            swordprice = (swordprice + (1 *swordspurchased))
            damage = (damage * (2 * swordspurchased))
            items.append(f"sword{swordnumber}")
        elif itembought == ("coinbag") and coins >= coinbagprice:
            print("Purchased")
            bagspurchased = int(coins / coinbagprice)
            coinbagnumber += bagspurchased
            coins -= (coinbagprice * bagspurchased)
            coinbagprice = (coinbagprice * 2)
            coinmulti += (1 * bagspurchased)
            items.append(f"coinbag{coinbagnumber}")
    elif playercommand == ("x"):
        chesthealth -= damage
        print(f"Health left - {chesthealth} ")
    if chesthealth <= 0 and level < 1000:
        level += 10
        chesthealth = (basehealth * level)
        coins += (coinsearned * coinmulti)
    if chesthealth <= 0 and level<100000000:
        level += 10000000
        chesthealth = (basehealth * level)
        coins += (coinsearned * coinmulti * 10)
    if chesthealth <= 0 and level < 10000000000000000000000000000000000000000000000000000000000:
        level += 100000000000000000
        chesthealth = (basehealth * level)
        coins += (coinsearned * coinmulti * 1000000)
