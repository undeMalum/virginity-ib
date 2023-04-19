from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

ANSWERS_CSV = BASE_DIR.joinpath("survey_answers.csv")
TOTAL_VIRGINS_SUBJECT_LEVEL = BASE_DIR.joinpath("results_csvs/total_virgins_subject_level.csv")
TOTAL_NONVIRGINS_SUBJECT_LEVEL = BASE_DIR.joinpath("results_csvs/total_nonvirgins_subject_level.csv")
TOTAL_SUBJECT_LEVELS = BASE_DIR.joinpath("results_csvs/subject_level.csv")
ALL_ANSWERS = BASE_DIR.joinpath("results_csvs/all_answers.csv")
DP1_SUBJECT_LEVELS = BASE_DIR.joinpath("results_csvs/subject_level_dp1.csv")
DP2_SUBJECT_LEVELS = BASE_DIR.joinpath("results_csvs/subject_level_dp2.csv")

PDF = BASE_DIR.joinpath("charts/results.pdf")

if __name__ == "__main__":
    print(
        ANSWERS_CSV,
        TOTAL_VIRGINS_SUBJECT_LEVEL,
        TOTAL_NONVIRGINS_SUBJECT_LEVEL,
        TOTAL_SUBJECT_LEVELS,
        ALL_ANSWERS,
        DP1_SUBJECT_LEVELS,
        DP2_SUBJECT_LEVELS,
        PDF,
        sep="\n"
    )
