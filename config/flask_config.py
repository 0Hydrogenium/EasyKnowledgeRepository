import os
import logging


class Config:
    APP_ID = os.environ.get("PM_APP_ID")  # 接口用
    APP_SECRET = os.environ.get("PM_APP_SECRET")  # 接口用
    SECRET_KEY = "3bfab48fc27316dd59f4b963e9087ea57b0a27c9d19b7dd7"  # Flask用
    LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(threadName)s:%(name)s - %(message)s"
    LOGGING_FILE = "./logs/app.log"
    TASK_FILE_FOLDER = "./logs/history"
    ACCESS_TOKEN_URL = os.environ.get("PM_ACCESS_TOKEN_URL")
    SAVE_INFO_URL = os.environ.get("PM_SAVE_INFO_URL")
    GET_DYNAMIC_FORMULA_URL = os.environ.get("PM_GET_DYNAMIC_FORMULA_URL")
    GET_CORPORA_URL = os.environ.get("PM_GET_CORPORA_URL")
    # LLH_0130:
    GET_CORPORA_CLASS_URL = os.environ.get("PM_GET_CORPORA_CLASS_URL")
    ALLOW_USE_LOCAL_CORPORA_AS_FALLBACK = os.environ.get("PM_ALLOW_USE_LOCAL_CORPORA_AS_FALLBACK")
    MAX_CONVERSION_TIME = os.environ.get("PM_MAX_CONVERSION_TIME")
    PORT = os.environ.get("FLASK_RUN_PORT")
    HOST = "0.0.0.0"
    JSON_AS_ASCII = False


class ProductionConfig(Config):
    LOGGING_LEVEL = logging.DEBUG
    DEBUG = False
    pass