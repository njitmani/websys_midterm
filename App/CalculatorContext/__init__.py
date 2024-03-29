from App.utils import logging

class CalculatorContext:
    def __init__(self, strategy, history_manager):
        self._strategy = strategy
        self.history_manager = history_manager

    def execute_operation(self, *operands):
        # Execute the operation using the provided strategy
        result = self._strategy.execute(*operands)
        
        # Prepare details for history logging
        operation_name = self._strategy.__class__.__name__
        
        # Add an entry to the history log
        # Adjusted to match the updated add_entry method signature
        if self.history_manager is not None:
            self.history_manager.add_entry(operation_name, operands, result)
        
        return result