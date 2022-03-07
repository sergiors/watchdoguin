#!/usr/bin/python3

import logging
import time
import RPi.GPIO as GPIO

from ping import ping
from datetime import date, datetime
from pytz import timezone

reset_pin = 38

tz = timezone('America/Sao_Paulo')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(reset_pin, GPIO.OUT)

log_file = f'logs/{date.today()}.log'
logging.Formatter.converter = lambda *args: datetime.now(tz).timetuple()
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def hey_there():
    if ping('192.168.1.4', 22):
        logging.debug('rig okay')
        return

    logging.warning('rig is not working')

    GPIO.output(reset_pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(reset_pin, GPIO.HIGH)

    logging.info('rig restarted')


if __name__ == '__main__':
    hey_there()
    GPIO.cleanup()
