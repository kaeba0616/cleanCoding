## 리펙토링을 통한 객체 지향 알아보기

- 기존 프로젝트 파일

  - https://github.com/yansfil/devall-class-oop-test/tree/oop-example

- 상황

  - 사용자가 상점에서 상품을 구매하는 코드를 구현합니다.
  - 사용자와 상점은 돈을 가지고 있고, 거래가 일어나면 돈을 주고받습니다.

- 리펙토링 전 코드

```
class GrabStore:
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

class User:
    def __init___(self):
        self.money = 0
        self.store = GrabStore()
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
        if self.money >= product["price"]
            self.store.products.pop(product_id) # 상점에서 사움 꺼내기
            self.money -= product["price"] # 사용자가 돈 내기
            self.store.money += product["price"] # 상점에서 돈 받기
            return product

        else:
            raise Exception("잔돈이 부족합니다.")


# 실행코드
if __name__ == "__main__":
    user = User()
    user.set_money(100000)
    user.purchase_product(product_id=1)
```
