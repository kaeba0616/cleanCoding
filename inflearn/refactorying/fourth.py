# 1번. 다른 Store가 들어오면 어떻게 될까?
# 개선점
# 1. Store 추상화를 한다.
# 2. 의존성 주입을 한다.

# 2번. Store에 있는 상품과 돈을 마음대로 접근할 수 있다.
# 개선점
# 1. Store의 책임을 정의하고 캡슐화한다.
# 2. User의 결제 로직을 수정한다.
# 3. User도 캡슐화해보자.

# 3번. User가 많은 행위를 책임지고 있다. Store가 판매하는 책임을 가져야하지 않을까?
# 개선점
# 1. 상점에서 상품을 판매하는 행위를 추상화하고 구체적인 로직을 해당 메서드로 옮긴다.

# 4번. product dictionary 책임을 가지자
# 개선점
# 1. dictionary type을 클래스(데이터 클래스) 객체로 변환하자.

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int
    
    # product = Product(name=name, price=price)
    # produc.name

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
    def sell_product(self, product_id, money):
        ...

    
    
        
class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "그랩마켓"
        self._products = products

    def set_money(self, money: int):
        self._money = money

    def set_product(self, products):
        self._products = products

    def show_product(self, product_id):
        return self._products[product_id]
    
    def sell_product(self, product_id, money):
        # Validatio 코드는 최소화
        product = self.show_product(product_id=product_id)
        if not product:
            raise Exception("해당 상품이 없습니다.")

        self._take_money(money=money)
        try: 
            _product = self._take_out_product(product_id=product_id)
            return _product

        except Exception as e:
            self._return_money(money=money)
            raise e
            
    def _take_out_product(self, product_id):
        return self._products.pop(product_id)
        
    def _return_money(self, money):
        self._money -= money
    
    def _take_money(self, money):
        self._money += money
    
class User:
    def __init___(self, money, store: Store):
        self._money = money
        self.store = store
        self.belongs = []

    def get_money(self):
        return self._money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_products(self, product_id):
        product = self.store.show_product(product_id=product_id)
        return product

    def purchase_product(self, product_id):
        product = self.see_product(product_id=product_id) # keyword parameter
        price = product.price
        if self._check_money_enough(price=price):
            self._give_money(money=price) # 사용자가 돈 내기
            try :
                my_product = self.store.sell_product(product_id=product_id, money=price) # 상점에서 사움 꺼내기
                self._add_belong(my_product) # 사용자가 상품 소유
                return my_product
            except Exception as e:
                self._take_money(money=price)
                price(f"There is a problem in the store. {str(e)}")

        else:
            raise Exception("잔돈이 부족합니다.")

    def _check_money_enough(self, price):
        return self._money >= price

    def _give_money(self, money):
        self._money -= money
    
    def _take_money(self, money):
        self._money += money

    def _add_belong(self, product):
        self.belongs.append(product) # lIST에 추가
        
# 실행코드
if __name__ == "__main__": 
    store = GrabStore(
        products={
            1: Product(name="키보드", price=30000),
            2: Product(name="모니터", price=50000),
        }
    )
    
    user = User(money=100000, store=store)
    user.purchase_product(product_id=1)
    print(f"user의 잔돈 : {user.get_money()}" )
    print(f"user가 구매한 상품 : {user.get_belongs()}")
    