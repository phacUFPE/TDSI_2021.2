from sqlite3 import Row

from typing import List

from backend.beans.product import Product
from backend.utils.constants import ProductFieldsConstants


class Converter:
    """
    Class responsible for the conversion of the sqlite3 database values.
    """
    @staticmethod
    def convert_product_from_sqlite(row: Row) -> Product:
        """
        Converts a given sqlite3 row into a Product object.
        """
        return Product(
            id=row[ProductFieldsConstants.ID],
            name=row[ProductFieldsConstants.NAME],
            price=row[ProductFieldsConstants.PRICE],
            created=row[ProductFieldsConstants.CREATED]
        )

    @staticmethod
    def convert_products_from_sqlite(rows: List[Row]) -> List[Product]:
        """
        Converts a list of sqlite3 rows into a list of Product objects.
        """
        products = []
        for row in rows:
            product = Converter.convert_product_from_sqlite(row)
            products.append(product)

        return products
