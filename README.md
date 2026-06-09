#  AI OCR Character Recognition System
<div align="center">

# 🔍 AI OCR Studio

##  Overview

AI OCR Character Recognition System is a powerful web-based application built using **Python** and **Streamlit** that extracts text from images using Optical Character Recognition (OCR) technology.
### Intelligent Handwritten & Printed Text Recognition System
<img width="1918" height="862" alt="image" src="https://github.com/user-attachments/assets/243ec8a7-244b-4456-8709-0b0e00164bcd" />
<img width="1918" height="867" alt="image" src="https://github.com/user-attachments/assets/1ea1540b-e33b-467c-8c45-8d9edde7f8bd" />

# 📄 AI OCR Character Recognition System

<div align="center">

The application supports:

* 🔤 Character Recognition
* 📝 Text Extraction from Images
* 🔢 Handwritten & Printed Text Recognition
* 📊 OCR Analytics Dashboard
* 📄 Export Results (TXT/PDF)
* 🖼️ Image Preprocessing
* ⚡ Real-Time OCR Processing

This project is designed for students, researchers, businesses, and developers who need automated text extraction from images and scanned documents.

---
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red.svg)
![OCR](https://img.shields.io/badge/OCR-AI%20Powered-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


##  Features

###  OCR Text Extraction

* Extract text from images
* Detect printed and handwritten text
* Support for multiple image formats
* High accuracy recognition

###  Image Processing

* Grayscale conversion
* Noise reduction
* Thresholding
* Image enhancement
* OCR optimization

###  Analytics Dashboard

* Character count
* Word count
* Line count
* Processing statistics
* OCR confidence analysis

###  Export Options

* Export extracted text to TXT
* Export OCR reports
* Save processed results

###  Interactive Web Interface

* Streamlit-based UI
* Drag-and-drop image upload
* Real-time processing
* User-friendly dashboard

---

##  Project Architecture

```text
AI_OCR_CHARACTER_RECOGNITION/
│
├── .streamlit/
│
├── uploads/
│   └── Uploaded images
│
├── outputs/
│   └── OCR results
│
├── analytics.py
│   └── OCR analytics and statistics
│
├── app.py
│   └── Main Streamlit application
│
├── digit_recognizer.py
│   └── Character and digit recognition
│
├── export_utils.py
│   └── Export TXT/PDF utilities
│
├── image_processor.py
│   └── Image preprocessing functions
│
├── ocr_engine.py
│   └── OCR extraction engine
│
├── Dockerfile
│   └── Container deployment
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Core Programming     |
| Streamlit           | Web Application      |
| OpenCV              | Image Processing     |
| EasyOCR / Tesseract | OCR Engine           |
| Pandas              | Data Analysis        |
| ReportLab           | PDF Export           |
| Pillow              | Image Handling       |
| NumPy               | Numerical Processing |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_OCR_CHARACTER_RECOGNITION.git

cd AI_OCR_CHARACTER_RECOGNITION
```

###  Create Virtual Environment

```bash
python -m venv env
```

### Windows

```bash
env\Scripts\activate
```

### Linux/Mac

```bash
source env/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📸 How It Works

### Step 1

Upload an image

Supported formats:

```text
PNG
JPG
JPEG
BMP
```

### Step 2

Image preprocessing:

* Resize
* Denoise
* Grayscale
* Thresholding

### Step 3

OCR Engine extracts text

### Step 4

Analytics generated:

* Characters
* Words
* Lines
* Processing metrics

### Step 5

Export results

* TXT
* PDF

---

##  OCR Analytics Example

```text
Extracted Text: Hello World

Characters: 11
Words: 2
Lines: 1

Confidence Score: 97%
```

---

##  Docker Support

Build Docker Image

```bash
docker build -t ai-ocr .
```

Run Container

```bash
docker run -p 8501:8501 ai-ocr
```

---

##  Example Workflow

```text
Upload Image
      ↓
Image Processing
      ↓
OCR Extraction
      ↓
Analytics Generation
      ↓
Export Results
```

---

##  Use Cases

### Education

* Digitize notes
* Extract textbook content
* Research document processing

### Business

* Invoice OCR
* Form digitization
* Document management

### Healthcare

* Medical record extraction
* Prescription digitization

### Government

* Archive digitization
* Record management

---

##  Future Enhancements

* Multi-language OCR
* AI-powered text correction
* Handwriting recognition
* Document summarization
* Translation support
* Cloud deployment
* Database integration

---

##  Author

**Vinitha Abhinashree M**

BCA Graduate | IIT Madras BS in Data Science Student

AI • Machine Learning • OCR • Computer Vision • Data Science

---

##  Project Highlights

✅ OCR Text Recognition

✅ Character Detection

✅ Image Preprocessing

✅ Analytics Dashboard

✅ Export Functionality

✅ Streamlit Web Application

✅ Docker Deployment

---

##  License

This project is licensed under the MIT License.


### 🌟 If you found this project useful, don't forget to Star the Repository! ⭐

