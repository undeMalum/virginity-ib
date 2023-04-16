from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
ANSWERS_CSV = BASE_DIR.joinpath("survey_answers.csv")

if __name__ == "__main__":
    print(ANSWERS_CSV)
