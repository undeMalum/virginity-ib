from matplotlib import pyplot as plt
import pandas as pd

from src.paths.paths import (
    TOTAL_SUBJECT_LEVELS
)


def fill_percentage_and_value(x):
    print(x)
    return f"{x:.1f}%\n({total*x/100:.0f})"


total_subject_level = pd.read_csv(TOTAL_SUBJECT_LEVELS)
pie_chart = total_subject_level[
    (total_subject_level["Level"] == "Standard Level") & (total_subject_level["Subject"] == "History")
]

pie_chart_values = [pie_chart.to_dict(orient="list")["Virgins"][0], pie_chart.to_dict(orient="list")["Non-virgins"][0]]
total = 0
for value in pie_chart_values:
    total += value
plt.pie(
    pie_chart_values,
    labels=["Virgins", "Non-virgins"],
    autopct=fill_percentage_and_value
)

plt.title("Virginity for History Standard Level")

plt.tight_layout()
plt.show()
