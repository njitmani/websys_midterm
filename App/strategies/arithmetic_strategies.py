from App.utils.wrapper import wrapper
from .base_strategy import OperationStrategy


class Addition(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        return sum(operands)
    
class Subtraction(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        result = operands[0]
        for operand in operands[1:]:
            result -= operand
        return result
    
class Multiplication(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        result = 1
        for operand in operands:
            result *= operand
        return result

class Division(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        self.validate_operands(*operands)
        operand1, operand2 = operands
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return operand1 / operand2