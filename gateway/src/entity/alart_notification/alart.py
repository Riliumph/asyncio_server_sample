from dataclasses import dataclass
from datetime import datetime

from util import alart_time


@dataclass
class Alart:
    severities = ["fatal", "error", "warning", "info"]

    _msg: str
    _severity: str
    _occurence_time: datetime

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, v: str):
        self._msg = v

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, v: str):
        if v not in self.severities:
            raise ValueError(f"{v}は認可されたレベルではありません")
        self._severity = v

    @property
    def occurence_time(self):
        return self._occurence_time

    @occurence_time.setter
    def ocurence_time(self, time_text: str):
        try:
            dt = datetime.fromisoformat(time_text)
            dt_text = dt.strftime(alart_time.displayed_format)
            self._occurence_time = dt_text
        except ValueError as e:
            raise e
