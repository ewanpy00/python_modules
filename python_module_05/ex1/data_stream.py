from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.total_processed = 0
        self.error_count = 0
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    @abstractmethod
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        pass
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

class SensorStream():
    def __init__(self, stream_id):
        print("Initializing Sensor Stream...")
        self.super(stream_id)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        # return [element for element in data_batch if isinstance(element, dict())]
        clear_data = []
        for element in data_batch:
            if isinstance(element, dict):
                required_keys = ["temp", "humidity", "pressure"]
                
                if isinstance(element["temp"], (int, float)) and isinstance(element["humidity"], (int, float)) and isinstance(element["humidity"], (int, float)):
                    clear_data += [element]
            
    # add criteria
            

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        try:
            print(f"Processing sensor batch: {clear_data}")
            clear_data = self.filter_data(data_batch)
            sum = 0
            count = 0
            for data in data_batch:
                sum += data.items()
                count += 1
            return f"Sensor analysis: {count} readings processed, avg temp: {sum/count:.2F}°C"
        except Exception as e:
            print("invalid input sensor data")
            return "Error occured during the processing"

def main():
    batch_sensor = [
         {"temp":22.5, "humidity":65, "pressure":1013}
    ]