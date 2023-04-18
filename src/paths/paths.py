from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

ANSWERS_CSV = BASE_DIR.joinpath("survey_answers.csv")
TOTAL_VIRGINS_SUBJECT_LEVEL = BASE_DIR.joinpath("results_csvs/total_virgins_subject_level.csv")
TOTAL_NONVIRGINS_SUBJECT_LEVEL = BASE_DIR.joinpath("results_csvs/total_nonvirgins_subject_level.csv")

if __name__ == "__main__":
    print(
        ANSWERS_CSV,
        TOTAL_VIRGINS_SUBJECT_LEVEL,
        TOTAL_NONVIRGINS_SUBJECT_LEVEL
    )
