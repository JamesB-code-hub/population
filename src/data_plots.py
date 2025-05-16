from src.animals import Rabbit
from src.enums import GeneType
import pandas as pd
from matplotlib import pyplot as plt
from celluloid import Camera
from collections import Counter


class GeneData:
    def __init__(self, gene_type):
        self.gene_data: dict[int, dict[str, int]] = {}
        self.gene_type = gene_type

    def collect_data(
        self,
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
        self.rabbit_history: dict[int, list[Rabbit]] = {}

    def update_rabbit_history(self, generation: int, rabbits: list[Rabbit]):
        self.rabbit_history[generation] = rabbits

    def add_gene_data_template(self, gene_type: GeneType):
        self.gene_data[gene_type] = GeneData(gene_type)

    def collect_all_data(self, rabbits: list[Rabbit], generation):
        self.update_rabbit_history(generation, rabbits)
        for gene_type, gene_data in self.gene_data.items():
            gene_data.collect_data(rabbits, generation, gene_type)

    def plot_all_data(self):
        for gene_type, gene_data in self.gene_data.items():
            gene_data.plot_genes()

    def plot_cross_plot(self, gene_type_one: GeneType, gene_type_two: GeneType):
        # genes_one = [r.genes[gene_type_one].expressed_gene.stat for r in self.rabbit_history[1]]
        # genes_two = [r.genes[gene_type_two].expressed_gene.stat for r in self.rabbit_history[1]]
        # plt.scatter(genes_one, genes_two)
        # plt.show()
        # colors = cm.rainbow(np.linspace(0, 1, numpoints))
        camera = Camera(plt.figure())
        for generation, rabbit in self.rabbit_history.items():
            genes_one = [
                r.genes[gene_type_one].expressed_gene.stat
                for r in self.rabbit_history[generation]
            ]
            genes_two = [
                r.genes[gene_type_two].expressed_gene.stat
                for r in self.rabbit_history[generation]
            ]
            c = Counter(zip(genes_one, genes_two))
            # create a list of the sizes, here multiplied by 10 for scale
            s = [10 * c[(x, y)] for x, y in zip(genes_one, genes_two)]
            plt.scatter(genes_one, genes_two, color="blue", s=s)
            plt.xlabel(gene_type_one)
            plt.ylabel(gene_type_two)
            # plt.title(f"Generation {generation}", loc = 'left')
            camera.snap()
        camera.animate(interval=200, blit=True)
        # need to save this
        plt.show()


def create_gene_data_manager() -> GeneDataManager:
    gene_data_manager = GeneDataManager()
    gene_data_manager.add_gene_data_template(GeneType.SPEED)
    gene_data_manager.add_gene_data_template(GeneType.SIZE)
    return gene_data_manager


def count_occurences(list: list) -> dict[str, int]:
    unsorted_dict = dict((x, list.count(x)) for x in set(list))
    return dict(sorted(unsorted_dict.items()))
