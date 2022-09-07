import os


class AppConfig:
    CPU_CORES = os.getenv('CPU_CORES', None)
    MEMORY_MB = os.getenv('MEMORY_MB', None)
    CPU_PERCENT = os.getenv('CPU_PERCENT', 90)


app_config = AppConfig()
