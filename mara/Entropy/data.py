from enum import Enum
from datetime import datetime, timedelta
class Data(Enum):
    DATE = datetime.now()
    BUDGET = int
    DAILY_SPEND = int
    RESET = DATE - timedelta(days=7)
    TIME_STAMP = datetime.now().strftime("%Y-%m-%d")
    

