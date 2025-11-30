from random import randint, choice
from models.draconid import Draconid
from data.db_handler import save_draconid
from game_logic.personality import determine_phenotype
import json
import os


def load_data(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


COLOR_TABLE = load_data("color_table.json")
HEX_CODES = load_data("hex_codes.json")

species = ["dragon", "fae", "wyvern", "cockatrice", "amphithere", "wyrm", "sea serpent", "quetzalcoatl", "lindwurm",
           "salamander", "lung dragon", "drake", "hydra", "kirin"]

sex = ["male", "female"]

prefixes = ["Fire", "Sharp", "Ice", "Thunder", "Earth", "Cloud"]

suffixes = ["tail", "storm", "wing", "fang", "claw", "scale", "horn", "talon"]

color_alleles = ["red", "blue", "yellow", "null"]

lightness = ["neutral", "white", "black"]

draconid_list = []


def gen_name():
    prefix = choice(prefixes)
    suffix = choice(suffixes)
    name = "".join([prefix, suffix])
    return name


def determine_color(main_color_gene, lightness_gene):
    lightness_modifier = determine_lightness(lightness_gene)
    key = "_".join(sorted([main_color_gene[0], main_color_gene[1]]))
    return COLOR_TABLE[key][lightness_modifier]


def gen_random_color():
    allele1 = choice(color_alleles)
    allele2 = choice(color_alleles)
    main_color_gene = [allele1, allele2]

    light_allele1 = choice(lightness)
    light_allele2 = choice(lightness)
    lightness_gene = [light_allele1, light_allele2]

    genotype = [main_color_gene, lightness_gene]
    phenotype = determine_color(main_color_gene, lightness_gene)

    return {"genotype": genotype, "phenotype": phenotype}


def determine_lightness(lightness_gene):
    if lightness_gene[0] == "neutral" or lightness_gene[1] == "neutral":
        lightness_pheno = "neutral"
    elif lightness_gene[0] != lightness_gene[1]:
        lightness_pheno = "silver"
    else:
        lightness_pheno = lightness_gene[0]
    return lightness_pheno


def gen_draconid():
    d_species = choice(species)
    d_sex = choice(sex)
    d_age = randint(20, 150)
    d_name = gen_name()
    d_color = gen_random_color()
    new_draconid = Draconid(None, d_species, d_age, d_name, d_sex, d_color)
    draconid_list.append(new_draconid)
    return new_draconid


def gen_dragon_breeding_pair():
    mother = Draconid(None, "dragon", randint(20, 100), gen_name(), "female", gen_random_color())
    father = Draconid(None, "dragon", randint(20, 100), gen_name(), "male", gen_random_color())
    return [mother, father]


def baby_color(parent1, parent2):
    baby_genotype = [
        [choice(parent1["genotype"][0]), choice(parent2["genotype"][0])],
        [choice(parent1["genotype"][1]), choice(parent2["genotype"][1])]
    ]
    baby_phenotype = determine_color(baby_genotype[0], baby_genotype[1])
    print(baby_phenotype)
    return baby_phenotype


def gen_baby_personality(parent1, parent2):
    """
    Function accepts parents' PERSONALITY GENOTYPE
    """
    social_factor = inherit_facet(parent1["social"], parent2["social"])
    aggression_factor = inherit_facet(parent1["aggression"], parent2["aggression"])
    energy_factor = inherit_facet(parent1["energy"], parent2["energy"])
    temperament_factor = inherit_facet(parent1["temperament"], parent2["temperament"])
    curiosity_factor = inherit_facet(parent1["curiosity"], parent2["curiosity"])
    baby_facets = {"social": social_factor, "aggression": aggression_factor, "energy": energy_factor,
                   "temperament": temperament_factor, "curiosity": curiosity_factor}
    baby_full_personality = determine_phenotype(baby_facets)
    return baby_full_personality


def inherit_facet(facet1, facet2):
    low_value = max(min(facet1, facet2) - 1, 1)
    high_value = min(max(facet1, facet2) + 1, 10)
    inherited_value = randint(low_value, high_value)
    return inherited_value
