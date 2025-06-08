from dataclasses import dataclass, field, fields
from datetime import datetime


@dataclass
class Alart:
    severities = ["fatal", "error", "warning", "info"]

    # dataclassが__init__/__repr__/__eq__などを作るために定義。
    # プロパティと名前が被せているので、属性はプロパティに上書きされる。
    # 内部でアクセスするときは必ず接頭辞に_を付けてアクセスすること。
    msg: str
    severity: str
    occurence_time: datetime

    @property
    def msg(self) -> str:
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
    def occurence_time(self) -> datetime:
        return self._occurence_time

    @occurence_time.setter
    def occurence_time(self, v: str):
        try:
            dt = datetime.fromisoformat(v)
            self._occurence_time = dt
        except ValueError as e:
            raise e
