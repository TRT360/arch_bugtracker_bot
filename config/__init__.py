from loguru import logger

from config.configs import Configs
from config.consts import CRITICAL_LOG_FILE
from config.model import ParserConfig, SystemConfig, TelegramConfig

try:
    __configs = Configs()

    telegram_config: TelegramConfig = __configs.telegram_config
    system_config: SystemConfig = __configs.system_config
    parser_config: ParserConfig = __configs.parser_config

    logger.remove(0)
    for log_conf in __configs.logging_configs:
        logger.add(sink=log_conf.sink, format=log_conf.format_, level=log_conf.level)

except Exception as err:
    with open(CRITICAL_LOG_FILE, 'a') as err_out:
        err_out.write(f'Can\'t load config file: {err}\n')

    raise Exception('Can\'t load config file\n')
