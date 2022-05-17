from backend.utils.constants import ProductFieldsConstants


class Product:
    """
    Class for product object representation.
    """
    def __init__(self, id: int, name: str, price: float, created: str):
        self.id = id
        self.name = name
        self.price = price
        self.created = created

    def __repr__(self) -> str:
        return f'<Product: {self.name} - {self.price} - {self.created}>'

    def to_object(self) -> object:
        """
        Returns the Product into a object.
        """
        return {
            f'{ProductFieldsConstants.ID}': self.id,
            f'{ProductFieldsConstants.NAME}': self.name,
            f'{ProductFieldsConstants.PRICE}': self.price,
            f'{ProductFieldsConstants.CREATED}': self.created
        }
