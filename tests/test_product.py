from tests.factories import ProductFactory, UserFactory
from src.documents import Product

def test_product_create():

    productFactory = ProductFactory.build()
    user = UserFactory.create()

    product = Product(name=productFactory.name, user=user.id)
    product.save()

    new_product = [product.to_json() for product in Product.scan()]

    assert Product.count() == 1
    assert new_product[0]["name"] == productFactory.name
    assert new_product[0]["user"] == user.id

def test_product(add_product):

    product = add_product()

    new_product = Product.get(product.id)

    assert new_product.name == product.name
    assert new_product.user == product.user

def test_products(add_product):

    quantity = 10

    for _ in range(0, quantity):
        add_product()

    assert Product.count() == quantity

def test_product_update(add_product):

    product = add_product()

    new_product = Product.get(product.id)

    new_product.name = "admin@example.com"
    new_product.save()

    assert [product.to_json() for product in Product.scan()][0]["name"] == "admin@example.com"

def test_product_delete(add_product):

    product = add_product()

    new_product = Product.get(product.id)

    assert Product.count() == 1

    new_product.delete()

    assert Product.count() == 0

def test_products_paginate(add_product):

    quantity = 26

    for _ in range(0, quantity):
        add_product()

    page_1 = Product.scan(limit=10)

    page_1_products = [x for x in page_1]

    assert len(page_1_products) == 10

    page_2 = Product.scan(limit=10, last_evaluated_key=page_1.last_evaluated_key)

    page_2_products = [x for x in page_2]

    assert len(page_2_products) == 10

    page_3 = Product.scan(limit=10, last_evaluated_key=page_2.last_evaluated_key)

    [x for x in page_3]

    assert page_3.total_count == 6

    assert page_3.last_evaluated_key == None


def test_products_by_user(add_product):

    quantity = 10

    user = UserFactory.create()

    for _ in range(0, quantity):
        add_product(user=user.id)

    for _ in range(0, quantity):
        add_product()

    assert Product.count() == quantity * 2

    products_by_user = [product for product in Product.user_index.query(user.id)]

    assert len(products_by_user) == quantity
