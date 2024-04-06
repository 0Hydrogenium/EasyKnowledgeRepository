from database.neo4jdb import Neo4jDB
from database.static import NodeName, EdgeName
from function.branches_into_graph import branches_into_graph
from paper2node.paper_parser import LLMModel


def generate_theme_tree(root_theme: str):
    theme_list = LLMModel().generate_theme_tree(root_theme)

    branches_into_graph(theme_list, NodeName.EntityTheme, EdgeName.Theme2Theme)

