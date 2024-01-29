"""Database wrapper utility."""
import psycopg2


class Database:
    """
    Wrap connection to the database in a test context.

    TODO: Re-add adapter for SQLite.
    TODO: Add adapters for other databases.
    """

    def __init__(self, dsn: str):
        """Object constructor."""
        self.dsn = dsn
        self.conn = None
        self.connect()

    def connect(self):
        """Connect to database, optionally disconnecting when already connected."""
        if self.conn is not None:
            self.conn.close()
        self.conn = psycopg2.connect(self.dsn)
        self.conn.autocommit = True

    def execute(self, query):
        """Invoke an SQL statement."""
        cursor = self.conn.cursor()
        cursor.execute(query)
        return Result(cursor=cursor)

    def reset(self):
        """Clear database content, to provide each test case with a blank slide."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM content;")
        cursor.execute("DELETE FROM section;")
        cursor.execute("DELETE FROM document;")
        cursor.close()


class Result:
    """Wrap SQLAlchemy result object."""

    def __init__(self, cursor):
        """Object constructor."""
        self.cursor = cursor

    def fetchall(self):
        """Fetch all records, exhaustively."""
        return self.cursor.fetchall()

    def __del__(self):
        """When object is destroyed, also close the cursor."""
        self.cursor.close()
