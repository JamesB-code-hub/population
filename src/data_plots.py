from src.animals import Rabbit
from src.enums import GeneType
import pandas as pd
from matplotlib import pyplot as plt


def collect_data(
    rabbits: list[Rabbit],
    gene_data: dict[int, dict[str, int]],
    generation: int,
    gene_type: GeneType,
) -> dict[str, int]:
    genes = [r.genes[gene_type].gene_one.name() for r in rabbits] + [
        r.genes[gene_type].gene_two.name() for r in rabbits
    ]
    occurences = count_occurences(genes)
    gene_data[generation + 1] = occurences
    return gene_data


def count_occurences(list: list) -> dict[str, int]:
    unsorted_dict = dict((x, list.count(x)) for x in set(list))
    return dict(sorted(unsorted_dict.items()))


def plot_genes(gene_data: dict[int, dict[str, int]]):
    df = pd.DataFrame(gene_data).transpose()
    df.plot(kind="bar", stacked=True, title="Stacked Bar Graph by dataframe")
    plt.show()
