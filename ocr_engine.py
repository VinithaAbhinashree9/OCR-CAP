import easyocr
import pandas as pd


class OCREngine:

    def __init__(self):
        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    # -------------------------
    # EXTRACT TEXT
    # -------------------------

    def extract_text(self, image_path):

        results = self.reader.readtext(
            image_path
        )

        extracted_text = []

        for result in results:
            extracted_text.append(result[1])

        return " ".join(extracted_text)

    # -------------------------
    # DETAILED RESULTS
    # -------------------------

    def extract_details(self, image_path):

        results = self.reader.readtext(
            image_path
        )

        data = []

        for result in results:

            bbox = result[0]
            text = result[1]
            confidence = result[2]

            data.append({
                "Text": text,
                "Confidence": round(
                    confidence * 100,
                    2
                )
            })

        return pd.DataFrame(data)

    # -------------------------
    # COUNT DIGITS
    # -------------------------

    def count_digits(
            self,
            extracted_text):

        digits = [
            ch for ch in extracted_text
            if ch.isdigit()
        ]

        return len(digits)

    # -------------------------
    # COUNT ALPHABETS
    # -------------------------

    def count_alphabets(
            self,
            extracted_text):

        alphabets = [
            ch for ch in extracted_text
            if ch.isalpha()
        ]

        return len(alphabets)

    # -------------------------
    # OCR SUMMARY
    # -------------------------

    def generate_summary(
            self,
            extracted_text):

        return {

            "Characters":
            len(extracted_text),

            "Words":
            len(
                extracted_text.split()
            ),

            "Digits":
            self.count_digits(
                extracted_text
            ),

            "Alphabets":
            self.count_alphabets(
                extracted_text
            )
        }