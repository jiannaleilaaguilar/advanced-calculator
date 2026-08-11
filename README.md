# Advanced Python Calculator Application
**NAME: Jianna Aguilar
**COURSE ID: IS218-450

An extensible, production-ready command-line calculator built with Python. Designed using core object-oriented principles and established software design patterns, this project features dynamic operation dynamic loading, interactive history tracking with undo/redo capabilities, customizable environmental settings, and automated logging.

---

## Key Features & Design Patterns

* **Factory Pattern (`app/operations.py`)**: Implements an `OperationFactory` to dynamically instantiate concrete calculation strategies (e.g., addition, subtraction, power, root, modulus) based on command input.
* **Memento Pattern (`app/calculator_memento.py`)**: Manages state snapshots (`Memento` and `HistoryCaretaker`) enabling robust, non-destructive `undo` and `redo` operations on calculation history.
* **Observer Pattern (`app/logger.py`)**: Decouples calculation events from side-effects. The `HistoryManager` notifies attached observers (`LoggingObserver` for execution logs and `AutoSaveObserver` for persistent CSV storage).
* **Facade Pattern (`app/calculator.py`)**: Provides a unified, high-level `Calculator` interface orchestrating input validation, operation execution, memento state management, and observer notifications.
* **REPL CLI**: Interactive terminal interface with color-coded feedback (`colorama`) for enhanced output formatting.

---

## Project Architecture

```text
advanced_calculator/
│
├── app/
│   ├── __init__.py
│   ├── calculation.py          # Data model for individual calculations
│   ├── calculator.py           # Facade orchestrator & REPL CLI entry point
│   ├── calculator_config.py    # Environment & app configuration
│   ├── calculator_memento.py   # Memento pattern implementation (Undo/Redo)
│   ├── exceptions.py          # Custom exception taxonomy
│   ├── history.py             # Calculation history & Subject in Observer pattern
│   ├── input_validators.py    # Sanitization & boundary checks
│   ├── logger.py              # Observer pattern implementations (Logging/Auto-Save)
│   └── operations.py          # Command strategy and OperationFactory
│
├── tests/
│   ├── test_calculator.py     # Integration tests for Facade & history
│   └── test_operations.py     # Unit tests for operations and factory
│
├── .env.example               # Template environment configuration file
├── .gitignore                 # Artifact exclusion rules
├── README.md                  # Project documentation
└── requirements.txt           # Project dependencies
