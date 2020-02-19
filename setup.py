from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
KEYSPACE = "playersessionservicekey"

session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)

session.execute("use playersessionservicekey")

session.set_keyspace(KEYSPACE)


session.execute("""
        CREATE TABLE IF NOT EXISTS Playersessionservicetable (
            country text,
            event text,
            player_id text,
            session_id text,
            ts timestamp,
            PRIMARY KEY (player_id,session_id,ts)
        )
        """)

print("Setup is done...")
