from flask import Flask, jsonify

from config.os_config import init_working_directory
from config.log_config import init_logger
from paper2node.load_papers import load_papers
from search.init import get_all_nodes
from theme2tree.generate_theme_tree import generate_theme_tree
from config import flask_config

app = Flask(__name__)

# 初始化全局根目录
init_working_directory()
# 初始化日志
logger = init_logger()


@app.get("/getNodes")
def get_nodes():
    output_list = get_all_nodes()
    output_json = {
        "nodes": output_list
    }

    return jsonify(output_json)


# 主程序
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)

    # logger.info("EasyPapers 程序已启动")
    # logger.info("加载论文中...")
    # load_papers()
    # logger.info("论文加载成功")

    # logger.info("加载主题树中...")
    # generate_theme_tree("Financial Quantification")
    # logger.info("主题树加载成功")
