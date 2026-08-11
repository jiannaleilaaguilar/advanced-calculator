from typing import List
from app.calculation import Calculation

class Memento:
    """Stores a snapshot of calculation history."""
    def __init__(self, history: List[Calculation]):
        self._state = list(history)

    def get_state(self) -> List[Calculation]:
        return list(self._state)

class HistoryCaretaker:
    """Manages undo and redo stacks using Mementos."""
    def __init__(self):
        self._undo_stack: List[Memento] = []
        self._redo_stack: List[Memento] = []

    def save_state(self, current_history: List[Calculation]):
        self._undo_stack.append(Memento(current_history))
        self._redo_stack.clear()

    def undo(self, current_history: List[Calculation]) -> List[Calculation]:
        if not self._undo_stack:
            return current_history
        self._redo_stack.append(Memento(current_history))
        return self._undo_stack.pop().get_state()

    def redo(self, current_history: List[Calculation]) -> List[Calculation]:
        if not self._redo_stack:
            return current_history
        self._undo_stack.append(Memento(current_history))
        return self._redo_stack.pop().get_state()
