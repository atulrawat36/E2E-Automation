import pytest
from playwright.sync_api import APIRequestContext

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_context(playwright):
    return playwright.request.new_context(base_url=BASE_URL)


def test_get_posts(api_context: APIRequestContext):
    response = api_context.get("/posts")

    assert response.status == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100

    for post in data:
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)
        assert isinstance(post["userId"], int)


def test_get_post_by_id(api_context: APIRequestContext):
    response = api_context.get("/posts/1")

    assert response.status == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_get_post_invalid(api_context: APIRequestContext):
    response = api_context.get("/posts/9999")

    assert response.status == 404


def test_create_post(api_context: APIRequestContext):
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = api_context.post("/posts", data=payload)

    assert response.status == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post(api_context: APIRequestContext):
    payload = {
        "id": 1,
        "title": "updated",
        "body": "updated body",
        "userId": 1
    }

    response = api_context.put("/posts/1", data=payload)

    assert response.status == 200

    data = response.json()
    assert data["title"] == "updated"
    assert data["body"] == "updated body"


def test_delete_post(api_context: APIRequestContext):
    response = api_context.delete("/posts/1")

    assert response.status == 200
    assert response.text() == "{}"


def test_user_posts_filter(api_context: APIRequestContext):
    user_id = 1

    response = api_context.get(f"/users/{user_id}/posts")

    assert response.status == 200

    data = response.json()
    assert isinstance(data, list)

    for post in data:
        assert post["userId"] == user_id