"""The main module that shows lazy initialization design pattern"""
from functools import cached_property

class _DatabaseEmulator():
    def connect(self) -> None:
        """Connect to the database"""
        print("### connecting to the db...")

    def execute(self, statement: str):
        """Execute the statement to the database"""
        print("### executing the db statement: " + statement)

class Database():
    """
    A database object that wraps a database.
    the database only gets initalized when an execution is made
    """

    @cached_property
    def my_db(self):
        """A Cashed property that is instatiated when called"""
        print("### instantiating the db emulator")
        this_db = _DatabaseEmulator()
        this_db.connect()
        print("### connected to the database")

        return this_db

    def execute(self, statement: str):
        """Execute a statement"""
        self.my_db.execute(statement)

def main() -> None:
    """The main function to show the design pattern"""
    print("instantiating the database...")
    my_database = Database()
    print("database is instantiated")

    print("# 1st statement")
    my_database.execute("1st statement")

    print("# 2nd statement")
    my_database.execute("2nd statement")

main()
