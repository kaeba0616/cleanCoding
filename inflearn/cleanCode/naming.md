## convention

|   naming   |                          case                          |
| :--------: | :----------------------------------------------------: |
| snake_case |                      Python, Ruby                      |
| camelCase  |                    Java, Javascript                    |
| PascalCase | 대부분의 프로그래밍 언어에서 클래스를 네이밍할 때 사용 |
| kebab-case |            HTML Element를 표현할 때 사용함             |

## 변수와 상수

- 일반적으로 변수와 상수를 네이밍 할때 **명사** or **형용사** 구문 형태로 지음

```
user_data = ...
is_valid = ...
```

## Function & method

- 일반적으로 **동사** or **형용사**

```
def send_data():
    ...
def input_is_invalid():
    ...
```

## Class

- **명사**

```
class Client:
    ...

class RequestBody:
    ...
```

## TIPs

- 구체적이고 **명시적**으로 적을 것

```
# as-is
dt = "20210901KST"
for i in data:
    ...

# to-be
datetime_with_timezone="20210901KST"
for product in products:
    ...
```

- 불필요한(애매한) 표현은 제거할 것

```
# as-is
product_with_price = Product("아이폰", 3000)
the_message = 1
name_string = "grab"

# to-be
product = Product("아이폰", 3000)
message = 1
name = "grab"
```
