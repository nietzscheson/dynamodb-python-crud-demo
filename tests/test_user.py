from tests.factories import UserFactory
from src.documents import User

def test_user_create():

    userFactory = UserFactory.build()

    user = User(username=userFactory.username, email=userFactory.email)
    user.save()

    new_user = [user.to_json() for user in User.scan()]

    assert User.count() == 1
    assert new_user[0]["username"] == userFactory.username
    assert new_user[0]["email"] == userFactory.email

def test_user(add_user):

    user = add_user()

    new_user = User.get(user.id)

    assert new_user.username == user.username
    assert new_user.email == user.email

def test_users(add_user):

    quantity = 10

    for _ in range(0, quantity):
        add_user()

    users = [user.to_json() for user in User.scan()]

    assert len(users) == quantity

def test_user_update(add_user):

    user = add_user()

    new_user = User.get(user.id)

    new_user.email = "admin@example.com"
    new_user.save()

    assert [user.to_json() for user in User.scan()][0]["email"] == "admin@example.com"

def test_user_delete(add_user):

    user = add_user()

    new_user = User.get(user.id)

    assert User.count() == 1

    new_user.delete()

    assert User.count() == 0

def test_users_paginate_two_pages(add_user):

    quantity = 26

    for _ in range(0, quantity):
        add_user(email=f"0{_}@example.com")

    page_1 = User.scan(limit=25)

    page_1_users = [x for x in page_1]

    assert len(page_1_users) == 25

    page_2 = User.scan(limit=25, last_evaluated_key=page_1.last_evaluated_key)

    page_2_users = [x for x in page_2]

    assert len(page_2_users) == 1

    assert page_2.last_evaluated_key == None


def test_users_paginate_three_pages(add_user):

    quantity = 52

    for _ in range(0, quantity):
        add_user()

    page_1 = User.scan(limit=25, last_evaluated_key=None)

    [x for x in page_1]

    assert page_1.total_count == 25

    page_2 = User.scan(limit=25, last_evaluated_key=page_1.last_evaluated_key)

    [x for x in page_2]

    assert page_2.total_count == 25

    page_3 = User.scan(limit=25, last_evaluated_key=page_2.last_evaluated_key)

    [x for x in page_3]

    assert page_3.total_count == 2

    assert page_3.last_evaluated_key == None

