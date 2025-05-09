from src.genes import SpeedGene, GenePair, Gene
from src.enums import Dominancy, GeneType
from src.animals import Rabbit
import random
from matplotlib import pyplot as plt
import pandas as pd


def create_gene_pool() -> dict[GeneType, list[Gene]]:
    gene_mapping = {}
    speed_genes = create_speed_genes()
    gene_mapping[GeneType.SPEED] = speed_genes
    return gene_mapping


def create_speed_genes() -> list[SpeedGene]:
    speed_genes = []
    speed_genes.append(SpeedGene("speed1", Dominancy.DOMINANT, 1, 1))
    speed_genes.append(SpeedGene("speed2", Dominancy.DOMINANT, 1, 2))
    speed_genes.append(SpeedGene("speed3", Dominancy.DOMINANT, 1, 3))
    speed_genes.append(SpeedGene("speed4", Dominancy.DOMINANT, 1, 4))
    return speed_genes


def create_rabbits(
    gene_mapping: dict[GeneType, list[Gene]], starting_rabbits: int
) -> list[Rabbit]:
    rabbits = []

    for rabbit in range(starting_rabbits):
        new_genes = {}
        for gene_type, genes in gene_mapping.items():
            selected_genes = random.choices(
                genes, [gene.initial_weighting for gene in genes], k=2
            )
            selected_pair = GenePair(selected_genes[0], selected_genes[1])
            new_genes[gene_type] = selected_pair
        new_rabbit = Rabbit(new_genes)
        rabbits.append(new_rabbit)
    return rabbits

def assign_partners(rabbits: list[Rabbit]):
    random.shuffle(rabbits)
    for i, rabbit in enumerate(rabbits):
        if i + 1 > len(rabbits) - 1:
            continue
        if i%2 == 0:
            rabbit.assign_partner(rabbits[i+1])
            rabbits[i+1].assign_partner(rabbit)

def survival_check(rabbits: list[Rabbit]) -> list[Gene]:
    return [rabbit for rabbit in rabbits if rabbit.survives()]


def run_lifecycle(rabbits: list[Rabbit]) -> list[Rabbit]:
    rabbits = survival_check(rabbits)
    assign_partners(rabbits)
    next_gen_rabbits = []
    for rabbit in rabbits:
        rabbit.determine_offspring_number()
        children = rabbit.reproduce()
        next_gen_rabbits = next_gen_rabbits + children
        population_cap = 60
        random.shuffle(next_gen_rabbits)
        if len(next_gen_rabbits) > population_cap:
            next_gen_rabbits = next_gen_rabbits[slice(population_cap)]
    return next_gen_rabbits

def simulate_generations(generations: int):
    gene_pool = create_gene_pool()
    rabbits = create_rabbits(gene_pool, 30)
    gene_data = {}
    gene_data = collect_data(rabbits, gene_data, 0)
    for generation in range(generations):
        rabbits = run_lifecycle(rabbits)
        gene_data = collect_data(rabbits, gene_data, generation)
        
    plot_genes(gene_data)

def collect_data(rabbits: list[Rabbit], gene_data: dict[int, dict[str, int]], generation: int) -> dict[str, int]:
    genes = [r.genes[GeneType.SPEED].gene_one.name for r in rabbits] + [r.genes[GeneType.SPEED].gene_two.name for r in rabbits]
    occurences = count_occurences(genes)
    gene_data[generation + 1] = occurences
    return gene_data

def count_occurences(list: list) -> dict[str, int]:
    unsorted_dict =  dict((x,list.count(x)) for x in set(list))
    return dict(sorted(unsorted_dict.items()))

def plot_genes(gene_data: dict[int, dict[str, int]]):
    df = pd.DataFrame(gene_data).transpose()
    print(df)
    df.plot(kind='bar', stacked=True,
        title='Stacked Bar Graph by dataframe')
    plt.show()

simulate_generations(40)