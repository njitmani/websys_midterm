# Advanced Calculator App

The Advanced Calculator App is a sophisticated Python application designed for performing a variety of mathematical operations. It encompasses basic arithmetic, statistical analysis, and extends functionality through dynamically loaded plugins. This document outlines the setup, usage, and development details of the calculator app.

## Features

- **Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Statistical Operations**: Calculate mean, median, and standard deviation.
- **History Management**: Tracks the history of calculations with options to view, save, clear, or delete.
- **Plugin System**: Extend functionality with additional operations via plugins.
- **Configuration via Environment Variables**: Customize behavior using environment variables.

## Setup and Installation

### Prerequisites

- Python 3.8 or newer
- Pip for package management

### Installation

1. **Clone the Repository**:
   Clone the project to your local machine using `git clone <repository_url>`, then navigate into the project directory.

2. **Virtual Environment**:
   Create a virtual environment for project dependencies:
   - **Windows**: `python -m venv env` then `.\env\Scripts\activate`
   - **macOS/Linux**: `python3 -m venv env` then `source env/bin/activate`

3. **Install Dependencies**:
   Install required Python packages with `pip install -r requirements.txt`.

4. **Environment Configuration**:
   Create a `.env` file in the project root to specify configurations such as `LOG_LEVEL` and `HISTORY_SAVE_PATH`. Refer to the Environment Variables section for more details.

## Usage

Run the calculator application via the command line:

```bash
python main.py
```

Follow the CLI prompts to perform calculations, manage history, or utilize plugins.

For example, if you are adding operands, do:

```
add <operand1> <operand2> [<operand3> ...]
```

Certain operations like `log` and `square` require only one operand.

## Supported Operations

- **Basic Arithmetic**: `add`, `subtract`, `multiply`, `divide`
- **Statistical Calculations**: `mean`, `median`, `stddev`
- **History Commands**: `view history`, `clear history`, `delete history`

## History Management

The `HistoryManager` class provides functionalities to manage calculation history, stored in `history.csv` within the `data` folder. Ensure the directory and file exist or are creatable by the application.

## Logging
All operations performed in the app create a log in the `operations.log` in the `logs` directory.

## Plugin System

Extend the app's capabilities by adding plugins in the `plugins` directory. Plugins must implement the `OperationStrategy` interface.

## Environment Variables

Configure the application behavior using the following environment variables in your `.env` file:

- `LOG_LEVEL`: Sets the logging level (e.g., `INFO`, `DEBUG`).
- `HISTORY_SAVE_PATH`: Specifies the path for saving the history file.
- `ENABLE_HISTORY_FEATURE`: Enables or disables history management (`True` or `False`).

## Development

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.