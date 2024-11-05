from data_fetcher import fetch_data

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def main(template_path="animals_template.html", output_path="animals.html"):
    """
    Main function that drives the program flow:
    - Reads the HTML template.
    - Prompts the user for an animal search term.
    - Fetches data from the API and generates HTML content.
    - Writes the updated HTML to a specified output file.

    :param template_path: Path to the HTML template file.
    :param output_path: Path for the final HTML file with animal data.
    """
    html_template = read_html_template(template_path)
    search_term = get_user_search_term()
    animal_data = create_html_string(search_term)
    new_html_string = add_data_to_template(html_template, animal_data)
    write_html_file(output_path, new_html_string)


def get_user_search_term() -> str:
    """
    Prompts the user to enter an animal name for searching.

    :return: A string containing the user's input (search term).
    """
    search_term = input("Please enter the desired animal: ")
    return search_term


def read_html_template(file_path: str) -> str:
    """
    Reads the contents of an HTML template file and returns it as a string.

    :param file_path: Path to the HTML template file.
    :return: String containing the HTML template content.
    """
    with open(file_path, "r") as template:
        return template.read()


def write_html_file(file_path: str, html_data: str) -> None:
    """
    Writes the provided HTML data to a specified output file.

    :param file_path: Path for the output HTML file.
    :param html_data: HTML content to write to the file.
    :return: None
    """
    with open(file_path, "w") as new_file:
        new_file.write(html_data)


def add_data_to_template(template: str, content: str) -> str:
    """
    Replaces the placeholder in the HTML template with the provided content.

    :param template: HTML template string with a placeholder.
    :param content: HTML content to insert in place of the placeholder.
    :return: Modified HTML string with the content inserted.
    """
    return template.replace(PLACEHOLDER, content)


def create_html_string(search_term: str) -> str:
    """
    Generates an HTML string based on JSON data for a specific search term.

    :param search_term: Name of the animal to search in the API.
    :return: HTML string with animal information or a message indicating the animal was not found.
    """
    animals_data = fetch_data(search_term)
    if animals_data:
        return "".join(serialize_animal(animal) for animal in animals_data)
    else:
        return f"""<h2>The animal "{search_term}" doesn't exist.</h2>"""


def serialize_animal(animal_obj: dict) -> str:
    """
    Serializes a single animal object into an HTML string representation.

    :param animal_obj: Dictionary containing animal data.
    :return: HTML list item string for the animal, with placeholders for missing attributes.
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
    Formats a label and value as an HTML list item if the value is present.

    :param label: Attribute label (e.g., "Location").
    :param value: Attribute value; only included if it's not "Unknown".
    :return: HTML string for the attribute, or an empty string if the value is missing.
    """
    if value and value != "Unknown":
        return f"<li><strong>{label}:</strong> {value}</li>\n"
    return ""


if __name__ == "__main__":
    main()
