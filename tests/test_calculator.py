import os
import pytest
from app.calculator import Calculator, print_success, print_error, print_info
from app.exceptions import ValidationError
from app.calculator_config import Config
from app.logger import Observer
from app.calculation import Calculation

@pytest.fixture
def calc():
    c = Calculator()
    c.history_manager.history.clear()
    return c

def test_print_helpers(capsys):
    print_success("Success message")
    print_error("Error message")
    print_info("Info message")
    captured = capsys.readouterr()
    assert "Success message" in captured.out
    assert "Error message" in captured.out
    assert "Info message" in captured.out

def test_calculator_execution(calc):
    res = calc.calculate('add', '10', '5')
    assert res == 15.0
    assert len(calc.history_manager.history) == 1

def test_validation_errors(calc):
    with pytest.raises(ValidationError):
        calc.calculate('add', 'invalid', '5')
    with pytest.raises(ValidationError):
        calc.calculate('add', '1e10', '5')

def test_undo_redo_full_and_empty_branches(calc):
    assert calc.caretaker.undo([]) == []
    assert calc.caretaker.redo([]) == []

    calc.calculate('add', '2', '3')
    calc.calculate('multiply', '4', '2')
    assert len(calc.history_manager.history) == 2

    calc.undo()
    assert len(calc.history_manager.history) == 1
    assert calc.history_manager.history[0].operation == 'add'

    calc.redo()
    assert len(calc.history_manager.history) == 2
    assert calc.history_manager.history[1].operation == 'multiply'

def test_save_and_load_csv(calc, tmp_path):
    test_file = os.path.join(tmp_path, "test_history.csv")
    calc.calculate('power', '2', '3')
    
    calc.history_manager.save_to_csv(test_file)
    assert os.path.exists(test_file)

    calc.history_manager.history.clear()
    assert len(calc.history_manager.history) == 0

    calc.history_manager.load_from_csv(test_file)
    assert len(calc.history_manager.history) == 1
    assert calc.history_manager.history[0].operation == 'power'

def test_load_nonexistent_csv(calc):
    with pytest.raises(FileNotFoundError):
        calc.history_manager.load_from_csv("non_existent_file.csv")

def test_abstract_observer():
    class DummyObserver(Observer):
        def update(self, calculation: Calculation):
            pass
    obs = DummyObserver()
    obs.update(Calculation('add', 1, 2, 3))
