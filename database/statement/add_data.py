from database.static import *


# 创建 论文->主题 边
def create_paper2theme_edge(g, paper, theme):
    cypher_str = "MATCH (p:{}) WHERE p.title = '{}' MATCH (t:{}) WHERE t.value = '{}' CREATE (p)-[:{}]->(t)"
    cypher = cypher_str.format(NodeName.EntityPaper, paper, NodeName.EntityTheme, theme, EdgeName.Paper2Theme)

    return g.run(cypher)


# 创建新的主题节点
def create_theme_node(g, theme):
    cypher_str = "CREATE (e:{}) SET e.value = '{}'"
    cypher = cypher_str.format(NodeName.EntityTheme, theme)

    return g.run(cypher)


# 创建新的论文节点
def create_paper_node(g, title, authors, path, abstract, content):
    cypher_str = "CREATE (e:{}) SET e.title = '{}', e.authors = '{}', e.path = '{}', e.abstract = '{}', e.content = '{}'"
    cypher = cypher_str.format(NodeName.EntityPaper, title.replace("'", "#"), str(authors).replace("'", "#"), path.replace("'", "#"), abstract.replace("'", "#"), content.replace("'", "#"))

    return g.run(cypher)


# 智能创建 节点-边-节点
def intelligent_create_node_edge_node(g, node1_id, node2_id, node1_value, node2_value, has_edge, node_type, edge_type):
    if has_edge:
        return
    else:
        cypher = "CREATE (e1)-[:{}]->(e2)".format(edge_type)

    if node1_id != None and node2_id != None:
        cypher = "MATCH (e1) WHERE e1:{0} and e1.value = '{1}' MATCH (e2) WHERE e2:{0} and e2.value = '{2}' ".format(node_type, node1_value, node2_value) + cypher
    elif node1_id != None:
        cypher = "MATCH (e1) WHERE e1:{} and e1.value = '{}' ".format(node_type, node1_value) + cypher + " SET e2:{}, e2.value = '{}'".format(node_type, node2_value)
    elif node2_id != None:
        cypher = "MATCH (e2) WHERE e2:{} and e2.value = '{}' ".format(node_type, node2_value) + cypher + " SET e1:{}, e1.value = '{}'".format(node_type, node1_value)
    else:
        cypher = cypher + " SET e1:{0}, e1.value = '{1}', e2:{0}, e2.value = '{2}'".format(node_type, node1_value, node2_value)

    return g.run(cypher)