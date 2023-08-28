## Function

- 함수의 역할은 하나만 할 수 있도록 하자! **SRP**
  - 함수의 역할이 많아진다면, 오류가 날 가능성이 커지고 가독서이 떨어집니다. 또한 함수에 대한 테스트를 진행하기가 어렵습니다.

```
# as-is
def create_user(email, password):
    # validation 로직
    if "@" not in email or len(password) <6 :
        raise Exception("유저 정보를 제대로 입력하세요.")

    user = {"email" : email, "password" : password}

    database = Database("mysql")
    databaes.add(user)

    email_client = EmailClient()
    email_client_set_config(...)
    email_client.send(email, "회원가입을 축하합니다.")

    return True
```

```
# to-be
def create_user(email, password):
    validation_create_user(email, password)

    user = build_user(email, password)

    save_user(user)
    send_email(email)
    return

def validation_create_user(email, password):
    if "@" not in email or len(password) < 6:
        raise Exception("유저 정보를 제대로 입력하세요.")

def build_user(email, password):
    return{
        "email" : email,
        "password" : password
    }

def save_user(user):
    database = Database("mysql")
    database.add(user)

def send_email(email):
    email_client = EmailClient()
    email_client.set_config(...)
    email_client.send(email, "회원가입을 축하합니다.")
```

- 반복하지 말자 **DRY**
  - 관심사를 잘 분리하고 의존성을 줄이기 위해 반복되는 코드를 하나의 함수로 만들어 사용합니다.

```
# as-is
def create_user(email, password):
    # validation logic
    if "@" not in email or len(password) < 6:
        raise Exception("유저 정보를 제대로 입력하세요.")
    ...

def update_user(email, password):
    # validation logic
    if "@" not in email or len(password) < 6:
        raise Exception("유저 정보를 제대로 입력하세요.")
    ...
```

```
# to-be

def validate_create_user(email, password):
    if "@" not in email or len(password) < 6:
        raise Exception("유저 정보를 제대로 입력하세요.")

def create_user(email, password):
    validate_create_user(email, password)
    ...

def update_user(email, password):
    validate_create_user(email, password)
    ...
```

- 파라미터 수는 적게 유지하자

```
# as-is
def save_user(user_name, email, password, created_at):
    ...

# to-be
def save_user(user:User):
    ...
```

- 사이트 이펙트를 잘 핸들링하자
  - 사이트 이펙트(side effect)는 함수가 실행됬을 때 함수 이외의 어떤 것들에 변화를 주는 것을 뜻합니다. 사이드 이펙트를 잘 다루지 못하면, 예측하지 못하는 문제들이 발생할 수 있습니다.

```
# No side effect
def get_user_instance(email, password):
    user = User(email, password)
    return user

# There is a side effect
def update_user_instance(user):
    user.email = "new email" #인자로 받은 user 객체를 업데이트합니다.
    ...

# There is a side effect
def create_user(email, password):
    user = User(email, password)
    start_db_session() # 외부의 DB Session에 변화를 줄 수 있습니다.
    ...
```

    - 잘 핸들링 하는 방법
        - 코드를 통해 충분히 예측할 수 있도록 네이밍을 잘하는 것이 중요합니다.
            - update, set 같은 직관적인 prefix를 붙여서 사이드 이펙트가 있을 수 있음을 암시합니다.

        - 함수의 사이트 이펙트가 있는 부분과 없는 부분으로 잘 나눠서 관리합니다.
            - 명령(side effect O)과 조회(side effect X)를 분리하는 **CQRS** 방식이 있습니다.

        - 일반적으로 update를 남발하기 보단 순수 형태로 사용하는 것이 더 직관적이고 에러를 방지할 수 있습니다.

```
# as-is

carts = []

# 사이드 이펙를 발생시킴
def add_cart(product):
    carts.append(product)

product = Product(...)
add_cart(product)
```

```
# to-be

carts = []
def get_added_cart(product):
    reutrn [...carts, product]

product = Product(...)
carts = get_added_cart(product)
```
