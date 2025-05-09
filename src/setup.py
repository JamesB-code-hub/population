from src.genes import GenePair, Gene, ScalingGene
from src.enums import Dominancy, GeneType
from src.animals import Rabbit
import random
import numpy as np
import pandas as pd


def create_gene_pool() -> dict[GeneType, list[Gene]]:
    gene_mapping = {}
    gene_mapping[GeneType.SPEED] = create_speed_genes()
    gene_mapping[GeneType.SIZE] = create_size_genes()
    return gene_mapping


def create_speed_genes() -> list[ScalingGene]:
    speed_genes = []
    data = np.array(
        [
            ["speed3d", Dominancy.DOMINANT, 1, 3],
            ["speed2", Dominancy.DOMINANT, 1, 2],
            ["speed3", Dominancy.RECESSIVE, 1, 3],
            ["speed4", Dominancy.DOMINANT, 1, 4],
        ]
    )
    df = pd.DataFrame(data, columns=["Name", "Dominancy", "Initial Weighting", "Stat"])
    for index, row in df.iterrows():
        speed_genes.append(
            ScalingGene(row["Dominancy"], float(row["Initial Weighting"]), GeneType.SPEED, float(row["Stat"]))
        )
    return speed_genes


def create_size_genes() -> list[ScalingGene]:
    size_genes = []
    data = np.array(
        [
            ["size3d", Dominancy.DOMINANT, 1, 3],
            ["size2", Dominancy.DOMINANT, 1, 2],
            ["size3", Dominancy.RECESSIVE, 1, 3],
            ["size4", Dominancy.DOMINANT, 1, 4],
        ]
    )
    df = pd.DataFrame(data, columns=["Name", "Dominancy", "Initial Weighting", "Stat"])
    for index, row in df.iterrows():
        size_genes.append(
            ScalingGene(row["Dominancy"], float(row["Initial Weighting"]), GeneType.SIZE, float(row["Stat"]))
        )
    return size_genes


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
