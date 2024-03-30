from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, *operands):
        """
        Executes the function with the given operands.

        Args:
            *operands: The operands to be passed to the function.

        Returns:
            None
        """
        pass

    def validate_operands(self, *operands):
        """
        Validate operands to ensure they are numeric (int or float).
        
        Parameters:
            *operands (numeric): The operands to be validated.
        
        Raises:
            ValueError: If any operand is not numeric.
        """
        # LBYL
        if not all(isinstance(op, (int, float)) for op in operands):
            raise ValueError("All operands must be numeric.")