from sqlite3 import Connection, connect, Row
from typing import List

from backend.beans.product import Product
from backend.converters.converter import Converter
from backend.utils.constants import (
    DatabaseConstants,
    SQLQueries
)


class DatabaseService:
    """
    Service responsible to handle the database operations.
    """

    @staticmethod
    def get_db_connection() -> Connection:
        """
        Gets the sqlite3 database connection.
        """
        conn = connect(f'{DatabaseConstants.NAME}.db')
        conn.row_factory = Row
        return conn

    @staticmethod
    def get_all_products() -> List[Product]:
        """
        Gets all products from the database.
        """
        conn = DatabaseService.get_db_connection()

        cursor = conn.cursor()
        cursor.execute(SQLQueries.GET_ALL)
        products = cursor.fetchall()

        conn.close()

        products = Converter.convert_products_from_sqlite(products)

        return products

    @staticmethod
    def add_product(name: str, price: float) -> bool:
        """
        Adds a product to the database.
        """
        conn = DatabaseService.get_db_connection()
        added = True

        try:
            conn.execute(SQLQueries.INSERT_PRODUCT, (name, price))
            conn.commit()
            conn.close()
        except Exception:
            added = False

        return added
