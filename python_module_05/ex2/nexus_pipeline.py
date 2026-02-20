from abc import ABC, abstractmethod
from typing import List, Callable, Any

class ProcessingPipeline(ABC):
    def __init__(self, stages: List[Callable] | None = None):
        self._stages = stages or []

    def add_stage(self, stage: Callable) -> None:
        self._stages.append(stage)

    def remove_stage(self, stage: Callable) -> None:
        self._stages.remove(stage)

    def clear_stages(self) -> None:
        self._stages.clear()

    def run(self, data: Any) -> Any:
        result = data
        for stage in self._stages:
            result = stage(result)
        return result

    @abstractmethod
    def validate_stage(self, stage: Callable) -> bool:
        pass

# ---------------------------------------Adapters---------------------------------------

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    # ---------------------------------------STAGES---------------------------------------

class inputStage():
    def process(self, data: Any) -> Any:
        return
    
class TransformStage():
    def process(self, data: Any) -> Any:
        return
    
class OutputStage():
    def process(self, data: Any) -> Any:
        return
    