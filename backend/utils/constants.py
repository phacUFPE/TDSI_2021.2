class DatabaseConstants:
    NAME = 'database'
    SCHEMA_NAME = 'schema'
    TABLE_NAME = 'products'
    TYPE = 'sqlite'


class EnvironmentNameConstants:
    FAILURE_PORT = 'FAILURE_PORT'


class ErrorMessages:
    MISSING_OR_INVALID_FIELD = 'The field {0} is missing or is an invalid value.'
    SOMETHING_WRONG = 'Something went wrong. Please contact the administrator.'
    WRONG_METHOD = 'Wrong http method. Accepts only POST method'


class HttpMethods:
    GET = 'GET'
    POST = 'POST'


class HttpStatuses:
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500


class ProductFieldsConstants:
    ID = 'id'
    CREATED = 'created'
    NAME = 'name'
    PRICE = 'price'


class ResponseFieldsConstants:
    DATA = 'data'


class RouteConstants:
    HOME = '/'
    PRODUCTS = '/products'


class SuccessMessages:
    PRODUCT_ADDED_SUCCESSFULLY = 'Product added successfully!'


class SQLQueries:
    GET_ALL = f'SELECT * FROM {DatabaseConstants.TABLE_NAME}'
    INSERT_PRODUCT = (
        f'INSERT INTO {DatabaseConstants.TABLE_NAME} ({ProductFieldsConstants.NAME}, {ProductFieldsConstants.PRICE})'
        'VALUES (?, ?)'
    )
