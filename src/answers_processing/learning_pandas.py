"""There's nothing interesting in this file. I'm just learning pandas and matplotlib."""

import pandas as pd

from src.paths.paths import ANSWERS_CSV

df = pd.read_csv(ANSWERS_CSV)

if __name__ == "__main__":
    subjects = []
    # for idx in range(4, 15, 2):
    #     count_subjects = df[df.columns[idx:idx+2]].value_counts().to_dict()
    #     subjects.append(count_subjects)

    print(df[["Virginity", "Education level"]])

    # for idx in range(4, 15, 2):
    #     count_subjects = df.loc[df['Virginity'] == "Yes", ["Subject 1", "Subject 1 level"]].value_counts().to_dict()
    #     subjects.append(count_subjects)
    #     print(count_subjects)

    # for key in subjects[0]:
    #     sbj_counter = [subject[key] for subject in subjects]
    #     print(f"{key[0]} {key[1]}: {sbj_counter}")

    print(df.loc[df['Virginity'] == "Yes", "Subject 1"].value_counts())
    print(df.loc[(df['Virginity'] == "Yes") & (df['Education level'] == "DP1"), ["Subject 1", "Subject 1 level"]].value_counts())
    print(
        pd.concat([df.loc[(df['Virginity'] == "Yes") & (df['Education level'] == "DP1"), ["Subject 1",
                                                                               "Subject 1 level"]].value_counts(),
         df.loc[(df['Virginity'] == "Yes") & (df['Education level'] == "DP1"), ["Subject 2",
                                                                                "Subject 2 level"]].value_counts()
         ])
    )