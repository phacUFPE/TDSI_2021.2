import os
from urllib.parse import urlparse

from flask import Flask, Response, request
from flask_cors import CORS

from backend.scripts import init_db
from backend.services.database_service import DatabaseService
from backend.utils.constants import (
    EnvironmentNameConstants,
    ErrorMessages,
    HttpMethods,
    HttpStatuses,
    ProductFieldsConstants,
    ResponseFieldsConstants,
    RouteConstants,
    SuccessMessages
)
from backend.utils.functions import UtilFunctions


init_db()
app = Flask(__name__)
CORS(app)


@app.route(RouteConstants.PRODUCTS, methods=[HttpMethods.GET])
def get_products():
    """
    Returns response with all products.
    """
    products = DatabaseService.get_all_products()
    return {ResponseFieldsConstants.DATA: [product.to_object() for product in products]}


@app.route(RouteConstants.PRODUCTS, methods=[HttpMethods.POST])
def add_product():
    """
    Creates a product.
    * Returns 400 Bad Request and a error message with with missing fields.
    * Returns 500 Internal Server Error and a error message
    if something goes wrong with the database insertion.
    * Returns 200 OK and a success message if the product was inserted.
    """
    failure_port = int(os.getenv(EnvironmentNameConstants.FAILURE_PORT))
    url = urlparse(request.base_url)
    if url.port == failure_port:
        UtilFunctions.kill_processes_on_port(failure_port)

    response = Response(
        status=HttpStatuses.BAD_REQUEST,
        response=ErrorMessages.WRONG_METHOD
    )

    if request.method == HttpMethods.POST:
        name = request.json[ProductFieldsConstants.NAME]
        price = request.json[ProductFieldsConstants.PRICE]

        if not name:
            response = Response(
                status=HttpStatuses.BAD_REQUEST,
                response=ErrorMessages.MISSING_OR_INVALID_FIELD.format(ProductFieldsConstants.NAME)
            )
        elif not price or not UtilFunctions.isfloat(price) or float(price) < 0:
            response = Response(
                status=HttpStatuses.BAD_REQUEST,
                response=ErrorMessages.MISSING_OR_INVALID_FIELD.format(ProductFieldsConstants.PRICE)
            )
        else:
            added = DatabaseService.add_product(name, float(price))
            if added:
                response = Response(response=SuccessMessages.PRODUCT_ADDED_SUCCESSFULLY)
            else:
                response = Response(
                    status=HttpStatuses.INTERNAL_SERVER_ERROR,
                    response=ErrorMessages.SOMETHING_WRONG
                )

    return response


if __name__ == '__main__':
    app.run(debug=True)
