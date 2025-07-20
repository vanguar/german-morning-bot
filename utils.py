from datetime import datetime

def utc_date_str():
    return datetime.utcnow().strftime("%Y-%m-%d")
