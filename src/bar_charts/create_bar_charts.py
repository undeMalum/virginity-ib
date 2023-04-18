from matplotlib import pyplot as plt
import pandas as pd

from src.paths.paths import (
    TOTAL_VIRGINS_SUBJECT_LEVEL,
    TOTAL_NONVIRGINS_SUBJECT_LEVEL
)

total_virgins = pd.read_csv(TOTAL_VIRGINS_SUBJECT_LEVEL)
total_nonvirgins = pd.read_csv(TOTAL_NONVIRGINS_SUBJECT_LEVEL)
joined_virgins_and_nonvirgins = pd.concat([total_virgins, total_nonvirgins["Count"]], axis="columns")
cln_names = ["Subject", "Level", "Virgin Count", "Non-virgin Count"]
joined_virgins_and_nonvirgins.columns = cln_names
print(joined_virgins_and_nonvirgins)
# ["Subject", "Level"]
bar = joined_virgins_and_nonvirgins.loc[joined_virgins_and_nonvirgins["Level"] == "Standard Level"].plot.bar(
    x="Subject",
    y=["Virgin Count", "Non-virgin Count"],
    rot=0,
    stacked=True
)
plt.show()
