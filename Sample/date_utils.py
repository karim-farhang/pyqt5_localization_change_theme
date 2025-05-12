from datetime import datetime
import jdatetime
from hijri_converter import Gregorian

def get_gregorian_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_jalali_date():
    return jdatetime.date.today().strftime('%Y-%m-%d')

def get_hijri_date():
    today = datetime.now()
    hijri = Gregorian(today.year, today.month, today.day).to_hijri()
    return f"{hijri.year}-{hijri.month:02d}-{hijri.day:02d}"
