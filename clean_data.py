# Written by Jason Cain, Spring 2022

import os
from typing import List

import pandas as pd

DATA_PATH = "./data/wdbc.data"
METADATA_PATH = "./data/wdbc.names"
HEADERS = [
    "ID",
    "diagnosis",
    "mean_radius",
    "mean_texture",
    "mean_perimeter",
    "mean_area",
    "mean_smoothness",
    "mean_compactness",
    "mean_concavity",
    "mean_concave_points",
    "mean_symmetry",
    "mean_fractal_dimension",
    "stderror_radius",
    "stderror_texture",
    "stderror_perimeter",
    "stderror_area",
    "stderror_smoothness",
    "stderror_compactness",
    "stderror_concavity",
    "stderror_concave_points",
    "stderror_symmetry",
    "stderror_fractal_dimension",
    "worst_radius",
    "worst_texture",
    "worst_perimeter",
    "worst_area",
    "worst_smoothness",
    "worst_compactness",
    "worst_concavity",
    "worst_concave_points",
    "worst_symmetry",
    "worst_fractal_dimension",
]


def load_files(
    directory: str = DATA_PATH, headers: List[str] = HEADERS
) -> pd.DataFrame:
    """Load in data file."""
    cancer_dataframe = pd.read_csv(DATA_PATH, names=headers, index_col=[0, 1])
    return cancer_dataframe


def get_only_mean_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.filter(regex="mean_")


def generate_clean_dataframe() -> pd.DataFrame:
    df = load_files()
    df = get_only_mean_values(df)
    return df


def main() -> None:
    cancer_dataframe = generate_clean_dataframe()
    print(cancer_dataframe.describe())
    print(cancer_dataframe)


if __name__ == "__main__":
    main()