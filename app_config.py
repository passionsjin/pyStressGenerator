import os


class AppConfig:
    CPU_CORES = os.getenv('CPU_CORES', None)
    MEMORY = os.getenv('MEMORY', None)
    CPU_PERCENT = os.getenv('CPU_PERCENT', 90)


app_config = AppConfig()
