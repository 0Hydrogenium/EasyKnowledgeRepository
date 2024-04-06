import logging
import os.path


# 日志信息常量类
class LogInfo:
    # 日志级别
    level = logging.DEBUG
    # 日志输出格式
    format = "%(asctime)s - %(levelname)s - %(message)s"


# 初始化日志
def init_logger() -> logging.Logger:
    # 日志文件目录
    APP_LOG_PATH = "./log/app.log"

    # 如果app.log文件不存在，则创建
    if not os.path.exists(APP_LOG_PATH):
        with open(APP_LOG_PATH, "w"):
            pass

    # 配置日志基本信息
    logging.basicConfig(
        filename=APP_LOG_PATH,
        level=LogInfo.level,
        format=LogInfo.format
    )

    # 配置日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LogInfo.level)
    console_handler.setFormatter(logging.Formatter(LogInfo.format))

    # 初始化日志记录仪
    logger = logging.getLogger("APP")
    logger.addHandler(console_handler)

    return logger
