from App.utils.wrapper import wrapper
from ..strategies.base_strategy import OperationStrategy


class Power(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        A description of the entire function, its parameters, and its return types.
        """
        if len(operands) != 2:
            return "Error: power operation requires exactly two operands."
        base, exponent = operands
        return base ** exponent