import logging

from database.neo4jdb import Neo4jDB
from paper2node.paper_reader import read_paper
from paper2node.paper_parser import parse_paper


logger = logging.getLogger("APP")


# 将论文处理后存储到Neo4j数据库中
def transform_paper_to_node(path):
    logger.info("读取单个论文文件pdf中...")
    paper_obj = read_paper(path)
    title, authors, path, abstract, content = paper_obj.get_all_values()
    keywords = parse_paper(paper_obj.abstract)

    logger.info("读取到的论文如下: ")
    logger.info("标题: {}".format(title))
    logger.info("作者: {}".format(authors))
    logger.info("文件路径: {}".format(path))
    logger.info("摘要: {}".format(abstract))
    logger.info("全文: {}".format(content))

    Neo4jDB.execute_create_paper_node(paper_obj)
    logger.info("创建论文节点 {} 成功".format(paper_obj.title))
    for keyword in keywords:
        Neo4jDB.execute_create_theme_node(keyword)
        logger.info("创建主题节点 {} 成功".format(keyword))
        Neo4jDB.execute_create_paper2theme_edge(paper_obj.title, keyword)
        logger.info("创建论文-节点边 {} 成功".format(paper_obj.title, keyword))







