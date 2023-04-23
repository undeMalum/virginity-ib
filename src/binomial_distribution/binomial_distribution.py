import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from src.paths.paths import ALL_ANSWERS

df = pd.read_csv(ALL_ANSWERS)
count_students = df["Virgins"] + df["Non-virgins"]
# print(df.loc[count_students > 900])
percentage = df.loc[count_students > 900]
students_number_subject = df["Virgins"] + df["Non-virgins"]
percentages = df["Virgins"] / students_number_subject * 100
subject_percentage = pd.concat([df["Subject"], percentages], axis="columns")
subject_percentage.columns = ["Subject", "Percentage"]
# print(subject_percentage[count_students > 900])
#
# s = np.random.binomial(10, .5, 1000)
# plt.bar(s)
# plt.show()


from scipy import stats
# import matplotlib.pyplot as plt
# setting the values
# of n and p
n = students_number_subject.loc[subject_percentage["Subject"] == "Mathematics: AA"].item()
p = subject_percentage.loc[subject_percentage["Subject"] == "Mathematics: AA"]["Percentage"].item() / 100


def create_binomial_distribution(n, p):
    # defining list of r values
    r_values = list(range(n + 1))
    # list of pmf values
    dist = [stats.binom.pmf(r, n, p) for r in r_values]
    return r_values, dist


r, d = create_binomial_distribution(n, p)
r2, d2 = create_binomial_distribution(n, 0.412)
# plotting the graph
plt.bar(stats.zscore(r), d)  # stats.zscore(r_values)
plt.bar(stats.zscore(r2), d2)
plt.show()
