from pathlib import Path

import pandas as pd

from src.paths.paths import (
    ANSWERS_CSV,
    DP1_SUBJECT_LEVELS,
    DP2_SUBJECT_LEVELS
)
from src.answers_processing.dp import DP

df = pd.read_csv(ANSWERS_CSV)


def write_total(virgin: bool, dp: DP):
    series_storage = []
    virginity = {False: "No", True: "Yes"}
    for idx in range(4, 17, 2):
        count_subjects = df.loc[(df['Virginity'] == virginity[virgin]) & (df["Education level"] == dp.value),
                                df.columns[idx:idx+2]].value_counts()
        series_storage.append(count_subjects)

    concatenated_subjects = pd.concat(series_storage).sort_index()

    already_added = []
    subjects = []
    for subject in concatenated_subjects.items():
        if (subject[0][0], subject[0][1]) not in already_added:
            already_added.append((subject[0][0], subject[0][1]))
            subjects.append((subject[0][0], subject[0][1], concatenated_subjects.loc[subject[0]].sum()))

    combined_subjects = pd.DataFrame(subjects, columns=["Subject", "Level", "Count"])

    return combined_subjects


def join_csvs(csv_path_dp1: Path, csv_path_dp2: Path):
    cln_names = ["Subject", "Level", "Virgins", "Non-virgins"]

    virgins_dp1 = write_total(True, DP.DP1)
    nonvirgins_dp1 = write_total(False, DP.DP1)
    joined_virgins_and_nonvirgins_dp1 = pd.concat([virgins_dp1, nonvirgins_dp1["Count"]], axis="columns")
    joined_virgins_and_nonvirgins_dp1.columns = cln_names
    joined_virgins_and_nonvirgins_dp1.to_csv(csv_path_dp1, mode="a", index=False)

    virgins_dp2 = write_total(True, DP.DP2)
    nonvirgins_dp2 = write_total(False, DP.DP2)
    joined_virgins_and_nonvirgins_dp2 = pd.concat([virgins_dp2, nonvirgins_dp2["Count"]], axis="columns")
    joined_virgins_and_nonvirgins_dp2.columns = cln_names
    joined_virgins_and_nonvirgins_dp2.to_csv(csv_path_dp2, mode="a", index=False)


if __name__ == "__main__":
    join_csvs(DP1_SUBJECT_LEVELS, DP2_SUBJECT_LEVELS)
