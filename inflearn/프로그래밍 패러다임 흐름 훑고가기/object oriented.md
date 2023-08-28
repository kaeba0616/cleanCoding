## Object oriented Programming

- 객체라고 하는 단위에 책임을 명확히 하고 서로 협력하도록 프로그래밍을 하는 패러다임이다.
- 모든 것을 객체로 나누어 생각하고, 필요할 때 객체들을 활용하고 서로 협력하여 일을 수행합니다.

- 절차지향과 다르게 객체는 데이터와 함수(메서드)를 함께 가지고 있습니다. 객체 내부의 데이터는 외부에 공개할 필요가 없거나 해서는 안 되는 데이터라면 모두 자신 내부에 숨겨 외부에서 알지 못하도록 합니다.

```
class Processor:
    def __init__(self,
                file_reader: FileReader,
                data_parser: DataParser,
                repository: Repository) -> None:
        self.file_reader = file_reader
        self.data_parser = data_parser
        self.repository = repository

    def execute(self, file_path: str) -> None:
        data = self.file_reader.read(file_path)
        parsed_data = self.data_parser.parse(data)
        self.repository.save(parsed_data)


class FileReader:
    def __init__(self) -> None:
        self.file_type = ["txt"]
        self.file_history = [] # 만약 절차 지향이라면 file_history 데이터를 중앙 집중으로 관리하게 됩니다.

    def read(self, file_path: str) -> str:
        self._validate(file_path)
        ...

    def _validate(self, file_path: str) -> None:
        for file_type in self.file_types:
            if file_path.endswith(file_type):
                return
        raise ValueError("파일 확장자는 txt, csv, xlsx 중 하나여야 합니다.")

class DataParser:
    def parse(self, data: str) -> List[str]:
        ...

class repository:
    def init(self, data_base_url: str, ...):
        ...

    def save(self, data: List[str]) -> None:
        ...

class Main:
    @staticmethod
    def run(self) -> None:
        processor = Processor(
            file_reader = FileReader(),
            data_parser = DataParser(),
            respository = Repository()
        )
        processor.execute("input_file.txt")

if __name__ == "__main__":
    Main.run()
```

- csv, xlsx 파일도 읽어야 하는 상황이라면

```
class FileReader(ABC):
    def read(self, file_path: str) -> str:
        self._validate(file_path)
        data = self._open_file(file_path)
        return self._read(data)

    @abstractmethod
    def _read(self, data: str) -> str:
        pass

    # 공통으로 사용하는 메서드입니다.
    def _validate(self, file_path: str) -> None:
        if not file_path.endswith(self.file_type):
            raise ValueError(f"파일 확장자가 {self.file_type} 아닙니다.")

    @abstractmethod
    def _open_file(file_path: str) -> str
        ...

# txt 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
class TxtFileReader(FileReader):
    def file_type(self) -> str:
        return "txt"

    def _read(self, data: str) -> str:
        ...
    ...

# csv 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
class CsvFileReader(FileReader):
    def file_type(self) -> str:
        return "csv"

    def _read(self, data: str) -> str:
        ...
    ...

# xlsx 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
class XlsxFileReader(FileReader):
    def file_type(self) -> str:
        return "xlsx"

    def _read(self, data: str) -> str:
        ...
    ...

class Main:
    def run(self) -> None:
        processor = Processor(
            file_reader = TxtFileReader(),
            data_parser = DataParser(),
            repository = Repository()
        )

class Main:
    def run(self) -> None:
        processor = Processor(
            file_reader = CsvFileReader(),
            data_parser = DataParser(),
            repository = Repository()
        )
```

## 장단점

- 객체 지향은 여러 명의 개발자들이 협력을 해야 하거나, 확장 가능하도록 코드를 설계해야 하는 경우에 적합합니다.

- 하지만 확장이 가능하고 유연한 만큼, 처음 코드를 보든 사람들은 어렵고 헷갈릴 수 있습니다. 또한 실행 환경에서 입력에 따라 다양한 작업 흐름이 만들어지기 때문에 디버깅하기가 상대적으로 어렵습니다.
