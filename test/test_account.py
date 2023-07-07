import pytest


@pytest.mark.django_db
class TestAccount:
    fields = {'id', 'username', 'email'}

    def test_login(self, client, users):
        user = users[0]
        user.set_password('123456')
        user.save()

        url = '/api/auth/login'
        data = {
            'username': user.username,
            'password': '123456'
        }
        resp = client.post(url, data=data)
        assert resp.status_code == 200
        assert resp.json().get('username') == user.username
        assert 'access_token' in resp.json().keys()

    def test_logout(self, client, users):
        user = users[0]
        user.set_password('123456')
        user.save()
        client.force_authenticate(user=user)

        url = '/api/auth/logout'
        resp = client.delete(url)
        assert resp.status_code == 204

    def test_show_profile(self, client, users):
        user = users[0]
        client.force_authenticate(user=user)

        url = '/api/profile'
        resp = client.get(url)
        assert resp.status_code == 200
        assert resp.json().get('username') == user.username

    def test_update_profile(self, client, users):
        user = users[0]
        client.force_authenticate(user=user)

        url = '/api/profile'
        data = {
            'username': 'hhbbee',
            'email': 'ss@bb.com'
        }
        resp = client.patch(url, data=data)
        assert resp.status_code == 200
        assert resp.json().get('username') == data['username']
        assert resp.json().get('email') == data['email']

    def test_update_profile_fail(self, client, users):
        user = users[0]
        client.force_authenticate(user=user)

        url = '/api/profile'
        data = {
            'username': users[-1].username,
            'email': 'ss@ee.com'
        }
        resp = client.patch(url, data=data)
        assert resp.status_code == 400

    def test_list_user(self, client, users):
        user = users[0]
        client.force_authenticate(user=user)

        url = '/api/users'
        resp = client.get(url)
        assert resp.status_code == 200
        assert set(resp.json()['results'][0].keys()) == self.fields

    def test_show_user(self, client, users):
        sample = users[-1]
        user = users[0]
        client.force_authenticate(user=user)

        url = f'/api/users/{sample.id}'
        resp = client.get(url)
        assert resp.status_code == 200
        assert set(resp.json().keys()) == self.fields

    def test_login_failed(self, client, users):
        client.logout()
        user = users[0]
        user.set_password('123456')
        user.save()

        url = '/api/auth/login'
        data = {
            'username': user.username,
            'password': '88888'
        }
        resp = client.post(url, data=data)
        assert resp.status_code == 400

    def test_anonymous_show_profile(self, client):
        client.logout()

        url = '/api/profile'
        resp = client.get(url)
        assert resp.status_code == 401
