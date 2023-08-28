## formatting

- Vertical Formatting
  - 한 파일에 코드를 다 넣지 말고, 개념에 맞게 파일을 나눠서 사용합니다.

```
# as-is
# store.py에 전부 있음
class Fruitstore:
    ...

class ComputerStore:
    ...

# to-be
# fruit_store.py
class FruitsStore:
    ...

# computer_store.py
class Computer_store:
    ...
```

- 다른 개념의 코드는 Spacing으로 분리하기
  - 비슷한 개념의 코드는 붙여서 사용하기

```
def test_user_buy_product():
    user = User()
    product = Product()

    product.set_sold_out(True);
    user.get(product)

    assert resut == "success"
```

- Horizontal Formatting
  - 한줄에 코드를 다 넣기보단 변수 들을 활용하여 가독성 높이기

```
# as-is
product_list.extend({Product("모니터"), Product("키보드"), Product("노트북")})

# to-be
items = {Product("monitor"), Product("keyboard"), Prodcut("notebook")}
product_list.extend(itmes)
```

- 네이밍 잘해서 갈이 줄이기

```
# as-is
user_with_name_and_email = User("그랩", "grab@world.com")

# to-be
user = User("그랩", "grab@world.com")
```
