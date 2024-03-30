from App.utils.wrapper import wrapper
from ..strategies.base_strategy import OperationStrategy
from math import log


class Log(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        Executes the log operation with the given operands.

        Parameters:
            *operands (any): The operands to be used in the log operation.

        Returns:
            any: The result of the log operation.

        Raises:
            ValueError: If the number of operands is not either 1 or 2.

        """
        if len(operands) not in [1, 2]:
            return "Error: log operation requires one or two operands."
        if len(operands) == 1:
            return log(operands[0])
        else:
            return log(operands[0], operands[1])