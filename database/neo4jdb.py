from neo4j import GraphDatabase
import logging

from database.statement.add_data import *
from database.statement.get_data import *
from paper2node.paper import Paper

# 初始化Neo4j图数据库驱动器
NEO4J_DB_DRIVER = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))

logger = logging.getLogger("APP")


# Neo4j数据库类
class Neo4jDB:
    driver = NEO4J_DB_DRIVER

    @classmethod
    def is_activated(cls):
        return False if cls.driver.verify_connectivity() else True

    @classmethod
    def execute_query_node(cls) -> list:
        if cls.is_activated():
            return cls.driver.session().execute_read(query_node)

    @classmethod
    def execute_create_paper2theme_edge(cls, paper, theme):
        if cls.is_activated():
            cls.driver.session().execute_write(create_paper2theme_edge, paper, theme)

    @classmethod
    def execute_create_theme_node(cls, theme: str):
        if cls.is_activated():
            cls.driver.session().execute_write(create_theme_node, theme)

    @classmethod
    def execute_create_paper_node(cls, paper_obj):
        title, authors, path, abstract, content = paper_obj.get_all_values()

        if cls.is_activated():
            cls.driver.session().execute_write(create_paper_node, title, authors, path, abstract, content)

    @classmethod
    def execute_search_text(cls, text):
        if cls.is_activated():
            neo4j_obj_list = cls.driver.session().execute_read(search_text, text)

            paper_obj_list = []
            for neo4j_obj in neo4j_obj_list:
                paper_obj = Paper()
                paper_obj.set_all_values(neo4j_obj["title"], neo4j_obj["authors"], neo4j_obj["path"],
                                         neo4j_obj["abstract"], neo4j_obj["content"])
                paper_obj_list.append(paper_obj)

    @classmethod
    def execute_intelligent_create_node_edge_node(cls, node_value1, node_value2, node_type, edge_type):
        if cls.is_activated():
            node1_id = cls.driver.session().execute_read(query_node_on_id, node_value1, node_type)
            node2_id = cls.driver.session().execute_read(query_node_on_id, node_value2, node_type)
            has_edge = cls.driver.session().execute_read(query_edge_on_id, node_value1, node_value2, node_type, edge_type)

            node1_id = node1_id[0] if node1_id else None
            node2_id = node2_id[0] if node2_id else None
            has_edge = bool(has_edge)

            cls.driver.session().execute_write(intelligent_create_node_edge_node, node1_id, node2_id, node_value1,
                                               node_value2, has_edge, node_type, edge_type)
