import re

def normalize_name(name: str) -> str:
    name = name.upper().strip()
    name = re.sub(r"\s+OT$", "", name)
    return re.sub(r"\s+", "_", name)

