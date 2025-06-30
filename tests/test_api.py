from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: arrange (organizar)
    - A: act (agir)
    - A: assert (afirmar)
    - teardown (seria a 4th etapada de um teste)
    :return:
    """
    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': "Ola mundo!"}
    assert response.status_code == HTTPStatus.OK
