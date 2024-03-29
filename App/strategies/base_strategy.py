from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, *operands):
        pass

    def validate_operands(self, *operands):
        # LBYL
        if not all(isinstance(op, (int, float)) for op in operands):
            raise ValueError("All operands must be numeric.")