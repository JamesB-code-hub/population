from src.animals import Rabbit
from src.enums import GeneType
import pandas as pd
from matplotlib import pyplot as plt

class GeneData:
    def __init__(self, gene_type):
        self.gene_data: dict[int, dict[str, int]] = {}
        self.gene_type = gene_type

    def collect_data(self,
        rabbits: list[Rabbit],
        generation: int,
        gene_type: GeneType,
    ):
        genes = [r.genes[gene_type].gene_one.name() for r in rabbits] + [
            r.genes[gene_type].gene_two.name() for r in rabbits
        ]
        occurences = count_occurences(genes)
        self.gene_data[generation + 1] = occurences

    def plot_genes(self):
        df = pd.DataFrame(self.gene_data).transpose()
        df.plot(kind="bar", stacked=True, title="Stacked Bar Graph by dataframe")
        plt.show()

class GeneDataManager:
    def __init__(self):
        self.gene_data: dict[GeneType, GeneData] = {}

    def add_gene_data_template(self, gene_type: GeneType):
        self.gene_data[gene_type] = GeneData(gene_type)

    def collect_all_data(self, rabbits: list[Rabbit], generation):
        for gene_type, gene_data in self.gene_data.items():
            gene_data.collect_data(rabbits, generation, gene_type)
    
    def plot_all_data(self):
        for gene_type, gene_data in self.gene_data.items():
            gene_data.plot_genes()

    def plot_cross_plot(self, rabbits: list[Rabbit], gene_type_one: GeneType, gene_type_two: GeneType):
        genes_one = [r.genes[gene_type_one].expressed_gene.stat for r in rabbits]
        genes_two = [r.genes[gene_type_two].expressed_gene.stat for r in rabbits]
        plt.scatter(genes_one, genes_two)
        plt.show()

def create_gene_data_manager() -> GeneDataManager:
    gene_data_manager = GeneDataManager()
    gene_data_manager.add_gene_data_template(GeneType.SPEED)
    gene_data_manager.add_gene_data_template(GeneType.SIZE)
    return gene_data_manager

def count_occurences(list: list) -> dict[str, int]:
    unsorted_dict = dict((x, list.count(x)) for x in set(list))
    return dict(sorted(unsorted_dict.items()))



