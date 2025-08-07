from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root_deve_retornar_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: arrange (organizar)
    - A: act (agir)
    - A: assert (afirmar)
    - teardown (seria a 4th etapada de um teste)
    :return:
    """
    # # arrange
    # client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': 'Ola mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@exemple.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@exemple.com',
            'password': 'segredo',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@exemple.com',
        'id': 1,
    }


def test_update_user_problem(client, user):
    response = client.put(
        '/users/2',
        json={
            'username': 'bob',
            'email': 'bob@exemple.com',
            'password': 'segredo',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() != {
        'username': 'bob',
        'email': 'bob@exemple.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
