import multiprocessing
import signal
import sys
from time import sleep

import psutil

from app_config import app_config


def cpu_stress(core, percent):
    for _ in range(core):
        multiprocessing.Process(target=loop, args=(percent, )).start()


def loop(percent):
    while True:
        if psutil.cpu_percent(interval=None) > percent:
            sleep(0.05)
        9*9


def memory_stress(memory_byte):
    try:
        # Each element takes approx 8 bytes
        # Multiply n by 1024**2 to convert from MB to Bytes
        _ = [0] * int((memory_byte / 8))

        while True:
            # This is just to keep the process running until halted
            sleep(1)
    except MemoryError:
        # We didn't have enough RAM for our attempt, so we will recursively try
        # smaller amounts 10% smaller at a time
        memory_stress(int(memory_byte * 0.9))


def main():
    core = app_config.CPU_CORES
    memory_mb = app_config.MEMORY_MB
    percent = app_config.CPU_PERCENT

    if core is None:
        core = multiprocessing.cpu_count()
    if memory_mb is None:
        memory_mb = int(psutil.virtual_memory().total / (1024 ** 2))
    if percent is None:
        percent = 80

    signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))

    if core:
        multiprocessing.Process(target=cpu_stress,
                                args=(int(core), int(percent))).start()

    if memory_mb:
        memory_byte = int(memory_mb) * (1024 ** 2)
        memory_stress(memory_byte)