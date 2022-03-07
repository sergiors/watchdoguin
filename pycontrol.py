#!/usr/bin/python3

import RPi.GPIO as GPIO
import click
import time

power_pin = 40
reset_pin = 38


@click.group()
@click.pass_context
def cli(ctx):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(power_pin, GPIO.OUT)
    GPIO.setup(reset_pin, GPIO.OUT)
    GPIO.output(power_pin, GPIO.HIGH)
    GPIO.output(reset_pin, GPIO.HIGH)

    ctx.call_on_close(_on_close)


def _on_close():
    GPIO.cleanup()


@cli.command()
def power(**kwargs):
    GPIO.output(power_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(power_pin, GPIO.HIGH)


@cli.command()
def reset(**kwargs):
    GPIO.output(reset_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(reset_pin, GPIO.HIGH)


if __name__ == '__main__':
    cli()
