import data.db_handler


class Draconid:
    def __init__(self, draconid_id, species, age, name, sex):
        self.id = draconid_id
        self.species = species
        self.age = age
        self.name = name
        self.sex = sex

    def __str__(self):
        return f"{self.name, self.species, self.age, self.sex}"


def draco_info(draconid_id):
    print(f"{draconid_id.name}, of the {draconid_id.species} species, age {draconid_id.age}, {draconid_id.sex}")


