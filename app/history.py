import os
import pandas as pd
from typing import List
from app.calculation import Calculation
from app.logger import Observer

class HistoryManager:
    def __init__(self):
        self.history: List[Calculation] = []
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def add_calculation(self, calc: Calculation):
        self.history.append(calc)
        self._notify(calc)

    def _notify(self, calc: Calculation):
        for observer in self._observers:
            observer.update(calc)

    def save_to_csv(self, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data = [c.to_dict() for c in self.history]
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)

    def load_from_csv(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"History file '{file_path}' not found.")
        df = pd.read_csv(file_path)
        self.history.clear()
        for _, row in df.iterrows():
            calc = Calculation(row['operation'], float(row['a']), float(row['b']), float(row['result']))
            calc.timestamp = str(row['timestamp'])
            self.history.append(calc)
