from statistics import mean, median, stdev
from App.strategies.base_strategy import OperationStrategy
from App.utils.wrapper import wrapper

class MeanOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        return mean(operands)

class MedianOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        return median(operands)

class StdDevOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        if len(operands) < 2:
            raise ValueError("Standard deviation requires at least two operands.")
        return stdev(operands)