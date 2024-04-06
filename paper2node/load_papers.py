import os
import logging

from paper2node.transform_paper_to_node import transform_paper_to_node


# 论文文件根目录
root_path = "./data"

logger = logging.getLogger("APP")


# 加载论文函数
def load_papers():
    logger.info("论文文件根目录: {}".format(root_path))

    # 递归读取文件根目录下的所有pdf文件
    def recursive_load_every_folder(path):
        for file in os.listdir(path):
            total_dir = path + "/" + file
            # 跳过中文翻译的pdf文件
            if file[-6:] == "zh.pdf":
                continue
            # 若当前目录为pdf，则将其路径添加到列表
            if file[-4:] == ".pdf":
                pdf_dir_list.append(total_dir)
                continue
            # 若当前目录为文件夹，则递归读取该文件夹下的所有文件
            recursive_load_every_folder(total_dir)

    pdf_dir_list = []
    recursive_load_every_folder(root_path)
    logger.info("读取到的论文文件: {}".format(pdf_dir_list))

    for dir in pdf_dir_list:
        logger.info("转换 {} 论文到图数据库节点中...".format(dir))
        transform_paper_to_node(dir)

