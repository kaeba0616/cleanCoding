## annotation

- 법적인 정보를 담을 때

```
Copyright (C) 2021 ...
```

- 의도를 명확하게 설명할 때

```
#throughput을 늘리기 위해 스레드를 10개까지 늘린다.
for idx in range(10):
    thread = threading .Thread(target=...)
    thread.start()
```

- 중요성을 강조할 때

```
# 최종 결제를 하기 위해 진행해야 하는 validation 함수
def validation_buyablue(wallet, price, ...):
    ...
```

- 결과를 경고할때

```
# WARNING: API 서버가 항상 양호한지 알 수 없음.
def connect_api_server():
    ...
```

## 관용적으로 사용되는 키워드 (annotation)

- TODO : 당장은 아니지만 다음에 해야 할 때
- FIXME : 치명적인 에러를 발생하는 코드가 아니지만 수정해야 할때
- XXX : 더 생각해볼 필요가 있을 때

```
# TODO@grab : 객체의 책임 더 분리하기
class GrabStore:
    ...
    # FIXME : 반복문의 depth를 줄이기
    def sell_food(self):
        for food in food_list:
            for discount in discount_list:
                ...
```
