## SRP(단일 책임 원칙) 지키기

- 하나의 클래스는 하나의 책임만 가지도록 합니다.

  - as-is

  ```
  class Store:
      def communicate_user(self):
          ...

      def manage_products(self):
          ...

      def manage_money(self):
          ...
  ```

  - to-be

  ```
  class CounterManager:
      def communicate_user(self):
          ...

  class ProductManager:
      def manage_products(self):
          ...

  class Owner:
      def manage_money(self):
          ...

  Class Store:
      def __init__(self, counter_manager: CounterManager, product_manager: ProductManager, owner : Owner)
          self.counter_manager = conuter_manager
          self.product_manager = product_manager
          self.owner = owner

      def sell_product(self):
          self.counter_manager.communicate_user()
          ...

      def manage_products():
          ...
  ```

## 응집도 높이자.

- 응집도는 클래스의 변수와 메서드들이 얼마나 유기적으로 엮여있냐를 나타내는 지표입니다.

  - 응집도가 높을수록 클래스의 메서드들은 인스턴스 변수들을 많이 사용합니다.
  - 응집도가 낮을수록 클래스이 메서드들은 인스턴스 변수들을 적게 혹은 사용하지 않습니다.

  - as-is

  ```
  class LowCohesion:
      def __init__(self):
          self.a =...
          self.b =...
          self.c =...

      def process_a(self):
          print(self.a)

      def process_b(self):
          print(self.b)

      def process_c(self):
          print(self.c)
  ```

  - to-be

  ```
  class HighCohesion:
      def __init__(self):
          self.abc = ...

      def process_a(self):
          self.abc.process_a()

      def process_b(self):
          self.abc.process_b()

      def process_c(self):
          self.abc.process_c()
  ```

## 변경하기 쉽게 만들자

- 일반적으로 변경하기 쉽게 설계하기 위해선 추상화를 해두고, 구체 클래스에 의존하지 않고 추상 클래스(인터페이스)에 의존하도록 코드를 짜는 것이 중요합니다.

  - as-is

  ```
  class Developer:
      def coding(self):
          print("코딩을 합니다")

  class Designer:
      def design(self):
          print("디자인을 합니다")

  class Analyst:
      def analyze(self):
          print("분석을 합니다")

  class Company:
      def __init__(self, employees):
          self.employees = employees

      def make_work(self):
          for employee in self.employees:
              if type(employee) == Developer:
                  employee.coding()

              elif type(employee) == Designer:
                  employee.design()

              elif type(employee) == Analyst:
                  employee.analyze()
  ```

  - to-be

  ```
  class Employee(metaclass = abc.ABCMeta):
      @abc abstractmethod
      def work(self):
          ...

  class Developer(Employee):
      def work(self):
          print("코딩을 합니다.")

  class Designer(Employee):
      def work(self):
          print("디자인을 합니다.")

  class Analyst(Employee):
      def work(self):
          print("분석을 합니다.")

  class Manager(Employee):
      def work(self):
          print("매니징을 합니다.")

  class Company:
      def __init__ (self, employees: List[Employee])
          self.employees = employees

      def make_work(self):
          for employee in self.emplyoees:
              employee.work()
  ```
