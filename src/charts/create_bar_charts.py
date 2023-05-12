from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

from src.paths.paths import (
    TOTAL_SUBJECT_LEVELS,
    ALL_ANSWERS
)
from src.charts.levels import Levels


def create_subject_level_chart(level: Levels):
    total_subject_level = pd.read_csv(TOTAL_SUBJECT_LEVELS)

    bar = total_subject_level.loc[total_subject_level["Level"] == level.value].plot.bar(
        x="Subject",
        y=["Virgins", "Non-virgins"],
        rot=0,
        stacked=True
    )
    bar.set_xlabel("Subjects")
    bar.set_ylabel("Number of students")
    plt.title(f"Virginity across {level.value} subjects")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium',
    )
    plt.tight_layout()
    return plt


def create_all_chart():
    total_subject_level = pd.read_csv(ALL_ANSWERS)

    bar = total_subject_level.plot.bar(
        x="Subject",
        y=["Virgins", "Non-virgins"],
        rot=0,
        stacked=True
    )
    bar.set_xlabel("Subjects")
    bar.set_ylabel("Number of students")
    plt.title("Virginity across all subjects")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium',
    )
    plt.tight_layout()
    return plt


def create_all_chart_percentages():
    total_subject_level = pd.read_csv(ALL_ANSWERS)

    students_number_subject = total_subject_level["Virgins"] + total_subject_level["Non-virgins"]
    percentages = total_subject_level["Virgins"] / students_number_subject
    subject_percentage = pd.concat([total_subject_level["Subject"], percentages], axis="columns")
    subject_percentage.columns = ["Subject", "Percentage"]

    bar = subject_percentage.plot.bar(
        x="Subject",
        y="Percentage",
    )
    bar.set_xlabel("Subjects")
    bar.set_ylabel("Percentage of virgins")
    bar.yaxis.set_major_formatter(PercentFormatter(1))
    bar.legend(["Virgins"])
    plt.title("Virginity percentage across all subjects")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium',
    )
    plt.ylim(0, 1)
    plt.tight_layout()
    return plt


def create_subject_level_chart_percentage(level: Levels):
    total_subject_level = pd.read_csv(TOTAL_SUBJECT_LEVELS)

    subject_from_level = total_subject_level.loc[total_subject_level["Level"] == level.value]
    students_number_subject = subject_from_level["Virgins"] + subject_from_level["Non-virgins"]
    percentages = subject_from_level["Virgins"] / students_number_subject
    subject_percentage = pd.concat([subject_from_level["Subject"], percentages], axis="columns")
    subject_percentage.columns = ["Subject", "Percentage"]

    bar = subject_percentage.plot.bar(
        x="Subject",
        y="Percentage",
    )
    bar.set_xlabel("Subjects")
    bar.set_ylabel("Percentage of virgins")
    bar.yaxis.set_major_formatter(PercentFormatter(1))
    bar.legend(["Virgins"])
    plt.title(f"Virginity percentage across {level.value} subjects")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium',
    )
    plt.ylim(0, 1)
    plt.tight_layout()
    return plt


if __name__ == "__main__":
    # chart = create_subject_level_chart(Levels.HIGHER_LEVEL)
    chart = create_subject_level_chart_percentage(Levels.STANDARD_LEVEL)
    plt.show()
