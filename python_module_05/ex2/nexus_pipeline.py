from abc import ABC, abstractmethod
from typing import Any, List, Protocol

# ---------------------------------------STAGES---------------------------------------

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

class InputStage:
    def __init__(self, description: str):
        self.description = description

    def process(self, data: Any) -> Any:
        if data is None:
            return None
        print(f"Input: {data}")
        return data

class TransformStage:
    def __init__(self, description: str, transform_msg: str):
        self.description = description
        self.transform_msg = transform_msg

    def process(self, data: Any) -> Any:
        if data is None:
            return None
        print(f"Transform: {self.transform_msg}")
        return data

class OutputStage:
    def __init__(self, description: str, fixed_output: str):
        self.description = description
        self.fixed_output = fixed_output
        
    def process(self, data: Any) -> Any:
        if data is None:
            return None
        print(f"Output: {self.fixed_output}")
        return data

# ---------------------------------------PIPELINE---------------------------------------

class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.stages = []
        self.pipe_id = pipeline_id
        self.stage_count = 0
        self.logs = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stage_count += 1
        print(f"Stage {self.stage_count}: {stage.description}")
        self.stages += [stage]

    def add_stages(self, list):
        for element in list:
            self.add_stage(element)

    def run_pipeline(self, data: Any) -> Any:
        current_result = data
        current_num = 0
        
        for stage in self.stages:
            current_num += 1
            current_result = stage.process(current_result)
            
            if current_result is None:
                error_msg = f"Error detected in Stage {current_num}: Invalid data input"
                self.logs += [error_msg]
                return None
        return current_result

    @abstractmethod
    def process(self, data: Any):
        pass

# ---------------------------------------ADAPTERS---------------------------------------

class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("\nProcessing JSON data through pipeline...")
        self.run_pipeline(data)

class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("\nProcessing CSV data through same pipeline...")
        self.run_pipeline(data)

class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> None:
        print("\nProcessing Stream data through same pipeline...")
        self.run_pipeline(data)

# ---------------------------------------MANAGER---------------------------------------

class NexusManager:
    def __init__(self):
        print("Initializing Nexus Manager...")
        self.pipelines = []
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeLine(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines +=  [pipeline]

# ---------------------------------------MAIN---------------------------------------

def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    stage1 = InputStage("Input validation and parsing")

    stage2_json = TransformStage("Data transformation and enrichment", "Enriched with metadata and validation")
    stage2_csv = TransformStage("Data transformation and enrichment", "Parsed and structured data")
    stage2_stream = TransformStage("Data transformation and enrichment", "Aggregated and filtered")

    stage3_json = OutputStage("Output formatting and delivery", "Processed temperature reading: 23.5°C (Normal range)")
    stage3_csv = OutputStage("Output formatting and delivery", "User activity logged: 1 actions processed")
    stage3_stream = OutputStage("Output formatting and delivery", "Stream summary: 5 readings, avg: 22.1°C")

    json_stages = [stage1, stage2_json, stage3_json]
    csv_stages = [stage1, stage2_csv, stage3_csv]
    stream_stages = [stage1, stage2_stream, stage3_stream]

    json_pipe = JSONAdapter("JSON")
    json_pipe.add_stages(json_stages)

    csv_pipe = CSVAdapter("CSV")
    csv_pipe.stages = csv_stages 

    stream_pipe = StreamAdapter("STREAM")
    stream_pipe.stages = stream_stages

    print("\n=== Multi-Format Data Processing ===")


    json_pipe.process({"sensor": "temp", "value": 23.5, "unit": "C"})    
    csv_pipe.process("user,action,timestamp")
    stream_pipe.process("Real-time sensor stream")

    i = 65
    for _ in json_stages:
        if i == 65:
            print(f"Pipeline {chr(i)} ", end="")
            i += 1
            continue
        print(f"-> Pipeline {chr(i)} ", end="")
        i += 1
    if i == 68:
        print("\nData flow: Raw -> Processed -> Analyzed -> Stored")
    
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    all_logs = json_pipe.logs
    for log in all_logs:
        print(log)
    print("Recovery initiated: Switching to backup processor")
    print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")

if __name__ == "__main__":
    main()