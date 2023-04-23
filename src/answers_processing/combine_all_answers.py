from pathlib import Path

import numpy as np
import pandas as pd

from src.paths.paths import (
    ANSWERS_CSV,
    ALL_ANSWERS
)

df = pd.read_csv(ANSWERS_CSV)


def write_total(virgin: bool):
    series_storage = []
    virginity = {False: "No", True: "Yes"}
    for idx in range(4, 17, 2):
        count_subjects = df.loc[
            (df['Virginity'] == virginity[virgin]) &
            ~(
                (
                    ((df[df.columns[idx]] == "ES&S") & (df[df.columns[idx+1]] == "Higher Level")) |
                    ((df[df.columns[idx]] == "Language ab inito") & (df[df.columns[idx+1]] == "Higher Level"))
                 ) |
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
    # pd.set_option('display.max_rows', None, 'display.max_columns', None)
    total_virgins = write_total(False)
    total_nonvirgins = write_total(True)

    # add all missing subjects from nonvirgins to virgins
    total_virgins_with_subjects_from_nonvirgins = total_virgins["Subject"].to_frame().merge(
        total_nonvirgins,
        on="Subject",
        how="right",
    )

    # add all missing subjects from virgins to all
    all_available_subjects = total_virgins_with_subjects_from_nonvirgins.merge(
        total_virgins,
        on="Subject",
        how="outer"
    )

    # sort values
    all_available_subjects = all_available_subjects.sort_values("Subject")
    # rename columns
    cln_names = ["Subject", "Non-virgins", "Virgins"]
    all_available_subjects.columns = cln_names

    # replace all NaN values with 0
    all_available_subjects = all_available_subjects.replace(np.nan, 0)

    all_available_subjects.to_csv(csv_path, mode="a", index=False)


if __name__ == "__main__":
    create_csv_all(ALL_ANSWERS)
