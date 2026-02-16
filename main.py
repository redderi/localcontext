
from src.app import App
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_format = logging.Formatter("%(levelname)s: %(message)s")
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)


def start_app():
    app = App()
    try:
        app.run()
    except Exception as e:
        logger.exception(f"Can't run app - {e}")

if __name__ == "__main__":
    start_app()