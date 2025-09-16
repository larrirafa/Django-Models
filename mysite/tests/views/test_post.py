import pytest


from django.urls import reverse


def test_post(client):
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200
    assert response.content  == b'Hello, world.'