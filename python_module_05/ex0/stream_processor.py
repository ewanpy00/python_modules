from abc import ABC, abstractmethod
from typing import Any

class ValidationError(Exception):
    pass

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, result: str) -> str:
        return result

class NumericProcessor(DataProcessor):
    def __init__(self, numerics: list[int]):
        print(f"{self.process(numerics)}")

    def process(self, data: Any):
        i = 0
        sum = 0
        print(f"Processing data: {data}")
        for num in data:
            try:
                valid = self.validate(num)
                if valid is False:
                    raise ValidationError
                sum = sum + int(num)
                i += 1 
            except ValidationError:
                print("Incorrect value occured") 
        print("Validation: Numeric data verified")
        return self.format_output(f"Output: Processed {i} numeric values, sum={sum}, avg={sum/i}")
        
    
    def format_output(self, result: str):
        return result


    def validate(self, num: int):
        try:
            int(num)
            return True
        except ValueError:
            return False

    
class TextProcessor(DataProcessor):
    def __init__(self, data: str):
        self.charecters = 0
        self.words = 0
        print(f"{self.process(data)}")

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        count = 0
        i = 0
        in_word = False
        check = True
        try:
            check = self.validate(data)
            for char in data:
                try:
                    if char != " ":
                        if not in_word:
                            count+=1
                            in_word = True
                    else:
                        in_word = False
                    if check == False:
                        raise ValidationError
                except Exception as e:
                    print("An error occured while processing the input:", e)
                i += 1
        except ValidationError:
            print("Validation error occured!")
        print("Validation: Text data verified")
        return self.format_output(f"Output: Processed text: {i} characters, {count} words")
    
    def validate(self, data: Any) -> bool:
        check = False
        for char in data:
            if char != " " and data != "\t":
                check = True
                return check
        return check
    
    def format_output(self, result):
        return result
        
        
def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    numerics = [1, "acb", 3, 4, 5]
    NumericProcessor(numerics)
    print("\nInitializing Text Processor...")
    text = "Hello Nexus World"
    TextProcessor(text)


if __name__ == "__main__":
    main()