from dataclasses import dataclass
from src.enums import Dominancy
import random


@dataclass(frozen=True)
class Gene:
    name: str
    dominancy: Dominancy
    initial_weighting: float

    def check(self):
        print(self.name)


@dataclass(frozen=True)
class SpeedGene(Gene):
    name: str
    dominancy: Dominancy
    speed: float


class GenePair:
    def __init__(self, gene_one: Gene, gene_two: Gene):
        self.gene_one = gene_one
        self.gene_two = gene_two
        self.expressed_gene = self._redetermine_expressed()

    def _redetermine_expressed(self) -> Gene:
        if self.gene_one.dominancy == self.gene_two.dominancy:
            return random.choice([self.gene_one, self.gene_two])
        if self.gene_one.dominancy == Dominancy.DOMINANT:
            return self.gene_one
        return self.gene_two

    def pick_random(self):
        return random.choice([self.gene_one, self.gene_two])
