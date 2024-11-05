import requests

API_KEY = "r5QWeiJF2YCkHuYYor8vow==XqJrIrkRFsNIxe5E"
API_URL = f"https://api.api-ninjas.com/v1/animals?X-Api-Key="


def create_full_api_url(api_url: str, api_key: str, search_term: str="monkey"):
    """
    Creates a complete API URL with the specified API key and search term.

    :param api_url: Base URL of the API.
    :param api_key: API key for authorization.
    :param search_term: Animal name to search in the API.
    :return: The full API URL with query parameters.
    """
    api_url_string = api_url + api_key + "&name=" + search_term
    return api_url_string


def fetch_data(search_term: str) -> list:
    """
    Fetches animal data from the API for the given search term.

    :param search_term: Name of the animal to search.
    :return: List of animal data dictionaries if the request is successful, otherwise an empty list.
    """
    api_url_string = create_full_api_url(API_URL, API_KEY, search_term)
    try:
        animal_data = requests.get(api_url_string)
        animal_data_list = animal_data.json()
        return animal_data_list
    except requests.RequestException as e:
        print("Error: ", e)
        return []
