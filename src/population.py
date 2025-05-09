from src.genes import Gene
from src.enums import GeneType
from src.animals import Rabbit
from src import setup, data_plots
import random


def assign_partners(rabbits: list[Rabbit]):
    random.shuffle(rabbits)
    for i, rabbit in enumerate(rabbits):
        if i + 1 > len(rabbits) - 1:
            continue
        if i % 2 == 0:
            rabbit.assign_partner(rabbits[i + 1])
            rabbits[i + 1].assign_partner(rabbit)


def survival_check(rabbits: list[Rabbit]) -> list[Gene]:
    return [rabbit for rabbit in rabbits if rabbit.survives()]


def run_lifecycle(rabbits: list[Rabbit]) -> list[Rabbit]:
    rabbits = survival_check(rabbits)
    assign_partners(rabbits)
    new_rabbits = breed_survivors(rabbits)
    return new_rabbits


def breed_survivors(rabbits: list[Rabbit]) -> list[Rabbit]:
    next_gen_rabbits = []
    for rabbit in rabbits:
        rabbit.determine_offspring_number()
        children = rabbit.reproduce()
        next_gen_rabbits = next_gen_rabbits + children
        next_gen_rabbits = cap_population(next_gen_rabbits)
    return next_gen_rabbits


def cap_population(rabbits: list[Rabbit]) -> list[Rabbit]:
    population_cap = 60
    random.shuffle(rabbits)
    if len(rabbits) > population_cap:
        rabbits = rabbits[slice(population_cap)]
    return rabbits


def simulate_generations(generations: int):
    gene_pool = setup.create_gene_pool()
    rabbits = setup.create_rabbits(gene_pool, 30)
    gene_data = {}
    gene_data = data_plots.collect_data(rabbits, gene_data, 0, GeneType.SPEED)
    for generation in range(generations):
        rabbits = run_lifecycle(rabbits)
        gene_data = data_plots.collect_data(
            rabbits, gene_data, generation, GeneType.SPEED
        )

    data_plots.plot_genes(gene_data)


simulate_generations(40)
