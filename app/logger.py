from abc import ABC, abstractmethod
import os
import logging
import pandas as pd
from app.calculation import Calculation

class Observer(ABC):
    @abstractmethod
    def update(self, calculation: Calculation):
        pass

class LoggingObserver(Observer):
    def __init__(self, log_file: str):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("CalculatorLogger")

    def update(self, calculation: Calculation):
        self.logger.info(
            f"Operation: {calculation.operation} | Inputs: ({calculation.a}, {calculation.b}) | Result: {calculation.result}"
        )

class AutoSaveObserver(Observer):
    def __init__(self, file_path: str):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def update(self, calculation: Calculation):
        df = pd.DataFrame([calculation.to_dict()])
        header = not os.path.exists(self.file_path)
        df.to_csv(self.file_path, mode='a', header=header, index=False)
