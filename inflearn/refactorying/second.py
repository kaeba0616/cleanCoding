# 1번. 다른 Store가 들어오면 어떻게 될까?
# 개선점
# 1. Store 추상화를 한다.
# 2. 의존성 주입을 한다.

# 2번. Store에 있는 상품과 돈을 마음대로 접근할 수 있다.
# 개선점
# 1. Store의 책임을 정의하고 캡슐화한다.
# 2. User의 결제 로직을 수정한다.
# 3. User도 캡슐화해보자.

from abc import ABC, abstractmethod

class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.money = 0
        self.name = ""
        self.products = {}
        
    @abstractmethod
    def show_product(self, product_id):
        ...
    
    @abstractmethod
    def give_product(self, product_id):
        ...
    
    @abstractmethod
    def take_money(self, money):
        ...
    
    
        
class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "그랩마켓"
        self._products = products

    def set_money(self, money):
        self._money = money

    def set_product(self, products):
        self._products = products

    def show_product(self, product_id):
        return self._products[product_id]
    
    def give_product(self, product_id):
        return self._products.pop(product_id)
    
    def take_money(self, money):
        self._money += money
    
class User:
    def __init___(self, money, store: Store):
        self.money = money
        self.store = store
        self.belongs = []

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_products(self, product_id):
        product = self.store.show_product(product_id=product_id)
        return product

    def purchase_product(self, product_id):
        product = self.see_product(product_id=product_id) # keyword parameter
        if self.money >= product["price"]:
            self.store.give_product(product_id=product_id) # 상점에서 사움 꺼내기
            self.money -= product["price"] # 사용자가 돈 내기
            self.store.take_money(product["price"]) # 상점에서 돈 받기
            self.belongs.append(product) # 사용자가 상품 소유
            return product

        else:
            raise Exception("잔돈이 부족합니다.")


# 실행코드
if __name__ == "__main__": 
    store = GrabStore(
        products={
            1: {"name": "키보드", "price" : 30000},
            2: {"name": "모니터", "price" : 50000},
        }
    )
    
    user = User(money=100000, store=store)
    user.purchase_product(product_id=1)
    print(f"user가 구매한 상품 : {user.get_belongs()}")