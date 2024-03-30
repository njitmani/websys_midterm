from .HistoryManager import HistoryManager


class HistoryFacade:
    def __init__(self):
        """
        Initializes the object with a new instance of HistoryManager for managing history.
        """
        self.history_manager = HistoryManager()

    def add_operation(self, operation, operands, result):
        """
        Adds an operation to the history manager.

        Args:
            operation (str): The name of the operation.
            operands (list): The operands used in the operation.
            result (any): The result of the operation.

        Returns:
            None
        """
        self.history_manager.add_entry(operation, operands, result)

    def show_history(self):
        """
        Method to show the history using the history manager.
        """
        self.history_manager.print_history()

    def clear_operations_history(self):
        self.history_manager.clear_history()

    def delete_history(self):
        """
        Deletes the history file using the history manager.
        """
        self.history_manager.delete_history_file()