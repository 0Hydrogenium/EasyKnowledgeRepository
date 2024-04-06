from database.neo4jdb import Neo4jDB


def branches_into_graph(branch_list, node_type, edge_type):
    for branch in branch_list:
        stack = branch

        pop1 = stack.pop()
        while len(stack) >= 1:
            pop2 = stack.pop()
            Neo4jDB.execute_intelligent_create_node_edge_node(pop2, pop1, node_type, edge_type)
            pop1 = pop2
