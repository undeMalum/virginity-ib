import math

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

from src.paths.paths import ALL_ANSWERS


def get_virgin_percentage_for_subject(subject: str):
    df = pd.read_csv(ALL_ANSWERS)
    # get the percentage of virgins for each subject
    count_students = df["Virgins"] + df["Non-virgins"]
    percentages = df["Virgins"] / count_students
    subject_percentage = pd.concat([df["Subject"], percentages], axis="columns")
    subject_percentage.columns = ["Subject", "Percentage"]
    # get percentage for the specified subject
    virgin_p = subject_percentage.loc[subject_percentage["Subject"] == subject]["Percentage"].item()
    return virgin_p


def create_binomial_distribution(n: int, p: int):
    # list of all number of successes less or equal to n
    s_val = list(range(n + 1))
    # list of pmf values
    dist = [stats.binom.pmf(s, n, p) for s in s_val]
    return s_val, dist


# setting the values for binomial distribution: n (number of students in an imaginary class)
# and p (percentage of virgins)
number_of_students = 20
virgin_percentage = get_virgin_percentage_for_subject("Mathematics: AA")
number_of_successes, distribution = create_binomial_distribution(number_of_students, virgin_percentage)

# plot for bell curve
x_axis = np.arange(0, number_of_students, 0.01)
# calculate mean and standard deviation
mean = number_of_students * virgin_percentage
standard_deviation = math.sqrt(number_of_students * virgin_percentage * (1 - virgin_percentage))

if __name__ == "__main__":
    # plotting the graph
    binom_dist, bell_curve = plt.subplots()
    bell_curve.bar(number_of_successes, distribution)
    bell_curve.set_xlabel("Number of virgins")
    bell_curve.set_ylabel("Probability")
    bell_curve.plot(x_axis, stats.norm.pdf(x_axis, mean, standard_deviation), color="red")
    plt.show()
