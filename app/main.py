class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = []

    for data in people:
        temp = Person(data["name"], data["age"])
        result.append(temp)
        Person.people[temp.name] = temp

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] in Person.people:
            person.wife = Person.people[data["wife"]]

        if "husband" in data and data["husband"] in Person.people:
            person.husband = Person.people[data["husband"]]

    return result
