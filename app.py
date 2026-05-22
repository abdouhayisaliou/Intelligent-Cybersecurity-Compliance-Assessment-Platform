# =========================================================
# IMPORTATION DES MODULES
# =========================================================

from flask import Flask, render_template, request
from requirements_catalog import REQUIREMENTS

import numpy as np
import tensorflow as tf
import joblib
import os


# =========================================================
# INITIALISATION DE L'APPLICATION FLASK
# =========================================================

app = Flask(__name__)


# =========================================================
# CHARGEMENT DU MODÈLE IA ET DU SCALER
# =========================================================

ai_model = tf.keras.models.load_model("cyber_compliance_model.keras")
scaler = joblib.load("scaler.pkl")


# =========================================================
# LABELS DE SORTIE IA
# =========================================================

AI_COMPLIANCE_LABELS = {
    0: "Produit conforme",
    1: "Produit faiblement non conforme",
    2: "Produit moyennement non conforme",
    3: "Produit fortement non conforme"
}


# =========================================================
# FONCTION D'ÉVALUATION NORMATIVE
# =========================================================

def evaluate_security_level(results):

    score = 0
    max_score = len(REQUIREMENTS)

    failed_requirements = []

    sl1_ok = True
    sl2_ok = True
    sl3_ok = True

    input_vector = []

    for req in REQUIREMENTS:

        req_id = req["id"]
        user_value = results.get(req_id)

        if user_value is None or user_value == "":
            failed_requirements.append(req)
            sl1_ok = False
            sl2_ok = False
            sl3_ok = False
            input_vector.append(0)
            continue

        user_value = int(user_value)
        input_vector.append(user_value)

        if req["type"] == "binary":

            if user_value == req["expected"]:
                score += 1
            else:
                failed_requirements.append(req)

                if req["security_level"] <= 1:
                    sl1_ok = False
                if req["security_level"] <= 2:
                    sl2_ok = False
                if req["security_level"] <= 3:
                    sl3_ok = False

        elif req["type"] == "numeric":

            thresholds = req["thresholds"]

            if user_value >= thresholds["SL1"]:
                score += 0.3
            else:
                failed_requirements.append(req)
                sl1_ok = False

            if user_value >= thresholds["SL2"]:
                score += 0.3
            else:
                sl2_ok = False

            if user_value >= thresholds["SL3"]:
                score += 0.4
            else:
                sl3_ok = False

        elif req["type"] == "numeric_max":

            thresholds = req["thresholds"]

            if user_value <= thresholds["SL1"]:
                score += 0.3
            else:
                failed_requirements.append(req)
                sl1_ok = False

            if user_value <= thresholds["SL2"]:
                score += 0.3
            else:
                sl2_ok = False

            if user_value <= thresholds["SL3"]:
                score += 0.4
            else:
                sl3_ok = False

        else:
            failed_requirements.append(req)
            sl1_ok = False
            sl2_ok = False
            sl3_ok = False

    percentage = round((score / max_score) * 100, 2)

    if percentage >= 90:
        compliance_state = "Produit conforme"
    elif percentage >= 70:
        compliance_state = "Produit faiblement non conforme"
    elif percentage >= 50:
        compliance_state = "Produit moyennement non conforme"
    else:
        compliance_state = "Produit fortement non conforme"

    if sl1_ok and sl2_ok and sl3_ok:
        security_level = "SL3"
    elif sl1_ok and sl2_ok:
        security_level = "SL2"
    elif sl1_ok:
        security_level = "SL1"
    else:
        security_level = "NON ATTEINT"

    return {
        "score": percentage,
        "compliance_state": compliance_state,
        "security_level": security_level,
        "failed_requirements": failed_requirements,
        "input_vector": input_vector
    }


# =========================================================
# FONCTION DE PRÉDICTION IA
# =========================================================

def predict_with_ai(input_vector):

    input_array = np.array([input_vector])

    input_scaled = scaler.transform(input_array)

    prediction = ai_model.predict(input_scaled)

    predicted_class = int(np.argmax(prediction))

    confidence = round(float(np.max(prediction)) * 100, 2)

    return {
        "ai_class": predicted_class,
        "ai_label": AI_COMPLIANCE_LABELS[predicted_class],
        "confidence": confidence
    }


# =========================================================
# ROUTE PRINCIPALE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        results = request.form.to_dict()

        evaluation = evaluate_security_level(results)

        ai_prediction = predict_with_ai(evaluation["input_vector"])

        return render_template(
            "result.html",
            evaluation=evaluation,
            ai_prediction=ai_prediction
        )

    return render_template(
        "index.html",
        requirements=REQUIREMENTS
    )


# =========================================================
# LANCEMENT DU SERVEUR FLASK
# =========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
