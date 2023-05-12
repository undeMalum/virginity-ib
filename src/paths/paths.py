from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

ANSWERS_CSV = BASE_DIR.joinpath("survey_answers.csv")
TOTAL_SUBJECT_LEVELS = BASE_DIR.joinpath("results_csvs/subject_level.csv")
ALL_ANSWERS = BASE_DIR.joinpath("results_csvs/all_answers.csv")

PDF = BASE_DIR.joinpath("charts/results.pdf")

if __name__ == "__main__":
    print(
        ANSWERS_CSV,
        TOTAL_SUBJECT_LEVELS,
        ALL_ANSWERS,
        PDF,
        sep="\n"
    )
