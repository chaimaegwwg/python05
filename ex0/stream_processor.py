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


class Overrid_Numeric(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            int(data)
        except ValueError:
            return False
        return True

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            v = int(data)
            lst = [n for n in range(1, v + 1)]
            return lst
        else:
            return f"{data}"

    def proccessed(self, data: Any) -> str | int:
        if self.validate(data) is True:
            value = int(data)
            s = sum(i for i in range(1, value+1))
            s = sum(i for i in range(1, value+1))
            arg = s / value
            return f"Processed {value} numeric values, sum={s}, avg={arg}"
        else:
            error, string = data.split(":", 1)
            if error == "ERROR":
                self.validate("Log entry verified")
                return f"[ALERT] ERROR level detected: {string}"
            else:
                value = len(data)
                count_world = len(data.split())
                return f" Processed text: {value} characters, {count_world} words"

    # def format_output(self, data: Any) -> str | int:


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    n = Overrid_Numeric()
    data = "ERROR: Connection timeout"
    lst = n.process(data)
    print("Processing data:", lst)
    if n.validate(data):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Text data verified")
    n = n.proccessed(data)
    print("Output:", n)
    # z = n.format_output(data)
    # if not z:
    # else:
        # print("Output: Processed", x, "numeric values, sum=", y, f"avg ={z}")


main()
