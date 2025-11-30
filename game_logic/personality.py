import json
import os
from random import randint, choice


def load_data(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


PERSONALITIES = load_data("personalities.json")
FACETS = load_data("facets.json")


def gen_facets():
    social = randint(1, 10)
    aggression = randint(1, 10)
    energy = randint(1, 10)
    temperament = randint(1, 10)
    curiosity = randint(1, 10)
    facet_list = {"social": social, "aggression": aggression, "energy": energy,
                  "temperament": temperament, "curiosity": curiosity}
    return facet_list


def determine_personality(facet_list):
    facet_values = []
    for facet, value in facet_list.items():
        if value <= 5:
            facet_values.append("low")
        else:
            facet_values.append("high")
    for label, facets in PERSONALITIES.items():
        if list(facets.values()) == facet_values:
            return label


def gen_personality():
    facets = gen_facets()
    personality = determine_personality(facets)
    max_distance = 0
    extreme_facets = []
    for facet, value in facets.items():
        facet_distance = abs(5.5 - value)
        if facet_distance > max_distance:
            max_distance = facet_distance
            extreme_facets = [(facet, value)]
        elif facet_distance == max_distance:
            extreme_facets.append((facet, value))
    extreme_facet, extreme_value = choice(extreme_facets)
    personality_modifier = FACETS[extreme_facet][str(extreme_value)]
    full_personality = {"genotype": facets, "phenotype": f'{personality}, {personality_modifier}'}
    print(full_personality)
    return full_personality


def determine_phenotype(facets):
    personality = determine_personality(facets)
    max_distance = 0
    extreme_facets = []
    for facet, value in facets.items():
        facet_distance = abs(5.5 - value)
        if facet_distance > max_distance:
            max_distance = facet_distance
            extreme_facets = [(facet, value)]
        elif facet_distance == max_distance:
            extreme_facets.append((facet, value))
    extreme_facet, extreme_value = choice(extreme_facets)
    personality_modifier = FACETS[extreme_facet][str(extreme_value)]
    full_personality = {"genotype": facets, "phenotype": f'{personality}, {personality_modifier}'}
    print(full_personality)
    return full_personality
