import pandas as pd

from src.paths.paths import ANSWERS_CSV

df = pd.read_csv(ANSWERS_CSV)

duplicate = df[df.duplicated(["Subject 1", "Subject 1 level"])]

if __name__ == "__main__":
    # print(df['Subject 1'].value_counts().to_dict())
    # print(df["Subject 1 level"].value_counts().to_dict())
    # print(df[df.columns[4:6]].value_counts().to_dict())
    subjects = []
    for idx in range(4, 15, 2):
        print(idx)
        count_subjects = df[df.columns[idx:idx+2]].value_counts().to_dict()
        subjects.append(count_subjects)
        print(count_subjects)

    print(dict(zip(*subjects)))
