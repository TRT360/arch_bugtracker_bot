from pathlib import Path
from typing import Any, Callable

import yaml
from pydantic import BaseSettings

from config.consts import CONFIG_FILE, CRITICAL_LOG_FILE, DEFAULT_CONFIG_FILE
from config.model import LoggingConfig, ParserConfig, SystemConfig, TelegramConfig


class Configs(BaseSettings):
    telegram_config: TelegramConfig
    system_config: SystemConfig
    parser_config: ParserConfig
    logging_configs: list[LoggingConfig]

    class Config:
        @classmethod
        def customise_sources(
            cls,
            init_settings: Callable,
            env_settings: Callable,
            file_secret_settings: Callable,
        ) -> tuple[Callable]:
            return (yaml_settings_source, )


def yaml_settings_source(config: BaseSettings) -> dict[str, Any]:
    config_source_data: dict[str, Any] = {}
    try:
        for source in (DEFAULT_CONFIG_FILE, CONFIG_FILE):
            if not (source := Path(source)).resolve().exists():
                continue

            with open(source, 'r') as file:
                if config_source_data := yaml.safe_load(file):
                    config_source_data['logging_configs']
                    return config_source_data

    except Exception as err:
        with open(CRITICAL_LOG_FILE, 'a') as err_out:
            info = f'Can\'t load config file: {err}\n'
            err_out.write(info)

    raise Exception('Can\'t load config file\n')
