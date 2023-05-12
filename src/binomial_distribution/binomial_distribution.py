import math

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from src.paths.paths import ALL_ANSWERS

df = pd.read_csv(ALL_ANSWERS)
count_students = df["Virgins"] + df["Non-virgins"]
percentages = (df["Virgins"] / count_students * 100) / 100
subject_percentage = pd.concat([df["Subject"], percentages], axis="columns")
subject_percentage.columns = ["Subject", "Percentage"]

# setting the values
# of n and p
n = count_students.loc[subject_percentage["Subject"] == "Mathematics: AA"].item()
p = subject_percentage.loc[subject_percentage["Subject"] == "Mathematics: AA"]["Percentage"].item()


def create_binomial_distribution(n, p):
    # defining list of r values
    r_values = list(range(n + 1))
    # list of pmf values
    dist = [stats.binom.pmf(r, n, p) for r in r_values]
    return r_values, dist


r2, d2 = create_binomial_distribution(20, p)  # 0.412)

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-20, 20, 0.01)
# Calculating mean and standard deviation
mean = 20 * p
sd = math.sqrt(20*p*(1-p))

# plotting the graph
bar1, bar2 = plt.subplots()
bar2.bar(r2, d2)  # stats.zscore(r2)
bar2.set_xlabel("Number of virgins")
bar2.set_ylabel("Probability")
bar2.plot(x_axis, stats.norm.pdf(x_axis, mean, sd), color="red")
#plt.bar(r, d)  # stats.zscore(r_values), stats.zscore(r)
plt.show()
