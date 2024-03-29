from App.utils.wrapper import wrapper
from ..strategies.base_strategy import OperationStrategy
from math import log

class Log(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        if len(operands) not in [1, 2]:
            return "Error: log operation requires one or two operands."
        if len(operands) == 1:
            return log(operands[0])
        else:
            return log(operands[0], operands[1])