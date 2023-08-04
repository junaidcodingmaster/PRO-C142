import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_article():
    response = requests.get(BASE_URL + "/get_article")
    return response.status_code

def test_like_article():
    response = requests.post(BASE_URL + "/like_article")
    return response.status_code

def test_not_like_article():
    response = requests.post(BASE_URL + "/not_like_article")
    return response.status_code

def test_get_popular_articles():
    response = requests.get(BASE_URL + "/popular_articles")
    return response.status_code

def test_get_recommended_articles(contentId):
    response = requests.get(BASE_URL + f"/recommended_articles/{contentId}")
    return response.status_code

if __name__ == "__main__":
    content_id = input("content_id: ")

    # Run the test cases
    results = {
        "get_article": test_get_article(),
        "like_article": test_like_article(),
        "not_like_article": test_not_like_article(),
        "get_popular_articles": test_get_popular_articles(),
        "get_recommended_articles": test_get_recommended_articles(content_id),
    }

    print()

    for test_name, status in results.items():
        if status == 200:
            print(test_name, ": Passed")
        else:
            print(test_name, ": Failed")
