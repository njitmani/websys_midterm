from functools import wraps
import logging
import os

# Set up logging to file
logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

# Configure logging
logger = logging.getLogger('CalculatorApp')
handler = logging.FileHandler(os.path.join(logs_dir, 'operations.log'))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def wrapper(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        """
        Decorator function that checks for exceptions and logs the result of the decorated function.

        Parameters:
            *args (Any): Variable length argument list.
            **kwargs (Any): Arbitrary keyword arguments.

        Returns:
            str: The result of the decorated function if no exceptions occur.
            str: An error message if a TypeError is caught.
            str: An error message if a ZeroDivisionError is caught.
            str: An error message if a ValueError is caught.
            str: An error message if any other exception is caught.

        Raises:
            None

        Notes:
            - This function uses the `wraps` decorator from the `functools` module to preserve the original function's name and docstring.
            - The function logs the name and arguments of the decorated function using the `logger.info` method.
            - If the decorated function raises a ZeroDivisionError, a ValueError, or any other exception, an error message is logged using the `logger.error` method.
            - The function returns the result of the decorated function if no exceptions occur.
            - If a TypeError is caught, the function returns the error message "Error: Invalid operands."
            - If a ZeroDivisionError is caught, the function returns the error message "Error: Cannot divide by zero."
            - If a ValueError is caught, the function returns the error message "Error: Invalid value."
            - If any other exception is caught, the function returns the error message "Error: An unexpected error occurred."
        """
        try:
            result = func(*args, **kwargs)
            logger.info(f"Performed {func.__name__}: {args[1:]} = {result}")
            return result
        except TypeError as e:
            logger.error(f"Type error in operation: {e}")
            return "Error: Invalid operands."
        except ZeroDivisionError as e:
            logger.error(f"Attempted to divide by zero: {e}")
            return "Error: Cannot divide by zero."
        except ValueError as e:
            logger.error(f"Value error in operation: {e}")
            return "Error: Invalid value." 
        except Exception as e:
            logger.error(f"Unexpected error in operation: {e}", exc_info=True)
            return "Error: An unexpected error occurred." 
    return wrapped_func