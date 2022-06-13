from pathlib import Path

CONFIG_FILE = Path('./config/sources/config.yml').resolve()
DEFAULT_CONFIG_FILE = Path('./config/sources/config-local.yml').resolve()

__CRITICAL_LOG_FILE = Path('./logs').resolve()
__CRITICAL_LOG_FILE.mkdir(parents=True, exist_ok=True)
__CRITICAL_LOG_FILE = __CRITICAL_LOG_FILE / Path('critical.log')
__CRITICAL_LOG_FILE.touch(exist_ok=True)

CRITICAL_LOG_FILE = __CRITICAL_LOG_FILE
