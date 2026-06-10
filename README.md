# AI OCR Studio 
###  Live Demo

 **Try the Application Here:**

[Streamlit App](https://ocr-cap-54mqstc2npveuhwrjysytn.streamlit.app/)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/OCR-AI_Powered-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenCV-Image_Processing-orange?style=for-the-badge" />
</p>

An AI-powered Optical Character Recognition (OCR) application that extracts text from handwritten and printed documents using advanced image preprocessing and character recognition techniques. Built with Streamlit for an interactive user experience and designed for educational, business, and research applications.

---

##  Application Preview

### Dashboard Interface

![Dashboard](https://github.com/user-attachments/assets/243ec8a7-244b-4456-8709-0b0e00164bcd)

### OCR Results & Analytics

![OCR Results](https://github.com/user-attachments/assets/1ea1540b-e33b-467c-8c45-8d9edde7f8bd)

---

##  Features

###  OCR Text Extraction
- Extract text from images and scanned documents
- Handwritten character recognition
- Printed text recognition
- Multi-format image support
- Real-time OCR processing

###  Image Preprocessing
- Grayscale conversion
- Noise reduction
- Thresholding
- Contrast enhancement
- OCR optimization

###  Analytics Dashboard
- Character count
- Word count
- Line count
- OCR statistics
- Recognition performance metrics

###  Export Functionality
- Export extracted text to TXT
- Generate PDF reports
- Save OCR results for future use

### Modern User Interface
- Interactive Streamlit dashboard
- Drag-and-drop file upload
- Instant OCR results
- Responsive design


### Project Architecture

```text
AI_OCR_CHARACTER_RECOGNITION/
│
├── .streamlit/
│
├── uploads/
│   └── Uploaded Images
│
├── outputs/
│   └── Exported OCR Results
│
├── app.py
├── analytics.py
├── digit_recognizer.py
├── image_processor.py
├── ocr_engine.py
├── export_utils.py
├── requirements.txt
├── Dockerfile
├── README.md
└── test.py
```

---

##  Module Description

### app.py

Main Streamlit Application.

Responsibilities:

- User Interface
- File Upload
- OCR Processing
- Result Display
- Analytics Visualization

---

### image_processor.py

Handles image preprocessing operations:

- Grayscale Conversion
- Noise Removal
- Thresholding
- Image Enhancement
- Edge Detection

---

### digit_recognizer.py

Deep Learning model for handwritten digit recognition.

Features:

- CNN-based Recognition
- MNIST-trained Model
- Confidence Prediction

---

### ocr_engine.py

Core OCR engine.

Supports:

- Printed Text Recognition
- Handwritten Text Recognition
- Character Detection
- Text Extraction

---

### analytics.py

Generates OCR insights:

- Character Count
- Word Count
- Confidence Analysis
- Recognition Statistics

---

### export_utils.py

Export recognized text into:

- TXT Files
- Structured Reports

---

##  Technologies Used

### Programming Language

- Python 3.10+

### Machine Learning

- TensorFlow
- Keras
- NumPy

### OCR

- EasyOCR
- Tesseract OCR

### Image Processing

- OpenCV
- Pillow

### Data Analysis

- Pandas

### Frontend

- Streamlit

### Visualization

- Plotly
- Matplotlib

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/OCR-CAP.git

cd AI-OCR-Character-Recognition
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

This application is deployed using Streamlit Community Cloud.

### Access the App

🔗 https://ocr-cap-54mqstc2npveuhwrjysytn.streamlit.app/
---

##  Workflow

```text
Upload Image
      │
      ▼
Image Preprocessing
      │
      ▼
OCR Engine
      │
      ▼
Character Detection
      │
      ▼
Text Recognition
      │
      ▼
Analytics Generation
      │
      ▼
Export Results
```

---

##  Future Enhancements

- PDF OCR Support
- Multi-language Recognition
- Real-time Camera OCR
- Document Classification
- AI-Powered Text Summarization
- RAG-Based Question Answering
- Cloud Deployment

---

##  Use Cases

### Education

- Handwritten Notes Digitization
- Assignment Evaluation

### Business

- Invoice Processing
- Document Digitization

### Research

- Historical Document Analysis
- Data Extraction

### Personal Use

- Note Scanning
- Text Archiving

---

## Sample Output

Input Image:

- Handwritten Notes
- Printed Documents
- Mixed Content

Output:

```text
Recognized Text:
-----------------
Hello World
AI OCR System

Confidence Score:
96.4%
```

---

##  Requirements

- Python 3.10+
- Streamlit
- TensorFlow
- OpenCV
- EasyOCR
- Pandas
- Pillow

---

##  Author

**Vinitha Abhinashree M**

BCA Graduate | IIT Madras BS Data Science Student

AI • Machine Learning • Computer Vision • OCR • Generative AI

---

## Project Highlights

- Deep Learning-Based OCR
- Modern Streamlit Dashboard
- Analytics Integration
- Export Functionality
- Docker Support
- Production-Ready Architecture

---

### If you like this project, don't forget to ⭐ the repository!
