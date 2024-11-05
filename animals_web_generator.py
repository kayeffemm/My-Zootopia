import requests

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
API_KEY = "r5QWeiJF2YCkHuYYor8vow==XqJrIrkRFsNIxe5E"
API_URL = f"https://api.api-ninjas.com/v1/animals?X-Api-Key="


def main(template_path="animals_template.html", data_path="animals_data.json", output_path="animals.html"):
    html_template = read_html_template(template_path)
    search_term = get_user_search_term()
    animal_data = create_html_string(search_term)
    new_html_string = add_data_to_template(html_template, animal_data)
    write_html_file(output_path, new_html_string)


def get_user_search_term() -> str:
    """
    Prompts User to enter the animal name of choice
    :return: string
    """
    search_term = input("Please enter the desired animal: ")
    return search_term


def create_full_api_url(api_url: str, api_key: str, search_term: str="monkey"):
    """
    Creates a full URL string with given data (api_url, api_key, search_term)
    :param api_url: string
    :param api_key: string
    :param search_term: string
    :return: string
    """
    api_url_string = api_url + api_key + "&name=" + search_term
    return api_url_string


def requests_data_from_api(search_term: str) -> list:
    """
    Requests data from API and returns data as list.
    :param search_term: string
    :return: list
    """
    api_url_string = create_full_api_url(API_URL, API_KEY, search_term)
    try:
        animal_data = requests.get(api_url_string)
        animal_data_list = animal_data.json()
        return animal_data_list
    except requests.RequestException as e:
        print("Error: ", e)
        return []


def read_html_template(file_path: str) -> str:
    """
    Loads html file and returns data as string.
    :param file_path: string
    :return: string
    """
    with open(file_path, "r") as template:
        return template.read()


def write_html_file(file_path: str, html_data: str) -> None:
    """
    Creates a new HTML file with provided data.
    :param file_path: string
    :param html_data: string
    :return: None
    """
    with open(file_path, "w") as new_file:
        new_file.write(html_data)


def add_data_to_template(template: str, content: str) -> str:
    """
    adds content to given template string:
    :param template: string
    :param content: string
    :return: string
    """
    return template.replace(PLACEHOLDER, content)


def create_html_string(search_term: str) -> str:
    """
    Generates an HTML string from JSON data at the provided file path.
    :param search_term: string
    :return: string
    """
    animals_data = requests_data_from_api(search_term)
    return "".join(serialize_animal(animal) for animal in animals_data)


def serialize_animal(animal_obj: dict) -> str:
    """
    Gets a single animal object and serializes it to an HTML string.
    :param animal_obj: dict
    :return: string
    """
    animal_name = animal_obj.get("name", "Unknown")
    animal_first_location = next(iter(animal_obj.get("locations", [])), "Unknown")
    animal_features = animal_obj.get("characteristics", {}).get("distinctive_feature", "Unknown")
    animal_color = animal_obj.get("characteristics", {}).get("color", "Unknown")
    animal_type = animal_obj.get("characteristics", {}).get("type", "Unknown")
    animal_diet = animal_obj.get("characteristics", {}).get("diet", "Unknown")
    animal_lifespan = animal_obj.get("characteristics", {}).get("lifespan", "Unknown")

    html_string = '<li class="cards__item">'
    html_string += f'<div class="card__title">{animal_name}</div>\n'
    html_string += '<p class="card__text">'
    html_string += '<ul>'
    html_string += format_animal_attribute("Location", animal_first_location)
    html_string += format_animal_attribute("Features", animal_features)
    html_string += format_animal_attribute("Color", animal_color)
    html_string += format_animal_attribute("Type", animal_type)
    html_string += format_animal_attribute("Diet", animal_diet)
    html_string += format_animal_attribute("Lifespan", animal_lifespan)
    html_string += '</ul>\n</p>\n</li>\n'

    return html_string


def format_animal_attribute(label: str, value: str) -> str:
    """
    Formats label and value into an HTML list
    :param label: string
    :param value: string
    :return: string
    """
    if value and value != "Unknown":
        return f"<li><strong>{label}:</strong> {value}</li>\n"
    return ""


if __name__ == "__main__":
    main()
