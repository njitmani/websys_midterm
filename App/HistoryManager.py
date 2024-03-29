import pandas as pd
import os
from .utils.config import HISTORY_SAVE_PATH

class HistoryManager:
    def __init__(self, filename=HISTORY_SAVE_PATH, directory='data'):
        """
        Constructor for initializing the OperationsHistory object.

        Parameters:
            filename (str): The name of the file for storing operations history. Defaults to 'operations_history.csv'.
            directory (str): The directory for storing the operations history file. Defaults to 'data'.

        Returns:
            None
        """
        self.directory = directory
        self.filename = filename
        self.filepath = os.path.join(self.directory, self.filename)
        
        # Ensure the directory exists
        os.makedirs(self.directory, exist_ok=True)

        # Load existing history if it exists
        if os.path.exists(self.filepath):
            # Load existing history from the file
            self.history_df = pd.read_csv(self.filepath)
        else:
            # Initialize an empty DataFrame if the file does not exist
            self.history_df = pd.DataFrame(columns=['Operation', 'Operands', 'Result'])

    def add_entry(self, operation, operands, result):
        """
        Adds a new entry to the history DataFrame.

        Parameters:
            operation (str): The operation performed.
            operands (list): The operands used in the operation.
            result (str): The result of the operation.

        Returns:
            None
        """
        new_entry = pd.DataFrame([[operation, operands, result]],
                                 columns=self.history_df.columns)
        # Prepare for concatenation by ensuring no all-NA columns; this step may vary based on your needs
        new_entry.dropna(axis=1, how='all', inplace=True)
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True).dropna(axis=1, how='all')
        self.save_history()

    def save_history(self):
        """
        Saves the history data to a CSV file specified by `self.filepath`.

        This function converts the `self.history_df` DataFrame to a CSV file using the `to_csv` method.
        The `index` parameter is set to `False` to exclude the index column from the CSV file.

        Parameters:
            None

        Returns:
            None
        """
        self.history_df.to_csv(self.filepath, index=False)

    def print_history(self):
        """
        Method to print the history DataFrame. Prints 'Empty history.' if the DataFrame is empty.
        """
        if self.history_df.empty:
            print("Empty history.")
        else:
            print(self.history_df)

    def clear_history(self):
        """
            Clear the in-memory history.
        """
        self.history_df = pd.DataFrame(columns=['Operation', 'Operands', 'Result'])
        self.save_history()
        print("History cleared.")

    def delete_history_file(self):
        """Delete the history CSV file."""
        try:
            if os.path.exists(self.filepath):
                os.remove(self.filepath)
                print(f"History file '{self.filepath}' successfully deleted.")
            else:
                print("History file does not exist.")
        except Exception as e:
            print(f"Error deleting history file: {e}")