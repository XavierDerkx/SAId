#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Global variables and parameters."""

from pathlib import Path
import pandas as pd

# TODO add a unit test module


def init():
    """Initialise data source for alpha decays."""
    # global DATA_FILE
    global DATA_SOURCE

    DATA_FILE = Path("./data/all_alphas.csv")
    df = pd.read_csv(DATA_FILE)

    # merge columns into a dict
    columns = ["I", "E", "HL"]
    df["decay"] = df[columns].to_dict(orient="records")
    # df = df.drop(columns=columns)
    # df = df.groupby(["A", "Z"])["decay"].agg(list).reset_index()
    DATA_SOURCE = df


def get_decays(A: "int", Z: "int") -> list:
    """Get the list of decays for a given isotope."""
    return DATA_SOURCE.loc[DATA_SOURCE['A'].eq(A) &
                           DATA_SOURCE['Z'].eq(Z)]["decay"].tolist()


def find_isotopes(E: "float", HL: "float",
                  deltaE: "float" = 0.1, deltaHL: "float" = 0.1) \
                  -> pd.DataFrame:
    """Find if any isotope matches a decay."""
    return
    DATA_SOURCE.loc[DATA_SOURCE['E'].between(E*(1-deltaE), E*(1+deltaE)) &
                    DATA_SOURCE['HL'].between(HL*(1-deltaHL), HL*(1+deltaHL))]
