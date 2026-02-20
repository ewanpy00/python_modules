from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.total_processed = 0
        self.error_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.total_processed,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        print("\nInitializing Sensor Stream...")
        super().__init__(stream_id)
        self.criteria = "Positive values"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        clear_data = []
        for element in data_batch:
            if isinstance(element, dict) and "temp" in element:
                if criteria == "Positive values":
                    if element["temp"] >= 0:
                        clear_data += [element]
                elif criteria == "Negative values":
                    if element["temp"] < 0:
                        clear_data += [element]
        return clear_data

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(f"Processing sensor batch: {data_batch}")
        try:
            clear_data = self.filter_data(data_batch, self.criteria)
            count = 0
            sum = 0
            for element in clear_data:
                count += 1
                sum += element["temp"]
            if count == 0:
                return "Sensor analysis: 0 readings processed"
            
            avg_temp = sum/count
            self.total_processed += count
            return f"Sensor analysis: {count} readings processed, avg temp: {avg_temp:.1f}°C"
        except Exception:
            self.error_count += 1
            return "Error occurred during the processing"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        print("\nInitializing Transaction Stream...")
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        print(f"Processing transaction batch: {data_batch}")
        try:
            count = 0
            net_flow = 0
            for data in data_batch:
                if "buy" in data: net_flow -= data["buy"]
                if "sell" in data: net_flow += data["sell"]
                count += 1
            
            self.total_processed += count
            return f"Transaction analysis: {count} operations, net flow: {net_flow:+} units"
        except Exception:
            self.error_count += 1
            return "Error processing transactions"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        print("\nInitializing Event Stream...")
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        print(f"Processing event batch: {data_batch}")
        count = 0
        errors = 0
        for element in data_batch:
            if "error" in element:
                errors += 1
            count += 1
        self.total_processed += count
        self.error_count += errors
        return f"Event analysis: {count} events, {errors} error detected"

class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams += [stream]

    def process_all(self, batches: List[List[Any]]):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        i = 0
        for stream in self.streams:
            result = stream.process_batch(batches[i])
            i += 1
            print(f"- {result}")

def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    sensor_data = [{"temp":22.5, "humidity":65, "pressure":2},
                   {"temp":10, "humidity":65, "pressure":10},
                   {"temp":-10, "humidity":65, "pressure":1}
                        ]
    sensor.process_batch(sensor_data)

    transaction = TransactionStream("TRANS_001")
    trans_data = [{"buy": 100}, {"sell": 150}, {"buy": 120}, {"buy": 12}, {"sell": 120}]
    transaction.process_batch(trans_data)

    event = EventStream("EVENT_001")
    event_data = ["login", "error", "logout"]
    event.process_batch(event_data)

    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(transaction)
    manager.add_stream(event)

    manager.process_all([sensor_data, trans_data, event_data])
    
    print("\nAll streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    main()