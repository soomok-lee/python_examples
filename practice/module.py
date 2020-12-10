def add(a, b):
    print(a + b)
    return a + b

# class 
class FishCakeMake:
    def __init__(self, **kwargs):
        self.size = 10
        self.flavor = "red bean"
        self.price = 100
        if "size" in kwargs:
            self.size = kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")

    def __del__(self):
        print("deleted.")

    def __lt__(self, other):
        return self.price < other.price
    def __le__(self, other):
        return self.price <= other.price
    def __gt__(self, other):
        return self.price > other.price
    def __ge__(self, other):
        return self.price >= other.price
    def __eq__(self, other):
        return self.price == other.price
    def __ne__(self, other):
        return self.price != other.price
    
    def __str__(self): # 클래스가 print()에 의해 출력될 때 실행
        return "<class FishCakeMaker (size={}, price={}, flavor={})>".format(self.size, self.price, self.flavor)
      
    def show(self):
        print("size {}".format(self.size))
        print("flavor {}".format(self.flavor))
        print("price {}".format(self.price))
        print("*"*60)
        
# fish1 = FishCakeMake()
# fish2 = FishCakeMake(size=20, price=300)
# fish3 = FishCakeMake(size=25, price=500, flavor="vanilla")

# fish1.show()
# fish2.show()
# fish3.show()

# print(fish1) # __str__ 실행
# if fish1 < fish2:
#     print("fish2")
# else:
#     print("fish1")

# inheritance
class MarketGoods(FishCakeMake):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.market_price = self.price + margin

    def show(self):
        print(self.flavor, self.market_price)

# print(__name__)
if __name__ == "__main__":
    fish1 = MarketGoods(size=20, price=500)
    fish1.show()
 