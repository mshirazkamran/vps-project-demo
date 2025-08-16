from uvicorn.config import LOGGING_CONFIG
import logging.config


def setup_logging():
    config = LOGGING_CONFIG.copy()

    # add your application logger
    config["loggers"]["src"] = {
        "handlers": ["default"],  # reuse uvicorn's handler with colors
        "level": "INFO",
        "propagate": False,
    }

    logging.config.dictConfig(config)
