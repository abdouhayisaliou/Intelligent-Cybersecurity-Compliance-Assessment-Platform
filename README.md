# Plateforme Intelligente de Pré-Évaluation de Conformité Cybersécurité
## Capteurs Industriels Connectés — EN 18031-1 / IEC 62443

---

# Présentation du projet

Ce projet est une plateforme intelligente de pré-évaluation de conformité cybersécurité destinée aux capteurs industriels connectés (Wireless Sensors) et aux équipements IACS/OT.

Le système évalue la conformité cybersécurité en s’appuyant sur :
- EN 18031-1
- IEC 62443-4-1
- IEC 62443-4-2

La plateforme combine :
- un moteur de règles normatif ;
- un réseau de neurones ;
- une analyse cybersécurité automatisée ;
- une estimation des niveaux de sécurité SL.

---

# Objectif du projet

L’objectif du projet est de développer un prototype intelligent capable de :
- vérifier des exigences cybersécurité industrielles ;
- analyser automatiquement les réponses d’un utilisateur ;
- détecter les écarts de conformité ;
- proposer des recommandations de remédiation ;
- estimer les niveaux SL1 / SL2 / SL3 ;
- utiliser l’intelligence artificielle pour la prédiction de conformité.

---

# Fonctionnalités principales

## Évaluation cybersécurité

Le système évalue :
- l’authentification ;
- le contrôle d’accès ;
- les communications sécurisées ;
- la cryptographie ;
- le firmware sécurisé ;
- les mises à jour OTA ;
- la gestion des vulnérabilités ;
- la journalisation ;
- le monitoring ;
- la résilience ;
- le cycle de développement sécurisé.

---

## Classification conformité

Le système classe automatiquement les produits en :

- Produit conforme
- Produit faiblement non conforme
- Produit moyennement non conforme
- Produit fortement non conforme

---

## Évaluation Security Level

Le système estime :
- SL1
- SL2
- SL3

selon les concepts de la norme IEC 62443.

---

## Intelligence Artificielle

Le projet intègre :
- TensorFlow ;
- Keras ;
- les réseaux de neurones ;
- le machine learning supervisé.

Le modèle IA prédit automatiquement :
- le niveau de conformité ;
- le niveau de risque cybersécurité.

---

# Technologies utilisées

## Backend
- Python
- Flask

## Intelligence Artificielle
- TensorFlow
- Keras
- Scikit-learn
- Joblib

## Frontend
- HTML
- CSS

## Environnement
- VS Code
- Google Colab

---

# Structure du projet

```text
project/
│
├── app.py
├── requirements_catalog.py
├── generate_dataset_v2.py
├── cyber_compliance_model.keras
├── scaler.pkl
├── cyber_dataset_v2.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── Prototype-intelligent-de-pre-evaluation-de-conformite-cybersecurite.pptx
│
├── Questions Conformite En18031 Iec62443 V1.docx
│
└── README.md