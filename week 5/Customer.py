def buy(product, num, price):
    if check(product, num) is True:
        print("You bought", product, "and spent", num * price)
    else:
        print("Sorry! Weare out of this product")
def main():
    product = input()
    num = input()
    price = input()
    buy(product, num, price)
if __name__ == '__main__':
    main()