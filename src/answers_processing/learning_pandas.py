"""There's nothing interesting in this file. I'm just learning pandas and matplotlib."""

import pandas as pd

from src.paths.paths import ANSWERS_CSV

df = pd.read_csv(ANSWERS_CSV)

# print(
#     pd.concat([df.loc[(df['Virginity'] == "Yes") & (df['Education level'] == "DP1"), ["Subject 1",
#                                                                            "Subject 1 level"]].value_counts(),
#      df.loc[(df['Virginity'] == "Yes") & (df['Education level'] == "DP1"), ["Subject 2",
#                                                                             "Subject 2 level"]].value_counts()
#      ])
# )

# for idx in range(4, 15, 2):
#     count_subjects = df[df.columns[idx:idx+2]].value_counts().to_dict()
#     subjects.append(count_subjects)

# for key in subjects[0]:
#     sbj_counter = [subject[key] for subject in subjects]
#     print(f"{key[0]} {key[1]}: {sbj_counter}")
# joined = pd.DataFrame(df.loc[df['Virginity'] == "Yes", "Subject 1"].value_counts())
# print(df.loc[df['Virginity'] == "Yes", "Subject 1"].value_counts())
# print(df.loc[(df['Virginity'] == "Yes") & ((df['Education level'] == "DP1") | (df['Education level'] == "DP2")),
# ["Subject 1", "Subject 1 level"]].value_counts())

if __name__ == "__main__":
    series_storage = []

    # print(df[["Virginity", "Education level"]])

    for idx in range(4, 15, 2):
        count_subjects = df.loc[df['Virginity'] == "Yes", df.columns[idx:idx + 2]].value_counts()
        series_storage.append(count_subjects)

    concatenated_subjects = pd.concat(series_storage).sort_index()

    already_added = []
    subjects = []
    for subject in concatenated_subjects.items():
        if (subject[0][0], subject[0][1]) not in already_added:
            already_added.append((subject[0][0], subject[0][1]))
            subjects.append((subject[0][0], subject[0][1], concatenated_subjects.loc[subject[0]].sum()))

    pd.DataFrame(subjects, columns=["Subject", "Level", "Count"]).to_csv(
        r"C:\Users\Mateusz\PycharmProjects\virginity-ib\src\answers_processing\results.csv",
        mode="a",
        index=False
    )
