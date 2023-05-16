import datetime

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt

from src.charts.levels import Levels
from src.paths.paths import PDF, ALL_ANSWERS
from src.charts.create_bar_charts import (
    create_subject_level_chart,
    create_all_chart,
    create_all_chart_percentages,
    create_subject_level_chart_percentage
)
from src.charts.create_pie_charts import (
    create_pie_chart_subject_level,
    create_pie_chart_subject,
    get_all_subjects,
    create_pie_chart_all,
)

# create the summary PDF
with PdfPages(PDF) as pdf:
    plt.rcParams['text.usetex'] = False

    chart = create_pie_chart_all()
    pdf.savefig()
    chart.close()

    chart = create_all_chart()
    pdf.savefig()
    chart.close()

    chart = create_all_chart_percentages()
    pdf.savefig()
    chart.close()

    for level in Levels:
        chart = create_subject_level_chart(level)
        pdf.savefig()
        chart.close()

    for level in Levels:
        chart = create_subject_level_chart_percentage(level)
        pdf.savefig()
        chart.close()

    only_sl_subject = ("ES&S", "Language ab initio", "World religions")
    subjects = get_all_subjects(ALL_ANSWERS)
    for subject in subjects:
        for level in Levels:
            if subject not in only_sl_subject or (subject in only_sl_subject and level != Levels.HIGHER_LEVEL):
                chart = create_pie_chart_subject_level(subject, level)
                if chart is not None:
                    pdf.savefig()
                    chart.close()
        chart = create_pie_chart_subject(subject)
        pdf.savefig()
        chart.close()

    # set metadata for the PDF
    d = pdf.infodict()
    d['Title'] = "Virginity in IBDP"
    d['Author'] = "Mateusz Konat"
    d['Subject'] = "Virginity across different subjects of IBDP"
    d['Keywords'] = "IBDP virginity statistics"
    d['CreationDate'] = datetime.datetime(2023, 4, 27)
    d['ModDate'] = datetime.datetime.today()
