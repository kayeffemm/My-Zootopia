import json

def main():
    html_template = read_html_template("animals_template.html")
    animal_data = serialize_animal_content("animals_data.json")
    new_html_string = add_data_to_template(html_template, animal_data)
    write_html_file(new_html_string)
    print(new_html_string)


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


def write_html_file(html_data: str) -> None:
    """
    Creates a new HTML file with provided data.
    :param html_data: string
    :return: None
    """
    with open("animals.html", "w") as new_file:
        new_file.write(html_data)


def add_data_to_template(template: str, content: str) -> str:
    """
    adds content to given template string:
    :param template: string
    :param content: string
    :return: string
    """
    content_added = template.replace("__REPLACE_ANIMALS_INFO__", content)
    return content_added


def serialize_animal_content(file_path: str) -> str:
    """
    Gets animal name, diet, location and type if this information exists in given JSON and returns an HTML string.
    :param file_path: string
    :return: string
    """
    animals_data = load_data(file_path)
    output = ""

    for animal in animals_data:
        animal_name = animal.get("name")
        animal_diet = animal.get("characteristics", {}).get("diet")
        animal_first_location = animal.get("locations")[0]
        animal_type = animal.get("characteristics", {}).get("type")

        output += '<li class="cards__item">'
        output += f'Name: {animal_name}<br/>\n'
        if animal_diet:
            output += f'Diet: {animal_diet}<br/>\n'
        if animal_first_location:
            output += f'Location: {animal_first_location}<br/>\n'
        if animal_type:
            output += f'Type: {animal_type}<br/>\n'
        output += '</li>\n'

    return output


if __name__ == "__main__":
    main()
