from src.genes import SpeedGene, GenePair
from src.enums import Dominancy, GeneType

class Rabbit:
    def __init__(self, genes: dict[GeneType, GenePair]):
        self.genes = genes
        self.partner = None

    def assign_partner(self, rabbit):
        self.partner = rabbit

    def reproduce(self, offspring: int):
        new_genes = {}
        children = []
        for new_offspring in range(offspring):
            for gene_type, gene_pair in genes.items():
                first_gene = gene_pair.pick_random()
                second_gene = self.partner.genes[gene_type].pick_random()
                new_genes[gene_type] = GenePair(first_gene, second_gene)
            new_rabbit = Rabbit(new_genes)
            children.append(new_rabbit)
        return children

gene_a = SpeedGene(name="gene_a",dominancy=Dominancy.DOMINANT, speed=5)
gene_b = SpeedGene("gene_b", Dominancy.DOMINANT, 3)
speed_pair = GenePair(gene_a, gene_b)
genes = {GeneType.SPEED: speed_pair}
my_rabbit = Rabbit(genes)
my_rabbit.genes[GeneType.SPEED].expressed_gene.check()