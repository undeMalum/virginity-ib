from matplotlib import pyplot as plt
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
    plt.title(f"Virginity across all subjects")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium',
    )
    plt.tight_layout()
    return plt


if __name__ == "__main__":
    # chart = create_subject_level_chart(Levels.HIGHER_LEVEL)
    chart = create_all_chart()
    plt.show()
