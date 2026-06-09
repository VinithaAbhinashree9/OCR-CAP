import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


class ExportUtils:

    # -------------------------
    # EXPORT TXT
    # -------------------------

    @staticmethod
    def export_txt(
            text,
            output_path):

        with open(
                output_path,
                "w",
                encoding="utf-8") as f:

            f.write(text)

        return output_path

    # -------------------------
    # EXPORT CSV
    # -------------------------

    @staticmethod
    def export_csv(
            dataframe,
            output_path):

        dataframe.to_csv(
            output_path,
            index=False
        )

        return output_path

    # -------------------------
    # EXPORT PDF
    # -------------------------

    @staticmethod
    def export_pdf(
            text,
            statistics,
            output_path):

        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter
        )

        styles = getSampleStyleSheet()

        elements = []

        title = Paragraph(
            "OCR Analysis Report",
            styles["Title"]
        )

        elements.append(title)
        elements.append(
            Spacer(1, 12)
        )

        elements.append(
            Paragraph(
                "<b>Extracted Text</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

        elements.append(
            Paragraph(
                "<b>Statistics</b>",
                styles["Heading2"]
            )
        )

        for key, value in statistics.items():

            elements.append(
                Paragraph(
                    f"{key}: {value}",
                    styles["BodyText"]
                )
            )

        doc.build(elements)

        return output_path