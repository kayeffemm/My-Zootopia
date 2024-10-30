import json

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def main(template_path="animals_template.html", data_path="animals_data.json", output_path="animals.html"):
    html_template = read_html_template(template_path)
    animal_data = create_html_string(data_path)
    new_html_string = add_data_to_template(html_template, animal_data)
    write_html_file(output_path, new_html_string)


def load_data(file_path: str) -> list:
    """
    Loads a JSON file and returns data as list.
    :param file_path: string
    :return: list
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


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


def create_html_string(file_path: str) -> str:
    """
    Generates an HTML string from JSON data at the provided file path.
    :param file_path: string
    :return: string
    """
    animals_data = load_data(file_path)
    return "".join(serialize_animal(animal) for animal in animals_data)


def serialize_animal(animal_obj: dict) -> str:
    """
    Gets a single animal object and serializes it to an HTML string.
    :param animal_obj: dict
    :return: string
    """
    animal_name = animal_obj.get("name", "Unknown")
    animal_diet = animal_obj.get("characteristics", {}).get("diet", "Unknown")
    animal_first_location = next(iter(animal_obj.get("locations", [])), "Unknown")
    animal_type = animal_obj.get("characteristics", {}).get("type", "Unknown")

    html_string = '<li class="cards__item">'
    html_string += f'<div class="card__title">{animal_name}</div>\n'
    html_string += '<p class="card__text">'
    html_string += format_animal_attribute("Diet", animal_diet)
    html_string += format_animal_attribute("Location", animal_first_location)
    html_string += format_animal_attribute("Type", animal_type)
    html_string += '</p>\n</li>\n'

    return html_string


def format_animal_attribute(label: str, value: str) -> str:
    if value and value != "Unknown":
        return f"<strong>{label}:</strong> {value}<br/>\n"
    return ""


if __name__ == "__main__":
    main()
