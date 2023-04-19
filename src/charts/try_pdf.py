import datetime
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt

from src.charts.levels import Levels
from src.paths.paths import PDF, ALL_ANSWERS
from src.charts.create_bar_charts import create_subject_level_chart, create_all_chart
from src.charts.create_pie_charts import (
    create_pie_chart_subject_level,
    create_pie_chart_subject,
    get_all_subjects,
    create_pie_chart_all
)

# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.
with PdfPages(PDF) as pdf:
    plt.rcParams['text.usetex'] = False

    chart = create_all_chart()
    pdf.savefig()  # saves the current figure into a pdf page
    chart.close()

    chart = create_pie_chart_all()
    pdf.savefig()  # saves the current figure into a pdf page
    chart.close()

    for level in Levels:
        chart = create_subject_level_chart(level)
        pdf.savefig()  # saves the current figure into a pdf page
        chart.close()

    subjects = get_all_subjects(ALL_ANSWERS)
    for subject in subjects:
        for level in Levels:
            chart = create_pie_chart_subject_level(subject, level)
            if chart is not None:
                pdf.savefig()  # saves the current figure into a pdf page
                chart.close()
        chart = create_pie_chart_subject(subject)
        pdf.savefig()  # saves the current figure into a pdf page
        chart.close()



    # We can also set the file's metadata via the PdfPages object:
    d = pdf.infodict()
    d['Title'] = "Virginity in IBDP"
    d['Author'] = "Mateusz Konat"
    d['Subject'] = "Virginity across different subjects of IBDP"
    d['Keywords'] = "IBDP virginity statistics"
    d['CreationDate'] = datetime.datetime.today()
    d['ModDate'] = datetime.datetime.today()
