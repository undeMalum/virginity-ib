from pathlib import Path

import pandas as pd

from src.paths.paths import (
    ANSWERS_CSV,
    ALL_ANSWERS
)

df = pd.read_csv(ANSWERS_CSV)


def count_per_subject(virgin: bool):
    series_storage = []
    virginity = {False: "No", True: "Yes"}
    for idx in range(4, 17, 2):
        count_subjects = df.loc[
            (df['Virginity'] == virginity[virgin]) &
            ~(
                    ((df[df.columns[idx]] == "ES&S") & (df[df.columns[idx+1]] == "Higher Level")) |
                    ((df[df.columns[idx]] == "Language ab inito") & (df[df.columns[idx+1]] == "Higher Level")) |
                    ((df[df.columns[idx]] == "World religions") & (df[df.columns[idx + 1]] == "Higher Level"))
             ),
            df.columns[idx]].value_counts()
        series_storage.append(count_subjects)

    concatenated_subjects = pd.concat(series_storage).sort_index()

    already_added = []
    subjects = []
    for subject in concatenated_subjects.items():
        if subject[0] not in already_added:
            already_added.append(subject[0])
            subjects.append((subject[0], concatenated_subjects.loc[subject[0]].sum()))

    combined_subjects = pd.DataFrame(subjects, columns=["Subject", "Count"])

    return combined_subjects


def create_csv_all(csv_path: Path):
    virgins = count_per_subject(True)
    nonvirgins = count_per_subject(False)
    joined_virgins_and_nonvirgins = pd.concat([virgins, nonvirgins["Count"]], axis="columns")
    cln_names = ["Subject", "Virgins", "Non-virgins"]
    joined_virgins_and_nonvirgins.columns = cln_names
    joined_virgins_and_nonvirgins.to_csv(csv_path, mode="a", index=False)


if __name__ == "__main__":
    create_csv_all(ALL_ANSWERS)
