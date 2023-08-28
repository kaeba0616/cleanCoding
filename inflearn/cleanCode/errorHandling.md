## 에러 핸들링

- 오류 코드보다는 예외 사용하기

  - as-is

  ```
  from enum import Enum

  class ErrorCodes(Enum):
      VALUE_ERROR = "VALUE_ERROR"

  def we_can_raise_error():
      ...
      return ERROR_CODES.VALUE_ERROR

  def use_ugly_function():
      return = we_can_raise_error()
      if return == ErrorCodes.VALUE_ERROR:
          ... # 처리코드
  ```

  - to-be

  ```
  def we_can_raise_error():
      if ...
          raise ValueError("에러 발생")

  def use_awesone_function():
      try:
          we_can_occur_error()
          ...
      except ValueError as e:
          # 에러 처리 로직
  ```

## 예외 클래스 잘 정의하기

- 기본 exception만 쓰기 보단 내장된 built in Exception을 잘 활용하면 좋다.
- 상황에 맞게 Custom Exception을 만들어 사용하는 것도 좋다

```
class CustomException(Exception):
    ...

class WithParameterCustomException(Exception):
    def __init__(self, msg, kwargs):
        self.msg = msg
        self.kwargs = kwargs

    def __str__(self):
        return f"message {self.msg} with parameter {self(self.kwargs)}"

raise WithParameterCustomException("문제가 있습니다", {"name" : "grab"})
```

## 에러 핸들링 잘하기

- 에러를 포착했다면 잘 핸들링해줘야 합니다.

```
def we_can_raise_error():
    ...
    raise Exception("Error!")

# BAD: 에러가 났는지 확인할 수 없게 됩니다.
def use_ugly_function1():
    try:
        we_can_raise_error()
        ...
    except:
        pass

# BAD : 로그만 남긴다고 끝이 아닙니다.
def use_ugly_function2():
    try:
        we_can_raise_error()
        ...
    except Exception as e:
        print("에러 발생{e}")

# GOOD
def use_ugly_function2():
    try:
        we_can_raise_error()
        ...
    except Exception as e:
        logging.error(...) # error log 남기기
        notify_error(...) # 예측불가능한 외부 I/O 이슈라면 회사 내 채널에 알리기(이메일 슬랙 ..)
        raise OtherException(e) # 만약 이 함수를 호출하는 다른 함수에서 추가로 처리해야 한다면 에러를 전파하기

    finally:
        ... # 에러가 발생하더라도 항상 실행되어야 하는 로직이 있다면 finally 문을 넣어주기
```

- 에러 핸들링을 모을 수 있으면 한곳으로 모읍니다. 보통 같은 수준의 로직을 처리한다면 한 곳으로 모아서 처리하는게 더 에러를 포착하기 쉽습니다.

  - as-is

  ```
  def act_1():
      try:
          we_can_raise_error1()
          ...
      except:
          #handling

  def act_2():
      try:
          we_can_raise_error2()
          ...
      except:
          #handling

  def act_3():
      try:
          we_can_raise_error3()
          ...
      except:
          #handling

  # 에러가 날 지점을 한눈에 확인할 수 없습니다.
  # act_1이 실패하면 act_2가 실행되면 안된다면? 핸들링하기 어려워집니다.

  def main():
      act_1()
      act_2()
      act_3()
  ```

  - to-be

  ```
  def act_1():
      we_can_raise_error1()
      ...

  def act_2():
      we_can_raise_error1()
      ...

  def act_3():
      we_can_raise_error1()
      ...

  # 직관적이며 에러가 날 지점을 확인하고 처리할 수 있습니다.
  # 트랜잭션같이 한 단위로 묶여야하는 처리에도 유용합니다.

  def main():
      try:
          act_1()
          act_2()
          act_3()
      except SomeException1 as e1:
          ...

      except SomeException2 as e2:
          ...

      except SomeException3 as e3:
          ...

      finally:
          ...
  ```
