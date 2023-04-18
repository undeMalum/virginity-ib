from matplotlib import pyplot as plt
import pandas as pd

from src.paths.paths import (
    TOTAL_SUBJECT_LEVELS
)

total_subject_level = pd.read_csv(TOTAL_SUBJECT_LEVELS)

bar = total_subject_level.loc[total_subject_level["Level"] == "Standard Level"].plot.bar(
    x="Subject",
    y=["Virgins", "Non-virgins"],
    rot=0,
    stacked=True
)
plt.title("Virginity across Standard Level subjects")
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='medium',
)
plt.tight_layout()
plt.show()
