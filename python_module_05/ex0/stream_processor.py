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
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) != list:
            return False
        for x in data:
            if type(x) != int and type(x) != float:
                return False
        return True

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValidationError("Invalid numeric data")
        
        print("Validation: Numeric data verified")
        count = len(data)
        total = sum(data)
        avg = total / count if count > 0 else 0.0
        
        res_str = f"Processed {count} numeric values, sum={total}, avg={avg}"
        return self.format_output(res_str)

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) == str

    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            raise ValidationError("Invalid text data")
        
        print("Validation: Text data verified")
        chars = len(data)
        words = len(data.split())
        
        res_str = f"Processed text: {chars} characters, {words} words"
        return self.format_output(res_str)

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            raise ValidationError("Invalid log format")
        
        print("Validation: Log entry verified")
        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()
        
        tag = "[ALERT]" if level.upper() == "ERROR" else "[INFO]"
        return f"Output: {tag} {level} level detected: {message}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    
    print("\nInitializing Numeric Processor...")
    num_proc = NumericProcessor()
    print(num_proc.process([1, 2, 3, 4, 5]))
    
    print("\nInitializing Text Processor...")
    txt_proc = TextProcessor()
    print(txt_proc.process("Hello Nexus World"))
    
    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    print(log_proc.process("ERROR: Connection timeout"))
    
    print("\n=== Polymorphic Processing Demo ===")
    print("Code Nexus Polymorphic Data Streams in the Digital Matrix")
    print("Processing multiple data types through same interface...\n")
    
    mixed_data = [
        (NumericProcessor(), ["abc", 2, 3]),
        (TextProcessor(), "Hello Matrix"),
        (LogProcessor(), "INFO: System ready")
    ]
    
    for i, (processor, data) in enumerate(mixed_data, 1):
        try:
            result = processor.process(data)
            clean_result = result.replace("Output: ", "")
            print(f"Result {i}: {clean_result}")
        except ValidationError as e:
            print(f"Result {i}: Error - {e}")

    print("Foundation systems online. Nexus ready for advanced streams")

if __name__ == "__main__":
    main()