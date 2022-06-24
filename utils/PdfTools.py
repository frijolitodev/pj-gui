from turtle import width
from pandas import DataFrame
from pylatex import Document, Section, Subsection, Tabular, Math, Figure, Alignat
from data.classes import LatexSection

from utils.Fs import remove_file


class PdfTools:
    def __init__(self, sections: LatexSection) -> None:
        geometry_options = { "tmargin": "1.5in", "lmargin": "1.5in" }
        self.doc = Document(geometry_options=geometry_options)



    def export_table(self, dataframe: DataFrame, filename: str):
        remove_file(f"{filename}.csv")
        remove_file(f"{filename}.html")

        dataframe.to_csv(f"{filename}.csv")
        dataframe.to_html(f"{filename}.html")

    def write_math(self, text: str):
        with self.doc.create(Alignat(numbering=False, escape=False)) as math:
            math.append(text)

    def write_section(self, name, command):
        with self.doc.create(Section(name)):
            command()

    def write_subsection(self, name, command):
        with self.doc.create(Subsection(name)):
            command()

    def write_plot(self, plot_filename):
        with self.doc.create(Figure(position="h!")) as plot:
            plot.add_image(plot_filename, width="400px")

    def write_graph(self, graph_filename):
        with self.doc.create(Figure(position="h!")) as graph:
            graph.add_image(graph_filename, width="400px")
