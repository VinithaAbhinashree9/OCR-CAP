from export_utils import ExportUtils
import pandas as pd

sample_text = """
Name Rahul
Roll No 1254
Marks 89
"""

stats = {
    "Characters": 30,
    "Words": 5,
    "Digits": 6,
    "Alphabets": 18
}

df = pd.DataFrame({
    "Text": ["Rahul", "1254", "89"],
    "Confidence": [98, 96, 95]
})

ExportUtils.export_txt(
    sample_text,
    "outputs/result.txt"
)

ExportUtils.export_csv(
    df,
    "outputs/result.csv"
)

ExportUtils.export_pdf(
    sample_text,
    stats,
    "outputs/result.pdf"
)

print("Export Successful")