# SRP (Single Responsibility Principle / 단일 책임 원칙)

- 객체는 하나의 책임만을 지녀야 한다는 법칙이다.

- 여러 책임을 동시에 가지는 객체는 처음에 코드를 짤 때는 편합니다. 하지만 코드가 복잡해질수록 에러가 날 확률도 높아지며 직관적으로 코드를 이해하기 어려워집니다. so before you build the object, it's important to assign responsible clearly.

## AS-IS

```
# 하나의 클래스(객체)가 여러 책임을 가지고 있습니다.

class Employee:
    def coding(self):
        print("코딩을 합니다.")

    def design(self):
        print("디자인을 합니다.")

    def analyze(self):
        print("분석을 합니다.")
```

## TO-BE

```
# 각 개체는 역할을 나눠서 가지고 있습니다.

class Developer:
    def coding(self):
        print("코딩을 합니다.")

class Designer:
    def design(self):
        print("디자인을 합니다.")

class Analyst:
    def analyze(self):
        print("분석을 합니다.")

```
