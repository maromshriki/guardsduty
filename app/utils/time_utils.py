from datetime import time
import pandas as pd

def parse_time(value) -> time:
    """
    מקבל ערך מאקסל ומחזיר datetime.time תקני
    """
    if isinstance(value, time):
        return value

    if pd.isna(value):
        return None

    parsed = pd.to_datetime(value)
    return parsed.time()

