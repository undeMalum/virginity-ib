from pathlib import Path

import pandas as pd

from src.paths.paths import (
    ANSWERS_CSV,
    TOTAL_VIRGINS_SUBJECT_LEVEL,
    TOTAL_NONVIRGINS_SUBJECT_LEVEL
)

df = pd.read_csv(ANSWERS_CSV)


def write_total(virgin: bool, csv_path: Path):
    series_storage = []
    virginity = {False: "No", True: "Yes"}
    for idx in range(4, 15, 2):
        count_subjects = df.loc[df['Virginity'] == virginity[virgin], df.columns[idx:idx + 2]].value_counts()
        series_storage.append(count_subjects)

    concatenated_subjects = pd.concat(series_storage).sort_index()

    already_added = []
    subjects = []
    for subject in concatenated_subjects.items():
        if (subject[0][0], subject[0][1]) not in already_added:
            already_added.append((subject[0][0], subject[0][1]))
            subjects.append((subject[0][0], subject[0][1], concatenated_subjects.loc[subject[0]].sum()))

    combined_subjects = pd.DataFrame(subjects, columns=["Subject", "Level", "Count"])

    combined_subjects.to_csv(
        csv_path,
        mode="a",
        index=False
    )
    print("Processed.")


if __name__ == "__main__":
    option = input("V/NV: ")
    if option == "V":
        write_total(True, TOTAL_VIRGINS_SUBJECT_LEVEL)
    elif option == "NV":
        write_total(False, TOTAL_NONVIRGINS_SUBJECT_LEVEL)
