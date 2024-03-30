from statistics import mean, median, stdev
from App.strategies.base_strategy import OperationStrategy
from App.utils.wrapper import wrapper


class MeanOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        A function that executes a given operation on the provided operands and returns the result.
        
        Parameters:
            *operands (int or float): The operands on which the operation will be executed.
            
        Returns:
            float: The mean value of the operands.
        """
        self.validate_operands(*operands)
        return mean(operands)


class MedianOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        Executes the function by calculating the median of the given operands.

        Parameters:
            *operands (float): The operands to calculate the median from.

        Returns:
            float: The median value of the operands.

        Raises:
            ValueError: If the number of operands is not even.

        Example:
            >>> obj = MyClass()
            >>> obj.execute(1, 2, 3, 4, 5)
            3.0
        """
        self.validate_operands(*operands)
        return median(operands)


class StdDevOperation(OperationStrategy):
    @wrapper
    def execute(self, *operands):
        """
        Executes the function with the given operands and returns the standard deviation.

        Parameters:
            *operands: The operands to be used in the function.

        Returns:
            The standard deviation of the operands.

        Raises:
            ValueError: If there are less than two operands.

        """
        self.validate_operands(*operands)
        if len(operands) < 2:
            raise ValueError(
                "Standard deviation requires at least two operands.")
        return stdev(operands)