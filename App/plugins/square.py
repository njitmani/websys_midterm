from App.utils.wrapper import wrapper
from ..strategies.base_strategy import OperationStrategy


class Square(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        Executes the square plugin by taking a single operand and returning its square.

        Parameters:
            *operands (Any): The operands to be squared.

        Raises:
            ValueError: If the number of operands is not equal to 1.

        Returns:
            Any: The square of the operand.
        """
        if len(operands) != 1:
            raise ValueError("Square plugin requires exactly 1 operand")
        return operands[0] ** 2