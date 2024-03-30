import logging
from App.CalculatorContext import CalculatorContext
from App.HistoryManager import HistoryFacade as History
from App.strategies.statistical_strategies import MeanOperation, MedianOperation, StdDevOperation
from .strategies.arithmetic_strategies import Addition, Subtraction, Multiplication, Division
from .utils.plugin_loader import load_plugins
from .utils.config import ENABLE_HISTORY_FEATURE


class CalculatorApp:
    def __init__(self):
        """
        Initializes the class instance.

        :return: None
        """
        self.logger = logging.getLogger(__name__)
        if ENABLE_HISTORY_FEATURE:
            self.history = History()
        else:
            self.history = None
        self.strategies = {
            "add": Addition(),
            "subtract": Subtraction(),
            "multiply": Multiplication(),
            "divide": Division(),
            "mean": MeanOperation(),
            "median": MedianOperation(),
            "stddev": StdDevOperation(),
        }
        self.strategies.update(load_plugins())

    def display_menu(self):
        """
        Display the available commands for the calculator.

        This function prints a list of available commands that the user can use in the calculator. The commands include the names of the strategies that the calculator supports, as well as additional commands for viewing and manipulating the calculation history. The function also provides instructions on how to use the commands.

        Parameters:
        - self: The instance of the calculator class.

        Returns:
        - None
        """
        print("\nAvailable Commands:")
        for command in self.strategies.keys():
            print(f" - {command}")
        if ENABLE_HISTORY_FEATURE:
            print(" - view history: View calculation history")
            print(" - clear history: Clear the calculation history")
            print(" - delete history: Delete the calculation history CSV file.")
        print(" - help: Show this menu again")
        print(" - quit: Exit the calculator\n")
        print("Enter 'command operands' (e.g., 'add 1 2') to perform a calculation, or use one of the above commands.")

    def run(self):
        """
        Runs the Advanced Calculator app allowing the user to input commands to perform various operations.
        Handles user input, executes operations, displays results, and logs warnings or errors when necessary.
        """
        print("Welcome to the Advanced Calculator")
        self.display_menu()

        while True:
            try:
                """
                    Process the user input for the calculator application.

                    This code block takes user input and performs the corresponding
                    operation on the calculation or action based on the input.
                    It handles various commands such as "quit", "view history",
                    "clear history", "delete history", and "help".
                    It also handles error and exception scenarios gracefully.

                    Returns:
                        None
                """
                user_input = input("input>>> ").strip().lower()
                if user_input == "quit":
                    self.logger.info("Calculator app terminated.")
                    break
                elif user_input == "view history":
                    if ENABLE_HISTORY_FEATURE:
                        self.history.print_history()
                    else:
                        print("History feature is disabled.")
                elif user_input == "clear history":
                    if ENABLE_HISTORY_FEATURE:
                        self.history.clear_history()
                    else:
                        print("History feature is disabled.")
                elif user_input == "delete history":
                    if ENABLE_HISTORY_FEATURE:
                        self.history.delete_history_file()
                    else:
                        print("History feature is disabled.")
                elif user_input == "help":
                    self.display_menu()
                else:
                    parts = user_input.split()
                    command, operands_str = parts[0], parts[1:]

                    if command not in self.strategies:
                        print(
                            "Unknown command. Type 'help' to see available commands.")
                        continue

                    try:
                        operands = list(map(float, operands_str))
                    except ValueError:
                        print("Error: All operands must be numeric.")
                        continue

                    calculator = CalculatorContext(
                        self.strategies[command], self.history)
                    result = calculator.execute_operation(*operands)
                    print(f"Result -> {result}")

            except ValueError as ve:
                self.logger.warning(f"Operation warning: {ve}")
                print(f"Warning: {ve}")
            except Exception as e:
                self.logger.error(
                    f"Unexpected error occurred: {e}",
                    exc_info=True)
                print("An unexpected error occurred. Please try again.")