from App.utils.wrapper import wrapper
from ..strategies.base_strategy import OperationStrategy

class Square(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        if len(operands) != 1:
            raise ValueError("Square plugin requires exactly 1 operand")
        return operands[0] ** 2