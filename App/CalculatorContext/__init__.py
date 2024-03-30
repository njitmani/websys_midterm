class CalculatorContext:
    def __init__(self, strategy, history):
        """
        Initializes a new instance of the class.

        Args:
            strategy (str): The strategy to be used.
            history (list): The history of the instance.

        Returns:
            None
        """
        self._strategy = strategy
        self.history = history

    def execute_operation(self, *operands):
        """
        Execute the operation using the provided strategy
        """
        # Execute the operation using the provided strategy
        result = self._strategy.execute(*operands)

        # Prepare details for history logging
        operation_name = self._strategy.__class__.__name__

        # Add an entry to the history log
        # Adjusted to match the updated add_operation method signature
        if self.history is not None:
            self.history.add_operation(operation_name, operands, result)

        return result