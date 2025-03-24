from random import randint, choice
from models.draconid import Draconid
from data.db_handler import save_draconid


species = ["dragon", "fae", "wyvern", "cockatrice", "amphithere", "wyrm", "sea serpent", "quetzalcoatl", "lindwurm",
           "salamander", "lung dragon", "drake", "hydra", "kirin"]

sex = ["male", "female"]

prefixes = ["Fire", "Sharp", "Ice", "Thunder", "Earth", "Cloud"]

suffixes = ["tail", "storm", "wing", "fang", "claw", "scale", "horn", "talon"]


def gen_name():
    prefix = choice(prefixes)
    suffix = choice(suffixes)
    name = "".join([prefix, suffix])
    return name


def gen_draconid():
    d_species = choice(species)
    d_sex = choice(sex)
    d_age = randint(20, 150)
    d_name = gen_name()
    new_draconid = Draconid(None, d_species, d_age, d_name, d_sex)
    save_draconid(new_draconid)
    return new_draconid

