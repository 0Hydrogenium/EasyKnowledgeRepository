from database.neo4jdb import Neo4jDB


def get_all_nodes() -> list:
    neo4j_db = Neo4jDB()

    return neo4j_db.execute_query_node()
