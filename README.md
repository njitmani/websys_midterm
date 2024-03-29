# Advanced Calculator Project

## Description

This Advanced Calculator is a Python-based application designed to perform a wide range of mathematical operations. It features a command-line interface (CLI) for easy interaction and supports basic arithmetic operations, statistical calculations, and dynamically loaded plugins for extended functionalities. The application also manages a calculation history, providing users with the ability to view, save, clear, and delete their calculation records.

## Features

- **Arithmetic Operations**: Perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
- **Statistical Operations**: Calculate mean, median, and standard deviation.
- **History Management**: Manage your calculation history with options to view, save, clear, or delete.
- **Plugin System**: Extend the calculator's functionality with dynamically loaded plugins.
- **Environment Configuration**: Configure application settings, including history feature toggling and logging levels, through environment variables.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Pip for installing dependencies

### Installation Steps

1. **Clone the Repository**

```
git clone https://github.com/njitmani/websys_midterm
cd websys_midterm
```


2. **Create and Activate a Virtual Environment**

- **Windows:**

  ```cmd
  python -m venv env
  .\env\Scripts\activate
  ```

- **macOS/Linux:**

  ```sh
  python3 -m venv env
  source env/bin/activate
  ```

3. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```


4. **Configure Environment Variables**

Create a `.env` file in the root directory of the project and define your configurations:

```
LOG_LEVEL=INFO
HISTORY_SAVE_PATH=data/history.csv
ENABLE_HISTORY_FEATURE=True
```


Remember to adjust the paths and values based on your environment.

## Usage

To start the calculator application, run:

```
python main.py
```


Follow the on-screen instructions to perform calculations or manage your calculation history.

## Supported Operations

- **Addition**: `add <number1> <number2> ...`
- **Subtraction**: `subtract <number1> <number2> ...`
- **Multiplication**: `multiply <number1> <number2> ...`
- **Division**: `divide <number1> <number2>`
- **Mean**: `mean <number1> <number2> ...`
- **Median**: `median <number1> <number2> ...`
- **Standard Deviation**: `stddev <number1> <number2> ...`
- **View History**: `view history`
- **Clear History**: `clear history`
- **Delete History**: `delete history`
- **Quit**: `quit`

Additional commands and plugins may be available depending on the dynamically loaded plugins.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to this project.

## License

[MIT License](./License)
