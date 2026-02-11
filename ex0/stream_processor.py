from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            value = int(data)
            s = sum(i for i in range(1, value+1))
            arg = s / value
            return f"Processed {value} numeric values, sum={s}, avg={arg}"
        else:
            return "Invalid numeric data"
    def count(self, data: int) -> list[int] | str:
        if self.validate(data) is True:
            v = int(data)
            lst = [n for n in range(1, v + 1)]
            return lst
        else:
            return f"{data}" 

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            int(data)
        except ValueError:
            return True
        return False
    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            if self.validate(data) is True:
                value = len(data)
                count_world = len(data.split())
                return f" Processed text: {value} characters, {count_world} words"  
        else:
            return "Invalid data"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        error, string = data.split(":", 1)
        error = error.strip()
        if error == "ERROR" or error == "WARNING" or error == "WARNING": 
            return True
        else:
            return False
    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            error, string = data.split(":", 1)
            error = error.strip()
            if error == "ERROR":
                return f"[ALERT] ERROR level detected:{string}"
            elif error == "WARNING":
                return f"[WARNING] {string}"
            else:
                return f"[INFO] {string}"
        else:
            return "Invalid log entry"


def main():

    l = LogProcessor()
    data = "ERROR  :         Connection timeout"

    print("Processing data:", data)

    if l.validate(data):
        print("Validation: Log entry verified")
    else:
        print("Validation: Invalid log entry")

    output = l.process(data)
    print("Output:", output)




    # t = TextProcessor()
    # data = "Hello Nexus World"

    # print("Processing data:", data)


    # if t.validate(data):
    #     print("Validation: Text data verified")
    # else:
    #     print("Validation: Invalid text data")
    # output = t.process(data)
    # print("Output:", output)

    # n = NumericProcessor()
    # data = 5
    # dt = n.count(data)
    # print("Processing data:",dt)
    # if n.validate(data):
    #     print("Validation: Numeric data verified")
    # else:
    #     print("Validation: Invalid numeric data")

    # v = n.process(data)
    # print("Output:",v)
    print("\n=== Polymorphic Processing Demo ===")


main()
