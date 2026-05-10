import random
import pandas as pd

from requirements_catalog import REQUIREMENTS


# =========================================================
# PARAMÈTRES
# =========================================================

NUMBER_OF_PRODUCTS = 5000
OUTPUT_FILE = "cyber_dataset_v2.csv"


# =========================================================
# ÉVALUATION D'UN PRODUIT
# Même logique que dans app.py
# =========================================================

def evaluate_product(product):

    score = 0
    max_score = len(REQUIREMENTS)

    sl1_ok = True
    sl2_ok = True
    sl3_ok = True

    failed_count = 0
    critical_failed_count = 0

    for req in REQUIREMENTS:

        req_id = req["id"]
        value = product[req_id]

        # ==========================
        # Question Oui / Non
        # ==========================

        if req["type"] == "binary":

            if value == req["expected"]:
                score += 1
            else:
                failed_count += 1

                if req.get("critical", False):
                    critical_failed_count += 1

                if req["security_level"] <= 1:
                    sl1_ok = False
                if req["security_level"] <= 2:
                    sl2_ok = False
                if req["security_level"] <= 3:
                    sl3_ok = False

        # ==========================
        # Numérique minimum
        # Plus la valeur est grande,
        # mieux c'est
        # ==========================

        elif req["type"] == "numeric":

            thresholds = req["thresholds"]

            if value >= thresholds["SL1"]:
                score += 0.3
            else:
                failed_count += 1
                sl1_ok = False

            if value >= thresholds["SL2"]:
                score += 0.3
            else:
                sl2_ok = False

            if value >= thresholds["SL3"]:
                score += 0.4
            else:
                sl3_ok = False

        # ==========================
        # Numérique maximum
        # Plus la valeur est petite,
        # mieux c'est
        # ==========================

        elif req["type"] == "numeric_max":

            thresholds = req["thresholds"]

            if value <= thresholds["SL1"]:
                score += 0.3
            else:
                failed_count += 1
                sl1_ok = False

            if value <= thresholds["SL2"]:
                score += 0.3
            else:
                sl2_ok = False

            if value <= thresholds["SL3"]:
                score += 0.4
            else:
                sl3_ok = False

    # =====================================================
    # SCORE GLOBAL
    # =====================================================

    percentage = round((score / max_score) * 100, 2)

    # =====================================================
    # CLASSE DE CONFORMITÉ
    # =====================================================

    if percentage >= 90 and critical_failed_count == 0:
        compliance_class = 0  # Conforme

    elif percentage >= 70:
        compliance_class = 1  # Faiblement non conforme

    elif percentage >= 50:
        compliance_class = 2  # Moyennement non conforme

    else:
        compliance_class = 3  # Fortement non conforme

    # =====================================================
    # SECURITY LEVEL
    # =====================================================

    if sl1_ok and sl2_ok and sl3_ok:
        security_level_class = 3  # SL3

    elif sl1_ok and sl2_ok:
        security_level_class = 2  # SL2

    elif sl1_ok:
        security_level_class = 1  # SL1

    else:
        security_level_class = 0  # Non atteint

    return percentage, compliance_class, security_level_class, failed_count, critical_failed_count


# =========================================================
# GÉNÉRATION D'UNE VALEUR POUR CHAQUE QUESTION
# =========================================================

def generate_value(req):

    if req["type"] == "binary":
        return random.choice([0, 1])

    elif req["type"] == "numeric":

        # valeur entre 0 et un peu plus que le seuil SL3
        max_value = req["thresholds"]["SL3"] + 10
        return random.randint(0, max_value)

    elif req["type"] == "numeric_max":

        # valeur entre 0 et un peu plus que le seuil SL1
        max_value = req["thresholds"]["SL1"] + 10
        return random.randint(0, max_value)

    else:
        return 0


# =========================================================
# GÉNÉRATION DU DATASET
# =========================================================

dataset = []

for _ in range(NUMBER_OF_PRODUCTS):

    product = {}

    for req in REQUIREMENTS:
        product[req["id"]] = generate_value(req)

    score, compliance_class, security_level_class, failed_count, critical_failed_count = evaluate_product(product)

    product["Score"] = score
    product["ComplianceClass"] = compliance_class
    product["SecurityLevelClass"] = security_level_class
    product["FailedCount"] = failed_count
    product["CriticalFailedCount"] = critical_failed_count

    dataset.append(product)


# =========================================================
# EXPORT CSV
# =========================================================

df = pd.DataFrame(dataset)

df.to_csv(OUTPUT_FILE, index=False)

print("Dataset généré avec succès.")
print("Fichier :", OUTPUT_FILE)
print("Nombre de produits :", NUMBER_OF_PRODUCTS)
print(df.head())