import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.secret_key = "change_this_secret_key"
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

waste_mapping = {
    "battery": "Non-Recyclable (Hazardous Waste)",
    "biological": "Non-Recyclable",
    "brown-glass": "Recyclable",
    "cardboard": "Recyclable",
    "clothes": "Donate",
    "green-glass": "Recyclable",
    "metal": "Recyclable",
    "paper": "Recyclable",
    "plastic": "Recyclable",
    "shoes": "Donate",
    "trash": "Non-Recyclable",
    "white-glass": "Recyclable"
}

class_labels = list(waste_mapping.keys())

model_path = os.path.join(app.root_path, "waste_type_adam.keras")
model = None

def load_waste_model():
    global model
    if model is None:
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found at {model_path}. "
                "Please place waste_type_adam.keras in the project root."
            )
        model = load_model(model_path)
    return model


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((128, 128))
    image_array = np.asarray(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify", methods=["GET", "POST"])
def classify():
    if request.method == "POST":
        if "image" not in request.files:
            flash("Please upload an image file.")
            return redirect(request.url)

        file = request.files["image"]

        if file.filename == "":
            flash("No file selected. Please choose an image.")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            if not os.path.exists(app.config["UPLOAD_FOLDER"]):
                os.makedirs(app.config["UPLOAD_FOLDER"])

            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            image_array = preprocess_image(save_path)
            try:
                current_model = load_waste_model()
            except FileNotFoundError as e:
                flash(str(e))
                return redirect(request.url)

            predictions = current_model.predict(image_array)
            prediction_index = int(np.argmax(predictions[0]))
            predicted_label = class_labels[prediction_index]
            category = waste_mapping.get(predicted_label, "Unknown")
            confidence = float(predictions[0][prediction_index]) * 100

            # CREATE ALL PREDICTIONS LIST FOR TOP 3 & VIEW ALL
            predictions_list = []
            for i, label in enumerate(class_labels):
                confidence_score = float(predictions[0][i]) * 100
                predictions_list.append({
                    "class": label,
                    "confidence": round(confidence_score, 2)
                })
            
            # Sort by confidence (highest first)
            predictions_list.sort(key=lambda x: x["confidence"], reverse=True)

            return render_template(
                "result.html",
                filename=filename,
                predicted_label=predicted_label.upper(),
                category=category,
                confidence=f"{confidence:.2f}%",
                confidence_percent=round(confidence, 2),  # for progress bar
                all_predictions=predictions_list  # for top 3 and view all modal
            )

        flash("Invalid file type. Use PNG, JPG, JPEG, or GIF.")
        return redirect(request.url)

    return render_template("classify.html")


@app.route("/bins")
def bins():
    return render_template("bins.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return redirect(url_for("static", filename=f"uploads/{filename}"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000, debug=True)

