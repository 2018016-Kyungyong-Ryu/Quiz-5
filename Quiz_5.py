class bread:
    def __init__(self, kind, price):
        self.kind = kind
        self.price = price
        self.total = 0

    def sell(self):
        print(self.kind + " 붕어빵을 " + str(self.price) + "에 팔았습니다.")
        self.total = self.total + self.price

    def eat(self):
        print(self.kind + " 붕어빵 을 먹었습니다.")

# 크림 붕어빵 객체 생성
cream = bread("슈크림", 2000)
# 팥 붕어빵 객체 생성
bean = bread("팥", 1000)
# 김치 붕어빵 객체 생성
kimchi = bread("김치", 1500)
# 피자 붕어빵 객체 생성
pizza = bread("피자", 1500)

while True:
    choice = input("붕어빵을 고르세요 : ")
    b = int(input("몇개 고르실건가요? : "))
    if choice == "슈크림":
        while b>=1:
            b = b-1
            cream.sell()
        print("총 " + str(cream.total) + "이 나왔습니다.")
        cream.eat()
    elif choice == "팥":
        while b>=1:
            b = b-1
            bean.sell()
        print("총 " + str(bean.total) + "가 나왔습니다.")
        bean.eat()
    elif choice == "김치":
        while b>=1:
            b = b-1
            kimchi.sell()
        print("총 " + str(kimchi.total) + "가 나왔습니다.")
        kimchi.eat()
    elif choice == "피자":
        while b>=1:
            b = b-1
            pizza.sell()
        print("총" + str(pizza.total) + "가 나왔습니다.")
        pizza.eat()
    else:
        print("메뉴를 다시 선택해주세요")
