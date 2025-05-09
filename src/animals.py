from src.genes import GenePair
from src.enums import GeneType
import random


class Rabbit:
    def __init__(self, genes: dict[GeneType, GenePair]):
        self.genes = genes
        self.partner = None
        self.offspring_number = 1

    def assign_partner(self, rabbit):
        self.partner = rabbit

    def reproduce(self):
        new_genes = {}
        children = []
        if self.partner:
            for new_offspring in range(self.offspring_number):
                for gene_type, gene_pair in self.genes.items():
                    first_gene = gene_pair.pick_random()
                    second_gene = self.partner.genes[gene_type].pick_random()
                    new_genes[gene_type] = GenePair(first_gene, second_gene)
                new_rabbit = Rabbit(new_genes)
                children.append(new_rabbit)
        return children

    def speed(self):
        return self.genes[GeneType.SPEED].expressed_gene.stat / self.size()

    def size(self):
        return self.genes[GeneType.SIZE].expressed_gene.stat

    def survives(self):
        if self.speed() >= random.randrange(0, 400) / 100:
            return True
        return False

    def determine_offspring_number(self):
        self.offspring_number = convert_decimal_to_probabilitic_integer(5 - self.size())


def convert_decimal_to_probabilitic_integer(decimal: float) -> int:
    expected = decimal
    base = expected // 1
    remainder = (expected) % 1
    extra_child = random.choices([1, 0], [remainder, 1 - remainder], k=1)[0]
    return int(base + extra_child)
