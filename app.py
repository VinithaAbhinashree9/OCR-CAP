import os

# Fix: OMP Error #15 — multiple OpenMP runtimes (PyTorch/EasyOCR vs OpenCV)
# linked into the same process on Windows. This env var must be set before
# any library that loads libiomp5md.dll is imported.
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import streamlit as st

# Ensure working directories exist before any file operations
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

import pandas as pd
from PIL import Image

from image_processor import ImageProcessor
from ocr_engine import OCREngine
from analytics import OCRAnalytics
from export_utils import ExportUtils


# Cache heavy objects so they are built once per session,
# not on every file upload.
@st.cache_resource
def load_ocr_engine():
    return OCREngine()

@st.cache_resource
def load_image_processor():
    return ImageProcessor()

@st.cache_resource
def load_analytics():
    return OCRAnalytics()

st.set_page_config(
    page_title="AI OCR Studio",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg-base: #0b0f19;
    --bg-elevated: #131a2b;
    --bg-card: rgba(19, 26, 43, 0.85);
    --border: rgba(148, 163, 184, 0.12);
    --border-hover: rgba(56, 189, 248, 0.35);
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent: #38bdf8;
    --accent-soft: rgba(56, 189, 248, 0.12);
    --accent-glow: rgba(56, 189, 248, 0.25);
    --purple: #a78bfa;
    --success: #34d399;
    --radius-lg: 20px;
    --radius-md: 14px;
    --shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
}

#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(56, 189, 248, 0.08), transparent),
        radial-gradient(ellipse 60% 40% at 100% 0%, rgba(167, 139, 250, 0.06), transparent),
        var(--bg-base);
    font-family: 'Inter', sans-serif;
    color: var(--text-primary);
}

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1220 0%, #0b0f19 100%);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] h1 {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    letter-spacing: -0.01em;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
}

/* ── Hero ── */
.hero-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #131a2b 0%, #0f1525 50%, #131a2b 100%);
    padding: 2.5rem 2.75rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
    margin-bottom: 2rem;
}

.hero-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, var(--accent-glow), transparent 70%);
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    background: var(--accent-soft);
    color: var(--accent);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.2);
    margin-bottom: 1rem;
}

.hero-card h1 {
    color: var(--text-primary) !important;
    font-weight: 800 !important;
    font-size: 2.25rem !important;
    letter-spacing: -0.03em;
    margin: 0 0 0.5rem 0 !important;
    line-height: 1.15;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: var(--text-secondary);
    margin: 0;
    max-width: 640px;
    line-height: 1.6;
}

/* ── Metric cards ── */
.metric-card {
    background: var(--bg-card);
    backdrop-filter: blur(12px);
    padding: 1.4rem 1rem;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    text-align: center;
    transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
    margin-bottom: 0.5rem;
}

.metric-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
}

.metric-number {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), var(--purple));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.03em;
    line-height: 1.2;
}

.metric-title {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-top: 0.4rem;
}

/* ── Section cards ── */
.section-card {
    background: var(--bg-card);
    backdrop-filter: blur(12px);
    padding: 1.75rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    margin-bottom: 1.5rem;
}

.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.35rem;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    background: var(--bg-card);
    border: 1px dashed rgba(148, 163, 184, 0.2);
    border-radius: var(--radius-lg);
    margin-top: 1rem;
}

.empty-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    opacity: 0.7;
}

.empty-state h3 {
    color: var(--text-primary);
    font-weight: 600;
    margin: 0 0 0.5rem 0;
}

.empty-state p {
    color: var(--text-muted);
    margin: 0;
    font-size: 0.95rem;
}

/* ── Sidebar info panel ── */
.info-panel {
    background: var(--accent-soft);
    border: 1px solid rgba(56, 189, 248, 0.15);
    border-radius: var(--radius-md);
    padding: 1rem 1.1rem;
    margin-top: 1rem;
}

.info-panel h4 {
    color: var(--accent);
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin: 0 0 0.6rem 0;
}

.info-panel ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

.info-panel li {
    color: var(--text-secondary);
    font-size: 0.88rem;
    padding: 0.3rem 0;
    padding-left: 1.2rem;
    position: relative;
}

.info-panel li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: var(--success);
    font-weight: 700;
    font-size: 0.75rem;
}

/* ── Streamlit component overrides ── */
h2, h3, .stSubheader {
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em;
}

.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-elevated);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
    border: 1px solid var(--border);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: var(--text-muted);
    font-weight: 500;
    font-size: 0.88rem;
    padding: 0.5rem 1rem;
    background: transparent;
    border: none;
}

.stTabs [aria-selected="true"] {
    background: var(--accent-soft) !important;
    color: var(--accent) !important;
    border: 1px solid rgba(56, 189, 248, 0.2) !important;
}

.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.25rem;
}

div[data-testid="stFileUploader"] {
    background: var(--bg-elevated);
    border: 1px dashed rgba(148, 163, 184, 0.25);
    border-radius: var(--radius-md);
    padding: 0.5rem;
    transition: border-color 0.2s;
}

div[data-testid="stFileUploader"]:hover {
    border-color: var(--border-hover);
}

div[data-testid="stFileUploader"] label,
div[data-testid="stFileUploader"] small {
    color: var(--text-secondary) !important;
}

.stTextArea textarea {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
    font-size: 0.9rem !important;
}

.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px var(--accent-soft) !important;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    overflow: hidden;
}

.stSuccess {
    background: rgba(52, 211, 153, 0.1) !important;
    color: var(--success) !important;
    border: 1px solid rgba(52, 211, 153, 0.2);
    border-radius: var(--radius-md);
}

.stDownloadButton button {
    background: linear-gradient(135deg, #1e40af, #38bdf8) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: opacity 0.2s, transform 0.2s !important;
}

.stDownloadButton button:hover {
    opacity: 0.9;
    transform: translateY(-1px);
}

hr {
    border-color: var(--border) !important;
    margin: 1.25rem 0 !important;
}

/* Hide default info box — we use custom panel */
section[data-testid="stSidebar"] .stAlert { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <div class="hero-badge">AI-Powered OCR</div>
    <h1>AI OCR Studio</h1>
    <p class="hero-subtitle">
        Extract text from handwritten digits, alphabets, notes, and printed documents
        with real-time analytics and export.
    </p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Control Panel")

    uploaded_file = st.file_uploader(
        "Upload an image to begin",
        type=["png", "jpg", "jpeg","webp"],
        help="Supported formats: PNG, JPG, JPEG,webp",
    )

    st.markdown("---")

    st.markdown("""
    <div class="info-panel">
        <h4>Supported Inputs</h4>
        <ul>
            <li>Handwritten Digits</li>
            <li>Alphabets</li>
            <li>Notes &amp; Sketches</li>
            <li>Printed Documents</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if not uploaded_file:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">📷</div>
        <h3>No image uploaded yet</h3>
        <p>Use the sidebar to upload a PNG, JPG, or JPEG file to start OCR processing.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="section-label">Input</div>', unsafe_allow_html=True)
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    image.save("uploads/input.png")

    processor = load_image_processor()
    processed = processor.preprocess("uploads/input.png")
    processor.save_processed_image(processed, "outputs/processed.png")

    with col2:
        st.markdown('<div class="section-label">Pipeline</div>', unsafe_allow_html=True)
        st.subheader("Processed Image")
        st.image("outputs/processed.png", use_container_width=True)

    ocr = load_ocr_engine()
    text = ocr.extract_text("outputs/processed.png")
    details = ocr.extract_details("outputs/processed.png")

    analytics = load_analytics()
    stats = analytics.generate_statistics(text)
    confidence = analytics.average_confidence(details)

    st.markdown('<div class="section-label" style="margin-top:1.5rem">Overview</div>', unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5, gap="medium")

    metrics = [
        ("Words", stats["Words"]),
        ("Characters", stats["Characters"]),
        ("Digits", stats["Digits"]),
        ("Alphabets", stats["Alphabets"]),
        ("Confidence", f"{confidence}%"),
    ]

    for col, (title, val) in zip([c1, c2, c3, c4, c5], metrics):
        col.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{val}</div>
            <div class="metric-title">{title}</div>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Extracted Text",
        "Analytics",
        "OCR Details",
        "Export",
    ])

    with tab1:
        st.markdown("#### Extracted Content")
        st.text_area("extracted_text", text, height=300, label_visibility="collapsed")

    with tab2:
        chart_col1, chart_col2 = st.columns(2, gap="large")
        with chart_col1:
            st.plotly_chart(analytics.create_bar_chart(stats), use_container_width=True)
        with chart_col2:
            st.plotly_chart(analytics.create_pie_chart(stats), use_container_width=True)

    with tab3:
        st.dataframe(details, use_container_width=True, hide_index=True)

    with tab4:
        st.markdown("#### Download Results")

        txt_path = ExportUtils.export_txt(text, "outputs/result.txt")
        csv_path = ExportUtils.export_csv(details, "outputs/result.csv")
        pdf_path = ExportUtils.export_pdf(text, stats, "outputs/result.pdf")

        st.success("All export files generated successfully.")

        dl1, dl2, dl3 = st.columns(3, gap="medium")
        with dl1:
            with open(txt_path, "rb") as f:
                st.download_button("Download TXT", f, file_name="result.txt", use_container_width=True)
        with dl2:
            with open(csv_path, "rb") as f:
                st.download_button("Download CSV", f, file_name="result.csv", use_container_width=True)
        with dl3:
            with open(pdf_path, "rb") as f:
                st.download_button("Download PDF", f, file_name="result.pdf", use_container_width=True)