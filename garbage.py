# def test_read_unique_user(client):
#     response = client.get('/users/1')
#
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'alice',
#         'email': 'alice@exemple.com',
#         'id': 1,
#     }
#
# def test_read_unique_user_problem(client):
#     response = client.get('/users/2')
#
#     assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
#     assert response.json() != {
#         'username': 'alice',
#         'email': 'alice@exemple.com',
#         'id': 1,
#     }
