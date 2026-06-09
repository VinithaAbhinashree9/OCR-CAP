import pandas as pd
import plotly.express as px


class OCRAnalytics:

    def __init__(self):
        pass

    # -----------------------
    # BASIC STATS
    # -----------------------

    def generate_statistics(
            self,
            text):

        characters = len(text)

        words = len(
            text.split()
        )

        digits = sum(
            c.isdigit()
            for c in text
        )

        alphabets = sum(
            c.isalpha()
            for c in text
        )

        return {

            "Characters":
            characters,

            "Words":
            words,

            "Digits":
            digits,

            "Alphabets":
            alphabets
        }

    # -----------------------
    # CONFIDENCE SCORE
    # -----------------------

    def average_confidence(
            self,
            details_df):

        if details_df.empty:
            return 0

        return round(
            details_df[
                "Confidence"
            ].mean(),
            2
        )

    # -----------------------
    # DATAFRAME
    # -----------------------

    def stats_dataframe(
            self,
            stats):

        return pd.DataFrame(
            list(stats.items()),
            columns=[
                "Metric",
                "Value"
            ]
        )

    # -----------------------
    # PIE CHART
    # -----------------------

    def create_pie_chart(
            self,
            stats):

        chart_df = pd.DataFrame({

            "Category": [
                "Digits",
                "Alphabets"
            ],

            "Count": [
                stats["Digits"],
                stats["Alphabets"]
            ]
        })

        fig = px.pie(
            chart_df,
            names="Category",
            values="Count",
            title="Digits vs Alphabets",
            color_discrete_sequence=["#38bdf8", "#a78bfa"],
        )
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#cbd5e1", family="Inter, sans-serif"),
            title_font=dict(size=18, color="#f1f5f9"),
            margin=dict(t=50, b=40, l=40, r=40),
        )

        return fig

    # -----------------------
    # BAR CHART
    # -----------------------

    def create_bar_chart(
            self,
            stats):

        chart_df = pd.DataFrame({

            "Metric": [
                "Characters",
                "Words",
                "Digits",
                "Alphabets"
            ],

            "Value": [
                stats["Characters"],
                stats["Words"],
                stats["Digits"],
                stats["Alphabets"]
            ]
        })

        fig = px.bar(
            chart_df,
            x="Metric",
            y="Value",
            title="OCR Analytics",
            color="Value",
            color_continuous_scale=["#1e3a5f", "#38bdf8"],
        )
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#cbd5e1", family="Inter, sans-serif"),
            title_font=dict(size=18, color="#f1f5f9"),
            margin=dict(t=50, b=40, l=40, r=40),
            showlegend=False,
            coloraxis_showscale=False,
        )

        return fig