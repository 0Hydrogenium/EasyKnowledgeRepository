from database.static import NodeName, EdgeName
from function.branches_into_graph import branches_into_graph
from mindmap2node.mindmap_reader import read_mindmap


def load_mindmaps():
    path = "D:/我的/计算机网络.xmind"

    knowledge_path_list = read_mindmap(path)

    branches_into_graph(knowledge_path_list, NodeName.EntityKnowledge, EdgeName.Knowledge2Knowledge)


if __name__ == '__main__':
    load_mindmaps()
