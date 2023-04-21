from matplotlib import pyplot as plt
import pandas as pd

from src.paths.paths import (
    TOTAL_SUBJECT_LEVELS,
    ALL_ANSWERS,
    ANSWERS_CSV
)
from src.charts.levels import Levels


def get_all_subjects(csv_file):
    all_csv = pd.read_csv(csv_file)
    subjects = [subject for subject in all_csv["Subject"]]
    return subjects


def create_pie_chart_all():
    def fill_percentage_and_value(x):
        return f"{x:.1f}%\n({total * x / 100:.0f})"

    total_subject_level = pd.read_csv(ANSWERS_CSV)
    virgins = total_subject_level.loc[total_subject_level['Virginity'] == "Yes",
                                      total_subject_level.columns[1]].value_counts().to_dict()
    nonvirgins = total_subject_level.loc[total_subject_level['Virginity'] == "No",
                                         total_subject_level.columns[1]].value_counts().to_dict()
    pie_chart_values = [virgins["Yes"], nonvirgins["No"]]
    total = pie_chart_values[0] + pie_chart_values[1]
    plt.pie(
        pie_chart_values,
        labels=["Virgins", "Non-virgins"],
        autopct=fill_percentage_and_value
    )

    plt.title(f"Virginity")

    plt.tight_layout()

    return plt


def create_pie_chart_subject(subject: str):
    def fill_percentage_and_value(x):
        return f"{x:.1f}%\n({total * x / 100:.0f})"

    total_subject = pd.read_csv(ALL_ANSWERS)
    pie_chart = total_subject.loc[total_subject["Subject"] == subject]

    pie_chart_values = [pie_chart.to_dict(orient="list")["Virgins"][0],
                        pie_chart.to_dict(orient="list")["Non-virgins"][0]]
    total = 0
    for value in pie_chart_values:
        total += value
    plt.pie(
        pie_chart_values,
        labels=["Virgins", "Non-virgins"],
        autopct=fill_percentage_and_value
    )

    plt.title(f"Virginity for {subject}")

    plt.tight_layout()

    return plt


def create_pie_chart_subject_level(subject: str, level: Levels):
    def fill_percentage_and_value(x):
        return f"{x:.1f}%\n({total * x / 100:.0f})"

    total_subject_level = pd.read_csv(TOTAL_SUBJECT_LEVELS)
    pie_chart = total_subject_level[
        (total_subject_level["Level"] == level.value) & (total_subject_level["Subject"] == subject)
    ]
    if pie_chart.empty:
        return

    pie_chart_values = [pie_chart.to_dict(orient="list")["Virgins"][0],
                        pie_chart.to_dict(orient="list")["Non-virgins"][0]]
    total = 0
    for value in pie_chart_values:
        total += value
    plt.pie(
        pie_chart_values,
        labels=["Virgins", "Non-virgins"],
        autopct=fill_percentage_and_value
    )

    plt.title(f"Virginity for {subject} {level.value}")

    plt.tight_layout()

    return plt


if __name__ == "__main__":
    sub = get_all_subjects(ALL_ANSWERS)
    create_pie_chart_subject(sub[9])
    plt.show()
