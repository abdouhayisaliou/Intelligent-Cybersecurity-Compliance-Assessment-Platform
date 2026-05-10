REQUIREMENTS = [
    {
        "id": "Q1",
        "title": "Gestion des identités et des comptes",
        "question": "Le produit impose-t-il une identité unique pour chaque utilisateur, service ou équipement, avec suppression des identifiants par défaut et gestion sécurisée des comptes ?",
        "type": "binary",
        "family": "Identification et authentification",
        "standards": ["EN 18031-1 AUM", "IEC 62443-4-2 IAC"],
        "security_level": 1,
        "critical": True,
        "expected": 1,
        "root_cause": "Gestion insuffisante des identités, comptes ou identifiants par défaut.",
        "recommendations": [
            "Mettre en place des identités uniques",
            "Supprimer les identifiants par défaut",
            "Interdire les comptes partagés",
            "Documenter la gestion des comptes"
        ]
    },
    {
        "id": "Q2",
        "title": "Politique de mots de passe et authentification forte",
        "question": "Le produit applique-t-il une politique de mots de passe robuste, une protection contre le brute force et une authentification forte pour les accès sensibles ?",
        "type": "binary",
        "family": "Identification et authentification",
        "standards": ["EN 18031-1 AUM-2/AUM-6", "IEC 62443-4-2 IAC"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Authentification faible ou protection insuffisante contre les attaques par brute force.",
        "recommendations": [
            "Imposer une politique de mots de passe robustes",
            "Limiter les tentatives de connexion",
            "Activer le verrouillage temporaire",
            "Ajouter une authentification multifactorielle pour les accès sensibles"
        ]
    },
    {
        "id": "Q3",
        "title": "Longueur minimale du mot de passe",
        "question": "Quelle est la longueur minimale imposée pour les mots de passe ?",
        "type": "numeric",
        "unit": "caractères",
        "family": "Identification et authentification",
        "standards": ["IEC 62443-4-2 IAC"],
        "security_level": 2,
        "critical": False,
        "thresholds": {"SL1": 8, "SL2": 12, "SL3": 14},
        "root_cause": "Longueur minimale de mot de passe insuffisante.",
        "recommendations": [
            "Imposer au moins 12 caractères",
            "Utiliser des règles de complexité",
            "Éviter les mots de passe faibles ou prévisibles"
        ]
    },
    {
        "id": "Q4",
        "title": "Contrôle d’accès et privilèges",
        "question": "Le produit applique-t-il un contrôle d’accès par rôles avec séparation des privilèges utilisateurs/administrateurs et restriction des fonctions critiques ?",
        "type": "binary",
        "family": "Contrôle d’accès",
        "standards": ["EN 18031-1 ACM", "IEC 62443-4-2 UC"],
        "security_level": 1,
        "critical": True,
        "expected": 1,
        "root_cause": "Contrôle d’accès insuffisant ou mauvaise séparation des privilèges.",
        "recommendations": [
            "Mettre en place un contrôle d’accès basé sur les rôles",
            "Séparer comptes utilisateurs et administrateurs",
            "Limiter les privilèges au strict nécessaire"
        ]
    },
    {
        "id": "Q5",
        "title": "Surface d’attaque et interfaces exposées",
        "question": "Les ports, services, interfaces réseau, interfaces debug et fonctionnalités non nécessaires sont-ils désactivés ou limités au strict nécessaire ?",
        "type": "binary",
        "family": "Surface d’attaque",
        "standards": ["EN 18031-1 GEC-2/GEC-5", "IEC 62443-4-2 RDF"],
        "security_level": 1,
        "critical": True,
        "expected": 1,
        "root_cause": "Surface d’attaque trop large à cause de ports, services ou interfaces inutiles.",
        "recommendations": [
            "Fermer les ports inutiles",
            "Désactiver les interfaces debug",
            "Documenter les interfaces exposées",
            "Appliquer une configuration durcie par défaut"
        ]
    },
    {
        "id": "Q6",
        "title": "Nombre d’interfaces ou services exposés",
        "question": "Combien de ports, services ou interfaces réseau sont exposés par défaut ?",
        "type": "numeric_max",
        "unit": "interfaces/services",
        "family": "Surface d’attaque",
        "standards": ["EN 18031-1 GEC-2/GEC-5", "IEC 62443-4-2 RDF"],
        "security_level": 2,
        "critical": False,
        "thresholds": {"SL1": 5, "SL2": 3, "SL3": 2},
        "root_cause": "Nombre trop élevé d’interfaces ou services exposés.",
        "recommendations": [
            "Réduire le nombre de services exposés",
            "Désactiver les services optionnels par défaut",
            "Limiter l’exposition réseau au strict nécessaire"
        ]
    },
    {
        "id": "Q7",
        "title": "Communications sécurisées",
        "question": "Toutes les communications réseau et radio utilisent-elles des protocoles sécurisés assurant confidentialité, intégrité, authenticité et protection contre les attaques par rejeu ?",
        "type": "binary",
        "family": "Communication sécurisée",
        "standards": ["EN 18031-1 SCM", "IEC 62443-4-2 SI/DC"],
        "security_level": 1,
        "critical": True,
        "expected": 1,
        "root_cause": "Communications insuffisamment protégées.",
        "recommendations": [
            "Activer TLS ou un mécanisme équivalent",
            "Protéger l’intégrité et l’authenticité des messages",
            "Ajouter une protection contre le rejeu",
            "Désactiver les protocoles obsolètes"
        ]
    },
    {
        "id": "Q8",
        "title": "Gestion des clés cryptographiques",
        "question": "Le produit protège-t-il les clés cryptographiques contre l’exposition, le hardcoding et les valeurs statiques tout en permettant leur renouvellement sécurisé ?",
        "type": "binary",
        "family": "Cryptographie et clés",
        "standards": ["EN 18031-1 CCK", "IEC 62443-4-2 DC"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Gestion insuffisante des clés cryptographiques.",
        "recommendations": [
            "Ne jamais coder les clés en dur",
            "Protéger le stockage des clés",
            "Prévoir une rotation ou révocation des clés",
            "Utiliser des mécanismes cryptographiques reconnus"
        ]
    },
    {
        "id": "Q9",
        "title": "Taille minimale des clés symétriques",
        "question": "Quelle est la taille minimale des clés symétriques utilisées par le produit ?",
        "type": "numeric",
        "unit": "bits",
        "family": "Cryptographie et clés",
        "standards": ["EN 18031-1 CRY-1", "IEC 62443-4-2 DC"],
        "security_level": 2,
        "critical": False,
        "thresholds": {"SL1": 128, "SL2": 128, "SL3": 256},
        "root_cause": "Taille de clé cryptographique insuffisante.",
        "recommendations": [
            "Utiliser au minimum des clés symétriques de 128 bits",
            "Prévoir 256 bits pour les cas à sécurité renforcée",
            "Éviter les algorithmes obsolètes"
        ]
    },
    {
        "id": "Q10",
        "title": "Stockage sécurisé",
        "question": "Les données sensibles, secrets, certificats et paramètres de sécurité sont-ils stockés avec protection d’intégrité et de confidentialité ?",
        "type": "binary",
        "family": "Stockage sécurisé",
        "standards": ["EN 18031-1 SSM", "IEC 62443-4-2 SI/DC"],
        "security_level": 1,
        "critical": True,
        "expected": 1,
        "root_cause": "Stockage insuffisamment protégé des données sensibles ou secrets.",
        "recommendations": [
            "Chiffrer les données sensibles stockées",
            "Protéger les certificats et secrets",
            "Contrôler l’intégrité des paramètres de sécurité"
        ]
    },
    {
        "id": "Q11",
        "title": "Firmware signé et Secure Boot",
        "question": "Le produit vérifie-t-il l’intégrité et la signature du firmware via Secure Boot ou mécanisme équivalent, et empêche-t-il le chargement d’un firmware non autorisé ?",
        "type": "binary",
        "family": "Intégrité logicielle et firmware",
        "standards": ["EN 18031-1 SUM", "IEC 62443-4-2 SI"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Firmware ou chaîne de démarrage insuffisamment protégés.",
        "recommendations": [
            "Signer numériquement les firmwares",
            "Activer Secure Boot ou équivalent",
            "Vérifier l’intégrité avant exécution",
            "Bloquer les firmwares non autorisés"
        ]
    },
    {
        "id": "Q12",
        "title": "Mises à jour sécurisées",
        "question": "Les mises à jour locales ou OTA sont-elles authentifiées, sécurisées, vérifiées et documentées avec possibilité de déploiement contrôlé ?",
        "type": "binary",
        "family": "Mise à jour sécurisée",
        "standards": ["EN 18031-1 SUM", "IEC 62443-4-1"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Processus de mise à jour insuffisamment sécurisé.",
        "recommendations": [
            "Authentifier les paquets de mise à jour",
            "Vérifier l’intégrité des mises à jour",
            "Sécuriser les mises à jour OTA",
            "Documenter le processus de mise à jour"
        ]
    },
    {
        "id": "Q13",
        "title": "Gestion des vulnérabilités",
        "question": "Le fabricant dispose-t-il d’un processus documenté de gestion des vulnérabilités, de patch management et de correction des CVE critiques ?",
        "type": "binary",
        "family": "Gestion des vulnérabilités",
        "standards": ["EN 18031-1 GEC-1", "IEC 62443-4-1"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Absence ou insuffisance du processus de gestion des vulnérabilités.",
        "recommendations": [
            "Mettre en place un processus de gestion des vulnérabilités",
            "Prioriser les CVE selon la criticité",
            "Documenter le patch management",
            "Assurer un suivi jusqu’à correction"
        ]
    },
    {
        "id": "Q14",
        "title": "Nombre de CVE critiques non corrigées",
        "question": "Combien de CVE critiques connues restent non corrigées sur le produit ou ses dépendances ?",
        "type": "numeric_max",
        "unit": "CVE critiques",
        "family": "Gestion des vulnérabilités",
        "standards": ["EN 18031-1 GEC-1", "IEC 62443-4-1"],
        "security_level": 2,
        "critical": True,
        "thresholds": {"SL1": 0, "SL2": 0, "SL3": 0},
        "root_cause": "Présence de vulnérabilités critiques non corrigées.",
        "recommendations": [
            "Corriger toutes les CVE critiques",
            "Mettre à jour les composants affectés",
            "Mettre en place une veille vulnérabilités"
        ]
    },
    {
        "id": "Q15",
        "title": "Journalisation et traçabilité",
        "question": "Le produit journalise-t-il les événements de sécurité critiques avec protection des logs et possibilité d’export vers un système externe ?",
        "type": "binary",
        "family": "Journalisation et surveillance",
        "standards": ["IEC 62443-4-2 TRE", "EN 18031-1 NMM"],
        "security_level": 1,
        "critical": False,
        "expected": 1,
        "root_cause": "Journalisation ou traçabilité insuffisante des événements de sécurité.",
        "recommendations": [
            "Journaliser les événements critiques",
            "Protéger les logs contre modification",
            "Prévoir l’export vers un système de supervision"
        ]
    },
    {
        "id": "Q16",
        "title": "Durée de conservation des logs",
        "question": "Pendant combien de jours les journaux de sécurité sont-ils conservés ?",
        "type": "numeric",
        "unit": "jours",
        "family": "Journalisation et surveillance",
        "standards": ["IEC 62443-4-2 TRE"],
        "security_level": 2,
        "critical": False,
        "thresholds": {"SL1": 7, "SL2": 30, "SL3": 90},
        "root_cause": "Durée de conservation des logs insuffisante.",
        "recommendations": [
            "Conserver les logs au moins 30 jours",
            "Protéger les journaux contre suppression non autorisée",
            "Prévoir une conservation plus longue pour environnements critiques"
        ]
    },
    {
        "id": "Q17",
        "title": "Détection d’incidents et monitoring réseau",
        "question": "Le produit détecte-t-il les comportements anormaux, tentatives d’intrusion, scans réseau ou événements de sécurité suspects ?",
        "type": "binary",
        "family": "Journalisation et surveillance",
        "standards": ["EN 18031-1 NMM", "IEC 62443-4-2 TRE"],
        "security_level": 2,
        "critical": False,
        "expected": 1,
        "root_cause": "Mécanismes insuffisants de surveillance ou détection d’incidents.",
        "recommendations": [
            "Ajouter des alertes de sécurité",
            "Détecter les comportements anormaux",
            "Intégrer le produit à un système de supervision"
        ]
    },
    {
        "id": "Q18",
        "title": "Résilience et disponibilité",
        "question": "Le produit maintient-il un état sûr en cas d’erreur, surcharge ou attaque de type déni de service tout en protégeant la disponibilité des fonctions critiques ?",
        "type": "binary",
        "family": "Résilience et disponibilité",
        "standards": ["EN 18031-1 RLM", "IEC 62443-4-2 RA"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Résilience insuffisante face aux erreurs, surcharges ou attaques de disponibilité.",
        "recommendations": [
            "Prévoir un état sûr en cas d’erreur",
            "Limiter les effets d’un déni de service",
            "Protéger les fonctions critiques",
            "Tester les scénarios de surcharge"
        ]
    },
    {
        "id": "Q19",
        "title": "Cycle de développement sécurisé",
        "question": "Le produit suit-il un cycle de développement sécurisé intégrant exigences sécurité, threat modeling, règles de codage sécurisé, revues de code, tests sécurité et gestion des composants tiers ?",
        "type": "binary",
        "family": "Développement sécurisé",
        "standards": ["IEC 62443-4-1"],
        "security_level": 2,
        "critical": True,
        "expected": 1,
        "root_cause": "Cycle de développement sécurisé insuffisant ou non démontré.",
        "recommendations": [
            "Définir les exigences sécurité dès la conception",
            "Réaliser une analyse de risques ou threat modeling",
            "Appliquer des règles de codage sécurisé",
            "Réaliser des tests de sécurité avant livraison",
            "Gérer les composants tiers et dépendances"
        ]
    },
    {
        "id": "Q20",
        "title": "Documentation sécurité et hardening",
        "question": "Le produit fournit-il une documentation de sécurité incluant hardening, configuration sécurisée, gestion des comptes, maintenance, mise à jour et fin de vie ?",
        "type": "binary",
        "family": "Documentation et exploitation sécurisée",
        "standards": ["IEC 62443-4-1", "EN 18031-1 GEC-4"],
        "security_level": 1,
        "critical": False,
        "expected": 1,
        "root_cause": "Documentation de sécurité ou guide de durcissement insuffisant.",
        "recommendations": [
            "Fournir un guide de hardening",
            "Documenter la configuration sécurisée",
            "Décrire la gestion des comptes et mises à jour",
            "Préciser les conditions de maintenance et de fin de vie"
        ]
    }
]