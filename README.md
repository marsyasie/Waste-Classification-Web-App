
# AI-Powered Waste Classification Web App

A web application that classifies waste from uploaded images using a Convolutional Neural Network (CNN) with MobileNetV2 architecture.

## 📌 Overview

This project presents an AI-powered web application that helps users identify waste types from uploaded images. The system classifies waste into **12 distinct classes** and groups them into four main categories:

- ♻️ **Recyclable**
- 🗑️ **Non-recyclable**
- ⚠️ **Hazardous**
- 👕 **Donation**

The best model using the **Adam optimizer** achieved **91.30% test accuracy** with MobileNetV2 architecture.

---

## 🗂️ Project Structure

```
waste_web/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── templates/
│   ├── index.html         # Home page
│   ├── classify.html      # Upload page
│   ├── result.html        # Result page
│   └── bins.html          # Bin info page
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   └── images/            # Image assets
└── models/
    └── waste_type_adam.keras  # Trained model (download separately)
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/waste_web.git
cd waste_web
```

### 2. Download the model

Due to file size limits, the trained model is not included in this repository.

📥 **Download model here:** [Google Drive Link]

Place the file in the `models/` folder:
```
models/waste_type_adam.keras
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Access the web app

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

- **Architecture:** MobileNetV2 (transfer learning)
- **Optimizer:** Adam
- **Dataset:** 15,515 images, 12 classes
- **Input Size:** 128×128 pixels

---

## 🖥️ Web App Features

- **Home Page** — Introduction and navigation
- **Upload Page** — Drag & drop or browse image
- **Result Page** — Waste class, category, confidence score, top 3 predictions
- **Bin Info Page** — General bin colour reference
- **View All 12 Classes** — Full confidence scores for all classes

---

## 🛠️ Technologies Used

- **Backend:** Flask (Python)
- **Machine Learning:** TensorFlow / Keras, MobileNetV2
- **Image Processing:** Pillow, NumPy
- **Frontend:** HTML, CSS, Bootstrap
- **Evaluation:** Scikit-learn

---

## 📚 Dataset

- **Source:** Kaggle — Garbage Classification (12 classes)
- **Images:** 15,515 images
- **Classes:** paper, plastic, metal, cardboard, biological, green-glass, brown-glass, white-glass, clothes, shoes, batteries, trash

---

## 👩‍🎓 Author
📧 marsyasie4@gmail.com  


---

## 📄 License

This project is for academic purposes as part of the Final Year Project (FYP) at UiTM.

---

## 🙏 Acknowledgements

- Kaggle for the dataset
- UiTM for academic support
- Supervisor and examiners for guidance

---

## ⚠️ Notes

- The model file is not included due to size limits. Download from the link above.
- This application runs on **localhost**. For wider access, deploy to a public server.

---

**Thank you!** 🌱♻️

