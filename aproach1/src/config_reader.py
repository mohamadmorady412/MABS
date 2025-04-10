import yaml
from pathlib import Path
from logger import get_logger

log = get_logger(__name__)

CONFIG_FILE_PATH = Path("../config/config.yaml")

def load_config(config_file: Path = CONFIG_FILE_PATH) -> dict:
    try:
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        log.info(f"پیکربندی با موفقیت از '{config_file}' بارگیری شد.")
        return config
    except FileNotFoundError:
        error_message = f"فایل پیکربندی در مسیر '{config_file}' یافت نشد."
        log.error(error_message)
        raise FileNotFoundError(error_message)
    except yaml.YAMLError as e:
        error_message = f"خطا در هنگام بارگیری فایل YAML '{config_file}': {e}"
        log.error(error_message)
        raise yaml.YAMLError(error_message)
    except Exception as e:
        error_message = f"یک خطای غیرمنتظره در هنگام بارگیری پیکربندی رخ داد: {e}"
        log.error(error_message)
        raise
