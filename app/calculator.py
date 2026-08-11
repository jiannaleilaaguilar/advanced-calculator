from colorama import Fore, Style, init
from app.calculator_config import Config
from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import HistoryManager
from app.calculator_memento import HistoryCaretaker
from app.logger import LoggingObserver, AutoSaveObserver
from app.input_validators import validate_number
from app.exceptions import CalculatorError

init(autoreset=True)

def print_success(msg: str):
    print(f"{Fore.GREEN}{msg}{Style.RESET_ALL}")

def print_error(msg: str):
    print(f"{Fore.RED}Error: {msg}{Style.RESET_ALL}")

def print_info(msg: str):
    print(f"{Fore.CYAN}{msg}{Style.RESET_ALL}")

class Calculator:
    """Facade orchestrating History, Memento Caretaker, and Operation Factory."""
    def __init__(self):
        self.history_manager = HistoryManager()
        self.caretaker = HistoryCaretaker()
        
        # Register Observers
        self.history_manager.attach(LoggingObserver(Config.LOG_FILE))
        if Config.AUTO_SAVE:
            self.history_manager.attach(AutoSaveObserver(Config.HISTORY_FILE))

    def calculate(self, op_name: str, a_str: str, b_str: str) -> float:
        a = validate_number(a_str, Config.MAX_INPUT_VALUE)
        b = validate_number(b_str, Config.MAX_INPUT_VALUE)
        
        operation = OperationFactory.create(op_name)
        raw_result = operation.execute(a, b)
        result = round(raw_result, Config.PRECISION)
        
        # Save current state for undo functionality
        self.caretaker.save_state(self.history_manager.history)
        
        calc = Calculation(op_name, a, b, result)
        self.history_manager.add_calculation(calc)
        return result

    def undo(self):
        self.history_manager.history = self.caretaker.undo(self.history_manager.history)

    def redo(self):
        self.history_manager.history = self.caretaker.redo(self.history_manager.history)


def main():
    calc = Calculator()
    print_info("=" * 60)
    print_info(" Advanced Calculator Application Initialized ")
    print_info(" Type 'help' for available commands or 'exit' to quit. ")
    print_info("=" * 60)

    while True:  # pragma: no cover
        try:
            user_input = input(f"{Fore.YELLOW}calc> {Style.RESET_ALL}").strip().split()
            if not user_input:
                continue

            cmd = user_input[0].lower()

            if cmd == 'exit':
                print_info("Exiting application. Goodbye!")
                break
            elif cmd == 'help':
                print_info("\n--- Arithmetic Commands (Usage: <op> <a> <b>) ---")
                print_info("add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
                print_info("\n--- Management Commands ---")
                print_info("history  : Display calculation history")
                print_info("clear    : Clear current calculation history")
                print_info("undo     : Revert last calculation")
                print_info("redo     : Redo previously undone calculation")
                print_info("save     : Save history to CSV file")
                print_info("load     : Load history from CSV file")
                print_info("help     : Show this menu")
                print_info("exit     : Exit application\n")
            elif cmd == 'history':
                if not calc.history_manager.history:
                    print_info("Calculation history is empty.")
                else:
                    for idx, item in enumerate(calc.history_manager.history, 1):
                        print_info(f"{idx}. {item.operation}({item.a}, {item.b}) = {item.result} [{item.timestamp}]")
            elif cmd == 'clear':
                calc.caretaker.save_state(calc.history_manager.history)
                calc.history_manager.history.clear()
                print_success("Calculation history cleared.")
            elif cmd == 'undo':
                calc.undo()
                print_success("Undo operation performed.")
            elif cmd == 'redo':
                calc.redo()
                print_success("Redo operation performed.")
            elif cmd == 'save':
                calc.history_manager.save_to_csv(Config.HISTORY_FILE)
                print_success(f"History successfully saved to '{Config.HISTORY_FILE}'.")
            elif cmd == 'load':
                calc.history_manager.load_from_csv(Config.HISTORY_FILE)
                print_success(f"History successfully loaded from '{Config.HISTORY_FILE}'.")
            else:
                if len(user_input) != 3:
                    print_error("Invalid command structure. Format: <operation> <number1> <number2>")
                    continue
                res = calc.calculate(cmd, user_input[1], user_input[2])
                print_success(f"Result: {res}")

        except CalculatorError as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"Unexpected error occurred: {e}")

if __name__ == "__main__":  # pragma: no cover
    main()
