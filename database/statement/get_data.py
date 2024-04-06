from database.static import *


# 获取所有节点
def query_node(g):
    cypher = "MATCH (e) RETURN e"

    return [x["e"]["value"] for x in g.run(cypher)]


# 查找文本
def search_text(g, text):
    cypher_str = "MATCH (e:{0}) WHERE e.value CONTAINS '{1}' RETURN e"
    cypher = cypher_str.format(NodeName.EntityKnowledge, text)

    return [x["e"] for x in g.run(cypher)]


# 查询单个节点的id
def query_node_on_id(g, value, node_type):
    cypher_str = "MATCH (e: {}) WHERE e.value = '{}' RETURN id(e) AS id"
    cypher = cypher_str.format(node_type, value)

    return [x["id"] for x in g.run(cypher)]


# 查询单个边的id
def query_edge_on_id(g, value1, value2, node_type, edge_type):
    cypher_str = "MATCH (e1: {0})-[r: {1}]->(e2: {0}) WHERE e1.value = '{2}' AND e2.value = '{3}' RETURN id(r) AS id"
    cypher = cypher_str.format(node_type, edge_type, value1, value2)

    return [x["id"] for x in g.run(cypher)]