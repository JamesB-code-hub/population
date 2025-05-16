import pandas as pd
import sys
import os

sys.path.append(os.getcwd())


def hello() -> str:
    print(" nsot hello")
    return "hello"


x = pd.DataFrame()
hello()
print(x)
print(os.getcwd())
print(sys.prefix, sys.base_prefix)
