from loguru import logger
from config import system_config


if __name__ == '__main__':
    print(system_config)  # example
    logger.critical('some message')
