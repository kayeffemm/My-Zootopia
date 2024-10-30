import json

def main():
    animal_content_list = get_animal_content("animals_data.json")
    print_animal_content(animal_content_list)


def load_data(file_path: str) -> list:
    """
    Loads a JSON file.
    :param file_path: string
    :return: list
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_content(file_path: str) -> list:
    """
    Gets animal name, diet, location and type if this information exists in given JSON and returns a list.
    :param file_path: string
    :return: list
    """
    animals_data = load_data(file_path)
    animals_content_list = []
    for animal in animals_data:
        animal_name = animal.get("name")
        animal_diet = animal.get("characteristics", {}).get("diet")
        animal_first_location = animal.get("locations")[0]
        animal_type = animal.get("characteristics", {}).get("type")

        animals_content_list.append({"Name": animal_name,
                                "Diet": animal_diet,
                                "Location": animal_first_location,
                                "Type": animal_type
                                })
    return animals_content_list

def print_animal_content(animals_content_list: list) -> None:
    """
    Prints animal Content but only if value != None.
    :param animals_content_list: list
    :return: None
    """
    for animal in animals_content_list:
        for key, value in animal.items():
            if value:
                print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    main()
