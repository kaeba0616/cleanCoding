# 1번. 다른 Store가 들어오면 어떻게 될까?
# 개선점
# 1. Store 추상화를 한다.
# 2. 의존성 주입을 한다.

from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.money = 0
        self.name = ""
        self.products = {}
        
    @abstractmethod
    def set_money(self, money):
        ...
        
    @abstractmethod
    def set_product(self, products):
        ...
        
    @abstractmethod
    def get_money(self):
        ...
        
    @abstractmethod
    def get_product(self):
        ...
        
        
class GrabStore(Store):
    def __init__(self):
        self.money = 0
        self.name = "그랩마켓"
        self.products = {
            1: {"name": "키보드", "price" : 30000},
            2: {"name": "모니터", "price" : 50000},
        }

    def set_money(self, money):
        self.money = money

    def set_product(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_product(self):
        return self.products


class FruitsStore(Store):
    def __init__(self):
        self.money = 0
        self.name = "과일마켓"
        self.products = {
            1: {"name": "바나나", "price" : 30000},
            2: {"name": "사과", "price" : 50000},
        }

    def set_money(self, money):
        self.money = money

    def set_product(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_product(self):
        return self.products

class User:
    def __init___(self, store: Store):
        self.money = 0
        self.store = store
        self.belongs = []

    def set_money(self, money):
        self.money = money

    def set_belongs(self, belongs):
        self.belongs = belongs

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_products(self, product_id):
        products = self.store.get_products()
        return products[product_id]

    def purchase_product(self, product_id):
        product = self.see_products(product_id)
        if self.money >= product["price"]:
            self.store.products.pop(product_id) # 상점에서 사움 꺼내기
            self.money -= product["price"] # 사용자가 돈 내기
            self.store.money += product["price"] # 상점에서 돈 받기
            return product

        else:
            raise Exception("잔돈이 부족합니다.")


# 실행코드
if __name__ == "__main__":
    user_a = User(store=GrabStore())
    user_b = User(store=FruitsStore())