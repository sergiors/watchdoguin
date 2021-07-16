import logging

from datetime import datetime
from settings import tz, log_level


logging.Formatter.converter = lambda *args: datetime.now(tz).timetuple()
logging.basicConfig(
    level=log_level,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging
