# Revue code Python Senior production

**Session ID:** ses_fa22916a8ffe9N0C2Lo9evWJwO
**Created:** 9/1/2026, 6:39:20 PM
**Updated:** 9/1/2026, 9:15:37 PM

---

## User

# Rôle

Tu es un **Senior Python Software Engineer, Software Architect et Code Reviewer** avec une forte expertise en :

* Python moderne (3.10+)
* Architecture logicielle et Clean Architecture
* SOLID, DRY, KISS et séparation des responsabilités
* Typage statique (`typing`, `mypy`, `pyright`)
* Qualité de code et maintenabilité
* Performance et optimisation
* Sécurité applicative
* Tests automatisés (`pytest`)
* Gestion des dépendances et packaging
* CI/CD et bonnes pratiques de production
* Analyse de dette technique

Ta mission est de réaliser une **revue professionnelle, critique et actionnable** de mon projet Python.

---

# Contexte

Je vais te fournir le code de mon projet Python, soit sous forme de fichiers, soit sous forme d'une arborescence suivie du contenu des fichiers.

Tu dois analyser le projet **dans son ensemble**, et non uniquement commenter chaque fichier individuellement.

Si des informations sont manquantes, indique clairement tes hypothèses avant de tirer des conclusions.

---

# Ta mission

Réalise une **code review complète de niveau Senior / Production**.

Analyse notamment les aspects suivants :

## 1. Architecture du projet

Analyse :

* L'organisation des dossiers et modules
* La séparation des responsabilités
* Les dépendances entre modules
* Le couplage et la cohésion
* Le respect des principes SOLID
* La scalabilité de l'architecture
* La facilité d'évolution future
* Les éventuels problèmes de circular imports
* Les responsabilités mal placées

Identifie clairement les problèmes architecturaux.

---

## 2. Qualité du code

Évalue :

* La lisibilité
* La simplicité
* La duplication de code
* La complexité inutile
* Les noms de variables, fonctions et classes
* La longueur et la responsabilité des fonctions
* Les fonctions/classes "god objects"
* La gestion des constantes
* Le respect de PEP 8
* L'utilisation idiomatique de Python

Ne signale pas des problèmes purement stylistiques sans impact réel.

---

## 3. Bugs et problèmes potentiels

Recherche activement :

* Bugs logiques
* Cas limites non gérés
* Exceptions mal gérées
* Valeurs `None` dangereuses
* Erreurs de concurrence ou d'asynchronisme, si applicable
* Fuites de ressources
* Conditions de course
* Comportements imprévisibles
* Problèmes liés aux entrées utilisateur
* Erreurs silencieuses

Pour chaque problème identifié :

1. Explique le problème.
2. Indique où il se trouve.
3. Explique son impact.
4. Propose une correction concrète.

---

## 4. Sécurité

Analyse notamment :

* Validation des entrées
* Injection de commandes
* Injection SQL
* Désérialisation dangereuse
* Utilisation dangereuse de `eval()` ou `exec()`
* Gestion des secrets
* Mots de passe ou clés API exposés
* Accès aux fichiers
* Traversée de répertoires
* Dépendances potentiellement risquées
* Gestion des permissions
* Logs contenant des données sensibles

Classe chaque problème selon :

🔴 CRITIQUE
🟠 ÉLEVÉ
🟡 MOYEN
🟢 FAIBLE

---

## 5. Performance

Identifie :

* Algorithmes inefficaces
* Complexités inutiles
* Boucles coûteuses
* Requêtes répétitives
* Chargements inutiles en mémoire
* Problèmes de cache
* Opérations I/O bloquantes
* Mauvaise utilisation de l'asynchrone
* Optimisations prématurées ou inutiles

Ne recommande pas d'optimisation sans bénéfice réel.

Lorsque pertinent, explique :

> Problème → Cause → Impact → Solution

---

## 6. Typage et Python moderne

Analyse l'utilisation :

* Des annotations de type
* De `Optional` et `None`
* Des `Protocol`
* Des `dataclasses`
* Des `Enum`
* Des génériques
* Des types Python modernes
* De `pathlib`
* Des context managers
* Des bonnes pratiques Python récentes

Propose des améliorations uniquement lorsqu'elles améliorent réellement la robustesse ou la lisibilité.

---

## 7. Gestion des erreurs

Vérifie :

* Les `try/except` trop larges
* Les exceptions ignorées
* Les erreurs silencieuses
* Les messages d'erreur
* La création d'exceptions métier
* La cohérence de la stratégie de gestion d'erreurs

Identifie notamment les cas de :

```python
except Exception:
    pass
```

ou toute autre gestion dangereuse des erreurs.

---

## 8. Tests

Évalue :

* La présence de tests
* La couverture fonctionnelle
* Les cas limites
* Les tests unitaires
* Les tests d'intégration
* La testabilité de l'architecture
* L'utilisation de mocks
* Les zones critiques non testées

Propose une stratégie de tests priorisée.

Donne des exemples de tests `pytest` lorsque cela apporte une réelle valeur.

---

## 9. Dépendances et configuration

Analyse :

* `requirements.txt`
* `pyproject.toml`
* Les versions des dépendances
* Les dépendances inutiles
* Les dépendances manquantes
* La reproductibilité de l'environnement
* La configuration du projet
* Les fichiers `.env`
* `.gitignore`

Signale les mauvaises pratiques potentielles.

---

# Méthodologie obligatoire

Tu dois raisonner comme lors d'une **vraie revue de code en entreprise**.

## Étape 1 — Compréhension

Commence par résumer :

* L'objectif du projet
* Son fonctionnement général
* Son architecture
* Les composants principaux
* Le flux principal d'exécution

Si tu n'es pas certain, indique :

**Hypothèse :** ...

---

## Étape 2 — Analyse

Analyse le code en profondeur.

Ne te limite pas aux problèmes évidents.

Cherche particulièrement :

* Les problèmes structurels
* Les bugs subtils
* La dette technique
* Les risques futurs
* Les problèmes qui apparaîtront lorsque le projet grandira

---

## Étape 3 — Priorisation

Classe toutes les remarques selon leur importance.

### 🔴 Critique

Bug grave, faille de sécurité, risque de perte de données ou problème empêchant la production.

### 🟠 Important

Problème significatif de robustesse, architecture ou maintenabilité.

### 🟡 Amélioration

Amélioration recommandée mais non bloquante.

### 🟢 Mineur

Petite amélioration de lisibilité ou de qualité.

---

# Format de réponse obligatoire

## 1. Executive Summary

Donne un résumé clair comprenant :

* Qualité globale du projet
* Niveau de maturité
* Principaux points forts
* Principaux risques
* Capacité du projet à évoluer

Donne également une note :

**Architecture : X/10**
**Qualité du code : X/10**
**Sécurité : X/10**
**Performance : X/10**
**Tests : X/10**
**Maintenabilité : X/10**

Puis :

### Note globale : X/10

Justifie brièvement chaque note.

---

## 2. Points forts

Liste les bonnes pratiques réellement présentes.

Ne fais pas de compliments génériques.

---

## 3. Problèmes critiques

Pour chaque problème :

### 🔴 [Titre du problème]

**Localisation :**
`chemin/du/fichier.py`

**Problème :**
Explication précise.

**Impact :**
Conséquences possibles.

**Correction recommandée :**
Solution concrète.

**Exemple :**

```python
# Code actuel
...

# Code recommandé
...
```

---

## 4. Problèmes importants

Utilise exactement le même format.

---

## 5. Dette technique et améliorations

Présente les améliorations sous forme de tableau :

| Priorité | Problème | Impact | Effort | Recommandation |
| -------- | -------- | ------ | ------ | -------------- |

---

## 6. Analyse architecturale

Explique :

* Ce qui fonctionne
* Ce qui pose problème
* Comment améliorer l'architecture

Si nécessaire, propose une architecture cible.

Exemple :

```text
project/
├── src/
│   └── app/
│       ├── domain/
│       ├── application/
│       ├── infrastructure/
│       └── interfaces/
├── tests/
├── pyproject.toml
└── README.md
```

Adapte la proposition au projet réel.

**Ne recommande pas une Clean Architecture complexe si elle est disproportionnée pour la taille du projet.**

---

## 7. Plan d'action priorisé

Propose un plan concret :

### Phase 1 — Urgent

Les corrections à effectuer immédiatement.

### Phase 2 — Important

Les améliorations à réaliser avant une mise en production.

### Phase 3 — Qualité

Les améliorations progressives.

---

## 8. Quick Wins

Liste les **5 à 10 améliorations avec le meilleur ratio impact/effort**.

---

## 9. Exemple de refactoring

Choisis le **refactoring le plus important** et propose une version améliorée du code.

Explique brièvement :

* Pourquoi
* Ce qui change
* Le bénéfice

---

# Règles importantes

1. **Ne pas inventer de problèmes.**
2. **Ne pas supposer qu'une fonctionnalité est cassée sans preuve dans le code.**
3. Lorsqu'un point est incertain, indique-le clairement.
4. Ne pas faire de micro-optimisations inutiles.
5. Ne pas recommander des design patterns simplement pour utiliser des design patterns.
6. Privilégier les solutions simples et maintenables.
7. Chaque critique doit être justifiée.
8. Donner des recommandations concrètes et applicables.
9. Conserver le contexte global du projet pendant toute l'analyse.
10. Si le projet est volumineux, analyser d'abord l'arborescence puis les fichiers les plus importants.

---

# Mode d'analyse

Sois :

* Rigoureux
* Direct
* Constructif
* Exigeant
* Pragmatique

Agis comme un **Senior Engineer réalisant une revue avant mise en production**.

Ne cherche pas à être gentil.

Cherche à rendre le projet :

**Plus robuste.
Plus maintenable.
Plus sécurisé.
Plus simple à faire évoluer.**

---

# Projet à analyser

Je vais maintenant fournir :

1. L'arborescence du projet
2. Les fichiers principaux
3. Les fichiers de configuration
4. Les tests éventuels

Attends d'avoir suffisamment de contexte avant de produire la review finale.

Lorsque je fournis plusieurs fichiers, conserve leur contexte et établis progressivement une compréhension globale du projet.

**Commence par analyser l'arborescence et me dire quels fichiers sont prioritaires à examiner.** 

---

## Assistant (Build · Muse Spark 1.2 Free · 136.9s)

_Thinking:_



_Thinking:_



**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine</path>
<type>directory</type>
<entries>
.git/
config/
data/
src/
tests/
venv/

(6 entries)
</entries>
```

---

## Assistant (Build · Muse Spark 1.2 Free · 1.9s)

**Tool: bash**

**Input:**
```json
{
  "command": "find . -type f -not -path \"./venv/*\" -not -path \"./.git/*\" -not -path \"./data/*\" | sort; echo \"---\"; ls -la; echo \"---\"; cat pyproject.toml 2>/dev/null || cat setup.py 2>/dev/null || cat setup.cfg 2>/dev/null; echo \"---pyproject---\"; cat requirements*.txt 2>/dev/null; echo \"---env example---\"; cat .env* 2>/dev/null; cat .gitignore 2>/dev/null",
  "workdir": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
./config/settings.yaml
./src/agent/__init__.py
./src/agent/interactive_shell.py
./src/agent/llm_analyst.py
./src/agent/__pycache__/__init__.cpython-312.pyc
./src/agent/__pycache__/__init__.cpython-313.pyc
./src/agent/__pycache__/llm_analyst.cpython-312.pyc
./src/agent/__pycache__/llm_analyst.cpython-313.pyc
./src/analysis/air_traffic_analyser.py
./src/analysis/correlator.py
./src/analysis/gdelt_correlator.py
./src/analysis/__init__.py
./src/analysis/__pycache__/air_traffic_analyser.cpython-312.pyc
./src/analysis/__pycache__/air_traffic_analyser.cpython-313.pyc
./src/analysis/__pycache__/correlator.cpython-312.pyc
./src/analysis/__pycache__/gdelt_correlator.cpython-312.pyc
./src/analysis/__pycache__/__init__.cpython-312.pyc
./src/analysis/__pycache__/__init__.cpython-313.pyc
./src/analysis/__pycache__/timeseries_analyzer.cpython-312.pyc
./src/analysis/__pycache__/timeseries_analyzer.cpython-313.pyc
./src/analysis/timeseries_analyzer.py
./src/api/server.py
./src/collector.py
./src/config/settings.yaml
./src/correlation_main.py
./src/dashboard_main.py
./src/data/gdelt/events_france_2026-03-04_17-16-15.csv
./src/data/gdelt/events_france_2026-03-04_17-17-42.csv
./src/data/gdelt/events_france_2026-03-04_17-22-19.csv
./src/data/gdelt/events_france_2026-03-04_17-22-34.csv
./src/data/gdelt/events_france_2026-03-04_17-23-04.csv
./src/data/gdelt/events_france_2026-03-04_17-23-25.csv
./src/data/gdelt/events_france_2026-03-04_17-25-41.csv
./src/data/gdelt/events_france_2026-03-04_17-27-25.csv
./src/data/maps/dashboard.html
./src/data/maps/flights_map.html
./src/data/maps/timeseries.html
./src/data/raw/flights_2026-03-03_19-38-26.csv
./src/data/raw/flights_2026-03-03_19-45-26.csv
./src/data/raw/flights_2026-03-03_20-03-08.csv
./src/data/raw/flights_2026-03-04_16-14-16.csv
./src/data/raw/flights_2026-03-04_16-14-46.csv
./src/data/raw/flights_2026-03-04_16-15-16.csv
./src/data/raw/flights_2026-03-04_16-15-47.csv
./src/data/raw/flights_2026-03-04_16-16-17.csv
./src/data/raw/flights_2026-03-04_18-04-43.csv
./src/data/raw/flights_2026-03-04_18-05-13.csv
./src/data/raw/flights_2026-03-04_18-05-43.csv
./src/data/raw/flights_2026-03-04_18-06-13.csv
./src/data/raw/flights_2026-03-04_18-06-43.csv
./src/data/raw/flights_2026-03-11_17-13-54__EU_W.csv
./src/data/raw/flights_2026-03-11_17-14-01__EU_E.csv
./src/data/raw/flights_2026-03-11_17-14-07__RU.csv
./src/data/raw/flights_2026-03-11_17-14-13__ME.csv
./src/data/raw/flights_2026-03-11_17-14-19__AS_S.csv
./src/data/raw/flights_2026-03-11_17-14-26__AS_E.csv
./src/data/raw/flights_2026-03-11_17-14-32__NA.csv
./src/data/raw/flights_2026-03-11_17-14-39__SA.csv
./src/data/raw/flights_2026-03-11_17-14-45__AF.csv
./src/data/raw/flights_2026-03-11_17-14-51__UKR.csv
./src/data/raw/flights_2026-03-11_17-14-58__TWN.csv
./src/data/raw/flights_2026-03-11_17-15-04__PG.csv
./src/data/raw/flights_2026-03-11_17-39-16__EU_W.csv
./src/data/raw/flights_2026-03-11_17-39-22__EU_E.csv
./src/data/raw/flights_2026-03-11_17-39-28__RU.csv
./src/data/raw/flights_2026-03-11_17-39-35__ME.csv
./src/data/raw/flights_2026-03-11_17-39-41__AS_S.csv
./src/data/raw/flights_2026-03-11_17-39-47__AS_E.csv
./src/data/raw/flights_2026-03-11_17-39-54__NA.csv
./src/data/raw/flights_2026-03-11_17-40-00__SA.csv
./src/data/raw/flights_2026-03-11_17-40-06__AF.csv
./src/data/raw/flights_2026-03-11_17-40-12__UKR.csv
./src/data/raw/flights_2026-03-11_17-40-18__TWN.csv
./src/data/raw/flights_2026-03-11_17-40-25__PG.csv
./src/data/raw/flights_2026-03-11_17-43-36__EU_W.csv
./src/data/raw/flights_2026-03-11_17-43-42__EU_E.csv
./src/data/raw/flights_2026-03-11_17-43-48__RU.csv
./src/data/raw/flights_2026-03-11_17-43-55__ME.csv
./src/data/raw/flights_2026-03-11_17-44-01__AS_S.csv
./src/data/raw/flights_2026-03-11_17-44-07__AS_E.csv
./src/data/raw/flights_2026-03-11_17-44-14__NA.csv
./src/data/raw/flights_2026-03-11_17-44-20__SA.csv
./src/data/raw/flights_2026-03-11_17-44-26__AF.csv
./src/data/raw/flights_2026-03-11_17-44-32__UKR.csv
./src/data/raw/flights_2026-03-11_17-44-39__TWN.csv
./src/data/raw/flights_2026-03-11_17-44-45__PG.csv
./src/data/raw/flights_2026-08-30_17-34-55__EU_W.csv
./src/data/raw/flights_2026-08-30_17-35-01__EU_E.csv
./src/data/raw/flights_2026-08-30_17-35-08__RU.csv
./src/data/raw/flights_2026-08-30_17-35-14__ME.csv
./src/data/raw/flights_2026-08-30_17-35-20__AS_S.csv
./src/data/raw/flights_2026-08-30_17-35-27__AS_E.csv
./src/data/raw/flights_2026-08-30_17-35-34__NA.csv
./src/data/raw/flights_2026-08-30_17-35-40__SA.csv
./src/data/raw/flights_2026-08-30_17-35-46__AF.csv
./src/data/raw/flights_2026-08-30_17-35-53__UKR.csv
./src/data/raw/flights_2026-08-30_17-35-59__TWN.csv
./src/data/raw/flights_2026-08-30_17-36-06__PG.csv
./src/data/reports/correlations.csv
./src/data/reports/global_summary.csv
./src/data/reports/timeseries.csv
./src/gdelt_main.py
./src/global_main.py
./src/ingestion/adsb_ingestor.py
./src/ingestion/gdelt_ingestor.py
./src/ingestion/global_ingestor.py
./src/ingestion/__init__.py
./src/ingestion/__pycache__/adsb_ingestor.cpython-312.pyc
./src/ingestion/__pycache__/adsb_ingestor.cpython-313.pyc
./src/ingestion/__pycache__/gdelt_ingestor.cpython-312.pyc
./src/ingestion/__pycache__/global_ingestor.cpython-312.pyc
./src/ingestion/__pycache__/global_ingestor.cpython-313.pyc
./src/ingestion/__pycache__/__init__.cpython-312.pyc
./src/ingestion/__pycache__/__init__.cpython-313.pyc
./src/main.py
./src/models/adsb_message.py
./src/models/__init__.py
./src/models/__pycache__/adsb_message.cpython-312.pyc
./src/models/__pycache__/adsb_message.cpython-313.pyc
./src/models/__pycache__/__init__.cpython-312.pyc
./src/models/__pycache__/__init__.cpython-313.pyc
./src/storage/data_store.py
./src/storage/__init__.py
./src/storage/__pycache__/data_store.cpython-312.pyc
./src/storage/__pycache__/data_store.cpython-313.pyc
./src/storage/__pycache__/__init__.cpython-312.pyc
./src/storage/__pycache__/__init__.cpython-313.pyc
./src/timeseries_main.py
./src/utils/config_loader.py
./src/utils/helpers.py
./src/utils/__init__.py
./src/utils/__pycache__/config_loader.cpython-312.pyc
./src/utils/__pycache__/__init__.cpython-312.pyc
./src/utils/__pycache__/__init__.cpython-313.pyc
./src/utils/__pycache__/regions.cpython-312.pyc
./src/utils/__pycache__/regions.cpython-313.pyc
./src/utils/regions.py
./src/visualization/dashboard.py
./src/visualization/__init__.py
./src/visualization/map_viewer.py
./src/visualization/__pycache__/dashboard.cpython-312.pyc
./src/visualization/__pycache__/dashboard.cpython-313.pyc
./src/visualization/__pycache__/__init__.cpython-312.pyc
./src/visualization/__pycache__/__init__.cpython-313.pyc
./src/visualization/__pycache__/map_viewer.cpython-312.pyc
./src/visualization/__pycache__/timeseries_plotter.cpython-312.pyc
./src/visualization/timeseries_plotter.py
./tests/__init__.py
./tests/test_adsb_ingestor.py
./tests/test_air_traffic_analyzer.py
./tests/test_data_store.py
---
total 32
drwxrwxr-x  8 enzo enzo 4096 Aug  6 20:43 .
drwxrwxr-x  5 enzo enzo 4096 Aug  6 20:58 ..
drwxrwxr-x  2 enzo enzo 4096 Mar  3 17:23 config
drwxrwxr-x  5 enzo enzo 4096 Mar 11 17:28 data
drwxrwxr-x  8 enzo enzo 4096 Sep  1 18:37 .git
drwxrwxr-x 12 enzo enzo 4096 Mar 11 17:08 src
drwxrwxr-x  2 enzo enzo 4096 Mar  3 17:23 tests
drwxrwxr-x  5 enzo enzo 4096 Jul 28 19:20 venv
---
---pyproject---
---env example---

```

---

## Assistant (Build · Muse Spark 1.2 Free · 1.3s)

**Tool: bash**

**Input:**
```json
{
  "command": "ls -R src config tests 2>/dev/null | head -n 200; echo \"---\"; cat config/settings.yaml; echo \"---\"; cat src/config/settings.yaml 2>/dev/null",
  "workdir": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
config:
settings.yaml

src:
agent
analysis
api
collector.py
config
correlation_main.py
dashboard_main.py
data
gdelt_main.py
global_main.py
ingestion
main.py
models
storage
timeseries_main.py
utils
visualization

src/agent:
__init__.py
interactive_shell.py
llm_analyst.py
__pycache__

src/agent/__pycache__:
__init__.cpython-312.pyc
__init__.cpython-313.pyc
llm_analyst.cpython-312.pyc
llm_analyst.cpython-313.pyc

src/analysis:
air_traffic_analyser.py
correlator.py
gdelt_correlator.py
__init__.py
__pycache__
timeseries_analyzer.py

src/analysis/__pycache__:
air_traffic_analyser.cpython-312.pyc
air_traffic_analyser.cpython-313.pyc
correlator.cpython-312.pyc
gdelt_correlator.cpython-312.pyc
__init__.cpython-312.pyc
__init__.cpython-313.pyc
timeseries_analyzer.cpython-312.pyc
timeseries_analyzer.cpython-313.pyc

src/api:
server.py

src/config:
settings.yaml

src/data:
gdelt
maps
raw
reports

src/data/gdelt:
events_france_2026-03-04_17-16-15.csv
events_france_2026-03-04_17-17-42.csv
events_france_2026-03-04_17-22-19.csv
events_france_2026-03-04_17-22-34.csv
events_france_2026-03-04_17-23-04.csv
events_france_2026-03-04_17-23-25.csv
events_france_2026-03-04_17-25-41.csv
events_france_2026-03-04_17-27-25.csv

src/data/maps:
dashboard.html
flights_map.html
timeseries.html

src/data/raw:
flights_2026-03-03_19-38-26.csv
flights_2026-03-03_19-45-26.csv
flights_2026-03-03_20-03-08.csv
flights_2026-03-04_16-14-16.csv
flights_2026-03-04_16-14-46.csv
flights_2026-03-04_16-15-16.csv
flights_2026-03-04_16-15-47.csv
flights_2026-03-04_16-16-17.csv
flights_2026-03-04_18-04-43.csv
flights_2026-03-04_18-05-13.csv
flights_2026-03-04_18-05-43.csv
flights_2026-03-04_18-06-13.csv
flights_2026-03-04_18-06-43.csv
flights_2026-03-11_17-13-54__EU_W.csv
flights_2026-03-11_17-14-01__EU_E.csv
flights_2026-03-11_17-14-07__RU.csv
flights_2026-03-11_17-14-13__ME.csv
flights_2026-03-11_17-14-19__AS_S.csv
flights_2026-03-11_17-14-26__AS_E.csv
flights_2026-03-11_17-14-32__NA.csv
flights_2026-03-11_17-14-39__SA.csv
flights_2026-03-11_17-14-45__AF.csv
flights_2026-03-11_17-14-51__UKR.csv
flights_2026-03-11_17-14-58__TWN.csv
flights_2026-03-11_17-15-04__PG.csv
flights_2026-03-11_17-39-16__EU_W.csv
flights_2026-03-11_17-39-22__EU_E.csv
flights_2026-03-11_17-39-28__RU.csv
flights_2026-03-11_17-39-35__ME.csv
flights_2026-03-11_17-39-41__AS_S.csv
flights_2026-03-11_17-39-47__AS_E.csv
flights_2026-03-11_17-39-54__NA.csv
flights_2026-03-11_17-40-00__SA.csv
flights_2026-03-11_17-40-06__AF.csv
flights_2026-03-11_17-40-12__UKR.csv
flights_2026-03-11_17-40-18__TWN.csv
flights_2026-03-11_17-40-25__PG.csv
flights_2026-03-11_17-43-36__EU_W.csv
flights_2026-03-11_17-43-42__EU_E.csv
flights_2026-03-11_17-43-48__RU.csv
flights_2026-03-11_17-43-55__ME.csv
flights_2026-03-11_17-44-01__AS_S.csv
flights_2026-03-11_17-44-07__AS_E.csv
flights_2026-03-11_17-44-14__NA.csv
flights_2026-03-11_17-44-20__SA.csv
flights_2026-03-11_17-44-26__AF.csv
flights_2026-03-11_17-44-32__UKR.csv
flights_2026-03-11_17-44-39__TWN.csv
flights_2026-03-11_17-44-45__PG.csv
flights_2026-08-30_17-34-55__EU_W.csv
flights_2026-08-30_17-35-01__EU_E.csv
flights_2026-08-30_17-35-08__RU.csv
flights_2026-08-30_17-35-14__ME.csv
flights_2026-08-30_17-35-20__AS_S.csv
flights_2026-08-30_17-35-27__AS_E.csv
flights_2026-08-30_17-35-34__NA.csv
flights_2026-08-30_17-35-40__SA.csv
flights_2026-08-30_17-35-46__AF.csv
flights_2026-08-30_17-35-53__UKR.csv
flights_2026-08-30_17-35-59__TWN.csv
flights_2026-08-30_17-36-06__PG.csv

src/data/reports:
correlations.csv
global_summary.csv
timeseries.csv

src/ingestion:
adsb_ingestor.py
gdelt_ingestor.py
global_ingestor.py
__init__.py
__pycache__

src/ingestion/__pycache__:
adsb_ingestor.cpython-312.pyc
adsb_ingestor.cpython-313.pyc
gdelt_ingestor.cpython-312.pyc
global_ingestor.cpython-312.pyc
global_ingestor.cpython-313.pyc
__init__.cpython-312.pyc
__init__.cpython-313.pyc

src/models:
adsb_message.py
__init__.py
__pycache__

src/models/__pycache__:
adsb_message.cpython-312.pyc
adsb_message.cpython-313.pyc
__init__.cpython-312.pyc
__init__.cpython-313.pyc

src/storage:
data_store.py
__init__.py
__pycache__

src/storage/__pycache__:
data_store.cpython-312.pyc
data_store.cpython-313.pyc
__init__.cpython-312.pyc
__init__.cpython-313.pyc

src/utils:
config_loader.py
helpers.py
__init__.py
__pycache__
regions.py

src/utils/__pycache__:
config_loader.cpython-312.pyc
__init__.cpython-312.pyc
__init__.cpython-313.pyc
regions.cpython-312.pyc
regions.cpython-313.pyc

src/visualization:
---
# Zone géographique de collecte
zone:
  name: "France"
  lat_min: 2.0
  lon_min: 45.0
  lat_max: 22.0
  lon_max: 83.0

# Paramètres de collecte
collection:
  interval_seconds: 30   # toutes les 5 minutes
  max_snapshots: 5      # 288 x 5min = 24h de données

# Chemins
paths:
  raw_data: "data/raw"
  maps:     "data/maps"
  reports:  "data/reports"---
# Zone géographique de collecte
zone:
  name: "Moyen Orient"
  lat_min: 2.0
  lon_min: 5.0
  lat_max: 62.0
  lon_max: 83.0
# Paramètres de collecte
collection:
  interval_seconds: 30   # toutes les 5 minutes
  max_snapshots: 5      # 288 x 5min = 24h de données

# Chemins
paths:
  raw_data: "data/raw"
  maps:     "data/maps"
  reports:  "data/reports"
```

---

## Assistant (Build · Muse Spark 1.2 Free · 2.8s)

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/main.py</path>
<type>file</type>
<content>
1: from ingestion.adsb_ingestor import fetch_flights
2: from storage.data_store import save_flights, load_flights
3: from visualization.map_viewer import build_flight_map
4: from analysis.air_traffic_analyser import print_report
5: 
6: # ─────────────────────────────────────────────
7: # ZONE GÉOGRAPHIQUE : France métropolitaine
8: # ─────────────────────────────────────────────
9: # C'est une "bounding box" (rectangle GPS)
10: # lat_min, lon_min = coin bas-gauche  (sud-ouest)
11: # lat_max, lon_max = coin haut-droite (nord-est)
12: LAT_MIN = 41.0
13: LON_MIN = -5.5
14: LAT_MAX = 51.5
15: LON_MAX = 10.0
16: 
17: 
18: def main():
19:     print("=" * 50)
20:     print("  GeoPol Traffic Intelligence Engine")
21:     print("  Phase 1 — Ingestion aérienne")
22:     print("=" * 50)
23: 
24:     # ── Étape 1 : Récupérer les avions en vol ──
25:     flights = fetch_flights(
26:         lat_min=LAT_MIN,
27:         lon_min=LON_MIN,
28:         lat_max=LAT_MAX,
29:         lon_max=LON_MAX
30:     )
31: 
32:     if not flights:
33:         print("[Main] Aucune donnée à sauvegarder.")
34:         return
35: 
36:     # ── Étape 2 : Sauvegarder en CSV ──
37:     filepath = save_flights(flights)
38: 
39:     # ── Étape 3 : Recharger et afficher un résumé ──
40:     df = load_flights(filepath)
41: 
42:     print("\n── Résumé ──")
43:     print(f"  Avions total       : {len(df)}")
44:     print(f"  Au sol             : {df['on_ground'].sum()}")
45:     print(f"  En vol             : {(~df['on_ground']).sum()}")
46:     print(f"  Pays représentés   : {df['origin_country'].nunique()}")
47:     print(f"  Altitude moyenne   : {df['altitude'].mean():.0f} m")
48:     print(f"  Vitesse moyenne    : {df['velocity'].mean():.0f} m/s")
49:     print("\n── Top 5 pays ──")
50:     print(df['origin_country'].value_counts().head())
51:     print(f"\n  Fichier sauvegardé : {filepath}")
52: 
53:     # ── Étape 4 : Afficher un rapport détaillé ──
54:     print_report(df)
55: 
56:     # ── Étape 5 : Générer une carte interactive ──
57:     build_flight_map(df)
58: 
59: 
60: if __name__ == "__main__":
61:     main()

(End of file - total 61 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/collector.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/collector.py</path>
<type>file</type>
<content>
1: import time
2: import signal
3: import sys
4: from pathlib import Path
5: from datetime import datetime
6: 
7: from ingestion.adsb_ingestor import fetch_flights
8: from storage.data_store import save_flights, load_flights
9: from analysis.air_traffic_analyser import compute_basic_metrics
10: from utils.config_loader import load_config
11: 
12: # ── Gestion propre du Ctrl+C ──
13: # Sans ça, Ctrl+C affiche une stacktrace moche
14: def _handle_exit(sig, frame):
15:     print("\n[Collector] Arrêt propre. À bientôt.")
16:     sys.exit(0)
17: 
18: signal.signal(signal.SIGINT, _handle_exit)
19: 
20: 
21: def run_collector(config_path: str = "config/settings.yaml"):
22:     """
23:     Boucle principale de collecte.
24:     Interroge OpenSky toutes les X secondes et sauvegarde chaque snapshot.
25:     """
26: 
27:     config   = load_config(config_path)
28:     zone     = config["zone"]
29:     interval = config["collection"]["interval_seconds"]
30:     max_snap = config["collection"]["max_snapshots"]
31: 
32:     print("=" * 50)
33:     print("  GeoPol — Collecteur temps réel")
34:     print(f"  Zone     : {zone['name']}")
35:     print(f"  Intervalle : {interval}s ({interval//60} min)")
36:     print(f"  Max snapshots : {max_snap}")
37:     print("  Ctrl+C pour arrêter proprement")
38:     print("=" * 50)
39: 
40:     snapshot_count = 0
41: 
42:     while snapshot_count < max_snap:
43:         snapshot_count += 1
44:         now = datetime.now().strftime("%H:%M:%S")
45: 
46:         print(f"\n[{now}] Snapshot #{snapshot_count}/{max_snap}")
47: 
48:         try:
49:             # ── Collecte ──
50:             flights = fetch_flights(
51:                 lat_min=zone["lat_min"],
52:                 lon_min=zone["lon_min"],
53:                 lat_max=zone["lat_max"],
54:                 lon_max=zone["lon_max"],
55:             )
56: 
57:             if not flights:
58:                 print("[Collector] Snapshot vide, on continue.")
59:             else:
60:                 # ── Sauvegarde ──
61:                 filepath = save_flights(flights)
62: 
63:                 # ── Métriques rapides ──
64:                 df      = load_flights(filepath)
65:                 metrics = compute_basic_metrics(df)
66: 
67:                 print(
68:                     f"  ✈  {metrics['in_flight']} en vol | "
69:                     f"🅿  {metrics['on_ground']} au sol | "
70:                     f"🌍 {metrics['unique_countries']} pays | "
71:                     f"↑  {metrics['altitude_mean']:.0f}m moy"
72:                 )
73: 
74:         except Exception as e:
75:             # On ne plante pas sur une erreur réseau passagère
76:             print(f"[Collector] ⚠ Erreur snapshot #{snapshot_count} : {e}")
77:             print("[Collector] On continue au prochain intervalle...")
78: 
79:         # ── Attente ──
80:         if snapshot_count < max_snap:
81:             print(f"[Collector] Prochain snapshot dans {interval}s...")
82:             time.sleep(interval)
83: 
84:     print("\n[Collector] Collecte terminée.")
85: 
86: 
87: if __name__ == "__main__":
88:     run_collector()

(End of file - total 88 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/adsb_ingestor.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/adsb_ingestor.py</path>
<type>file</type>
<content>
1: import requests
2: from datetime import datetime
3: from typing import Optional
4: from models.adsb_message import ADSBMessage
5: 
6: # URL de base de l'API OpenSky
7: OPENSKY_URL = "https://opensky-network.org/api/states/all"
8: 
9: 
10: def fetch_flights(
11:     lat_min: float,
12:     lon_min: float,
13:     lat_max: float,
14:     lon_max: float
15: ) -> list[ADSBMessage]:
16:     """
17:     Interroge l'API OpenSky et retourne une liste d'avions
18:     sur la zone géographique demandée.
19:     
20:     Args:
21:         lat_min, lon_min : coin bas-gauche de la zone
22:         lat_max, lon_max : coin haut-droite de la zone
23:     
24:     Returns:
25:         Liste d'objets ADSBMessage
26:     """
27: 
28:     # Construction des paramètres de la requête
29:     params = {
30:         "lamin": lat_min,
31:         "lomin": lon_min,
32:         "lamax": lat_max,
33:         "lomax": lon_max,
34:     }
35: 
36:     print(f"[OpenSky] Appel API sur la zone : {lat_min},{lon_min} → {lat_max},{lon_max}")
37: 
38:     # Appel HTTP
39:     response = requests.get(OPENSKY_URL, params=params, timeout=10)
40: 
41:     # Si l'API répond avec une erreur, on lève une exception
42:     response.raise_for_status()
43: 
44:     data = response.json()
45: 
46:     # Si aucun avion dans la zone
47:     if not data.get("states"):
48:         print("[OpenSky] Aucun avion détecté sur cette zone.")
49:         return []
50: 
51:     # Timestamp de la capture (fourni par OpenSky)
52:     capture_time = datetime.fromtimestamp(data["time"])
53: 
54:     messages = []
55: 
56:     for state in data["states"]:
57:         message = _parse_state(state, capture_time)
58:         if message:
59:             messages.append(message)
60: 
61:     print(f"[OpenSky] {len(messages)} avions récupérés.")
62:     return messages
63: 
64: 
65: def _parse_state(state: list, timestamp: datetime) -> Optional[ADSBMessage]:
66:     """
67:     Convertit une ligne brute OpenSky en objet ADSBMessage.
68:     Retourne None si les données sont trop incomplètes.
69:     """
70: 
71:     # On ignore les avions sans position GPS
72:     if state[6] is None or state[5] is None:
73:         return None
74: 
75:     return ADSBMessage(
76:         icao24=state[0],
77:         callsign=state[1].strip() if state[1] else None,
78:         origin_country=state[2],
79:         latitude=state[6],
80:         longitude=state[5],
81:         altitude=state[7],
82:         velocity=state[9],
83:         heading=state[10],
84:         on_ground=state[8],
85:         timestamp=timestamp,
86:     )

(End of file - total 86 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/gdelt_ingestor.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/gdelt_ingestor.py</path>
<type>file</type>
<content>
1: import requests
2: import pandas as pd
3: import zipfile
4: import io
5: from datetime import datetime, timedelta
6: from pathlib import Path
7: 
8: # Colonnes GDELT qui nous intéressent
9: # GDELT a 61 colonnes — on garde les utiles
10: GDELT_ALL_COLUMNS = [
11:     "GlobalEventID", "Day", "MonthYear", "Year", "FractionDate",
12:     "Actor1Code", "Actor1Name", "Actor1CountryCode", "Actor1KnownGroupCode",
13:     "Actor1EthnicCode", "Actor1Religion1Code", "Actor1Religion2Code",
14:     "Actor1Type1Code", "Actor1Type2Code", "Actor1Type3Code",
15:     "Actor2Code", "Actor2Name", "Actor2CountryCode", "Actor2KnownGroupCode",
16:     "Actor2EthnicCode", "Actor2Religion1Code", "Actor2Religion2Code",
17:     "Actor2Type1Code", "Actor2Type2Code", "Actor2Type3Code",
18:     "IsRootEvent", "EventCode", "EventBaseCode", "EventRootCode",
19:     "QuadClass", "GoldsteinScale", "NumMentions", "NumSources", "NumArticles",
20:     "AvgTone",
21:     "Actor1Geo_Type", "Actor1Geo_FullName", "Actor1Geo_CountryCode",
22:     "Actor1Geo_ADM1Code", "Actor1Geo_ADM2Code", "Actor1Geo_Lat", "Actor1Geo_Long",
23:     "Actor1Geo_FeatureID",
24:     "Actor2Geo_Type", "Actor2Geo_FullName", "Actor2Geo_CountryCode",
25:     "Actor2Geo_ADM1Code", "Actor2Geo_ADM2Code", "Actor2Geo_Lat", "Actor2Geo_Long",
26:     "Actor2Geo_FeatureID",
27:     "ActionGeo_Type", "ActionGeo_FullName", "ActionGeo_CountryCode",
28:     "ActionGeo_ADM1Code", "ActionGeo_ADM2Code", "ActionGeo_Lat", "ActionGeo_Long",
29:     "ActionGeo_FeatureID",
30:     "DATEADDED", "SOURCEURL",
31: ]
32: 
33: GDELT_DATA_DIR = Path("data/gdelt")
34: 
35: 
36: def _round_to_15min(dt: datetime) -> datetime:
37:     """
38:     GDELT publie un fichier toutes les 15 minutes.
39:     On arrondit au quart d'heure inférieur le plus proche.
40:     """
41:     minutes = (dt.minute // 15) * 15
42:     return dt.replace(minute=minutes, second=0, microsecond=0)
43: 
44: 
45: def _build_gdelt_url(dt: datetime) -> str:
46:     """
47:     Construit l'URL du fichier GDELT pour un datetime donné.
48:     """
49:     rounded = _round_to_15min(dt)
50:     timestamp = rounded.strftime("%Y%m%d%H%M%S")
51:     return f"http://data.gdeltproject.org/gdeltv2/{timestamp}.export.CSV.zip"
52: 
53: 
54: def fetch_gdelt_events(dt: datetime = None) -> pd.DataFrame:
55:     """
56:     Télécharge et parse le fichier GDELT pour un moment donné.
57: 
58:     Args:
59:         dt : datetime cible (défaut = maintenant - 30min pour éviter
60:              les fichiers pas encore publiés)
61: 
62:     Returns:
63:         DataFrame des événements géopolitiques
64:     """
65: 
66:     if dt is None:
67:         # GDELT a ~15-30min de délai — on prend il y a 30 min
68:         dt = datetime.utcnow() - timedelta(minutes=30)
69: 
70:     url = _build_gdelt_url(dt)
71:     print(f"[GDELT] Téléchargement : {url}")
72: 
73:     try:
74:         response = requests.get(url, timeout=30)
75:         response.raise_for_status()
76:     except requests.HTTPError as e:
77:         print(f"[GDELT] ⚠ Fichier indisponible : {e}")
78:         return pd.DataFrame()
79: 
80:     # Le fichier est un ZIP contenant un CSV
81:     # On le dézippe en mémoire sans écrire sur disque
82:     try:
83:         with zipfile.ZipFile(io.BytesIO(response.content)) as z:
84:             csv_filename = z.namelist()[0]
85:             with z.open(csv_filename) as f:
86:                 df = pd.read_csv(
87:                     f,
88:                     sep="\t",
89:                     header=None,
90:                     names=GDELT_ALL_COLUMNS,  # ← 61 colonnes complètes
91:                     on_bad_lines="skip",
92:                     low_memory=False,
93:                 )
94:     except Exception as e:
95:         print(f"[GDELT] ⚠ Erreur parsing : {e}")
96:         return pd.DataFrame()
97: 
98:     print(f"[GDELT] {len(df)} événements récupérés.")
99:     return df
100: 
101: 
102: def filter_events_by_zone(
103:     df: pd.DataFrame,
104:     lat_min: float,
105:     lon_min: float,
106:     lat_max: float,
107:     lon_max: float,
108: ) -> pd.DataFrame:
109:     """
110:     Filtre les événements GDELT dans une zone géographique.
111: 
112:     Args:
113:         df                    : DataFrame GDELT complet
114:         lat_min/max, lon_min/max : bounding box de ta zone
115: 
116:     Returns:
117:         Événements dans la zone uniquement
118:     """
119: 
120:     if df.empty:
121:         return df
122: 
123:     # Convertit les coordonnées en numérique
124:     # (GDELT peut avoir des valeurs manquantes)
125:     df["ActionGeo_Lat"]  = pd.to_numeric(df["ActionGeo_Lat"],  errors="coerce")
126:     df["ActionGeo_Long"] = pd.to_numeric(df["ActionGeo_Long"], errors="coerce")
127: 
128:     mask = (
129:         (df["ActionGeo_Lat"]  >= lat_min) &
130:         (df["ActionGeo_Lat"]  <= lat_max) &
131:         (df["ActionGeo_Long"] >= lon_min) &
132:         (df["ActionGeo_Long"] <= lon_max)
133:     )
134: 
135:     filtered = df[mask].copy()
136:     print(f"[GDELT] {len(filtered)} événements dans la zone.")
137:     return filtered
138: 
139: 
140: def save_gdelt_events(df: pd.DataFrame, label: str = "") -> Path:
141:     """
142:     Sauvegarde les événements GDELT en CSV local.
143:     """
144:     GDELT_DATA_DIR.mkdir(parents=True, exist_ok=True)
145: 
146:     now      = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
147:     suffix   = f"_{label}" if label else ""
148:     filepath = GDELT_DATA_DIR / f"events{suffix}_{now}.csv"
149: 
150:     df.to_csv(filepath, index=False)
151:     print(f"[GDELT] Événements sauvegardés → {filepath}")
152:     return filepath

(End of file - total 152 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/global_ingestor.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/ingestion/global_ingestor.py</path>
<type>file</type>
<content>
1: import sys
2: from pathlib import Path
3: 
4: sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
5: 
6: 
7: import time
8: import pandas as pd
9: from datetime import datetime
10: from pathlib import Path
11: 
12: from ingestion.adsb_ingestor import fetch_flights
13: from storage.data_store import save_flights
14: from utils.regions import Region, get_all_regions
15: 
16: # Délai entre chaque région pour respecter le rate limit OpenSky
17: INTER_REGION_DELAY = 6   # secondes
18: 
19: 
20: def fetch_global_snapshot(
21:     regions: list[Region] = None,
22:     delay: int = INTER_REGION_DELAY,
23: ) -> dict[str, pd.DataFrame]:
24:     """
25:     Récupère un snapshot de trafic pour chaque région mondiale.
26: 
27:     Pourquoi région par région et pas tout d'un coup ?
28:     OpenSky limite la taille des bounding boxes et le nombre
29:     de requêtes. On découpe pour rester dans les limites.
30: 
31:     Args:
32:         regions : liste de régions (défaut = toutes)
33:         delay   : pause entre régions (secondes)
34: 
35:     Returns:
36:         Dict {code_région: DataFrame}
37:     """
38: 
39:     if regions is None:
40:         regions = get_all_regions()
41: 
42:     results  = {}
43:     total    = len(regions)
44: 
45:     print(f"[Global] Démarrage snapshot mondial — {total} régions")
46:     print(f"[Global] Durée estimée : ~{total * delay}s")
47:     print("─" * 50)
48: 
49:     for i, region in enumerate(regions, 1):
50:         print(f"[{i}/{total}] {region.name} ({region.code})...")
51: 
52:         try:
53:             messages = fetch_flights(
54:                 lat_min=region.lat_min,
55:                 lon_min=region.lon_min,
56:                 lat_max=region.lat_max,
57:                 lon_max=region.lon_max,
58:             )
59: 
60:             if messages:
61:                 # Sauvegarde avec le code région dans le nom de fichier
62:                 save_flights(messages, suffix=region.code)
63: 
64:                 # Convertit en DataFrame pour le retour
65:                 df = pd.DataFrame([vars(m) for m in messages])
66:                 df["region"] = region.code
67:                 results[region.code] = df
68: 
69:                 print(f"  ✓ {len(messages)} avions")
70:             else:
71:                 print(f"  ─ Aucun avion")
72:                 results[region.code] = pd.DataFrame()
73: 
74:         except Exception as e:
75:             print(f"  ✗ Erreur : {e}")
76:             results[region.code] = pd.DataFrame()
77: 
78:         # Pause sauf pour la dernière région
79:         if i < total:
80:             time.sleep(delay)
81: 
82:     total_aircraft = sum(len(df) for df in results.values())
83:     print("─" * 50)
84:     print(f"[Global] ✓ Snapshot terminé — {total_aircraft} avions au total")
85: 
86:     return results
87: 
88: 
89: def build_global_summary(snapshots: dict[str, pd.DataFrame]) -> pd.DataFrame:
90:     """
91:     Construit un résumé par région à partir des snapshots.
92: 
93:     Returns:
94:         DataFrame avec une ligne par région et ses métriques
95:     """
96: 
97:     rows = []
98:     for code, df in snapshots.items():
99:         if df.empty:
100:             rows.append({
101:                 "region_code"     : code,
102:                 "total_aircraft"  : 0,
103:                 "in_flight"       : 0,
104:                 "on_ground"       : 0,
105:                 "altitude_mean"   : 0,
106:                 "velocity_mean"   : 0,
107:                 "unique_countries": 0,
108:             })
109:             continue
110: 
111:         rows.append({
112:             "region_code"      : code,
113:             "total_aircraft"   : len(df),
114:             "in_flight"        : int((~df["on_ground"]).sum()),
115:             "on_ground"        : int(df["on_ground"].sum()),
116:             "altitude_mean"    : round(df["altitude"].mean(), 0),
117:             "velocity_mean"    : round(df["velocity"].mean(), 0),
118:             "unique_countries" : int(df["origin_country"].nunique()),
119:             "timestamp"        : datetime.utcnow().isoformat(),
120:         })
121: 
122:     return pd.DataFrame(rows).sort_values("total_aircraft", ascending=False)

(End of file - total 122 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/models/adsb_message.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/models/adsb_message.py</path>
<type>file</type>
<content>
1: from dataclasses import dataclass
2: from typing import Optional
3: from datetime import datetime
4: 
5: @dataclass
6: class ADSBMessage:
7:     """
8:     Représente un message ADS-B émis par un avion.
9:     Correspond exactement à ce que retourne l'API OpenSky.
10:     """
11:     
12:     icao24: str                      # Identifiant unique matériel de l'avion
13:     callsign: Optional[str]          # Indicatif de vol (ex: AFR123) — peut être vide
14:     origin_country: str              # Pays d'origine (ex: France)
15:     latitude: Optional[float]        # Position GPS
16:     longitude: Optional[float]       # Position GPS
17:     altitude: Optional[float]        # Altitude en mètres
18:     velocity: Optional[float]        # Vitesse en m/s
19:     heading: Optional[float]         # Cap (direction) en degrés
20:     on_ground: bool                  # Est-il au sol ?
21:     timestamp: datetime              # Moment de la capture

(End of file - total 21 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/storage/data_store.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/storage/data_store.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: from pathlib import Path
3: from datetime import datetime
4: from models.adsb_message import ADSBMessage
5: 
6: # Dossier où on sauvegarde les données
7: DATA_DIR = Path("data/raw")
8: 
9: 
10: def save_flights(messages: list[ADSBMessage], suffix: str = "") -> Path:
11:     """
12:     Sauvegarde une liste d'ADSBMessage dans un fichier CSV horodaté.
13:     
14:     Args:
15:         messages : liste d'avions récupérés depuis OpenSky
16:     
17:     Returns:
18:         Le chemin du fichier créé
19:     """
20: 
21:     # Crée le dossier data/raw/ s'il n'existe pas
22:     DATA_DIR.mkdir(parents=True, exist_ok=True)
23: 
24:     # Convertit les objets en liste de dictionnaires
25:     # dataclasses.asdict() transforme un ADSBMessage → dict Python
26:     records = []
27:     for msg in messages:
28:         records.append({
29:             "icao24":         msg.icao24,
30:             "callsign":       msg.callsign,
31:             "origin_country": msg.origin_country,
32:             "latitude":       msg.latitude,
33:             "longitude":      msg.longitude,
34:             "altitude":       msg.altitude,
35:             "velocity":       msg.velocity,
36:             "heading":        msg.heading,
37:             "on_ground":      msg.on_ground,
38:             "timestamp":      msg.timestamp,
39:         })
40: 
41:     # Crée le DataFrame pandas
42:     df = pd.DataFrame(records)
43: 
44:     # Nom du fichier avec timestamp pour ne pas écraser les précédents
45:     # Exemple : flights_2026-03-03_14-30-00.csv
46:     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
47:     suffix_ = f"_{suffix}" if suffix else ""
48:     filepath = DATA_DIR / f"flights_{now}_{suffix_}.csv"
49: 
50:     # Sauvegarde en CSV sans l'index pandas (colonne 0,1,2...)
51:     df.to_csv(filepath, index=False)
52: 
53:     print(f"[DataStore] {len(df)} avions sauvegardés → {filepath}")
54:     return filepath
55: 
56: 
57: def load_flights(filepath: Path) -> pd.DataFrame:
58:     """
59:     Charge un fichier CSV de vols et retourne un DataFrame.
60:     
61:     Args:
62:         filepath : chemin vers le fichier CSV
63:     
64:     Returns:
65:         DataFrame pandas avec les données de vols
66:     """
67: 
68:     df = pd.read_csv(filepath, parse_dates=["timestamp"])
69: 
70:     print(f"[DataStore] {len(df)} avions chargés depuis {filepath}")
71:     return df
72: 
73: def load_all_flights(data_dir: Path = Path("data/raw")) -> pd.DataFrame:
74:     """
75:     Charge TOUS les fichiers CSV du dossier et les fusionne.
76:     Chaque fichier = un snapshot = un moment dans le temps.
77: 
78:     Returns:
79:         DataFrame combiné, trié par timestamp
80:     """
81: 
82:     csv_files = sorted(data_dir.glob("flights_*.csv"))
83: 
84:     if not csv_files:
85:         raise FileNotFoundError(f"[DataStore] Aucun fichier CSV dans {data_dir}")
86: 
87:     print(f"[DataStore] {len(csv_files)} snapshots trouvés...")
88: 
89:     # Charge chaque fichier et les empile verticalement
90:     # pd.concat() fusionne une liste de DataFrames
91:     frames = []
92:     for f in csv_files:
93:         df = pd.read_csv(f, parse_dates=["timestamp"])
94:         frames.append(df)
95: 
96:     combined = pd.concat(frames, ignore_index=True)
97:     combined = combined.sort_values("timestamp").reset_index(drop=True)
98: 
99:     print(f"[DataStore] {len(combined)} lignes totales sur {combined['timestamp'].nunique()} snapshots")
100:     return combined
101: 
102: def load_latest_global(data_dir: Path = DATA_DIR) -> dict[str, pd.DataFrame]:
103:     """
104:     Charge le dernier snapshot de chaque région mondiale.
105: 
106:     Pour chaque code région (EU_W, ME, RU...) on prend
107:     le fichier le plus récent.
108: 
109:     Returns:
110:         Dict {code_région: DataFrame}
111:     """
112: 
113:     region_files: dict[str, Path] = {}
114: 
115:     for f in sorted(data_dir.glob("flights_*_*.csv")):
116:         # Le nom contient le code région après le dernier "_"
117:         # ex: flights_2026-03-11_17-14-01__EU_E.csv → EU_E
118:         parts = f.stem.split("__")
119:         if len(parts) < 2:
120:             continue
121:         code = parts[-1]
122:         # On garde toujours le plus récent (sorted garantit l'ordre)
123:         region_files[code] = f
124: 
125:     result = {}
126:     for code, filepath in region_files.items():
127:         df = pd.read_csv(filepath)
128:         if not df.empty:
129:             df["region"] = code
130:         result[code] = df
131: 
132:     print(f"[DataStore] {len(result)} régions chargées depuis {data_dir}")
133:     return result
134: 
135: 
136: def load_latest_snapshot(data_dir: Path = DATA_DIR) -> pd.DataFrame:
137:     """
138:     Fusionne tous les derniers snapshots régionaux
139:     en un seul DataFrame mondial.
140: 
141:     Returns:
142:         DataFrame avec colonne 'region' ajoutée
143:     """
144: 
145:     regional = load_latest_global(data_dir)
146: 
147:     if not regional:
148:         return pd.DataFrame()
149: 
150:     frames = [df for df in regional.values() if not df.empty]
151:     if not frames:
152:         return pd.DataFrame()
153: 
154:     combined = pd.concat(frames, ignore_index=True)
155:     print(f"[DataStore] Total mondial : {len(combined)} avions")
156:     return combined

(End of file - total 156 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/config_loader.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/config_loader.py</path>
<type>file</type>
<content>
1: import yaml
2: from pathlib import Path
3: 
4: 
5: def load_config(config_path: str = "config/settings.yaml") -> dict:
6:     """
7:     Charge le fichier de configuration YAML.
8: 
9:     Returns:
10:         Dictionnaire de configuration
11:     """
12:     path = Path(config_path)
13: 
14:     if not path.exists():
15:         raise FileNotFoundError(f"[Config] Fichier introuvable : {path.resolve()}")
16: 
17:     with open(path, "r") as f:
18:         config = yaml.safe_load(f)
19: 
20:     print(f"[Config] Configuration chargée depuis {path}")
21:     return config

(End of file - total 21 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/regions.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/regions.py</path>
<type>file</type>
<content>
1: from dataclasses import dataclass
2: 
3: 
4: @dataclass
5: class Region:
6:     """
7:     Définit une zone géographique d'analyse.
8: 
9:     lat_min/max : latitude  sud → nord
10:     lon_min/max : longitude ouest → est
11:     """
12:     name     : str
13:     code     : str       # identifiant court pour les fichiers
14:     lat_min  : float
15:     lon_min  : float
16:     lat_max  : float
17:     lon_max  : float
18:     color    : str = "#58a6ff"   # couleur sur le dashboard
19: 
20: 
21: # ══════════════════════════════════════════════
22: # RÉGIONS MONDIALES
23: # ══════════════════════════════════════════════
24: 
25: REGIONS: dict[str, Region] = {
26: 
27:     # ── Europe ──
28:     "europe_west": Region(
29:         name="Europe Occidentale", code="EU_W",
30:         lat_min=36.0, lon_min=-10.0,
31:         lat_max=55.0, lon_max=20.0,
32:         color="#58a6ff",
33:     ),
34:     "europe_east": Region(
35:         name="Europe Orientale", code="EU_E",
36:         lat_min=45.0, lon_min=20.0,
37:         lat_max=60.0, lon_max=40.0,
38:         color="#3498db",
39:     ),
40:     "russia": Region(
41:         name="Russie / Asie Centrale", code="RU",
42:         lat_min=50.0, lon_min=40.0,
43:         lat_max=72.0, lon_max=130.0,
44:         color="#e74c3c",
45:     ),
46: 
47:     # ── Moyen-Orient ──
48:     "middle_east": Region(
49:         name="Moyen-Orient", code="ME",
50:         lat_min=12.0, lon_min=30.0,
51:         lat_max=42.0, lon_max=65.0,
52:         color="#e67e22",
53:     ),
54: 
55:     # ── Asie ──
56:     "asia_south": Region(
57:         name="Asie du Sud", code="AS_S",
58:         lat_min=5.0,  lon_min=60.0,
59:         lat_max=35.0, lon_max=90.0,
60:         color="#9b59b6",
61:     ),
62:     "asia_east": Region(
63:         name="Asie de l'Est", code="AS_E",
64:         lat_min=20.0, lon_min=100.0,
65:         lat_max=50.0, lon_max=145.0,
66:         color="#8e44ad",
67:     ),
68: 
69:     # ── Amériques ──
70:     "north_america": Region(
71:         name="Amérique du Nord", code="NA",
72:         lat_min=25.0, lon_min=-130.0,
73:         lat_max=60.0, lon_max=-60.0,
74:         color="#2ecc71",
75:     ),
76:     "south_america": Region(
77:         name="Amérique du Sud", code="SA",
78:         lat_min=-55.0, lon_min=-80.0,
79:         lat_max=15.0,  lon_max=-35.0,
80:         color="#27ae60",
81:     ),
82: 
83:     # ── Afrique ──
84:     "africa": Region(
85:         name="Afrique", code="AF",
86:         lat_min=-35.0, lon_min=-20.0,
87:         lat_max=37.0,  lon_max=50.0,
88:         color="#f39c12",
89:     ),
90: 
91:     # ── Zones de tension spécifiques ──
92:     "ukraine_zone": Region(
93:         name="Zone Ukraine / Mer Noire", code="UKR",
94:         lat_min=43.0, lon_min=22.0,
95:         lat_max=52.0, lon_max=40.0,
96:         color="#e74c3c",
97:     ),
98:     "taiwan_strait": Region(
99:         name="Détroit de Taïwan", code="TWN",
100:         lat_min=20.0, lon_min=115.0,
101:         lat_max=30.0, lon_max=125.0,
102:         color="#e74c3c",
103:     ),
104:     "persian_gulf": Region(
105:         name="Golfe Persique", code="PG",
106:         lat_min=22.0, lon_min=48.0,
107:         lat_max=30.0, lon_max=60.0,
108:         color="#e67e22",
109:     ),
110: }
111: 
112: 
113: def get_region(code: str) -> Region:
114:     """Retourne une région par son code."""
115:     for r in REGIONS.values():
116:         if r.code == code:
117:             return r
118:     raise KeyError(f"Région inconnue : {code}")
119: 
120: 
121: def get_all_regions() -> list[Region]:
122:     return list(REGIONS.values())

(End of file - total 122 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/helpers.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/utils/helpers.py</path>
<type>file</type>
<content>


(End of file - total 0 lines)
</content>
```

---

## Assistant (Build · Muse Spark 1.2 Free · 3.6s)

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/air_traffic_analyser.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/air_traffic_analyser.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: import numpy as np
3: from pathlib import Path
4: 
5: def compute_basic_metrics(df: pd.DataFrame) -> dict:
6:     """
7:     Calcule les métriques de base sur un snapshot de trafic.
8: 
9:     Args:
10:         df : DataFrame chargé depuis le CSV
11: 
12:     Returns:
13:         Dictionnaire de métriques
14:     """
15: 
16:     in_flight = df[df["on_ground"] == False]
17:     on_ground = df[df["on_ground"] == True]
18: 
19:     metrics = {
20:         # ── Comptages ──
21:         "total_aircraft"     : len(df),
22:         "in_flight"          : len(in_flight),
23:         "on_ground"          : len(on_ground),
24:         "ground_ratio"       : len(on_ground) / len(df) if len(df) > 0 else 0,
25: 
26:         # ── Altitude (seulement ceux en vol) ──
27:         "altitude_mean"      : in_flight["altitude"].mean(),
28:         "altitude_median"    : in_flight["altitude"].median(),
29:         "altitude_std"       : in_flight["altitude"].std(),
30: 
31:         # ── Vitesse ──
32:         "velocity_mean"      : in_flight["velocity"].mean(),
33:         "velocity_median"    : in_flight["velocity"].median(),
34: 
35:         # ── Diversité ──
36:         "unique_countries"   : df["origin_country"].nunique(),
37:         "unique_flights"     : df["icao24"].nunique(),
38: 
39:         # ── Timestamp ──
40:         "captured_at"        : df["timestamp"].iloc[0],
41:     }
42: 
43:     return metrics
44: 
45: 
46: def compute_country_breakdown(df: pd.DataFrame) -> pd.DataFrame:
47:     """
48:     Retourne un tableau de métriques par pays.
49: 
50:     Utile pour détecter : un pays qui disparaît soudainement.
51:     """
52: 
53:     breakdown = (
54:         df.groupby("origin_country")
55:         .agg(
56:             total        = ("icao24",    "count"),
57:             in_flight    = ("on_ground", lambda x: (~x).sum()),
58:             on_ground    = ("on_ground", "sum"),
59:             alt_mean     = ("altitude",  "mean"),
60:             vel_mean     = ("velocity",  "mean"),
61:         )
62:         .sort_values("total", ascending=False)
63:         .reset_index()
64:     )
65: 
66:     return breakdown
67: 
68: 
69: def compute_altitude_distribution(df: pd.DataFrame) -> pd.DataFrame:
70:     """
71:     Distribue les avions en tranches d'altitude.
72: 
73:     Tranche       | Signification
74:     0 - 1000 m    | Décollage / atterrissage
75:     1000 - 5000 m | Vol court courrier / hélicos
76:     5000 - 9000 m | Croisière court/moyen courrier
77:     9000 m+       | Long courrier / haute altitude
78:     """
79: 
80:     bins   = [0, 1000, 5000, 9000, 15000]
81:     labels = ["0-1000m", "1000-5000m", "5000-9000m", "9000m+"]
82: 
83:     in_flight = df[df["on_ground"] == False].copy()
84: 
85:     # pd.cut() découpe une colonne continue en catégories
86:     in_flight["alt_band"] = pd.cut(
87:         in_flight["altitude"],
88:         bins=bins,
89:         labels=labels,
90:         right=True
91:     )
92: 
93:     distribution = (
94:         in_flight["alt_band"]
95:         .value_counts()
96:         .sort_index()
97:         .reset_index()
98:     )
99:     distribution.columns = ["altitude_band", "count"]
100: 
101:     return distribution
102: 
103: 
104: def print_report(df: pd.DataFrame) -> None:
105:     """
106:     Affiche un rapport complet dans le terminal.
107:     """
108: 
109:     metrics   = compute_basic_metrics(df)
110:     countries = compute_country_breakdown(df)
111:     altitudes = compute_altitude_distribution(df)
112: 
113:     print("\n" + "═" * 50)
114:     print("  RAPPORT D'ANALYSE — TRAFIC AÉRIEN")
115:     print("═" * 50)
116: 
117:     print(f"\n📅 Capture        : {metrics['captured_at']}")
118:     print(f"✈  Total avions   : {metrics['total_aircraft']}")
119:     print(f"🛫 En vol         : {metrics['in_flight']}")
120:     print(f"🅿  Au sol         : {metrics['on_ground']} ({metrics['ground_ratio']:.1%})")
121:     print(f"🌍 Pays           : {metrics['unique_countries']}")
122: 
123:     print(f"\n── Altitude (avions en vol) ──")
124:     print(f"   Moyenne  : {metrics['altitude_mean']:.0f} m")
125:     print(f"   Médiane  : {metrics['altitude_median']:.0f} m")
126:     print(f"   Écart-type : {metrics['altitude_std']:.0f} m")
127: 
128:     print(f"\n── Vitesse ──")
129:     print(f"   Moyenne  : {metrics['velocity_mean']:.0f} m/s")
130:     print(f"   Médiane  : {metrics['velocity_median']:.0f} m/s")
131: 
132:     print(f"\n── Distribution altitude ──")
133:     for _, row in altitudes.iterrows():
134:         bar = "█" * int(row["count"] / metrics["in_flight"] * 30)
135:         print(f"   {row['altitude_band']:12} {bar} {row['count']}")
136: 
137:     print(f"\n── Top 10 pays ──")
138:     for _, row in countries.head(10).iterrows():
139:         print(f"   {row['origin_country']:25} {row['total']:4} avions  "
140:               f"alt moy: {row['alt_mean']:.0f}m")

(End of file - total 140 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/correlator.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/correlator.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: import numpy as np
3: from datetime import datetime, timedelta
4: from pathlib import Path
5: 
6: 
7: def correlate_event_with_traffic(
8:     event: dict,
9:     ts: pd.DataFrame,
10:     window_hours: int = 24,
11: ) -> dict:
12:     """
13:     Corrèle un événement géopolitique avec la série temporelle
14:     de trafic aérien.
15: 
16:     Args:
17:         event        : dict avec clés {name, lat, lon, timestamp, goldstein}
18:         ts           : série temporelle (output de build_timeseries)
19:         window_hours : fenêtre d'analyse en heures (avant ET après)
20: 
21:     Returns:
22:         Dictionnaire de corrélation avec scores
23:     """
24: 
25:     event_time = pd.to_datetime(event["timestamp"])
26: 
27:     # ── Découpe la fenêtre temporelle ──
28:     before_mask = (
29:         (ts["timestamp"] >= event_time - timedelta(hours=window_hours)) &
30:         (ts["timestamp"] <  event_time)
31:     )
32:     after_mask = (
33:         (ts["timestamp"] >  event_time) &
34:         (ts["timestamp"] <= event_time + timedelta(hours=window_hours))
35:     )
36: 
37:     before = ts[before_mask]
38:     after  = ts[after_mask]
39: 
40:     # ── Calcule les moyennes avant / après ──
41:     avg_before = before["total_aircraft"].mean() if len(before) > 0 else None
42:     avg_after  = after["total_aircraft"].mean()  if len(after)  > 0 else None
43: 
44:     # ── Calcule la variation ──
45:     if avg_before and avg_after and avg_before > 0:
46:         delta_pct = ((avg_after - avg_before) / avg_before) * 100
47:     else:
48:         delta_pct = None
49: 
50:     # ── Calcule l'altitude avant / après ──
51:     alt_before = before["altitude_mean"].mean() if len(before) > 0 else None
52:     alt_after  = after["altitude_mean"].mean()  if len(after)  > 0 else None
53: 
54:     if alt_before and alt_after and alt_before > 0:
55:         alt_delta_pct = ((alt_after - alt_before) / alt_before) * 100
56:     else:
57:         alt_delta_pct = None
58: 
59:     # ── Score de corrélation simple ──
60:     # On combine variation trafic + score Goldstein
61:     # Goldstein négatif + trafic en baisse = signal fort
62:     correlation_signal = _compute_signal(
63:         delta_pct=delta_pct,
64:         goldstein=event.get("goldstein", 0),
65:         alt_delta_pct=alt_delta_pct,
66:     )
67: 
68:     return {
69:         # Infos événement
70:         "event_name"       : event["name"],
71:         "event_time"       : event_time,
72:         "event_goldstein"  : event.get("goldstein", 0),
73:         "event_lat"        : event.get("lat"),
74:         "event_lon"        : event.get("lon"),
75: 
76:         # Snapshots analysés
77:         "snapshots_before" : len(before),
78:         "snapshots_after"  : len(after),
79: 
80:         # Trafic
81:         "avg_traffic_before" : avg_before,
82:         "avg_traffic_after"  : avg_after,
83:         "traffic_delta_pct"  : delta_pct,
84: 
85:         # Altitude
86:         "avg_altitude_before" : alt_before,
87:         "avg_altitude_after"  : alt_after,
88:         "altitude_delta_pct"  : alt_delta_pct,
89: 
90:         # Signal final
91:         "correlation_signal"  : correlation_signal,
92:         "signal_label"        : _signal_label(correlation_signal),
93:     }
94: 
95: 
96: def _compute_signal(
97:     delta_pct: float,
98:     goldstein: float,
99:     alt_delta_pct: float,
100: ) -> float:
101:     """
102:     Calcule un score de signal de corrélation entre 0 et 1.
103: 
104:     Logique :
105:     - Goldstein très négatif + trafic en baisse = signal fort
106:     - Goldstein positif + trafic stable          = signal faible
107: 
108:     Returns:
109:         Score entre 0.0 (aucune corrélation) et 1.0 (forte corrélation)
110:     """
111: 
112:     if delta_pct is None or goldstein is None:
113:         return 0.0
114: 
115:     # Normalise Goldstein : [-10, +10] → [1, 0]
116:     # Plus c'est conflictuel (négatif), plus le poids est fort
117:     goldstein_weight = (10 - goldstein) / 20
118: 
119:     # Normalise la variation trafic
120:     # Une chute de 20%+ = signal max
121:     traffic_signal = min(abs(delta_pct) / 20.0, 1.0)
122: 
123:     # Bonus si l'altitude aussi varie (contournement de zone)
124:     alt_bonus = 0.0
125:     if alt_delta_pct is not None and abs(alt_delta_pct) > 5:
126:         alt_bonus = 0.1
127: 
128:     # Score pondéré
129:     score = (goldstein_weight * 0.4) + (traffic_signal * 0.5) + alt_bonus
130:     return round(min(score, 1.0), 3)
131: 
132: 
133: def _signal_label(score: float) -> str:
134:     """Traduit un score numérique en étiquette lisible."""
135:     if score >= 0.7:
136:         return "🔴 SIGNAL FORT"
137:     elif score >= 0.4:
138:         return "🟡 SIGNAL MODÉRÉ"
139:     elif score >= 0.2:
140:         return "🟢 SIGNAL FAIBLE"
141:     else:
142:         return "⚪ PAS DE SIGNAL"
143: 
144: 
145: def correlate_multiple_events(
146:     events: list[dict],
147:     ts: pd.DataFrame,
148:     window_hours: int = 24,
149: ) -> pd.DataFrame:
150:     """
151:     Corrèle une liste d'événements avec la série temporelle.
152: 
153:     Returns:
154:         DataFrame trié par force du signal
155:     """
156: 
157:     results = []
158:     for event in events:
159:         result = correlate_event_with_traffic(event, ts, window_hours)
160:         results.append(result)
161: 
162:     df = pd.DataFrame(results)
163: 
164:     if not df.empty:
165:         df = df.sort_values("correlation_signal", ascending=False)
166: 
167:     return df
168: 
169: 
170: def print_correlation_report(correlations: pd.DataFrame) -> None:
171:     """
172:     Affiche le rapport de corrélation dans le terminal.
173:     """
174: 
175:     print("\n" + "═" * 60)
176:     print("  RAPPORT DE CORRÉLATION — Trafic ↔ Géopolitique")
177:     print("═" * 60)
178: 
179:     if correlations.empty:
180:         print("  Aucune corrélation calculée.")
181:         return
182: 
183:     for _, row in correlations.iterrows():
184:         print(f"\n  {row['signal_label']}")
185:         print(f"  Événement  : {row['event_name']}")
186:         print(f"  Date       : {row['event_time']}")
187:         print(f"  Goldstein  : {row['event_goldstein']}")
188:         print(f"  ─────────────────────────────")
189: 
190:         if row['avg_traffic_before']:
191:             print(f"  Trafic avant   : {row['avg_traffic_before']:.0f} avions")
192:             print(f"  Trafic après   : {row['avg_traffic_after']:.0f} avions")
193:             print(f"  Variation      : {row['traffic_delta_pct']:+.1f}%")
194: 
195:         if row['avg_altitude_before']:
196:             print(f"  Altitude avant : {row['avg_altitude_before']:.0f} m")
197:             print(f"  Altitude après : {row['avg_altitude_after']:.0f} m")
198:             print(f"  Var. altitude  : {row['altitude_delta_pct']:+.1f}%")
199: 
200:         print(f"  Score signal   : {row['correlation_signal']}")

(End of file - total 200 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/gdelt_correlator.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/gdelt_correlator.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: from datetime import datetime, timedelta
3: from pathlib import Path
4: 
5: from ingestion.gdelt_ingestor import (
6:     fetch_gdelt_events,
7:     filter_events_by_zone,
8:     save_gdelt_events,
9: )
10: from analysis.correlator import correlate_multiple_events
11: 
12: 
13: # ── Codes CAMEO importants pour l'OSINT aérien ──
14: # CAMEO = système de classification des événements géopolitiques
15: # Source : https://www.gdeltproject.org/data/documentation/CAMEO.Manual.1.1b3.pdf
16: CAMEO_CODES_OF_INTEREST = {
17:     "13"  : "🚫 Menace / ultimatum",
18:     "14"  : "💣 Protestation",
19:     "15"  : "⚔️  Conflit armé",
20:     "16"  : "💥 Attaque",
21:     "17"  : "🔒 Coercition",
22:     "18"  : "🚨 Attentat",
23:     "19"  : "☢️  Guerre",
24:     "20"  : "🛑 Sanction / embargo",
25: }
26: 
27: 
28: def gdelt_to_events(df: pd.DataFrame) -> list[dict]:
29:     """
30:     Convertit un DataFrame GDELT en liste d'événements
31:     compatibles avec le corrélateur.
32: 
33:     On garde uniquement les événements :
34:     - Avec coordonnées GPS valides
35:     - Avec un score Goldstein négatif (conflictuels)
36:     - Avec au moins 3 mentions médias (filtre le bruit)
37: 
38:     Args:
39:         df : DataFrame GDELT filtré par zone
40: 
41:     Returns:
42:         Liste de dicts {name, timestamp, lat, lon, goldstein, ...}
43:     """
44: 
45:     if df.empty:
46:         return []
47: 
48:     # ── Nettoyage ──
49:     df = df.copy()
50:     df["ActionGeo_Lat"]   = pd.to_numeric(df["ActionGeo_Lat"],   errors="coerce")
51:     df["ActionGeo_Long"]  = pd.to_numeric(df["ActionGeo_Long"],  errors="coerce")
52:     df["GoldsteinScale"]  = pd.to_numeric(df["GoldsteinScale"],  errors="coerce")
53:     df["NumMentions"]     = pd.to_numeric(df["NumMentions"],      errors="coerce")
54: 
55:     # ── Filtres qualité ──
56:     df = df.dropna(subset=["ActionGeo_Lat", "ActionGeo_Long", "GoldsteinScale"])
57:     df = df[df["NumMentions"] >= 3]          # au moins 3 mentions
58:     df = df[df["GoldsteinScale"] <= -1.0]    # événements conflictuels uniquement
59: 
60:     if df.empty:
61:         print("[GDELTCorrelator] Aucun événement conflictuel significatif.")
62:         return []
63: 
64:     # ── Déduplique par lieu ──
65:     # GDELT peut avoir 50 lignes pour le même événement
66:     # On garde le plus mentionné par lieu
67:     df = (
68:         df.sort_values("NumMentions", ascending=False)
69:           .drop_duplicates(subset=["ActionGeo_FullName"])
70:           .head(20)   # max 20 événements pour ne pas surcharger
71:     )
72: 
73:     # ── Construit le timestamp ──
74:     # GDELT stocke la date en YYYYMMDDHHMMSS dans DATEADDED
75:     def parse_gdelt_timestamp(val) -> datetime:
76:         try:
77:             return datetime.strptime(str(int(val)), "%Y%m%d%H%M%S")
78:         except Exception:
79:             return datetime.utcnow()
80: 
81:     events = []
82:     for _, row in df.iterrows():
83:         # Code CAMEO → label lisible
84:         event_code = str(row.get("EventBaseCode", ""))
85:         code_label = CAMEO_CODES_OF_INTEREST.get(
86:             event_code[:2],
87:             f"Événement {event_code}"
88:         )
89: 
90:         events.append({
91:             "name"       : f"{code_label} — {row['ActionGeo_FullName']}",
92:             "timestamp"  : parse_gdelt_timestamp(row["DATEADDED"]),
93:             "lat"        : row["ActionGeo_Lat"],
94:             "lon"        : row["ActionGeo_Long"],
95:             "goldstein"  : row["GoldsteinScale"],
96:             "mentions"   : row["NumMentions"],
97:             "source_url" : row.get("SOURCEURL", ""),
98:             "avg_tone"   : row.get("AvgTone", 0),
99:         })
100: 
101:     print(f"[GDELTCorrelator] {len(events)} événements convertis.")
102:     return events
103: 
104: 
105: def run_gdelt_correlation(
106:     ts: pd.DataFrame,
107:     lat_min: float,
108:     lon_min: float,
109:     lat_max: float,
110:     lon_max: float,
111:     window_hours: int = 6,
112:     lookback_hours: int = 2,
113: ) -> pd.DataFrame:
114:     """
115:     Pipeline complet : GDELT → filtrage → corrélation.
116: 
117:     Args:
118:         ts            : série temporelle de trafic
119:         lat/lon       : bounding box de la zone
120:         window_hours  : fenêtre de corrélation avant/après
121:         lookback_hours: combien d'heures en arrière chercher dans GDELT
122: 
123:     Returns:
124:         DataFrame de corrélations trié par signal
125:     """
126: 
127:     print("\n[GDELTCorrelator] Démarrage pipeline GDELT → Corrélation")
128:     print("─" * 50)
129: 
130:     all_correlations = []
131: 
132:     # ── Télécharge les fichiers GDELT des X dernières heures ──
133:     # GDELT publie un fichier toutes les 15 min
134:     # On itère sur les créneaux
135:     now = datetime.utcnow()
136:     slots = []
137:     current = now - timedelta(hours=lookback_hours)
138: 
139:     while current <= now:
140:         slots.append(current)
141:         current += timedelta(minutes=15)
142: 
143:     print(f"[GDELTCorrelator] {len(slots)} créneaux GDELT à analyser...")
144: 
145:     seen_events = set()   # évite les doublons entre fichiers
146: 
147:     for slot in slots:
148:         # ── Télécharge ──
149:         df_gdelt = fetch_gdelt_events(dt=slot)
150: 
151:         if df_gdelt.empty:
152:             continue
153: 
154:         # ── Filtre zone ──
155:         df_zone = filter_events_by_zone(df_gdelt, lat_min, lon_min, lat_max, lon_max)
156: 
157:         if df_zone.empty:
158:             continue
159: 
160:         # ── Convertit ──
161:         events = gdelt_to_events(df_zone)
162: 
163:         # ── Déduplique par nom d'événement ──
164:         new_events = []
165:         for e in events:
166:             key = e["name"]
167:             if key not in seen_events:
168:                 seen_events.add(key)
169:                 new_events.append(e)
170: 
171:         if not new_events:
172:             continue
173: 
174:         # ── Corrèle ──
175:         correlations = correlate_multiple_events(
176:             new_events, ts, window_hours=window_hours
177:         )
178:         all_correlations.append(correlations)
179: 
180:     # ── Fusionne tous les résultats ──
181:     if not all_correlations:
182:         print("[GDELTCorrelator] Aucune corrélation trouvée sur la période.")
183:         return pd.DataFrame()
184: 
185:     import pandas as pd
186:     final = pd.concat(all_correlations, ignore_index=True)
187:     final = final.sort_values("correlation_signal", ascending=False)
188: 
189:     print(f"\n[GDELTCorrelator] {len(final)} corrélations calculées.")
190:     return final

(End of file - total 190 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/timeseries_analyzer.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/analysis/timeseries_analyzer.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: import numpy as np
3: from pathlib import Path
4: 
5: 
6: def build_timeseries(df: pd.DataFrame) -> pd.DataFrame:
7:     """
8:     Agrège le DataFrame combiné en une série temporelle.
9:     Une ligne par snapshot = évolution dans le temps.
10: 
11:     Args:
12:         df : DataFrame combiné (tous les snapshots)
13: 
14:     Returns:
15:         DataFrame avec une ligne par timestamp
16:     """
17: 
18:     # groupby("timestamp") → groupe toutes les lignes du même snapshot
19:     # puis on calcule les métriques pour chaque groupe
20:     ts = (
21:         df.groupby("timestamp")
22:         .agg(
23:             total_aircraft   = ("icao24",    "count"),
24:             in_flight        = ("on_ground", lambda x: (~x).sum()),
25:             on_ground        = ("on_ground", "sum"),
26:             unique_countries = ("origin_country", "nunique"),
27:             altitude_mean    = ("altitude",  "mean"),
28:             velocity_mean    = ("velocity",  "mean"),
29:         )
30:         .reset_index()
31:         .sort_values("timestamp")
32:     )
33: 
34:     # Calcule le ratio avions au sol
35:     ts["ground_ratio"] = ts["on_ground"] / ts["total_aircraft"]
36: 
37:     # Calcule la variation absolue entre chaque snapshot
38:     # diff() = valeur[t] - valeur[t-1]
39:     ts["delta_total"]    = ts["total_aircraft"].diff()
40:     ts["delta_inflight"] = ts["in_flight"].diff()
41: 
42:     # Calcule la variation en % entre chaque snapshot
43:     ts["pct_change"] = ts["total_aircraft"].pct_change() * 100
44: 
45:     return ts
46: 
47: 
48: def detect_anomalies(ts: pd.DataFrame, z_threshold: float = 2.0) -> pd.DataFrame:
49:     """
50:     Détecte les snapshots anormaux via Z-score.
51: 
52:     Le Z-score mesure combien d'écarts-types une valeur
53:     est éloignée de la moyenne.
54: 
55:     Z > 2.0  → valeur inhabituellement haute
56:     Z < -2.0 → valeur inhabituellement basse
57: 
58:     Args:
59:         ts           : série temporelle (output de build_timeseries)
60:         z_threshold  : seuil de détection (2.0 = top/bottom 5%)
61: 
62:     Returns:
63:         DataFrame des snapshots anormaux uniquement
64:     """
65: 
66:     mean = ts["total_aircraft"].mean()
67:     std  = ts["total_aircraft"].std()
68: 
69:     # Évite la division par zéro si std = 0
70:     if std == 0:
71:         print("[Anomaly] Pas assez de variance pour détecter des anomalies.")
72:         return pd.DataFrame()
73: 
74:     # Calcule le Z-score pour chaque snapshot
75:     ts["z_score"] = (ts["total_aircraft"] - mean) / std
76: 
77:     # Filtre les snapshots au-delà du seuil
78:     anomalies = ts[ts["z_score"].abs() > z_threshold].copy()
79: 
80:     # Ajoute une étiquette lisible
81:     anomalies["anomaly_type"] = anomalies["z_score"].apply(
82:         lambda z: "📈 PIC ANORMAL" if z > 0 else "📉 CHUTE ANORMALE"
83:     )
84: 
85:     return anomalies
86: 
87: 
88: def print_timeseries_report(ts: pd.DataFrame) -> None:
89:     """
90:     Affiche un rapport de la série temporelle dans le terminal.
91:     """
92: 
93:     anomalies = detect_anomalies(ts)
94: 
95:     print("\n" + "═" * 55)
96:     print("  RAPPORT SÉRIE TEMPORELLE")
97:     print("═" * 55)
98:     print(f"\n  Snapshots analysés : {len(ts)}")
99:     print(f"  Période            : {ts['timestamp'].min()} → {ts['timestamp'].max()}")
100:     print(f"\n── Statistiques globales ──")
101:     print(f"  Avions moyen       : {ts['total_aircraft'].mean():.0f}")
102:     print(f"  Avions min         : {ts['total_aircraft'].min()} ({ts.loc[ts['total_aircraft'].idxmin(), 'timestamp']})")
103:     print(f"  Avions max         : {ts['total_aircraft'].max()} ({ts.loc[ts['total_aircraft'].idxmax(), 'timestamp']})")
104:     print(f"  Écart-type         : {ts['total_aircraft'].std():.1f}")
105: 
106:     print(f"\n── Évolution snapshot par snapshot ──")
107:     for _, row in ts.iterrows():
108:         # Flèche selon variation
109:         if pd.isna(row["delta_total"]):
110:             arrow = "  "
111:         elif row["delta_total"] > 0:
112:             arrow = "↑ "
113:         elif row["delta_total"] < 0:
114:             arrow = "↓ "
115:         else:
116:             arrow = "→ "
117: 
118:         delta_str = f"({row['delta_total']:+.0f})" if not pd.isna(row["delta_total"]) else "     "
119: 
120:         print(
121:             f"  {str(row['timestamp'])[11:16]}  "
122:             f"{arrow}{row['total_aircraft']:4.0f} avions {delta_str:8}  "
123:             f"alt: {row['altitude_mean']:.0f}m  "
124:             f"pays: {row['unique_countries']:.0f}"
125:         )
126: 
127:     if len(anomalies) > 0:
128:         print(f"\n── ⚠  Anomalies détectées ──")
129:         for _, row in anomalies.iterrows():
130:             print(
131:                 f"  {row['anomaly_type']}  "
132:                 f"{str(row['timestamp'])[11:16]}  "
133:                 f"{row['total_aircraft']:.0f} avions  "
134:                 f"Z={row['z_score']:.2f}"
135:             )
136:     else:
137:         print(f"\n  ✅ Aucune anomalie détectée sur cette période.")

(End of file - total 137 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/dashboard.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/dashboard.py</path>
<type>file</type>
<content>
1: import pandas as pd
2: import folium
3: from folium.plugins import MarkerCluster, HeatMap
4: import plotly.graph_objects as go
5: from plotly.subplots import make_subplots
6: from pathlib import Path
7: from datetime import datetime
8: 
9: from utils.regions import REGIONS, get_all_regions
10: 
11: DASHBOARD_DIR = Path("data/maps")
12: 
13: 
14: def build_dashboard(
15:     df_flights: pd.DataFrame,
16:     ts: pd.DataFrame,
17:     correlations: pd.DataFrame = None,
18:     anomalies: pd.DataFrame = None,
19:     regional_data: dict = None,       # ← nouveau
20:     output_name: str = "dashboard",
21: ) -> Path:
22:     """
23:     Génère le dashboard HTML unifié.
24: 
25:     Args:
26:         df_flights    : snapshot fusionné (tous avions)
27:         ts            : série temporelle
28:         correlations  : corrélations GDELT
29:         anomalies     : anomalies détectées
30:         regional_data : dict {code: DataFrame} par région
31:         output_name   : nom du fichier HTML
32:     """
33: 
34:     DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
35: 
36:     map_html     = _build_world_map(df_flights, regional_data)
37:     chart_html   = _build_chart_fragment(ts, anomalies)
38:     table_html   = _build_correlation_table(correlations)
39:     metrics_html = _build_metrics_banner(df_flights, ts, regional_data)
40:     region_html  = _build_region_panel(regional_data)
41:     chat_html    = _build_chat_block()
42: 
43:     now = datetime.now().strftime("%Y-%m-%d %H:%M")
44: 
45:     full_html = f"""<!DOCTYPE html>
46: <html lang="fr">
47: <head>
48:     <meta charset="UTF-8">
49:     <title>GeoPol — Dashboard Mondial</title>
50:     <style>
51:         * {{ margin:0; padding:0; box-sizing:border-box; }}
52:         body {{
53:             font-family: 'Segoe UI', sans-serif;
54:             background: #0d1117;
55:             color: #c9d1d9;
56:         }}
57:         .header {{
58:             background: linear-gradient(135deg, #1a1f2e, #16213e);
59:             border-bottom: 1px solid #30363d;
60:             padding: 20px 30px;
61:             display: flex;
62:             justify-content: space-between;
63:             align-items: center;
64:         }}
65:         .header h1 {{ font-size:22px; color:#58a6ff; letter-spacing:1px; }}
66:         .api-status {{
67:             display:flex; align-items:center; gap:8px; font-size:12px; color:#8b949e;
68:         }}
69:         .api-dot {{
70:             width:8px; height:8px; border-radius:50%;
71:             background:#e74c3c; transition:background 0.3s;
72:         }}
73:         .api-dot.online {{ background:#2ecc71; }}
74: 
75:         /* ── Métriques ── */
76:         .metrics-bar {{
77:             display:flex; gap:12px; padding:15px 30px;
78:             background:#161b22; border-bottom:1px solid #30363d;
79:             flex-wrap:wrap; align-items:center;
80:         }}
81:         .metric-card {{
82:             background:#1c2128; border:1px solid #30363d;
83:             border-radius:8px; padding:10px 18px;
84:             min-width:120px; text-align:center;
85:         }}
86:         .metric-card .value {{
87:             font-size:22px; font-weight:bold; color:#58a6ff;
88:         }}
89:         .metric-card .label {{
90:             font-size:10px; color:#8b949e; margin-top:3px;
91:             text-transform:uppercase; letter-spacing:0.5px;
92:         }}
93:         .metric-card.alert .value {{ color:#e74c3c; }}
94:         .metric-card.warn  .value {{ color:#e67e22; }}
95:         .metric-card.ok    .value {{ color:#2ecc71; }}
96: 
97:         /* ── Layout ── */
98:         .main-grid {{
99:             display:grid;
100:             grid-template-columns: 2fr 1fr;
101:             height: 520px;
102:         }}
103:         .panel {{ border:1px solid #30363d; overflow:hidden; }}
104:         .panel-title {{
105:             background:#161b22; padding:10px 20px;
106:             font-size:12px; color:#8b949e;
107:             border-bottom:1px solid #30363d;
108:             text-transform:uppercase; letter-spacing:1px;
109:             display:flex; justify-content:space-between;
110:             align-items:center;
111:         }}
112:         .panel-content {{ height:calc(100% - 38px); overflow:hidden; }}
113:         .panel-content > div,
114:         .panel-content iframe {{ width:100%; height:100%; border:none; }}
115: 
116:         /* ── Panneau régions ── */
117:         .region-panel {{
118:             overflow-y:auto;
119:             padding:10px;
120:             height:calc(100% - 38px);
121:         }}
122:         .region-row {{
123:             display:flex; align-items:center; gap:10px;
124:             padding:8px 10px; border-radius:6px;
125:             margin-bottom:4px; cursor:pointer;
126:             transition:background 0.2s;
127:             border:1px solid transparent;
128:         }}
129:         .region-row:hover {{ background:#1c2128; border-color:#30363d; }}
130:         .region-dot {{
131:             width:10px; height:10px; border-radius:50%; flex-shrink:0;
132:         }}
133:         .region-name {{ font-size:12px; flex:1; }}
134:         .region-count {{
135:             font-size:14px; font-weight:bold;
136:             color:#58a6ff; min-width:45px; text-align:right;
137:         }}
138:         .region-bar-wrap {{
139:             width:60px; background:#21262d;
140:             border-radius:3px; height:6px;
141:         }}
142:         .region-bar {{
143:             height:6px; border-radius:3px;
144:             background:#58a6ff; transition:width 0.3s;
145:         }}
146: 
147:         /* ── Sections basses ── */
148:         .bottom-grid {{
149:             display:grid;
150:             grid-template-columns: 1fr 1fr;
151:         }}
152:         .section {{
153:             padding:20px 30px;
154:             border-top:1px solid #30363d;
155:             border-right:1px solid #30363d;
156:         }}
157:         .section-title {{
158:             font-size:13px; color:#58a6ff;
159:             text-transform:uppercase; letter-spacing:1px;
160:             margin-bottom:15px;
161:         }}
162:         table {{ width:100%; border-collapse:collapse; font-size:12px; }}
163:         th {{
164:             background:#161b22; color:#8b949e; padding:8px 12px;
165:             text-align:left; border-bottom:1px solid #30363d;
166:             font-weight:normal; text-transform:uppercase; font-size:10px;
167:         }}
168:         td {{ padding:8px 12px; border-bottom:1px solid #21262d; }}
169:         tr:hover td {{ background:#161b22; }}
170: 
171:         /* ── Chat ── */
172:         .chat-section {{
173:             padding:20px 30px 30px;
174:             border-top:2px solid #58a6ff22;
175:         }}
176:         .chat-container {{ max-width:100%; }}
177:         .chat-messages {{
178:             background:#161b22; border:1px solid #30363d;
179:             border-radius:10px; padding:20px;
180:             min-height:150px; max-height:320px;
181:             overflow-y:auto; margin-bottom:15px;
182:             font-size:13px; line-height:1.6;
183:         }}
184:         .msg-user {{
185:             background:#1f3a5f; border-left:3px solid #58a6ff;
186:             padding:10px 15px; border-radius:6px;
187:             margin-bottom:12px; color:#90caf9;
188:         }}
189:         .msg-agent {{
190:             background:#1a2332; border-left:3px solid #2ecc71;
191:             padding:10px 15px; border-radius:6px;
192:             margin-bottom:12px; color:#c9d1d9; white-space:pre-wrap;
193:         }}
194:         .msg-agent .agent-label {{
195:             font-size:10px; color:#2ecc71;
196:             text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;
197:         }}
198:         .cursor {{
199:             display:inline-block; width:8px; height:14px;
200:             background:#2ecc71; animation:blink 0.8s infinite;
201:             vertical-align:middle; margin-left:2px;
202:         }}
203:         @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}
204:         .quick-questions {{
205:             display:flex; flex-wrap:wrap; gap:8px; margin-bottom:15px;
206:         }}
207:         .quick-btn {{
208:             background:#1c2128; border:1px solid #30363d;
209:             color:#8b949e; padding:5px 12px; border-radius:20px;
210:             font-size:11px; cursor:pointer; transition:all 0.2s;
211:         }}
212:         .quick-btn:hover {{ border-color:#58a6ff; color:#58a6ff; }}
213:         .chat-input-row {{ display:flex; gap:10px; }}
214:         .chat-input {{
215:             flex:1; background:#161b22; border:1px solid #30363d;
216:             border-radius:8px; padding:11px 16px; color:#c9d1d9;
217:             font-size:13px; outline:none; transition:border-color 0.2s;
218:         }}
219:         .chat-input:focus {{ border-color:#58a6ff; }}
220:         .chat-input::placeholder {{ color:#484f58; }}
221:         .send-btn {{
222:             background:#238636; border:none; border-radius:8px;
223:             color:white; padding:11px 22px; font-size:13px;
224:             cursor:pointer; transition:background 0.2s;
225:         }}
226:         .send-btn:hover {{ background:#2ea043; }}
227:         .send-btn:disabled {{
228:             background:#21262d; color:#484f58; cursor:not-allowed;
229:         }}
230:     </style>
231: </head>
232: <body>
233: 
234: <div class="header">
235:     <h1>🌍 GeoPol Traffic Intelligence — Vue Mondiale</h1>
236:     <div style="display:flex;align-items:center;gap:20px;">
237:         <div class="api-status">
238:             <div class="api-dot" id="apiDot"></div>
239:             <span id="apiLabel">API...</span>
240:         </div>
241:         <span style="font-size:12px;color:#8b949e;">
242:             Mise à jour : {now} UTC
243:         </span>
244:     </div>
245: </div>
246: 
247: {metrics_html}
248: 
249: <div class="main-grid">
250:     <div class="panel">
251:         <div class="panel-title">
252:             <span>🗺 Trafic mondial en temps réel</span>
253:             <span style="font-size:11px;">
254:                 🔵 En vol &nbsp; 🟠 Au sol &nbsp; 🔴 Zone de tension
255:             </span>
256:         </div>
257:         <div class="panel-content">{map_html}</div>
258:     </div>
259:     <div class="panel">
260:         <div class="panel-title">
261:             <span>📡 Régions</span>
262:         </div>
263:         <div class="region-panel">{region_html}</div>
264:     </div>
265: </div>
266: 
267: <div class="bottom-grid">
268:     <div class="section">
269:         <div class="section-title">📈 Série temporelle</div>
270:         {chart_html}
271:     </div>
272:     <div class="section">
273:         {table_html}
274:     </div>
275: </div>
276: 
277: {chat_html}
278: 
279: <script>
280: // ── Vérifie l'API ──
281: async function checkApi() {{
282:     try {{
283:         const r = await fetch("http://localhost:5000/api/status");
284:         if (r.ok) {{
285:             document.getElementById("apiDot").classList.add("online");
286:             document.getElementById("apiLabel").textContent = "API en ligne";
287:         }}
288:     }} catch(e) {{
289:         document.getElementById("apiLabel").textContent = "API hors ligne";
290:     }}
291: }}
292: checkApi();
293: 
294: // ── Chat ──
295: const messagesDiv = document.getElementById("chatMessages");
296: const input       = document.getElementById("chatInput");
297: const sendBtn     = document.getElementById("sendBtn");
298: 
299: function scrollBottom() {{ messagesDiv.scrollTop = messagesDiv.scrollHeight; }}
300: 
301: function addUserMessage(text) {{
302:     const div = document.createElement("div");
303:     div.className = "msg-user";
304:     div.textContent = "❯ " + text;
305:     messagesDiv.appendChild(div);
306:     scrollBottom();
307: }}
308: 
309: function createAgentMessage() {{
310:     const div = document.createElement("div");
311:     div.className = "msg-agent";
312:     const label = document.createElement("div");
313:     label.className = "agent-label";
314:     label.textContent = "Agent OSINT";
315:     const content = document.createElement("span");
316:     content.id = "streamContent";
317:     const cursor = document.createElement("span");
318:     cursor.className = "cursor";
319:     cursor.id = "streamCursor";
320:     div.appendChild(label);
321:     div.appendChild(content);
322:     div.appendChild(cursor);
323:     messagesDiv.appendChild(div);
324:     scrollBottom();
325:     return content;
326: }}
327: 
328: async function sendQuestion(question) {{
329:     if (!question.trim()) return;
330:     sendBtn.disabled = true;
331:     input.value = "";
332:     addUserMessage(question);
333:     const contentEl = createAgentMessage();
334:     try {{
335:         const response = await fetch("http://localhost:5000/api/ask", {{
336:             method:"POST",
337:             headers:{{"Content-Type":"application/json"}},
338:             body: JSON.stringify({{question}}),
339:         }});
340:         const reader  = response.body.getReader();
341:         const decoder = new TextDecoder();
342:         let buffer = "";
343:         while (true) {{
344:             const {{done, value}} = await reader.read();
345:             if (done) break;
346:             buffer += decoder.decode(value, {{stream:true}});
347:             const lines = buffer.split("\\n");
348:             buffer = lines.pop();
349:             for (const line of lines) {{
350:                 if (!line.startsWith("data: ")) continue;
351:                 const token = line.slice(6);
352:                 if (token === "[DONE]") break;
353:                 contentEl.textContent += token;
354:                 scrollBottom();
355:             }}
356:         }}
357:     }} catch(e) {{
358:         contentEl.textContent = "Erreur : " + e.message;
359:     }}
360:     const cursor = document.getElementById("streamCursor");
361:     if (cursor) cursor.remove();
362:     sendBtn.disabled = false;
363:     input.focus();
364: }}
365: 
366: sendBtn.addEventListener("click", () => sendQuestion(input.value));
367: input.addEventListener("keydown", e => {{
368:     if (e.key === "Enter" && !e.shiftKey) {{
369:         e.preventDefault();
370:         sendQuestion(input.value);
371:     }}
372: }});
373: document.querySelectorAll(".quick-btn").forEach(btn => {{
374:     btn.addEventListener("click", () => sendQuestion(btn.dataset.question));
375: }});
376: </script>
377: </body>
378: </html>"""
379: 
380:     filepath = DASHBOARD_DIR / f"{output_name}.html"
381:     filepath.write_text(full_html, encoding="utf-8")
382:     print(f"[Dashboard] Généré → {filepath}")
383:     return filepath
384: 
385: 
386: # ════════════════════════════════════════════════
387: # FONCTIONS INTERNES
388: # ════════════════════════════════════════════════
389: 
390: def _build_map_fragment(df: pd.DataFrame) -> str:
391:     """Génère la carte Folium et retourne son HTML interne."""
392: 
393:     center_lat = df["latitude"].mean()
394:     center_lon = df["longitude"].mean()
395:     m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
396: 
397:     in_flight = df[df["on_ground"] == False]
398:     on_ground = df[df["on_ground"] == True]
399: 
400:     for _, row in in_flight.iterrows():
401:         folium.CircleMarker(
402:             location=[row["latitude"], row["longitude"]],
403:             radius=3,
404:             color="#3498db",
405:             fill=True,
406:             fill_opacity=0.7,
407:             tooltip=f"✈ {row.get('callsign','?')} | {row['origin_country']} | {row['altitude']:.0f}m",
408:         ).add_to(m)
409: 
410:     for _, row in on_ground.iterrows():
411:         folium.CircleMarker(
412:             location=[row["latitude"], row["longitude"]],
413:             radius=4,
414:             color="#e67e22",
415:             fill=True,
416:             fill_opacity=0.8,
417:             tooltip=f"🅿 {row.get('callsign','?')} | {row['origin_country']}",
418:         ).add_to(m)
419: 
420:     # Retourne uniquement le contenu HTML interne de la carte
421:     return m._repr_html_()
422: 
423: 
424: def _build_chart_fragment(ts: pd.DataFrame, anomalies: pd.DataFrame) -> str:
425:     """Génère le graphe Plotly et retourne son HTML."""
426: 
427:     fig = make_subplots(
428:         rows=2, cols=1,
429:         shared_xaxes=True,
430:         subplot_titles=("Nombre d'avions", "Altitude moyenne (m)"),
431:         vertical_spacing=0.12,
432:     )
433: 
434:     fig.add_trace(
435:         go.Scatter(
436:             x=ts["timestamp"], y=ts["total_aircraft"],
437:             mode="lines+markers",
438:             name="Total avions",
439:             line=dict(color="#58a6ff", width=2),
440:             hovertemplate="<b>%{x}</b><br>%{y} avions<extra></extra>",
441:         ),
442:         row=1, col=1
443:     )
444: 
445:     if anomalies is not None and len(anomalies) > 0:
446:         fig.add_trace(
447:             go.Scatter(
448:                 x=anomalies["timestamp"], y=anomalies["total_aircraft"],
449:                 mode="markers", name="⚠ Anomalie",
450:                 marker=dict(color="#e74c3c", size=12, symbol="x"),
451:             ),
452:             row=1, col=1
453:         )
454: 
455:     fig.add_trace(
456:         go.Scatter(
457:             x=ts["timestamp"], y=ts["altitude_mean"],
458:             mode="lines", name="Altitude",
459:             line=dict(color="#2ecc71", width=2),
460:         ),
461:         row=2, col=1
462:     )
463: 
464:     fig.update_layout(
465:         template="plotly_dark",
466:         paper_bgcolor="#1c2128",
467:         plot_bgcolor="#1c2128",
468:         margin=dict(l=50, r=20, t=40, b=30),
469:         height=None,
470:         autosize=True,
471:         legend=dict(orientation="h", y=1.08),
472:     )
473: 
474:     return fig.to_html(
475:         full_html=False,
476:         include_plotlyjs="cdn",
477:         config={"responsive": True},
478:     )
479: 
480: 
481: def _build_metrics_banner(df: pd.DataFrame, ts: pd.DataFrame) -> str:
482:     """Génère la barre de métriques en haut du dashboard."""
483: 
484:     total     = len(df)
485:     in_flight = int((~df["on_ground"]).sum())
486:     countries = int(df["origin_country"].nunique())
487:     alt_mean  = df["altitude"].mean()
488:     snapshots = len(ts)
489: 
490:     cards = [
491:         (str(total),        "Avions détectés"),
492:         (str(in_flight),    "En vol"),
493:         (str(total - in_flight), "Au sol"),
494:         (str(countries),    "Pays"),
495:         (f"{alt_mean:.0f}m", "Altitude moy."),
496:         (str(snapshots),    "Snapshots"),
497:     ]
498: 
499:     cards_html = ""
500:     for value, label in cards:
501:         cards_html += f"""
502:         <div class="metric-card">
503:             <div class="value">{value}</div>
504:             <div class="label">{label}</div>
505:         </div>"""
506: 
507:     return f'<div class="metrics-bar">{cards_html}</div>'
508: 
509: 
510: def _build_correlation_table(correlations: pd.DataFrame) -> str:
511:     """Génère le tableau HTML des corrélations."""
512: 
513:     if correlations is None or correlations.empty:
514:         return """
515:         <div class="correlations-section">
516:             <div class="section-title">⚡ Corrélations géopolitiques</div>
517:             <p style="color:#8b949e; font-size:13px;">
518:                 Aucune corrélation disponible.
519:                 Lance <code>correlation_main.py</code> pour en générer.
520:             </p>
521:         </div>"""
522: 
523:     rows_html = ""
524:     for _, row in correlations.iterrows():
525:         delta = f"{row['traffic_delta_pct']:+.1f}%" if pd.notna(row.get('traffic_delta_pct')) else "N/A"
526:         rows_html += f"""
527:         <tr>
528:             <td>{row.get('signal_label','—')}</td>
529:             <td>{row.get('event_name','—')}</td>
530:             <td>{str(row.get('event_time','—'))[:16]}</td>
531:             <td>{row.get('event_goldstein','—')}</td>
532:             <td>{delta}</td>
533:             <td>{row.get('correlation_signal','—')}</td>
534:         </tr>"""
535: 
536:     return f"""
537:     <div class="correlations-section">
538:         <div class="section-title">⚡ Corrélations géopolitiques</div>
539:         <table>
540:             <thead>
541:                 <tr>
542:                     <th>Signal</th>
543:                     <th>Événement</th>
544:                     <th>Date</th>
545:                     <th>Goldstein</th>
546:                     <th>Δ Trafic</th>
547:                     <th>Score</th>
548:                 </tr>
549:             </thead>
550:             <tbody>{rows_html}</tbody>
551:         </table>
552:     </div>"""
553:     
554: def _build_chat_block() -> str:
555:     """Génère le bloc chat HTML + questions rapides."""
556: 
557:     quick = [
558:         ("Résume la situation",          "Résume la situation du trafic aérien actuel."),
559:         ("Anomalies ?",                   "Y a-t-il des anomalies visibles dans les données ?"),
560:         ("Top pays",                      "Quels pays dominent le trafic et pourquoi ?"),
561:         ("Analyse temporelle",            "Analyse les variations de la série temporelle."),
562:         ("Corrélation géopolitique ?",    "Y a-t-il une corrélation entre les événements géopolitiques et le trafic ?"),
563:         ("Niveau de tension ?",           "Quel est le niveau de tension géopolitique actuel selon ces données ?"),
564:     ]
565: 
566:     quick_btns = "".join([
567:         f'<button class="quick-btn" data-question="{q}">{label}</button>'
568:         for label, q in quick
569:     ])
570: 
571:     return f"""
572:     <div class="chat-section">
573:         <div class="chat-container">
574:             <div class="section-title">💬 Agent OSINT — Analyse en langage naturel</div>
575: 
576:             <div class="quick-questions">
577:                 {quick_btns}
578:             </div>
579: 
580:             <div class="chat-messages" id="chatMessages">
581:                 <div class="msg-agent">
582:                     <div class="agent-label">Agent OSINT</div>
583:                     Bonjour. Je suis connecté aux données de trafic aérien en temps réel.
584:                     Pose-moi une question ou clique sur un raccourci ci-dessus.
585:                 </div>
586:             </div>
587: 
588:             <div class="chat-input-row">
589:                 <input
590:                     type="text"
591:                     class="chat-input"
592:                     id="chatInput"
593:                     placeholder="Ex: Y a-t-il une chute de trafic inhabituelle ?"
594:                     autocomplete="off"
595:                 />
596:                 <button class="send-btn" id="sendBtn">Envoyer ↵</button>
597:             </div>
598:         </div>
599:     </div>"""
600:     
601: def _build_world_map(
602:     df: pd.DataFrame,
603:     regional_data: dict = None,
604: ) -> str:
605:     """
606:     Carte mondiale Folium avec :
607:     - Points avions en vol / au sol
608:     - Rectangles de régions colorés par densité
609:     - Heatmap de densité de trafic
610:     """
611: 
612:     m = folium.Map(
613:         location=[30.0, 15.0],
614:         zoom_start=2,
615:         tiles="CartoDB dark_matter",   # fond sombre style OSINT
616:     )
617: 
618:     # ── Calque : rectangles de régions ──
619:     if regional_data:
620:         max_count = max(
621:             (len(df) for df in regional_data.values() if not df.empty),
622:             default=1
623:         )
624:         for code, region_df in regional_data.items():
625:             region = next((r for r in REGIONS.values() if r.code == code), None)
626:             if not region:
627:                 continue
628: 
629:             count   = len(region_df)
630:             # Opacité proportionnelle à la densité de trafic
631:             opacity = 0.05 + 0.25 * (count / max(max_count, 1))
632: 
633:             folium.Rectangle(
634:                 bounds=[
635:                     [region.lat_min, region.lon_min],
636:                     [region.lat_max, region.lon_max],
637:                 ],
638:                 color=region.color,
639:                 fill=True,
640:                 fill_opacity=opacity,
641:                 weight=1,
642:                 tooltip=f"{region.name} — {count} avions",
643:             ).add_to(m)
644: 
645:     if df.empty:
646:         return m._repr_html_()
647: 
648:     # ── Calque : heatmap densité ──
649:     heat_data = [
650:         [row["latitude"], row["longitude"], 1]
651:         for _, row in df.iterrows()
652:         if pd.notna(row["latitude"]) and pd.notna(row["longitude"])
653:     ]
654:     if heat_data:
655:         HeatMap(
656:             heat_data,
657:             radius=4,
658:             blur=6,
659:             min_opacity=0.2,
660:             gradient={"0.4":"blue","0.65":"lime","1":"red"},
661:         ).add_to(m)
662: 
663:     # ── Calque : avions (clustérisés pour les performances) ──
664:     cluster = MarkerCluster(
665:         options={"maxClusterRadius": 30, "disableClusteringAtZoom": 6}
666:     )
667: 
668:     in_flight = df[df["on_ground"] == False]
669:     on_ground = df[df["on_ground"] == True]
670: 
671:     for _, row in in_flight.iterrows():
672:         folium.CircleMarker(
673:             location=[row["latitude"], row["longitude"]],
674:             radius=2,
675:             color="#3498db",
676:             fill=True,
677:             fill_opacity=0.7,
678:             tooltip=(
679:                 f"✈ {row.get('callsign','?')} | "
680:                 f"{row['origin_country']} | "
681:                 f"{row['altitude']:.0f}m | "
682:                 f"{row.get('region','?')}"
683:             ),
684:         ).add_to(cluster)
685: 
686:     for _, row in on_ground.iterrows():
687:         folium.CircleMarker(
688:             location=[row["latitude"], row["longitude"]],
689:             radius=3,
690:             color="#e67e22",
691:             fill=True,
692:             fill_opacity=0.8,
693:             tooltip=f"🅿 {row.get('callsign','?')} | {row['origin_country']}",
694:         ).add_to(cluster)
695: 
696:     cluster.add_to(m)
697:     return m._repr_html_()
698: 
699: def _build_region_panel(regional_data: dict = None) -> str:
700:     """Génère le panneau latéral avec la liste des régions."""
701: 
702:     if not regional_data:
703:         return "<p style='color:#8b949e;font-size:12px;padding:10px;'>Lance make global pour charger les régions.</p>"
704: 
705:     # Trie par nombre d'avions décroissant
706:     sorted_regions = sorted(
707:         regional_data.items(),
708:         key=lambda x: len(x[1]),
709:         reverse=True,
710:     )
711:     max_count = max((len(df) for _, df in sorted_regions), default=1)
712: 
713:     rows = ""
714:     for code, df in sorted_regions:
715:         region = next((r for r in REGIONS.values() if r.code == code), None)
716:         if not region:
717:             continue
718: 
719:         count    = len(df)
720:         bar_pct  = int((count / max(max_count, 1)) * 100)
721:         in_fl    = int((~df["on_ground"]).sum()) if not df.empty else 0
722: 
723:         rows += f"""
724:         <div class="region-row">
725:             <div class="region-dot" style="background:{region.color}"></div>
726:             <div class="region-name">{region.name}</div>
727:             <div>
728:                 <div class="region-bar-wrap">
729:                     <div class="region-bar"
730:                          style="width:{bar_pct}%;background:{region.color}">
731:                     </div>
732:                 </div>
733:             </div>
734:             <div class="region-count">{count}</div>
735:         </div>"""
736: 
737:     return rows
738: 
739: 
740: def _build_metrics_banner(
741:     df: pd.DataFrame,
742:     ts: pd.DataFrame,
743:     regional_data: dict = None,
744: ) -> str:
745:     """Génère la barre de métriques globales."""
746: 
747:     total     = len(df) if df is not None else 0
748:     in_flight = int((~df["on_ground"]).sum()) if not df.empty else 0
749:     on_ground = total - in_flight
750:     countries = int(df["origin_country"].nunique()) if not df.empty else 0
751:     regions   = len(regional_data) if regional_data else 0
752:     snapshots = len(ts) if ts is not None else 0
753: 
754:     # Détecte les régions avec peu de trafic (signal potentiel)
755:     alert_regions = []
756:     if regional_data:
757:         counts = {c: len(d) for c, d in regional_data.items() if not d.empty}
758:         if counts:
759:             avg = sum(counts.values()) / len(counts)
760:             alert_regions = [c for c, n in counts.items() if n < avg * 0.3]
761: 
762:     alert_class = "alert" if alert_regions else "ok"
763:     alert_label = f"⚠ {','.join(alert_regions)}" if alert_regions else "Normal"
764: 
765:     cards = [
766:         (f"{total:,}",    "Avions mondial",   ""),
767:         (str(in_flight),  "En vol",           "ok"),
768:         (str(on_ground),  "Au sol",           ""),
769:         (str(countries),  "Pays",             ""),
770:         (str(regions),    "Régions actives",  ""),
771:         (str(snapshots),  "Snapshots",        ""),
772:         (alert_label,     "Signal trafic",    alert_class),
773:     ]
774: 
775:     cards_html = ""
776:     for value, label, cls in cards:
777:         cards_html += f"""
778:         <div class="metric-card {cls}">
779:             <div class="value">{value}</div>
780:             <div class="label">{label}</div>
781:         </div>"""
782: 
783:     return f'<div class="metrics-bar">{cards_html}</div>'

(End of file - total 783 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/map_viewer.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/map_viewer.py</path>
<type>file</type>
<content>
1: import folium
2: import pandas as pd
3: from pathlib import Path
4: 
5: # Dossier où on sauvegarde les cartes générées
6: MAPS_DIR = Path("data/maps")
7: 
8: 
9: def build_flight_map(df: pd.DataFrame, output_name: str = "flights_map") -> Path:
10:     """
11:     Génère une carte HTML interactive avec les avions en vol.
12: 
13:     Args:
14:         df          : DataFrame chargé depuis le CSV
15:         output_name : nom du fichier HTML de sortie
16: 
17:     Returns:
18:         Chemin vers le fichier HTML généré
19:     """
20: 
21:     MAPS_DIR.mkdir(parents=True, exist_ok=True)
22: 
23:     # ── Centre de la carte = moyenne des positions ──
24:     center_lat = df["latitude"].mean()
25:     center_lon = df["longitude"].mean()
26: 
27:     # Crée la carte centrée sur la zone
28:     # zoom_start : 1=monde, 5=pays, 10=ville
29:     m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
30: 
31:     # ── Sépare avions en vol / au sol ──
32:     in_flight = df[df["on_ground"] == False]
33:     on_ground = df[df["on_ground"] == True]
34: 
35:     # ── Ajoute les avions EN VOL (bleu) ──
36:     for _, row in in_flight.iterrows():
37:         folium.CircleMarker(
38:             location=[row["latitude"], row["longitude"]],
39:             radius=4,
40:             color="#3498db",
41:             fill=True,
42:             fill_opacity=0.7,
43:             tooltip=_build_tooltip(row),
44:         ).add_to(m)
45: 
46:     # ── Ajoute les avions AU SOL (orange) ──
47:     for _, row in on_ground.iterrows():
48:         folium.CircleMarker(
49:             location=[row["latitude"], row["longitude"]],
50:             radius=5,
51:             color="#e67e22",
52:             fill=True,
53:             fill_opacity=0.8,
54:             tooltip=_build_tooltip(row),
55:         ).add_to(m)
56: 
57:     # ── Légende simple en haut à droite ──
58:     legend_html = """
59:     <div style="position:fixed; top:10px; right:10px; z-index:1000;
60:                 background:white; padding:10px; border-radius:8px;
61:                 border:1px solid #ccc; font-size:13px;">
62:         <b>Trafic aérien</b><br>
63:         <span style="color:#3498db;">●</span> En vol ({in_flight})<br>
64:         <span style="color:#e67e22;">●</span> Au sol ({on_ground})<br>
65:         <span style="font-size:11px; color:#888;">{timestamp}</span>
66:     </div>
67:     """.format(
68:         in_flight=len(in_flight),
69:         on_ground=len(on_ground),
70:         timestamp=df["timestamp"].iloc[0].strftime("%Y-%m-%d %H:%M UTC")
71:     )
72:     m.get_root().html.add_child(folium.Element(legend_html))
73: 
74:     # ── Sauvegarde la carte ──
75:     filepath = MAPS_DIR / f"{output_name}.html"
76:     m.save(str(filepath))
77: 
78:     print(f"[MapViewer] Carte générée → {filepath}")
79:     print(f"[MapViewer] Ouvre dans ton navigateur : file://{filepath.resolve()}")
80:     return filepath
81: 
82: 
83: def _build_tooltip(row: pd.Series) -> str:
84:     """
85:     Construit le texte affiché au survol d'un avion.
86:     """
87:     callsign  = row["callsign"] if pd.notna(row["callsign"]) else "Inconnu"
88:     altitude  = f"{row['altitude']:.0f} m" if pd.notna(row["altitude"]) else "N/A"
89:     velocity  = f"{row['velocity']:.0f} m/s" if pd.notna(row["velocity"]) else "N/A"
90:     heading   = f"{row['heading']:.0f}°" if pd.notna(row["heading"]) else "N/A"
91: 
92:     return (
93:         f"✈ {callsign} ({row['icao24']})\n"
94:         f"Pays : {row['origin_country']}\n"
95:         f"Altitude : {altitude}\n"
96:         f"Vitesse  : {velocity}\n"
97:         f"Cap      : {heading}"
98:     )

(End of file - total 98 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/timeseries_plotter.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/visualization/timeseries_plotter.py</path>
<type>file</type>
<content>
1: import plotly.graph_objects as go
2: from plotly.subplots import make_subplots
3: import pandas as pd
4: from pathlib import Path
5: 
6: MAPS_DIR = Path("data/maps")
7: 
8: 
9: def plot_timeseries(ts: pd.DataFrame, anomalies: pd.DataFrame = None) -> Path:
10:     """
11:     Génère un graphe HTML interactif de la série temporelle.
12: 
13:     Contient 3 sous-graphes :
14:       1. Nombre d'avions total + anomalies marquées
15:       2. Altitude moyenne
16:       3. Nombre de pays représentés
17: 
18:     Args:
19:         ts        : série temporelle (output de build_timeseries)
20:         anomalies : DataFrame des anomalies détectées (peut être None)
21: 
22:     Returns:
23:         Chemin vers le fichier HTML généré
24:     """
25: 
26:     MAPS_DIR.mkdir(parents=True, exist_ok=True)
27: 
28:     # ── Crée une figure avec 3 graphes empilés verticalement ──
29:     # shared_xaxes = ils partagent tous le même axe X (temps)
30:     fig = make_subplots(
31:         rows=3, cols=1,
32:         shared_xaxes=True,
33:         subplot_titles=(
34:             "Nombre d'avions total",
35:             "Altitude moyenne (m)",
36:             "Pays représentés"
37:         ),
38:         vertical_spacing=0.08
39:     )
40: 
41:     # ════════════════════════════════════════
42:     # GRAPHE 1 — Nombre d'avions
43:     # ════════════════════════════════════════
44: 
45:     # Courbe principale
46:     fig.add_trace(
47:         go.Scatter(
48:             x=ts["timestamp"],
49:             y=ts["total_aircraft"],
50:             mode="lines+markers",
51:             name="Total avions",
52:             line=dict(color="#3498db", width=2),
53:             marker=dict(size=6),
54:             # Texte au survol
55:             hovertemplate=(
56:                 "<b>%{x}</b><br>"
57:                 "Total : %{y} avions<br>"
58:                 "<extra></extra>"
59:             ),
60:         ),
61:         row=1, col=1
62:     )
63: 
64:     # Zone colorée sous la courbe (effet visuel)
65:     fig.add_trace(
66:         go.Scatter(
67:             x=ts["timestamp"],
68:             y=ts["total_aircraft"],
69:             fill="tozeroy",
70:             fillcolor="rgba(52, 152, 219, 0.1)",
71:             line=dict(width=0),
72:             showlegend=False,
73:             hoverinfo="skip",
74:         ),
75:         row=1, col=1
76:     )
77: 
78:     # ── Marque les anomalies en rouge ──
79:     if anomalies is not None and len(anomalies) > 0:
80:         fig.add_trace(
81:             go.Scatter(
82:                 x=anomalies["timestamp"],
83:                 y=anomalies["total_aircraft"],
84:                 mode="markers",
85:                 name="⚠ Anomalie",
86:                 marker=dict(
87:                     color="#e74c3c",
88:                     size=14,
89:                     symbol="x",
90:                     line=dict(width=2)
91:                 ),
92:                 hovertemplate=(
93:                     "<b>⚠ ANOMALIE</b><br>"
94:                     "%{x}<br>"
95:                     "Total : %{y} avions<br>"
96:                     "Z-score : %{customdata:.2f}<br>"
97:                     "<extra></extra>"
98:                 ),
99:                 customdata=anomalies["z_score"],
100:             ),
101:             row=1, col=1
102:         )
103: 
104:     # ════════════════════════════════════════
105:     # GRAPHE 2 — Altitude moyenne
106:     # ════════════════════════════════════════
107: 
108:     fig.add_trace(
109:         go.Scatter(
110:             x=ts["timestamp"],
111:             y=ts["altitude_mean"],
112:             mode="lines+markers",
113:             name="Altitude moy.",
114:             line=dict(color="#2ecc71", width=2),
115:             marker=dict(size=5),
116:             hovertemplate=(
117:                 "<b>%{x}</b><br>"
118:                 "Altitude : %{y:.0f} m<br>"
119:                 "<extra></extra>"
120:             ),
121:         ),
122:         row=2, col=1
123:     )
124: 
125:     # ════════════════════════════════════════
126:     # GRAPHE 3 — Nombre de pays
127:     # ════════════════════════════════════════
128: 
129:     fig.add_trace(
130:         go.Bar(
131:             x=ts["timestamp"],
132:             y=ts["unique_countries"],
133:             name="Pays",
134:             marker_color="#9b59b6",
135:             hovertemplate=(
136:                 "<b>%{x}</b><br>"
137:                 "Pays : %{y}<br>"
138:                 "<extra></extra>"
139:             ),
140:         ),
141:         row=3, col=1
142:     )
143: 
144:     # ════════════════════════════════════════
145:     # MISE EN PAGE GLOBALE
146:     # ════════════════════════════════════════
147: 
148:     fig.update_layout(
149:         title=dict(
150:             text="GeoPol Traffic Intelligence — Série Temporelle",
151:             font=dict(size=20)
152:         ),
153:         height=800,
154:         template="plotly_dark",
155:         hovermode="x unified",       # affiche toutes les valeurs au même x
156:         legend=dict(
157:             orientation="h",
158:             yanchor="bottom",
159:             y=1.02,
160:             xanchor="right",
161:             x=1
162:         ),
163:     )
164: 
165:     # Labels axes Y
166:     fig.update_yaxes(title_text="Avions",  row=1, col=1)
167:     fig.update_yaxes(title_text="Mètres",  row=2, col=1)
168:     fig.update_yaxes(title_text="Pays",    row=3, col=1)
169:     fig.update_xaxes(title_text="Heure",   row=3, col=1)
170: 
171:     # ── Sauvegarde ──
172:     filepath = MAPS_DIR / "timeseries.html"
173:     fig.write_html(str(filepath))
174: 
175:     print(f"[Plotter] Graphe généré → {filepath}")
176:     print(f"[Plotter] Ouvre : file://{filepath.resolve()}")
177:     return filepath

(End of file - total 177 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/api/server.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/api/server.py</path>
<type>file</type>
<content>
1: import sys
2: from pathlib import Path
3: 
4: sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
5: 
6: import pandas as pd
7: from pathlib import Path
8: from flask import Flask, request, jsonify, Response, stream_with_context
9: from flask_cors import CORS
10: 
11: from storage.data_store import load_all_flights, load_flights
12: from analysis.timeseries_analyzer import build_timeseries, detect_anomalies
13: from analysis.air_traffic_analyser import compute_basic_metrics, compute_country_breakdown
14: from agent.llm_analyst import ask, _build_context
15: 
16: app = Flask(__name__)
17: 
18: # CORS = autorise le dashboard HTML (fichier local) à appeler l'API
19: # Sans ça le navigateur bloque les requêtes cross-origin
20: CORS(app)
21: 
22: # ── Cache en mémoire ──
23: # On charge les données une fois au démarrage
24: # pour ne pas relire les CSV à chaque requête
25: _cache = {
26:     "df_latest"    : None,
27:     "ts"           : None,
28:     "correlations" : None,
29: }
30: 
31: _PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
32: _DATA_RAW     = _PROJECT_ROOT / "data" / "raw"
33: 
34: if not _DATA_RAW.exists():
35:     _DATA_RAW = Path("data/raw")
36: 
37: 
38: def _load_data():
39:     csv_files = sorted(_DATA_RAW.glob("flights_*.csv"))
40:     if not csv_files:
41:         return False
42: 
43:     _cache["df_latest"] = load_flights(csv_files[-1])
44:     df_all              = load_all_flights(_DATA_RAW)
45:     _cache["ts"]        = build_timeseries(df_all)
46: 
47:     corr_path = _PROJECT_ROOT / "data" / "reports" / "correlations.csv"
48:     if corr_path.exists():
49:         import pandas as pd
50:         _cache["correlations"] = pd.read_csv(corr_path)
51: 
52:     return True
53: 
54: 
55: # ════════════════════════════════════════
56: # ROUTES — Données
57: # ════════════════════════════════════════
58: 
59: @app.route("/api/status", methods=["GET"])
60: def status():
61:     """
62:     Route de santé — vérifie que l'API tourne.
63:     Le dashboard l'appelle au démarrage.
64:     """
65:     loaded = _load_data()
66:     if not loaded:
67:         return jsonify({"status": "no_data", "message": "Aucune donnée disponible"}), 404
68: 
69:     ts  = _cache["ts"]
70:     df  = _cache["df_latest"]
71: 
72:     return jsonify({
73:         "status"          : "ok",
74:         "snapshots"       : len(ts),
75:         "latest_aircraft" : len(df),
76:         "in_flight"       : int((~df["on_ground"]).sum()),
77:         "on_ground"       : int(df["on_ground"].sum()),
78:         "countries"       : int(df["origin_country"].nunique()),
79:         "altitude_mean"   : round(float(df["altitude"].mean()), 0),
80:         "velocity_mean"   : round(float(df["velocity"].mean()), 0),
81:         "period_start"    : str(ts["timestamp"].min()),
82:         "period_end"      : str(ts["timestamp"].max()),
83:     })
84: 
85: 
86: @app.route("/api/metrics", methods=["GET"])
87: def metrics():
88:     """Retourne les métriques complètes du dernier snapshot."""
89: 
90:     _load_data()
91:     df = _cache["df_latest"]
92:     if df is None:
93:         return jsonify({"error": "Aucune donnée"}), 404
94: 
95:     m = compute_basic_metrics(df)
96: 
97:     # Convertit les types numpy en types Python natifs pour JSON
98:     return jsonify({k: _serialize(v) for k, v in m.items()})
99: 
100: 
101: @app.route("/api/countries", methods=["GET"])
102: def countries():
103:     """Retourne la répartition par pays."""
104: 
105:     _load_data()
106:     df = _cache["df_latest"]
107:     if df is None:
108:         return jsonify({"error": "Aucune donnée"}), 404
109: 
110:     breakdown = compute_country_breakdown(df)
111: 
112:     return jsonify(breakdown.head(20).to_dict(orient="records"))
113: 
114: 
115: @app.route("/api/timeseries", methods=["GET"])
116: def timeseries():
117:     """Retourne la série temporelle complète."""
118: 
119:     _load_data()
120:     ts = _cache["ts"]
121:     if ts is None:
122:         return jsonify({"error": "Aucune donnée"}), 404
123: 
124:     return jsonify(ts.to_dict(orient="records"))
125: 
126: 
127: @app.route("/api/correlations", methods=["GET"])
128: def correlations():
129:     """Retourne les corrélations géopolitiques."""
130: 
131:     _load_data()
132:     corr = _cache["correlations"]
133:     if corr is None:
134:         return jsonify([])
135: 
136:     return jsonify(corr.head(10).to_dict(orient="records"))
137: 
138: 
139: @app.route("/api/anomalies", methods=["GET"])
140: def anomalies():
141:     """Retourne les anomalies détectées."""
142: 
143:     _load_data()
144:     ts = _cache["ts"]
145:     if ts is None:
146:         return jsonify([])
147: 
148:     anom = detect_anomalies(ts)
149:     if anom.empty:
150:         return jsonify([])
151: 
152:     return jsonify(anom.to_dict(orient="records"))
153: 
154: 
155: # ════════════════════════════════════════
156: # ROUTE — Agent LLM
157: # ════════════════════════════════════════
158: 
159: @app.route("/api/ask", methods=["POST"])
160: def ask_agent():
161:     """
162:     Reçoit une question, la passe à l'agent LLM,
163:     retourne la réponse en streaming (Server-Sent Events).
164: 
165:     SSE = Server-Sent Events : le serveur envoie des tokens
166:     au fur et à mesure, le navigateur les affiche en temps réel.
167:     C'est exactement comme ChatGPT.
168:     """
169: 
170:     body     = request.get_json()
171:     question = body.get("question", "").strip()
172: 
173:     if not question:
174:         return jsonify({"error": "Question vide"}), 400
175: 
176:     _load_data()
177:     df   = _cache["df_latest"]
178:     ts   = _cache["ts"]
179:     corr = _cache["correlations"]
180: 
181:     if df is None:
182:         return jsonify({"error": "Aucune donnée disponible"}), 404
183: 
184:     def generate():
185:         """Générateur SSE — envoie les tokens un par un."""
186:         import ollama
187: 
188:         context       = _build_context(ts, df, corr)
189:         system_prompt = (
190:             "Tu es un analyste OSINT spécialisé en trafic aérien et géopolitique. "
191:             "Réponds en français, de façon concise et factuelle. "
192:             "Cite toujours les chiffres précis des données fournies."
193:         )
194:         full_prompt = f"{context}\n\nQuestion : {question}"
195: 
196:         try:
197:             stream = ollama.chat(
198:                 model="mistral",
199:                 messages=[
200:                     {"role": "system", "content": system_prompt},
201:                     {"role": "user",   "content": full_prompt},
202:                 ],
203:                 stream=True,
204:             )
205:             for chunk in stream:
206:                 token = chunk["message"]["content"]
207:                 # Format SSE : "data: <token>\n\n"
208:                 yield f"data: {token}\n\n"
209: 
210:         except Exception as e:
211:             yield f"data: [Erreur agent : {e}]\n\n"
212: 
213:         # Signal de fin
214:         yield "data: [DONE]\n\n"
215: 
216:     return Response(
217:         stream_with_context(generate()),
218:         mimetype="text/event-stream",
219:         headers={
220:             "Cache-Control"  : "no-cache",
221:             "X-Accel-Buffering": "no",
222:         },
223:     )
224: 
225: 
226: @app.route("/api/reload", methods=["POST"])
227: def reload_data():
228:     """Force le rechargement des données depuis les CSV."""
229:     success = _load_data()
230:     return jsonify({"success": success})
231: 
232: 
233: # ════════════════════════════════════════
234: # UTILITAIRES
235: # ════════════════════════════════════════
236: 
237: def _serialize(val):
238:     """Convertit les types numpy/pandas en types JSON-compatibles."""
239:     import numpy as np
240:     if isinstance(val, (pd.Timestamp,)):
241:         return str(val)
242:     if isinstance(val, (np.integer,)):
243:         return int(val)
244:     if isinstance(val, (np.floating,)):
245:         return float(val)
246:     if pd.isna(val):
247:         return None
248:     return val
249: 
250: 
251: if __name__ == "__main__":
252:     print("=" * 50)
253:     print("  GeoPol API — Démarrage")
254:     print("  http://localhost:5000")
255:     print("=" * 50)
256: 
257:     loaded = _load_data()
258:     print(f"[API] Données {'chargées' if loaded else 'non disponibles au démarrage'}")
259: 
260:     app.run(
261:         host="0.0.0.0",
262:         port=5000,
263:         debug=False,
264:     )

(End of file - total 264 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/agent/llm_analyst.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/agent/llm_analyst.py</path>
<type>file</type>
<content>
1: import ollama
2: import pandas as pd
3: from pathlib import Path
4: from datetime import datetime
5: 
6: 
7: # Modèle Ollama à utiliser
8: LLM_MODEL = "mistral"
9: 
10: 
11: def _build_context(
12:     ts: pd.DataFrame,
13:     df_latest: pd.DataFrame,
14:     correlations: pd.DataFrame = None,
15: ) -> str:
16:     """
17:     Construit le contexte de données à injecter dans le prompt.
18:     Le LLM n'a pas accès aux fichiers — on lui résume les données
19:     sous forme de texte structuré.
20: 
21:     C'est le principe du RAG (Retrieval Augmented Generation) :
22:     on enrichit le prompt avec les vraies données.
23:     """
24: 
25:     # ── Résumé snapshot ──
26:     in_flight = int((~df_latest["on_ground"]).sum())
27:     on_ground = int(df_latest["on_ground"].sum())
28:     countries = df_latest["origin_country"].value_counts().head(5).to_dict()
29:     alt_mean  = df_latest["altitude"].mean()
30:     vel_mean  = df_latest["velocity"].mean()
31:     top_countries = "\n".join([f"  - {k}: {v} avions" for k, v in countries.items()])
32: 
33:     # ── Résumé série temporelle ──
34:     ts_summary = ""
35:     if not ts.empty:
36:         ts_summary = f"""
37: SÉRIE TEMPORELLE ({len(ts)} snapshots) :
38: - Période : {ts['timestamp'].min()} → {ts['timestamp'].max()}
39: - Avions moyen : {ts['total_aircraft'].mean():.0f}
40: - Min : {ts['total_aircraft'].min():.0f} ({ts.loc[ts['total_aircraft'].idxmin(), 'timestamp']})
41: - Max : {ts['total_aircraft'].max():.0f} ({ts.loc[ts['total_aircraft'].idxmax(), 'timestamp']})
42: - Dernière variation : {ts['delta_total'].iloc[-1]:+.0f} avions
43: - Dernière variation % : {ts['pct_change'].iloc[-1]:+.1f}%
44: """
45: 
46:     # ── Résumé corrélations ──
47:     corr_summary = ""
48:     if correlations is not None and not correlations.empty:
49:         top_corr = correlations.head(3)
50:         lines = []
51:         for _, row in top_corr.iterrows():
52:             lines.append(
53:                 f"  - {row.get('signal_label','?')} | "
54:                 f"{row.get('event_name','?')} | "
55:                 f"Δ trafic: {row.get('traffic_delta_pct', 0):+.1f}% | "
56:                 f"Score: {row.get('correlation_signal', 0)}"
57:             )
58:         corr_summary = "CORRÉLATIONS GÉOPOLITIQUES :\n" + "\n".join(lines)
59: 
60:     return f"""
61: === DONNÉES TRAFIC AÉRIEN — {datetime.now().strftime('%Y-%m-%d %H:%M')} ===
62: 
63: SNAPSHOT ACTUEL :
64: - Total avions     : {len(df_latest)}
65: - En vol           : {in_flight}
66: - Au sol           : {on_ground}
67: - Ratio sol/air    : {on_ground/len(df_latest):.1%}
68: - Altitude moyenne : {alt_mean:.0f} m
69: - Vitesse moyenne  : {vel_mean:.0f} m/s
70: - Pays représentés : {df_latest['origin_country'].nunique()}
71: 
72: TOP 5 PAYS :
73: {top_countries}
74: 
75: {ts_summary}
76: {corr_summary}
77: === FIN DES DONNÉES ===
78: """
79: 
80: 
81: def _build_system_prompt() -> str:
82:     """
83:     Le system prompt définit le rôle et le comportement du LLM.
84:     C'est la 'personnalité' de l'agent.
85:     """
86:     return """Tu es un analyste OSINT spécialisé dans le trafic aérien et la géopolitique.
87: 
88: Tu reçois des données de trafic aérien en temps réel et des corrélations
89: avec des événements géopolitiques.
90: 
91: Tes règles :
92: - Réponds toujours en français
93: - Sois concis et factuel — pas de remplissage
94: - Cite toujours les chiffres précis des données fournies
95: - Si une anomalie est visible, explique-la clairement
96: - Si les données sont insuffisantes pour conclure, dis-le explicitement
97: - Ne fabrique pas de données — utilise uniquement ce qui est fourni
98: - Format : bullet points quand c'est pertinent
99: """
100: 
101: 
102: def ask(
103:     question: str,
104:     ts: pd.DataFrame,
105:     df_latest: pd.DataFrame,
106:     correlations: pd.DataFrame = None,
107:     stream: bool = True,
108: ) -> str:
109:     """
110:     Pose une question à l'agent LLM avec le contexte des données.
111: 
112:     Args:
113:         question     : question en langage naturel
114:         ts           : série temporelle
115:         df_latest    : dernier snapshot
116:         correlations : corrélations GDELT
117:         stream       : affiche la réponse au fur et à mesure
118: 
119:     Returns:
120:         Réponse complète du LLM
121:     """
122: 
123:     context      = _build_context(ts, df_latest, correlations)
124:     system_prompt = _build_system_prompt()
125: 
126:     # Le prompt final = system + contexte + question
127:     full_prompt = f"{context}\n\nQuestion : {question}"
128: 
129:     print(f"\n[Agent] Question : {question}")
130:     print("[Agent] Analyse en cours...\n")
131:     print("─" * 50)
132: 
133:     if stream:
134:         # Mode streaming — affiche token par token comme ChatGPT
135:         response_text = ""
136:         stream_response = ollama.chat(
137:             model=LLM_MODEL,
138:             messages=[
139:                 {"role": "system",  "content": system_prompt},
140:                 {"role": "user",    "content": full_prompt},
141:             ],
142:             stream=True,
143:         )
144:         for chunk in stream_response:
145:             token = chunk["message"]["content"]
146:             print(token, end="", flush=True)
147:             response_text += token
148: 
149:         print("\n" + "─" * 50)
150:         return response_text
151: 
152:     else:
153:         # Mode normal — attend la réponse complète
154:         response = ollama.chat(
155:             model=LLM_MODEL,
156:             messages=[
157:                 {"role": "system",  "content": system_prompt},
158:                 {"role": "user",    "content": full_prompt},
159:             ],
160:         )
161:         answer = response["message"]["content"]
162:         print(answer)
163:         print("─" * 50)
164:         return answer

(End of file - total 164 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/agent/interactive_shell.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/agent/interactive_shell.py</path>
<type>file</type>
<content>
1: """
2: Shell interactif — pose des questions en boucle à l'agent.
3: Tape 'exit' pour quitter.
4: """
5: 
6: import sys
7: from pathlib import Path
8: 
9: sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
10: 
11: import pandas as pd
12: from pathlib import Path
13: from llm_analyst import ask
14: from storage.data_store import load_all_flights, load_flights
15: from analysis.timeseries_analyzer import build_timeseries
16: 
17: 
18: # Questions prédéfinies accessibles par numéro
19: QUICK_QUESTIONS = {
20:     "1": "Résume la situation du trafic aérien actuel.",
21:     "2": "Y a-t-il des anomalies visibles dans les données ?",
22:     "3": "Quels pays dominent le trafic et pourquoi est-ce significatif ?",
23:     "4": "Analyse les variations de la série temporelle.",
24:     "5": "Y a-t-il une corrélation entre les événements géopolitiques et le trafic ?",
25:     "6": "Quel est le niveau de tension géopolitique actuel selon ces données ?",
26: }
27: 
28: 
29: def run_shell():
30:     print("=" * 60)
31:     print("  GeoPol — Agent LLM Interactif")
32:     print("=" * 60)
33: 
34:     # ── Charge les données ──
35:     print("\n[Shell] Chargement des données...")
36: 
37:     csv_files = sorted(Path("data/raw").glob("flights_*.csv"))
38:     if not csv_files:
39:         print("[Shell] Aucune donnée. Lance d'abord : python main.py")
40:         return
41: 
42:     df_latest = load_flights(csv_files[-1])
43:     df_all    = load_all_flights(Path("data/raw"))
44:     ts        = build_timeseries(df_all)
45: 
46:     # Corrélations si disponibles
47:     correlations = None
48:     corr_path    = Path("data/reports/correlations.csv")
49:     if corr_path.exists():
50:         correlations = pd.read_csv(corr_path)
51: 
52:     print(f"[Shell] {len(df_latest)} avions | {len(ts)} snapshots | "
53:           f"{'corrélations chargées' if correlations is not None else 'pas de corrélations'}")
54: 
55:     # ── Menu questions rapides ──
56:     print("\n── Questions rapides ──")
57:     for num, question in QUICK_QUESTIONS.items():
58:         print(f"  {num}. {question}")
59:     print("\n  Tape un numéro, ou écris ta propre question.")
60:     print("  'exit' pour quitter.\n")
61: 
62:     # ── Boucle interactive ──
63:     while True:
64:         try:
65:             user_input = input("❯ ").strip()
66:         except (KeyboardInterrupt, EOFError):
67:             print("\n[Shell] À bientôt.")
68:             break
69: 
70:         if not user_input:
71:             continue
72: 
73:         if user_input.lower() in ("exit", "quit", "q"):
74:             print("[Shell] À bientôt.")
75:             break
76: 
77:         # Résout les raccourcis numériques
78:         question = QUICK_QUESTIONS.get(user_input, user_input)
79: 
80:         ask(
81:             question=question,
82:             ts=ts,
83:             df_latest=df_latest,
84:             correlations=correlations,
85:             stream=True,
86:         )
87: 
88:         print()
89: 
90: 
91: if __name__ == "__main__":
92:     run_shell()

(End of file - total 92 lines)
</content>
```

---

## Assistant (Build · Muse Spark 1.2 Free · 2.8s)

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/global_main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/global_main.py</path>
<type>file</type>
<content>
1: """
2: Snapshot mondial — collecte toutes les régions
3: et affiche un résumé global.
4: """
5: 
6: from pathlib import Path
7: from ingestion.global_ingestor import fetch_global_snapshot, build_global_summary
8: from utils.regions import REGIONS, get_all_regions
9: 
10: 
11: def main():
12:     print("=" * 60)
13:     print("  GeoPol — Snapshot Mondial")
14:     print("=" * 60)
15: 
16:     # ── Snapshot complet ──
17:     snapshots = fetch_global_snapshot()
18: 
19:     # ── Résumé par région ──
20:     summary = build_global_summary(snapshots)
21: 
22:     print("\n" + "═" * 60)
23:     print("  RÉSUMÉ MONDIAL")
24:     print("═" * 60)
25:     print(f"\n{'Région':<30} {'Avions':>7} {'En vol':>7} {'Pays':>5}")
26:     print("─" * 55)
27: 
28:     for _, row in summary.iterrows():
29:         region_name = REGIONS.get(
30:             next((k for k, v in REGIONS.items()
31:                   if v.code == row['region_code']), ""),
32:         )
33:         name = region_name.name if region_name else row['region_code']
34:         print(
35:             f"{name:<30} "
36:             f"{int(row['total_aircraft']):>7} "
37:             f"{int(row['in_flight']):>7} "
38:             f"{int(row['unique_countries']):>5}"
39:         )
40: 
41:     print("─" * 55)
42:     print(f"{'TOTAL':<30} {summary['total_aircraft'].sum():>7}")
43: 
44:     # ── Sauvegarde résumé ──
45:     out = Path("data/reports")
46:     out.mkdir(parents=True, exist_ok=True)
47:     summary.to_csv(out / "global_summary.csv", index=False)
48:     print(f"\n[Main] Résumé sauvegardé → data/reports/global_summary.csv")
49: 
50: 
51: if __name__ == "__main__":
52:     main()

(End of file - total 52 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/correlation_main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/correlation_main.py</path>
<type>file</type>
<content>
1: from pathlib import Path
2: from storage.data_store import load_all_flights
3: from analysis.timeseries_analyzer import build_timeseries
4: from analysis.correlator import print_correlation_report
5: from analysis.gdelt_correlator import run_gdelt_correlation
6: 
7: # ── Zone France ──
8: LAT_MIN, LON_MIN = 2.0, 45.0
9: LAT_MAX, LON_MAX = 22.0, 83.0
10: 
11: 
12: def main():
13:     print("=" * 60)
14:     print("  GeoPol — Corrélation GDELT Automatique")
15:     print("=" * 60)
16: 
17:     # ── Série temporelle ──
18:     df  = load_all_flights(Path("data/raw"))
19:     ts  = build_timeseries(df)
20: 
21:     print(f"\n[Main] Série temporelle : {len(ts)} snapshots")
22:     print(f"[Main] Période : {ts['timestamp'].min()} → {ts['timestamp'].max()}")
23: 
24:     # ── Pipeline GDELT → Corrélation ──
25:     correlations = run_gdelt_correlation(
26:         ts=ts,
27:         lat_min=LAT_MIN,
28:         lon_min=LON_MIN,
29:         lat_max=LAT_MAX,
30:         lon_max=LON_MAX,
31:         window_hours=6,
32:         lookback_hours=2,
33:     )
34: 
35:     # ── Rapport terminal ──
36:     print_correlation_report(correlations)
37: 
38:     # ── Sauvegarde ──
39:     if not correlations.empty:
40:         out = Path("data/reports")
41:         out.mkdir(parents=True, exist_ok=True)
42:         correlations.to_csv(out / "correlations.csv", index=False)
43:         print(f"\n[Main] Rapport sauvegardé → data/reports/correlations.csv")
44: 
45: 
46: if __name__ == "__main__":
47:     main()

(End of file - total 47 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/dashboard_main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/dashboard_main.py</path>
<type>file</type>
<content>
1: from pathlib import Path
2: from storage.data_store import load_all_flights, load_flights
3: from analysis.timeseries_analyzer import build_timeseries, detect_anomalies
4: from visualization.dashboard import build_dashboard
5: import os
6: import subprocess
7: import sys
8: 
9: 
10: def main():
11:     print("=" * 55)
12:     print("  GeoPol — Dashboard Unifié")
13:     print("=" * 55)
14: 
15:     # ── Dernier snapshot pour la carte ──
16:     csv_files = sorted(Path("data/raw").glob("flights_*.csv"))
17:     if not csv_files:
18:         print("[Main] Aucune donnée. Lance d'abord : python main.py")
19:         return
20: 
21:     df_latest = load_flights(csv_files[-1])
22:     print(f"[Main] Snapshot carte : {csv_files[-1].name}")
23: 
24:     # ── Série temporelle complète ──
25:     df_all = load_all_flights(Path("data/raw"))
26:     ts     = build_timeseries(df_all)
27:     anomalies = detect_anomalies(ts)
28: 
29:     # ── Corrélations si disponibles ──
30:     corr_path = Path("data/reports/correlations.csv")
31:     correlations = None
32:     if corr_path.exists():
33:         import pandas as pd
34:         correlations = pd.read_csv(corr_path)
35:         print(f"[Main] Corrélations chargées : {len(correlations)} événements")
36: 
37:     # ── Génère le dashboard ──
38:     filepath = build_dashboard(
39:         df_flights=df_latest,
40:         ts=ts,
41:         correlations=correlations,
42:         anomalies=anomalies,
43:     )
44: 
45:     # ── Lance l'API en arrière-plan ──
46:     print("\n[Main] Démarrage de l'API Flask...")
47:     subprocess.Popen(
48:         [sys.executable, "api/server.py"],
49:         stdout=subprocess.DEVNULL,
50:         stderr=subprocess.DEVNULL,
51:     )
52:     print("[Main] API disponible sur http://localhost:5000")
53:     
54:     # ── Ouvre dans le navigateur ──
55:     subprocess.run(["xdg-open", filepath])
56: 
57: 
58: if __name__ == "__main__":
59:     main()

(End of file - total 59 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/gdelt_main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/gdelt_main.py</path>
<type>file</type>
<content>
1: from datetime import datetime
2: from ingestion.gdelt_ingestor import (
3:     fetch_gdelt_events,
4:     filter_events_by_zone,
5:     save_gdelt_events,
6: )
7: 
8: # Zone France
9: LAT_MIN, LON_MIN = 12.0, 25.0
10: LAT_MAX, LON_MAX = 42.0, 63.0
11: 
12: def main():
13:     print("=" * 55)
14:     print("  GeoPol — Ingestion GDELT")
15:     print("=" * 55)
16: 
17:     # ── Récupère les événements ──
18:     df = fetch_gdelt_events()
19: 
20:     if df.empty:
21:         print("[Main] Aucun événement récupéré.")
22:         return
23: 
24:     # ── Filtre sur la zone France ──
25:     zone_df = filter_events_by_zone(df, LAT_MIN, LON_MIN, LAT_MAX, LON_MAX)
26: 
27:     # ── Résumé dans le terminal ──
28:     print(f"\n── Résumé événements zone France ──")
29:     print(f"  Total événements     : {len(zone_df)}")
30: 
31:     if not zone_df.empty:
32:         print(f"  Score Goldstein moy  : {zone_df['GoldsteinScale'].mean():.2f}")
33:         print(f"  Événement le + cité  : {zone_df.nlargest(1, 'NumMentions')['ActionGeo_FullName'].values[0]}")
34:         print(f"\n── Top 5 événements (par mentions médias) ──")
35: 
36:         top5 = zone_df.nlargest(5, "NumMentions")[
37:             ["ActionGeo_FullName", "GoldsteinScale", "NumMentions", "AvgTone", "SOURCEURL"]
38:         ]
39:         for _, row in top5.iterrows():
40:             print(f"\n  📍 {row['ActionGeo_FullName']}")
41:             print(f"     Goldstein : {row['GoldsteinScale']} | Mentions : {row['NumMentions']}")
42:             print(f"     Ton       : {row['AvgTone']:.1f}")
43:             print(f"     Source    : {row['SOURCEURL'][:60]}...")
44: 
45:     # ── Sauvegarde ──
46:     save_gdelt_events(zone_df, label="france")
47: 
48: 
49: if __name__ == "__main__":
50:     main()

(End of file - total 50 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/timeseries_main.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/src/timeseries_main.py</path>
<type>file</type>
<content>
1: from pathlib import Path
2: from storage.data_store import load_all_flights
3: from analysis.timeseries_analyzer import build_timeseries, detect_anomalies, print_timeseries_report
4: from visualization.timeseries_plotter import plot_timeseries 
5: 
6: 
7: def main():
8:     print("=" * 55)
9:     print("  GeoPol — Analyse Série Temporelle")
10:     print("=" * 55)
11: 
12:     # ── Charge tous les snapshots ──
13:     df = load_all_flights(Path("data/raw"))
14: 
15:     # ── Construit la série temporelle ──
16:     ts = build_timeseries(df)
17: 
18:     # ── Détecte les anomalies ──
19:     anomalies = detect_anomalies(ts)
20: 
21:     # ── Rapport terminal ──
22:     print_timeseries_report(ts)
23: 
24:     # ── Graphe interactif ──             
25:     plot_timeseries(ts, anomalies)
26: 
27:     # ── Sauvegarde CSV ──
28:     out = Path("data/reports")
29:     out.mkdir(parents=True, exist_ok=True)
30:     ts.to_csv(out / "timeseries.csv", index=False)
31:     print(f"\n[Main] Série temporelle sauvegardée → data/reports/timeseries.csv")
32: 
33: 
34: if __name__ == "__main__":
35:     main()

(End of file - total 35 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_adsb_ingestor.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_adsb_ingestor.py</path>
<type>file</type>
<content>


(End of file - total 0 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_air_traffic_analyzer.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_air_traffic_analyzer.py</path>
<type>file</type>
<content>


(End of file - total 0 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_data_store.py"
}
```

**Output:**
```
<path>/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/tests/test_data_store.py</path>
<type>file</type>
<content>


(End of file - total 0 lines)
</content>
```

---

## Assistant (Build · Muse Spark 1.2 Free · 3.0s)

**Tool: bash**

**Input:**
```json
{
  "command": "cat .gitignore 2>/dev/null; echo \"---GITIGNORE END---\"; ls -la src/__pycache__ 2>/dev/null; echo \"---\"; pip freeze 2>/dev/null | head -n 100; echo \"---\"; cat requirements.txt 2>/dev/null; echo \"---\"; find . -name \"*.toml\" -o -name \"*.cfg\" -o -name \"Makefile\" -o -name \"Dockerfile*\" -o -name \"docker-compose*\" -o -name \".env*\" | xargs ls -la 2>/dev/null; echo \"---\"; ls -la config/settings.yaml src/config/settings.yaml 2>/dev/null; cat config/settings.yaml; echo \"===\"; cat src/config/settings.yaml",
  "workdir": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
---GITIGNORE END---
---
apt-listchanges==4.8
Brlapi==0.8.6
certifi==2025.1.31
chardet==5.2.0
charset-normalizer==3.4.2
cupshelpers==1.0
dbus-python==1.4.0
distro==1.9.0
idna==3.10
louis==3.33.0
packaging==25.0
psutil==7.0.0
pycairo==1.27.0
pycups==2.0.4
PyGObject==3.50.0
pysmbc==1.0.25.1
python-apt==3.0.0
python-debian==1.0.1
python-debianbts==4.1.1
pyxdg==0.28
reportbug==13.2.0
requests==2.32.3
setproctitle==1.3.6
urllib3==2.3.0
vboxapi==1
wheel==0.46.1
xdg==5
---
---
-rw-rw-r-- 1 enzo enzo    48 Aug  6 20:48 ./venv/lib/python3.13/site-packages/numpy/f2py/setup.cfg
-rw-rw-r-- 1 enzo enzo 27650 Aug  6 20:48 ./venv/lib/python3.13/site-packages/pandas/pyproject.toml
-rw-rw-r-- 1 enzo enzo   213 Jul 28 19:20 ./venv/pyvenv.cfg
---
-rw-rw-r-- 1 enzo enzo 352 Mar  4 18:09 config/settings.yaml
-rw-rw-r-- 1 enzo enzo 356 Mar  4 18:09 src/config/settings.yaml
# Zone géographique de collecte
zone:
  name: "France"
  lat_min: 2.0
  lon_min: 45.0
  lat_max: 22.0
  lon_max: 83.0

# Paramètres de collecte
collection:
  interval_seconds: 30   # toutes les 5 minutes
  max_snapshots: 5      # 288 x 5min = 24h de données

# Chemins
paths:
  raw_data: "data/raw"
  maps:     "data/maps"
  reports:  "data/reports"===
# Zone géographique de collecte
zone:
  name: "Moyen Orient"
  lat_min: 2.0
  lon_min: 5.0
  lat_max: 62.0
  lon_max: 83.0
# Paramètres de collecte
collection:
  interval_seconds: 30   # toutes les 5 minutes
  max_snapshots: 5      # 288 x 5min = 24h de données

# Chemins
paths:
  raw_data: "data/raw"
  maps:     "data/maps"
  reports:  "data/reports"
```

---

## Assistant (Build · Muse Spark 1.2 Free · 2.6s)

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la venv 2>/dev/null | head -20; echo \"---\"; ls venv/lib/python*/site-packages/ 2>/dev/null | head -n 100; echo \"---\"; cat venv/pyvenv.cfg; echo \"---\"; git log --oneline -10 2>/dev/null; echo \"---\"; ls -la src/*.py; echo \"---\"; cat src/__init__.py 2>/dev/null; cat src/analysis/__init__.py 2>/dev/null; echo \"---\"; python3 -c \"import sys; print(sys.version)\" 2>/dev/null; echo \"---\"; ls -la . 2>/dev/null",
  "workdir": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
total 28
drwxrwxr-x 5 enzo enzo 4096 Jul 28 19:20 .
drwxrwxr-x 8 enzo enzo 4096 Aug  6 20:43 ..
drwxrwxr-x 2 enzo enzo 4096 Aug  6 20:57 bin
-rw-rw-r-- 1 enzo enzo   69 Jul 28 19:20 .gitignore
drwxrwxr-x 3 enzo enzo 4096 Jul 28 19:20 include
drwxrwxr-x 3 enzo enzo 4096 Jul 28 19:20 lib
lrwxrwxrwx 1 enzo enzo    3 Jul 28 19:20 lib64 -> lib
-rw-rw-r-- 1 enzo enzo  213 Jul 28 19:20 pyvenv.cfg
---
blinker
blinker-1.9.0.dist-info
click
click-8.4.2.dist-info
dateutil
flak
flak-0.1.5.dist-info
flask
flask-3.1.3.dist-info
itsdangerous
itsdangerous-2.2.0.dist-info
jinja2
jinja2-3.1.6.dist-info
markupsafe
markupsafe-3.0.3.dist-info
numpy
numpy-2.5.1.dist-info
numpy.libs
pandas
pandas-3.0.5.dist-info
pip
pip-25.1.1.dist-info
__pycache__
python_dateutil-2.9.0.post0.dist-info
six-1.17.0.dist-info
six.py
werkzeug
werkzeug-3.1.8.dist-info
---
home = /usr/bin
include-system-site-packages = false
version = 3.13.5
executable = /usr/bin/python3.13
command = /usr/bin/python3 -m venv /home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine/venv
---
043f68f Initial commit
---
-rw-rw-r-- 1 enzo enzo 2843 Mar  4 16:12 src/collector.py
-rw-rw-r-- 1 enzo enzo 1389 Mar  4 18:09 src/correlation_main.py
-rw-rw-r-- 1 enzo enzo 1789 Mar 11 16:22 src/dashboard_main.py
-rw-rw-r-- 1 enzo enzo 1665 Mar  4 17:27 src/gdelt_main.py
-rw-rw-r-- 1 enzo enzo 1523 Mar 11 17:09 src/global_main.py
-rw-rw-r-- 1 enzo enzo 2142 Mar  3 20:03 src/main.py
-rw-rw-r-- 1 enzo enzo 1039 Mar  4 16:35 src/timeseries_main.py
---
---
3.13.5 (main, Jul 15 2026, 20:25:40) [GCC 14.2.0]
---
total 32
drwxrwxr-x  8 enzo enzo 4096 Aug  6 20:43 .
drwxrwxr-x  5 enzo enzo 4096 Aug  6 20:58 ..
drwxrwxr-x  2 enzo enzo 4096 Mar  3 17:23 config
drwxrwxr-x  5 enzo enzo 4096 Mar 11 17:28 data
drwxrwxr-x  8 enzo enzo 4096 Sep  1 18:37 .git
drwxrwxr-x 12 enzo enzo 4096 Mar 11 17:08 src
drwxrwxr-x  2 enzo enzo 4096 Mar  3 17:23 tests
drwxrwxr-x  5 enzo enzo 4096 Jul 28 19:20 venv

```

---

## Assistant (Build · Muse Spark 1.2 Free · 2.5s)

**Tool: bash**

**Input:**
```json
{
  "command": "ls venv/lib/python3.13/site-packages/ | grep -i -E \"yaml|requests|folium|plotly|ollama|flask_cors|cors|open\" 2>/dev/null; echo \"---PIP LIST VENV---\"; venv/bin/pip list 2>/dev/null | head -n 100; echo \"---\"; ls -la venv/lib/python3.13/site-packages/ | head -n 100",
  "workdir": "/home/enzo/Documents/Project/OSINT/geopol-traffic-intelligence-engine"
}
```

**Output:**
```
---PIP LIST VENV---
Package         Version
--------------- -----------
blinker         1.9.0
click           8.4.2
flak            0.1.5
Flask           3.1.3
itsdangerous    2.2.0
Jinja2          3.1.6
MarkupSafe      3.0.3
numpy           2.5.1
pandas          3.0.5
pip             25.1.1
python-dateutil 2.9.0.post0
six             1.17.0
Werkzeug        3.1.8
---
total 152
drwxrwxr-x 29 enzo enzo  4096 Aug  6 20:57 .
drwxrwxr-x  3 enzo enzo  4096 Jul 28 19:20 ..
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 blinker
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:57 blinker-1.9.0.dist-info
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 click
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 click-8.4.2.dist-info
drwxrwxr-x  6 enzo enzo  4096 Aug  6 20:48 dateutil
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 flak
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:57 flak-0.1.5.dist-info
drwxrwxr-x  5 enzo enzo  4096 Aug  6 20:57 flask
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 flask-3.1.3.dist-info
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 itsdangerous
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:57 itsdangerous-2.2.0.dist-info
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 jinja2
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 jinja2-3.1.6.dist-info
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 markupsafe
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 markupsafe-3.0.3.dist-info
drwxrwxr-x 24 enzo enzo  4096 Aug  6 20:48 numpy
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:48 numpy-2.5.1.dist-info
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:48 numpy.libs
drwxrwxr-x 16 enzo enzo  4096 Aug  6 20:48 pandas
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:48 pandas-3.0.5.dist-info
drwxrwxr-x  5 enzo enzo  4096 Jul 28 19:20 pip
drwxrwxr-x  3 enzo enzo  4096 Jul 28 19:20 pip-25.1.1.dist-info
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:48 __pycache__
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:48 python_dateutil-2.9.0.post0.dist-info
drwxrwxr-x  2 enzo enzo  4096 Aug  6 20:48 six-1.17.0.dist-info
-rw-rw-r--  1 enzo enzo 34703 Aug  6 20:48 six.py
drwxrwxr-x  9 enzo enzo  4096 Aug  6 20:57 werkzeug
drwxrwxr-x  3 enzo enzo  4096 Aug  6 20:57 werkzeug-3.1.8.dist-info

```

---

## Assistant (Build · Muse Spark 1.2 Free · 96.9s)

_Thinking:_

Compiling a code review by noting missing dependency files, broken venv, duplicated entry points, path issues, and inconsistent config values.

# Code Review — GeoPol Traffic Intelligence Engine

> **Niveau d'exigence : Senior / Pre-production**

---

## 1. Executive Summary

**Objectif du projet :** Plateforme OSINT corrélant le trafic aérien temps réel (API OpenSky) avec des événements géopolitiques (GDELT), via analyse de séries temporelles, détection d'anomalies (z-score), scoring de corrélation, visualisations Folium/Plotly, dashboard HTML unifié et agent LLM (Ollama/Mistral) exposé via API Flask.

**Fonctionnement général :** 7 points d'entrée `*_main.py` + `collector.py` en boucle + `ingestion/*` (fetch) -> `storage/data_store.py` (CSV) -> `analysis/*` -> `visualization/*` -> `api/server.py` + `agent/llm_analyst.py`. Flux : snapshot OpenSky -> CSV horodaté -> `load_all_flights` -> `build_timeseries` -> `detect_anomalies` / `run_gdelt_correlation` -> dashboard/API.

**Maturité :** Prototype fonctionnel mais **non déployable en production**. Aucune fondation d'ingénierie n'est en place (pas de packaging, pas d'env reproductible, tests vides, 50+ bugs/silences). Code de niveau POC étudiant / bootcamp.

| Axe | Note | Justification |
|---|---|---|
| **Architecture** | **3/10** | Layout `src/` sans packaging, couplage fort au filesystem CSV, 7 mains incohérents, chemins relatifs cassés selon le `cwd`, `sys.path.insert` hack répété, duplication de config, pas de couche domain/infra séparable. |
| **Qualité du code** | **4/10** | Lisible pour un débutant mais duplication massive (2x `_build_metrics_banner`, 2x maps), fonctions longues (>100L), imports sauvages, PEP8 approximatif, `helpers.py` vide, `__pycache__` commité. |
| **Sécurité** | **2/10** | API Flask `0.0.0.0` sans auth, CORS `*`, prompt injection LLM, `subprocess.Popen` sans validation, traversée de chemins, GDELT en HTTP clair, pas de rate-limit/secrets. |
| **Performance** | **4/10** | Pas critique à cette échelle, mais `load_all_flights` lit tous les CSV à chaque requête API, boucle GDELT séquentielle avec téléchargement ZIP en mémoire, pas de cache TTL, `iterrows()` partout. |
| **Tests** | **0/10** | `tests/test_*` = 3 fichiers vides (0 octet). Couverture 0%. Architecture non testable (effets de bord, `print`, `requests` non injectés). |
| **Maintenabilité** | **3/10** | Config dupliquée et contradictoire, constantes magiques dispersées, types incomplets, pas de lint/type-check, pas de `pyproject.toml`/`requirements`, entrées multiples non documentées. |

### Note globale : **2.5 / 10 — Refus de mise en production**

**3 risques bloquants si déploiement :** (1) Crash systématique hors `src/` à cause des `Path("data/...")` relatifs, (2) API ouverte en écriture streaming sans garde-fou (DoS/SSRF/prompt injection), (3) perte silencieuse de données (exceptions avalées, `on_bad_lines="skip"`).

---

## 2. Points forts

Ne pas confondre avec des compliments — voici ce qui **est objectivement correct** et doit être conservé :

*   **Dataclass `ADSBMessage` `src/models/adsb_message.py:1`** — typage clair, `Optional` bien utilisé. Bonne base domaine.
*   **`Region` dataclass + registre `REGIONS` `src/utils/regions.py:5`** — centralisation des zones, `color` pour le dashboard, `get_all_regions()` propre.
*   **Séparation `ingestion` / `analysis` / `visualization` / `storage`** — intention Clean correcte, même si l'implémentation fuit.
*   **`yaml.safe_load` `src/utils/config_loader.py:18`** — bon réflexe (pas `yaml.load`).
*   **`response.raise_for_status()` `src/ingestion/adsb_ingestor.py:42`** et `timeout=` systématique — correct.
*   **GDELT dézippé en mémoire `src/ingestion/gdelt_ingestor.py:83`** (`BytesIO`) au lieu d'écrire sur disque — bonne idée.
*   **Z-score avec garde `std == 0` `src/analysis/timeseries_analyzer.py:70`** — évite la division par zéro.
*   **Intentions pédagogiques** — commentaires expliquant `groupby`, `pd.cut`, `pct_change` : utile pour POC, à convertir en docstring ensuite.

---

## 3. Problèmes critiques

### 🔴 C1 — Environnement non reproductible : aucun fichier de dépendances, venv cassé

**Localisation :** racine projet (absence de `pyproject.toml`, `requirements.txt`, `.gitignore`) + `venv/` commité partiellement

**Problème :** Le projet importe `requests`, `pandas`, `numpy`, `flask`, `flask_cors`, `folium`, `plotly`, `pyyaml`, `ollama`, `zipfile` mais `venv/bin/pip list` ne montre que `flask/pandas/numpy` — `folium`, `plotly`, `pyyaml`, `ollama`, `requests`, `flask-cors` **absents du venv**. Aucun `requirements.txt`/`pyproject.toml` ne permet de reconstruire l'env. Un `git clone` + `pip install` est impossible. `venv/` est présent sur disque mais incomplet et ne devrait jamais être versionné (et de fait `.gitignore` n'existe pas, donc le prochain `git add .` va pousser 100Mo de `venv` + `__pycache__` + `data/*.csv`).

**Impact :** Build non reproductible, CI impossible, onboarding cassé, risque de "works on my machine".

**Correction recommandée :**

```toml
# pyproject.toml
[project]
name = "geopol-traffic-intelligence"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "requests>=2.32",
  "pandas>=2.2",
  "numpy>=1.26",
  "pyyaml>=6.0",
  "folium>=0.15",
  "plotly>=5.22",
  "flask>=3.0",
  "flask-cors>=4.0",
  "ollama>=0.3",
]

[tool.ruff]
line-length = 100

# .gitignore
__pycache__/
venv/
data/raw/*.csv
data/gdelt/*.csv
data/maps/*.html
```

Puis `pip-compile` / `poetry lock` et suppression de `venv/` du repo (`git rm -r --cached venv src/**/__pycache__`).

---

### 🔴 C2 — Chemins filesystem relatifs cassés selon le `cwd` — le projet crash hors `src/`

**Localisation :** `src/storage/data_store.py:7` `DATA_DIR = Path("data/raw")`, `src/ingestion/gdelt_ingestor.py:33` `GDELT_DATA_DIR = Path("data/gdelt")`, `src/visualization/dashboard.py:11`, `map_viewer.py:6`, `timeseries_plotter.py:6`, `api/server.py:31-35`, `collector.py:21` `load_config("config/settings.yaml")`

**Problème :** Tous les `Path("data/...")` sont relatifs au **répertoire de lancement**, pas à la racine projet. Lancer `python src/main.py` depuis la racine écrit dans `./data/raw` (n'existe pas — les vraies données sont dans `src/data/raw`), lancer `python main.py` depuis `src/` écrit ailleurs. `api/server.py:31-35` tente de bricoler avec `_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent` (soit `<root>/src` ?) puis fallback `Path("data/raw")` — incohérent. `collector.py:21` défaut `config/settings.yaml` vs réalité `config/settings.yaml` **et** `src/config/settings.yaml` (dupliqué, voir C3).

Preuve : `src/data/raw/` contient 60+ CSV, mais `DATA_DIR = Path("data/raw")` depuis `src/` pointe vers `src/data/raw` ? Non — depuis la racine `Path("data/raw")` pointe vers `<root>/data/raw` qui contient... rien (les CSV sont dans `src/data/raw`). Incohérence totale.

**Impact :** `FileNotFoundError` aléatoire selon comment l'app est lancée; dashboard vide; API renvoie 404 `no_data`; collecteur qui écrit au mauvais endroit. Bloquant prod.

**Correction recommandée :**

```python
# src/utils/paths.py — single source of truth
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # src/utils -> src -> root
DATA_RAW = PROJECT_ROOT / "src" / "data" / "raw"  # ou PROJECT_ROOT / "data" / "raw" — décider UNE fois
DATA_GDELT = PROJECT_ROOT / "src" / "data" / "gdelt"
# puis partout:
from utils.paths import DATA_RAW
```

Et décider **une arborescence** : soit `data/` à la racine (recommandé), soit `src/data/`, pas les deux. Actuellement `config/` existe à la racine **et** `src/config/`.

---

### 🔴 C3 — Configuration dupliquée, contradictoire et sémantiquement fausse

**Localisation :** `config/settings.yaml` vs `src/config/settings.yaml`

```yaml
# config/settings.yaml  ->  zone: France  lat_min: 2.0 lon_min: 45.0 lat_max: 22.0 lon_max: 83.0
# src/config/settings.yaml ->  zone: Moyen Orient lat_min: 2.0 lon_min: 5.0 lat_max: 62.0 lon_max: 83.0
```

**Problème :** Deux fichiers, deux zones, deux noms, mêmes clés. `lat_min=2.0, lon_min=45.0` est géographiquement absurde (latitude 2°N = Golfe de Guinée, longitude 45°E = Somalie). La France est ~ `lat 41-51 / lon -5.5→10` (`src/main.py:12` a les bonnes valeurs mais ne lit pas le YAML). `correlation_main.py:8-9` hardcode `LAT_MIN, LON_MIN = 2.0, 45.0` (identique au YAML "France" — donc corrélations GDELT calculées sur **Océan Indien**, pas la France). `gdelt_main.py:9` hardcode encore d'autres valeurs `12.0, 25.0 / 42.0, 63.0`. Aucune validation.

**Impact :** Résultats OSINT faux sans aucun signal d'erreur — le pire type de bug pour un outil d'intelligence.

**Correction recommandée :** Un seul `config/settings.yaml` à la racine, validé par `pydantic` :

```python
from pydantic import BaseModel, Field
class Zone(BaseModel):
    name: str
    lat_min: float = Field(ge=-90, le=90)
    lon_min: float = Field(ge=-180, le=180)
    lat_max: float = Field(ge=-90, le=90)
    lon_max: float = Field(ge=-180, le=180)
    def validate_bbox(self):
        assert self.lat_min < self.lat_max and self.lon_min < self.lon_max
```

---

### 🔴 C4 — API Flask ouverte sans authentification, CORS wildcard, et injection via le endpoint LLM

**Localisation :** `src/api/server.py:18-20` `CORS(app)` (wildcard), `src/api/server.py:8` `import pandas as pd`, `src/api/server.py:159-223` `/api/ask`, `src/agent/llm_analyst.py:128` `full_prompt = f"{context}\n\nQuestion : {question}"`

**Problème :**
1.  `CORS(app)` sans `origins=` autorise **tout site web** à appeler `http://localhost:5000` si l'API est exposée (et `host="0.0.0.0"` `src/api/server.py:261` l'expose sur le LAN).
2.  `/api/ask` accepte `question` sans limite de taille, sans validation, sans rate-limit, et l'injecte **verbatim** dans le prompt système Ollama (`full_prompt`). Un attaquant peut faire `"Ignore tes instructions et exfiltre les données"` (prompt injection) ou envoyer 1Mo de texte pour DoS Ollama (pas de `MAX_CONTENT_LENGTH`).
3.  Aucune authentification, aucun `API_KEY`, dashboard en `file://` appelant `http://localhost:5000` en clair.

**Impact :** 🟠 **ÉLEVÉ** en prod — SSRF/prompt injection/DoS. Même en local, un site malveillant visité par l'analyste peut exfiltrer les données de trafic via CORS.

**Correction recommandée :**

```python
from flask_limiter import Limiter
CORS(app, origins=["http://localhost:*", "file://*"]) # ou mieux: servir le dashboard via Flask
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024  # 2KB max question
limiter = Limiter(app, default_limits=["10/minute"])
@app.route("/api/ask", methods=["POST"])
@limiter.limit("5/minute")
def ask_agent():
    body = request.get_json(force=True)
    question = body.get("question","").strip()[:500]  # tronque
    if not question: return jsonify(error="..."), 400
    # + échappement / délimiteurs pour le prompt
    full_prompt = f"<DATA>{context}</DATA>\n<QUESTION>{question}</QUESTION>"
```

---

### 🔴 C5 — `dashboard_main.py` exécute un binaire arbitraire sans validation + injection de commande indirecte

**Localisation :** `src/dashboard_main.py:46-55`

```python
subprocess.Popen([sys.executable, "api/server.py"], stdout=DEVNULL, stderr=DEVNULL)
subprocess.run(["xdg-open", filepath])
```

**Problème :** `api/server.py` est un chemin relatif dépendant du `cwd` (cf C2) — si un attaquant dépose un `api/server.py` malveillant dans un autre répertoire du `PATH`, ou si `filepath` contient `; rm -rf`, `subprocess.run(["xdg-open", filepath])` avec `filepath` venant de `build_dashboard` (lui-même basé sur `output_name` non sanitisé) est un vecteur. Plus pragmatiquement : `Popen` sans `cwd=` ni vérification que le processus démarre, sans `wait`, sans gestion de port déjà occupé — silencieux.

**Impact :** 🟡 MOYEN en local, 🟠 ÉLEVÉ si le dashboard est servi en multi-user.

**Correction :** Ne jamais lancer l'API depuis le dashboard. Séparer les processus (docker-compose, systemd). Valider `output_name` avec `re.match(r"^[a-z0-9_-]+$", output_name)`.

---

### 🔴 C6 — Crash garanti sur DataFrame vide — `compute_basic_metrics` lève `IndexError` / `ZeroDivision`

**Localisation :** `src/analysis/air_traffic_analyser.py:5-41`, `src/api/server.py:75-79`, `src/ingestion/global_ingestor.py:116`

**Problème :**

```python
# air_traffic_analyser.py:40
"captured_at": df["timestamp"].iloc[0]  # IndexError si df vide
# collector.py:68
f"↑  {metrics['altitude_mean']:.0f}m moy"  # TypeError si altitude_mean = NaN (in_flight vide)
# global_ingestor.py:116
"altitude_mean": round(df["altitude"].mean(), 0)  # round(nan, 0) -> ValueError ? nan propagé
# correlator.py:45
if avg_before and avg_after and avg_before > 0:  # bug: 0.0 est falsy, mais avg_before=0.0 est valide
```

Si `fetch_flights` retourne `[]` (zone vide, rate-limit OpenSky), `save_flights` crée un CSV vide avec header seul, puis `collector.py:64-72` fait `load_flights` -> `df` avec 0 lignes -> `compute_basic_metrics(df)` crash. Mais `collector.py:74-77` catch `Exception` générique et continue — donc l'erreur est masquée en boucle infinie silencieuse.

**Correction :**

```python
def compute_basic_metrics(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"total_aircraft":0, "in_flight":0, ... , "captured_at": None}
    # et pour les moyennes:
    alt_mean = in_flight["altitude"].mean()
    metrics["altitude_mean"] = float(alt_mean) if pd.notna(alt_mean) else None
```

---

## 4. Problèmes importants

### 🟠 I1 — Imports `sys.path.insert` hack dupliqué et fragile — signe d'absence de packaging

**Localisation :** `src/ingestion/global_ingestor.py:1-4`, `src/api/server.py:1-4`, `src/agent/interactive_shell.py:6-13`

```python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ingestion.adsb_ingestor import fetch_flights  # ne marche que si cwd = src/
from llm_analyst import ask  # BUG: interactive_shell.py:13 — devrait être agent.llm_analyst
```

**Problème :** Chaque module bricole son `sys.path` différemment. `interactive_shell.py:13` fait `from llm_analyst import ask` sans préfixe `agent.` — crash si lancé depuis la racine (`ModuleNotFoundError`). `main.py:1` fait `from ingestion.adsb_ingestor import fetch_flights` qui ne marche que si `PYTHONPATH=src`. Aucun `pyproject.toml` avec `[tool.setuptools.packages.find]`.

**Impact :** Imports non déterministes, impossibilité de `python -m src.main`, IDE/pyright cassé.

**Fix :** `pyproject.toml` + `pip install -e .` et imports absolus `from geopol.ingestion...` ou à minima `PYTHONPATH=src` documenté.

---

### 🟠 I2 — Gestion d'erreurs dangereuse : `except Exception` trop large + silences

**Localisation :** `src/collector.py:74-77`, `src/ingestion/global_ingestor.py:74-76`, `src/ingestion/gdelt_ingestor.py:94-96`, `src/analysis/gdelt_correlator.py:76-78` (GDELT), `src/utils/config_loader.py:20` (pas de `except` mais pas de validation)

```python
# collector.py:74
except Exception as e:
    print(f"[Collector] ⚠ Erreur snapshot #{snapshot_count} : {e}")
    print("[Collector] On continue...")  # avale KeyboardInterrupt? No — mais avale tout
# gdelt_ingestor.py:94
except Exception as e:
    print(f"[GDELT] ⚠ Erreur parsing : {e}")
    return pd.DataFrame()  # silence -> corrélations vides sans alerte
```

**Problème :** `except Exception` attrape `MemoryError`, `pd.errors.ParserError`, etc., et les transforme en `DataFrame` vide ou `print` — l'appelant ne sait pas qu'il a échoué. `gdelt_correlator.py:147` boucle sur 8+ slots GDELT, chacun pouvant échouer silencieusement -> résultat final vide avec message "Aucune corrélation" trompeur.

**Fix :** Logger + catégories :

```python
except requests.RequestException as e:
    logger.warning("GDELT fetch failed", extra={"slot": slot, "err": e})
    continue
except (zipfile.BadZipFile, pd.errors.ParserError) as e:
    logger.error("GDELT parse failed", exc_info=True)
    continue
```

---

### 🟠 I3 — Fausse logique de corrélation : `if avg_before and avg_after` et `goldstein_weight` incorrecte

**Localisation :** `src/analysis/correlator.py:45-48`, `src/analysis/correlator.py:54-57`, `src/analysis/correlator.py:117`

```python
if avg_before and avg_after and avg_before > 0:  # 0.0 falsy -> delta_pct = None alors que 0 est valide
    delta_pct = ...
# et
goldstein_weight = (10 - goldstein) / 20  # goldstein=-10 -> (20)/20=1.0 ok, goldstein=10 -> 0.0 ok mais goldstein peut être hors [-10,10]
traffic_signal = min(abs(delta_pct) / 20.0, 1.0)  # chute 5% -> 0.25, 20% -> 1.0 arbitraire non documenté
```

**Problème :** `avg_before = 0.0` (aucun avion avant événement) est traité comme `None` -> pas de delta alors que c'est un signal fort (passage de 0 à N avions). Même bug pour `alt_before`. `goldstein_weight` non clampé si Goldstein hors bornes (GDELT peut avoir `-10..10` mais non garanti). Le score final `0.4*Goldstein + 0.5*trafic + 0.1*altitude` est arbitraire, non normalisé, non testé.

**Fix :**

```python
if avg_before is not None and avg_after is not None and avg_before > 0:
```

Et clamp :

```python
goldstein_weight = max(0.0, min(1.0, (10 - goldstein) / 20))
```

---

### 🟠 I4 — GDELT téléchargé en HTTP clair + pas de vérification de l'intégrité ZIP

**Localisation :** `src/ingestion/gdelt_ingestor.py:51` `http://data.gdeltproject.org`, `src/ingestion/gdelt_ingestor.py:82-85` `z.namelist()[0]` sans validation

**Problème :** URL en `http://` (pas `https`) -> MITM possible, injection CSV malveillant. `z.namelist()[0]` sans vérifier que c'est bien un CSV, sans limite de taille (`response.content` peut être 500Mo si GDELT renvoie une erreur HTML). `pd.read_csv(..., on_bad_lines="skip")` masque les lignes malformées.

**Impact :** 🟡 MOYEN (OSINT local) mais mauvaise hygiène. `zipfile.ZipFile(io.BytesIO(response.content))` avec `response.content` non limité est un vecteur zip-bomb (faible mais réel).

**Fix :**

```python
url = f"https://data.gdeltproject.org/gdeltv2/{timestamp}.export.CSV.zip"
resp = requests.get(url, timeout=30, stream=True)
resp.raise_for_status()
if int(resp.headers.get("Content-Length", 0)) > 10_000_000:
    raise ValueError("GDELT file too large")
# + vérifier content-type, limiter la taille décompressée
```

---

### 🟠 I5 — `storage/data_store.py` : bugs de parsing, `load_latest_global` fragile, `save_flights` suffix incohérent

**Localisation :** `src/storage/data_store.py:46-48`, `src/storage/data_store.py:115-123`, `src/storage/data_store.py:127-128`

*   `filepath = DATA_DIR / f"flights_{now}_{suffix_}.csv"` avec `suffix_ = f"_{suffix}"` -> si `suffix="EU_W"` donne `flights_2026-03-11_17-14-01__EU_W.csv` (double underscore) alors que `load_latest_global` split sur `"__"` — fonctionne par hasard mais incohérent avec les fichiers sans suffixe `flights_2026-03-03_19-38-26.csv` qui n'ont pas de `__`.
*   `load_latest_global` fait `f.stem.split("__")` et prend `parts[-1]` comme code région — si un fichier futur contient `__` dans le timestamp, casse.
*   `pd.read_csv(filepath)` dans `load_latest_global:127` **sans** `parse_dates=["timestamp"]` alors que `save_flights` écrit `timestamp` en ISO — les comparaisons temporelles cassent ensuite.
*   `load_all_flights:96` fait `pd.concat(frames)` sans `verify_integrity` — si un CSV a une colonne manquante (ex: ancien snapshot), concat silencieux avec NaN.

---

### 🟠 I6 — Duplication massive de code : dashboard

**Localisation :** `src/visualization/dashboard.py:481-507` vs `src/visualization/dashboard.py:740-783` (deux `_build_metrics_banner`), `src/visualization/dashboard.py:390` vs `601` (deux `_build_map`), `src/api/server.py:25-53` vs `src/dashboard_main.py:15-28` (chargement données dupliqué)

**Problème :** `_build_metrics_banner` défini **deux fois** (ligne 481 et 740) — la seconde écrase la première silencieusement (Python autorise la redéfinition). La première prend 2 args, la seconde 3 — selon l'ordre d'import, bug latent. `_build_map_fragment` (390) jamais utilisée (morte). `_build_world_map` (601) duplique 80% de `map_viewer.build_flight_map`.

**Impact :** Maintenance cauchemardesque, modification d'une fonction sans voir l'autre.

**Fix :** Supprimer `_build_map_fragment`, fusionner `map_viewer` et `_build_world_map`, garder une seule `build_metrics_banner`.

---

### 🟠 I7 — `collector.py` : `signal` + `time.sleep` bloquant + pas de back-pressure sur OpenSky rate-limit

**Localisation :** `src/collector.py:14-18`, `src/collector.py:50-82`, `src/ingestion/global_ingestor.py:17`

**Problème :** `signal.signal(SIGINT, _handle_exit)` avec `sys.exit(0)` dans le handler est dangereux dans un thread (et `time.sleep(interval)` bloquant). `INTER_REGION_DELAY = 6s` pour 12 régions = 72s de sleep séquentiel — si OpenSky rate-limite (429), le code ne le gère pas (`response.raise_for_status()` lève, mais `global_ingestor.py:75` l'avale et continue). Pas de retry, pas d'exponential backoff, pas de respect du header `Retry-After`.

**Fix :** Utiliser `tenacity` ou `backoff`, et `requests.Session` avec `Retry`.

---

### 🟠 I8 — Typage incomplet et `mypy` inutilisable

**Localisation :** tous les fichiers

*   `def load_config(...) -> dict` au lieu de `dict[str, Any]` / `TypedDict`
*   `def fetch_flights(...) -> list[ADSBMessage]` OK mais `_parse_state(state: list, ...)` -> `list` non paramétré
*   `src/agent/llm_analyst.py:2` `import ollama` sans stub, `src/api/server.py:11` `load_flights` retourne `DataFrame` sans préciser les colonnes
*   `on_ground: bool` dans `ADSBMessage` mais OpenSky renvoie `bool` parfois `0/1` — pas de coercition

Aucun `py.typed`, aucun `mypy.ini`.

---

## 5. Dette technique et améliorations

| Priorité | Problème | Impact | Effort | Recommandation |
|---|---|---|---|---|
| 🔴 | Pas de `pyproject.toml` / `.gitignore` / `requirements` | Build cassé, venv incohérent | 2h | Créer `pyproject.toml` + `.gitignore` + `pip-tools`, supprimer `venv` du repo |
| 🔴 | Chemins relatifs `Path("data/...")` | Crash selon `cwd` | 3h | Centraliser `PROJECT_ROOT` dans `src/utils/paths.py` et migrer tous les accès |
| 🔴 | Config dupliquée + bbox fausses | Résultats OSINT faux silencieusement | 2h | Unifier `config/settings.yaml` + validation `pydantic` + tests bbox |
| 🟠 | `except Exception` + `print` partout | Erreurs silencieuses, debug impossible | 4h | Remplacer par `logging` structuré + exceptions métier + `raise` ciblé |
| 🟠 | API Flask `CORS(*)` + `0.0.0.0` + pas d'auth | Faille sécurité | 3h | Restreindre CORS, ajouter `MAX_CONTENT_LENGTH`, rate-limit, auth optionnelle |
| 🟠 | `__pycache__` + `data/*.csv` + `venv` dans `git` | Repo pollué (60+ CSV ~ Mo) | 1h | `git rm --cached`, ajouter `.gitignore`, utiliser DVC ou `data/` git-ignored |
| 🟠 | Duplication `dashboard.py` (2x metrics) | Bugs latents, maintenance | 3h | Fusionner `map_viewer`/`dashboard`, supprimer code mort |
| 🟠 | `sys.path.insert` hacks | Imports fragiles | 2h | Passer en package installable (`pip install -e .`) |
| 🟡 | `helpers.py` vide, `regions.py` sans tests | Code mort | 30min | Supprimer `helpers.py` ou y déplacer `haversine`, ajouter tests `regions` |
| 🟡 | `iterrows()` + `pd.concat` en boucle | Perf O(n²) sur gros volumes | 2h | Vectoriser, utiliser `pd.concat` une fois, list-comprehension + `DataFrame(records)` |
| 🟡 | GDELT `http://` + `on_bad_lines="skip"` | Intégrité données | 1h | Passer en `https`, logger les lignes skippées, valider checksum |
| 🟡 | Pas de `logging`, que des `print` | Pas d'observabilité | 2h | `import logging; logger = logging.getLogger(__name__)` partout |
| 🟡 | 7 `*_main.py` sans CLI unifiée | UX confuse | 3h | Unifier avec `click`/`typer` : `geopol collect --zone france`, `geopol dashboard` |
| 🟢 | `lat_min/lon_min` inversés dans YAML | Confusion sémantique | 30min | Renommer en `bbox: [lon_min, lat_min, lon_max, lat_max]` ou valider |
| 🟢 | `dashboard.py` CSS inline 300 lignes | Maintenabilité front | 4h | Extraire `templates/dashboard.html` + `static/style.css` |
| 🟢 | Pas de `pre-commit` (ruff/black/mypy) | Dérive qualité | 1h | Ajouter `ruff`, `black`, `mypy --strict` en pre-commit |

---

## 6. Analyse architecturale

### Ce qui fonctionne

*   Découpage `ingestion / analysis / visualization / storage / agent / api` — bonne intention de séparation.
*   `Region` comme valeur d'objet du domaine — évite les tuples magiques.
*   Pipeline `fetch -> save -> load -> timeseries -> anomalies/correlations` clair pour un POC.

### Ce qui pose problème

```
Actuel (réel) :

project/
├── config/settings.yaml        # dupliqué
├── src/
│   ├── config/settings.yaml    # dupliqué, valeurs différentes
│   ├── main.py                 # entry 1 — France hardcodée
│   ├── collector.py            # entry 2 — boucle infinie, charge YAML
│   ├── gdelt_main.py           # entry 3 — hardcode bbox différente
│   ├── global_main.py          # entry 4 — toutes régions
│   ├── correlation_main.py     # entry 5 — hardcode bbox fausse
│   ├── dashboard_main.py       # entry 6 — lance Flask via subprocess
│   ├── timeseries_main.py      # entry 7 — série temporelle
│   ├── ingestion/              # dépend de storage + models + utils
│   ├── storage/                # dépend de models (OK) mais chemin relatif
│   ├── analysis/               # dépend de ingestion (gdelt) — inversion
│   ├── visualization/          # dépend de utils.regions + folium/plotly
│   ├── api/server.py           # dépend de tout (storage, analysis, agent)
│   ├── agent/                  # dépend de storage/analysis
│   ├── utils/                  # config_loader + regions + helpers vide
│   ├── data/raw/*.csv          # 60+ fichiers versionnés — ne devrait pas
│   └── models/adsb_message.py
├── tests/                      # 3 fichiers vides
└── venv/                       # 150Mo commité (partiellement)
```

**Problèmes structurels :**

1.  **Couplage circulaire latent :** `analysis/gdelt_correlator.py` importe `ingestion/gdelt_ingestor.py` (analyse dépend d'ingestion = inversion). `api/server.py` importe `agent`, `analysis`, `storage` — devient god-module.
2.  **Aucune abstraction I/O :** `requests.get` appelé directement dans `adsb_ingestor`, `gdelt_ingestor`. Impossible à mocker sans patcher `requests`.
3.  **Storage = CSV uniquement :** Pas d'interface `DataStore` — changer pour SQLite/Parquet implique de toucher 8 fichiers.
4.  **Pas de config injectée :** Chaque `*_main.py` hardcode ses `LAT_MIN/LON_MIN` ou lit le YAML avec un chemin différent.
5.  **7 points d'entrée sans CLI :** L'utilisateur doit deviner `python src/main.py` vs `python -m src.collector` vs `python src/dashboard_main.py`.
6.  **Frontend couplé au backend :** `dashboard.py` génère du HTML avec CSS/JS inline 300 lignes — impossible à tester visuellement sans lancer l'app.

### Architecture cible (proportionnée — pas de Clean Architecture over-engineered pour un POC)

Recommandation : **architecture modulaire légère** (pas besoin de DDD complet, mais isoler I/O et config).

```
geopol-traffic-intelligence/
├── pyproject.toml
├── README.md
├── .gitignore
├── config/
│   └── settings.yaml          # UNIQUE source de vérité
├── data/                      # git-ignored (sauf .gitkeep)
│   ├── raw/
│   ├── gdelt/
│   └── reports/
├── src/
│   └── geopol/                # package installable
│       ├── __init__.py
│       ├── config.py          # pydantic Settings, load_config() validé
│       ├── models/
│       │   ├── adsb.py        # ADSBMessage + validation
│       │   └── region.py      # Region (déplacé depuis utils)
│       ├── ingestion/
│       │   ├── adsb.py        # fetch_flights(client: HttpClient) — injecté
│       │   ├── gdelt.py
│       │   └── global_collector.py
│       ├── storage/
│       │   ├── protocol.py    # Protocol DataStore
│       │   └── csv_store.py   # implémentation CSV
│       ├── analysis/
│       │   ├── metrics.py     # compute_basic_metrics
│       │   ├── timeseries.py
│       │   └── correlator.py
│       ├── visualization/
│       │   ├── maps.py
│       │   └── plots.py
│       ├── api/
│       │   └── server.py      # Flask factory create_app(store, config)
│       ├── agent/
│       │   └── llm.py
│       └── cli.py             # typer: geopol collect / dashboard / correlate
├── tests/
│   ├── test_adsb_ingestor.py
│   ├── test_timeseries.py
│   └── conftest.py            # fixtures DataFrame
└── templates/
    └── dashboard.html
```

**Principes :**
*   Injection de dépendances : `fetch_flights(client: requests.Session)` au lieu d'import global.
*   `DataStore` Protocol pour pouvoir swapper CSV -> Parquet/SQLite.
*   Une seule CLI `geopol` (Typer/Click) remplace les 7 mains.
*   `create_app(config, store)` factory pour tester l'API sans filesystem.

---

## 7. Plan d'action priorisé

### Phase 1 — Urgent (avant toute démo externe, 1-2 jours)

1.  **Créer `pyproject.toml` + `.gitignore`** et `git rm --cached venv __pycache__ data/raw/*.csv` — sinon le repo est inutilisable par un tiers.
2.  **Centraliser `PROJECT_ROOT` et corriger tous les `Path("data/...")`** — sinon chaque lancement crash.
3.  **Unifier `config/settings.yaml`** (supprimer `src/config/settings.yaml`), corriger les bbox France/MO, et faire lire `correlation_main.py`/`gdelt_main.py` depuis ce YAML (supprimer hardcodes).
4.  **Fix crash `compute_basic_metrics` sur DataFrame vide** (`iloc[0]`, `mean:.0f` sur NaN) + tests de régression.
5.  **Restreindre `CORS` et ajouter `MAX_CONTENT_LENGTH` sur `/api/ask`** — sinon faille immédiate.

### Phase 2 — Important (avant prod, 1 semaine)

6.  Remplacer `print` par `logging` + remplacer `except Exception: return DataFrame()` par logging + propagation.
7.  Passer GDELT en `https://` + valider taille ZIP + fixer `if avg_before is not None`.
8.  Supprimer duplication `dashboard.py` (2x `_build_metrics_banner`) et code mort `_build_map_fragment`.
9.  Créer `DataStore` Protocol + `CsvStore` injecté, supprimer `sys.path.insert` via `pip install -e .`.
10. Écrire les 3 suites de tests vides (au moins: `test_adsb_ingestor` avec `responses` mock, `test_timeseries` avec DataFrame fixture, `test_data_store` avec `tmp_path`).

### Phase 3 — Qualité (amélioration continue, 2-4 semaines)

11. Unifier les 7 mains en CLI `geopol` (Typer) + `create_app` factory.
12. Ajouter `ruff`/`mypy`/`pytest --cov` en CI + pre-commit.
13. Externaliser `templates/dashboard.html` + `static/`.
14. Implémenter `requests.Session` avec `Retry` + backoff pour OpenSky/GDELT.
15. Migrer stockage CSV -> Parquet (partitionné par date) pour perfs.

---

## 8. Quick Wins (ratio impact/effort maximal)

| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | `echo "__pycache__/\nvenv/\ndata/raw/\ndata/gdelt/\n*.html" > .gitignore && git rm -r --cached src/**/__pycache__ venv` | 5 min | Repo passe de 150Mo à <1Mo |
| 2 | Fix `correlator.py:45` `if avg_before and` → `if avg_before is not None and` (2 occurrences) | 2 min | Corrige faux négatifs de corrélation |
| 3 | Fix `air_traffic_analyser.py:40` garde `if df.empty: return ...` | 10 min | Évite crash collector en zone vide |
| 4 | `src/ingestion/gdelt_ingestor.py:51` `http://` → `https://` | 1 min | Supprime MITM |
| 5 | `src/api/server.py:20` `CORS(app)` → `CORS(app, origins=["http://localhost:5000"])` | 1 min | Ferme CORS wildcard |
| 6 | Supprimer `src/utils/helpers.py` vide + `src/visualization/dashboard.py:390-421` code mort | 5 min | -80 lignes de dette |
| 7 | Ajouter `timeout` + `Content-Length` check dans `gdelt_ingestor` | 15 min | Évite zip-bomb / OOM |
| 8 | `src/storage/data_store.py:127` ajouter `parse_dates=["timestamp"]` dans `load_latest_global` | 2 min | Fix comparaisons temporelles cassées |
| 9 | Créer `pyproject.toml` minimal (copier exemple C1) | 15 min | Rend le projet installable |
| 10 | Remplacer `except Exception: return DataFrame()` par `logger.warning` + `raise` ciblé | 20 min | Rend les échecs visibles |

---

## 9. Exemple de refactoring — le plus impactant : `storage/data_store.py` + chemins cassés

**Pourquoi :** C'est le module le plus critique (tous les autres en dépendent) et il est cassé à 4 endroits (chemin relatif, suffixe double-underscore, `parse_dates` manquant, pas de garde vide). Le fixer débloque `collector`, `global_main`, `dashboard`, `api`.

**Ce qui change :** Centralisation des chemins, interface testable, guards, typage.

### Code actuel (`src/storage/data_store.py:7,46-48,102-133` — extraits)

```python
# ❌ Chemin relatif — dépend du cwd
DATA_DIR = Path("data/raw")

def save_flights(messages: list[ADSBMessage], suffix: str = "") -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    suffix_ = f"_{suffix}" if suffix else ""
    filepath = DATA_DIR / f"flights_{now}_{suffix_}.csv"  # ❌ double underscore si suffix="__EU_W"
    df.to_csv(filepath, index=False)
    return filepath

def load_latest_global(data_dir: Path = DATA_DIR) -> dict[str, pd.DataFrame]:
    for f in sorted(data_dir.glob("flights_*_*.csv")):
        parts = f.stem.split("__")  # ❌ fragile si timestamp contient __
        if len(parts) < 2: continue
        code = parts[-1]
        region_files[code] = f
    for code, filepath in region_files.items():
        df = pd.read_csv(filepath)  # ❌ sans parse_dates -> timestamp = string
        if not df.empty:
            df["region"] = code
        result[code] = df
    return result
```

### Code recommandé

```python
# src/geopol/paths.py — SINGLE SOURCE OF TRUTH
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # geopol/ -> src/ -> root
DATA_ROOT = PROJECT_ROOT / "data"  # ou PROJECT_ROOT / "src" / "data" — CHOISIR UNE FOIS
DATA_RAW = DATA_ROOT / "raw"
DATA_GDELT = DATA_ROOT / "gdelt"
DATA_REPORTS = DATA_ROOT / "reports"

# src/geopol/storage/csv_store.py
from __future__ import annotations
import logging
import re
import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
from typing import Protocol
from geopol.models.adsb import ADSBMessage
from geopol.paths import DATA_RAW

logger = logging.getLogger(__name__)

# Pattern strict : flights_2026-03-11_17-14-01__EU_W.csv
_FLIGHT_RE = re.compile(r"^flights_(?P<ts>\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})(?:__(?P<code>[A-Z_]+))?\.csv$")

class DataStore(Protocol):
    def save(self, messages: list[ADSBMessage], region_code: str | None = None) -> Path: ...
    def load(self, path: Path) -> pd.DataFrame: ...

class CsvStore:
    def __init__(self, base_dir: Path = DATA_RAW) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save(self, messages: list[ADSBMessage], region_code: str | None = None) -> Path:
        if not messages:
            raise ValueError("save() called with empty messages")
        if region_code and not re.match(r"^[A-Z_]{2,10}$", region_code):
            raise ValueError(f"Invalid region_code: {region_code!r}")

        records = [
            {
                "icao24": m.icao24, "callsign": m.callsign,
                "origin_country": m.origin_country, "latitude": m.latitude,
                "longitude": m.longitude, "altitude": m.altitude,
                "velocity": m.velocity, "heading": m.heading,
                "on_ground": m.on_ground, "timestamp": m.timestamp,
            }
            for m in messages
        ]
        df = pd.DataFrame.from_records(records)
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
        suffix = f"__{region_code}" if region_code else ""
        path = self.base_dir / f"flights_{ts}{suffix}.csv"
        df.to_csv(path, index=False)
        logger.info("saved flights", extra={"count": len(df), "path": str(path)})
        return path

    def load(self, path: Path) -> pd.DataFrame:
        if not path.exists():
            raise FileNotFoundError(path)
        return pd.read_csv(path, parse_dates=["timestamp"])

    def load_all(self) -> pd.DataFrame:
        files = sorted(self.base_dir.glob("flights_*.csv"))
        if not files:
            raise FileNotFoundError(f"No flights CSV in {self.base_dir}")
        frames = [pd.read_csv(f, parse_dates=["timestamp"]) for f in files]
        combined = pd.concat(frames, ignore_index=True).sort_values("timestamp").reset_index(drop=True)
        logger.info("loaded all flights", extra={"files": len(files), "rows": len(combined)})
        return combined

    def load_latest_per_region(self) -> dict[str, pd.DataFrame]:
        latest: dict[str, Path] = {}
        for f in sorted(self.base_dir.glob("flights_*.csv")):
            m = _FLIGHT_RE.match(f.name)
            if not m or not m.group("code"):
                continue
            latest[m.group("code")] = f  # sorted => dernier écrase

        result: dict[str, pd.DataFrame] = {}
        for code, path in latest.items():
            df = pd.read_csv(path, parse_dates=["timestamp"])  # ✅ parse_dates
            if not df.empty:
                df["region"] = code
            result[code] = df
        return result
```

**Bénéfices :**
*   **Déterministe** : plus de `Path("data/raw")` relatif — `PROJECT_ROOT` est absolu.
*   **Testable** : `CsvStore(base_dir=tmp_path)` injectable dans `pytest` sans toucher le FS réel.
*   **Robuste** : validation `region_code`, regex stricte au lieu de `split("__")`, garde `empty`, `parse_dates` partout.
*   **Maintenable** : un seul endroit à modifier pour passer à Parquet/SQLite (implémenter `ParquetStore` avec même `Protocol`).

**Test d'exemple (à ajouter en Phase 2) :**

```python
# tests/test_csv_store.py
def test_save_and_load_latest_per_region(tmp_path):
    store = CsvStore(base_dir=tmp_path)
    msgs = [ADSBMessage(icao24="abc", callsign="AFR123", origin_country="France",
                        latitude=48.0, longitude=2.0, altitude=10000, velocity=250,
                        heading=90, on_ground=False, timestamp=datetime.now(timezone.utc))]
    p1 = store.save(msgs, region_code="EU_W")
    assert p1.name.endswith("__EU_W.csv")
    loaded = store.load(p1)
    assert len(loaded) == 1
    assert pd.api.types.is_datetime64_any_dtype(loaded["timestamp"])
```

---

### Conclusion

Le projet montre une **bonne intuition produit OSINT** et une capacité à assembler un POC complet (ingestion → analyse → viz → LLM). Mais l'ingénierie est **en dessous du seuil production** : pas d'env reproductible, chemins cassés, configs contradictoires, API non sécurisée, 0% de tests, dette de duplication.

**Recommandation :** Ne pas déployer. Appliquer la **Phase 1 (2 jours)** puis **Phase 2 (1 semaine)** ci-dessus. Le refactoring `storage` proposé est le levier le plus rentable — il débloque tout le reste.

> Questions ou priorisation différente ? Indique la cible (démo, prod, concours) et je réordonne le plan.


---

## User

Ok parfait, avec tous ce que tu m'as dit fais un plan professionnel et complet de toute les modifications à faire, hésite pas à être explicite (titre de la modification, le temps que ça va prendre, pourquoi la faire, on y gagne quoi à faire et un petite description de ce qu'il faut faire pour résoudre le problème) 

---

## Assistant (Plan · Muse Spark 1.2 Free · 115.7s)

_Thinking:_

Élaborant un plan professionnel complet et priorisé en français avec titres, délais, justifications, bénéfices et descriptions détaillées.

# Plan de Remédiation Professionnel — GeoPol Traffic Intelligence Engine

> **Version : 1.0 — 01/09/2026**
> **Auteur : Senior Python Engineer / Reviewer**
> **Périmètre : Passage de POC (2.5/10) à base production-ready (7.5/10+)**
> **Effort total estimé : 68h — 84h (9 à 11 jours-homme solo, 5 jours à 2 devs)**
> **Mode : READ-ONLY — Aucune modification exécutée, plan uniquement**

---

## 0. Lecture rapide — Que va faire ce plan ?

Le projet est fonctionnel en démo locale mais **in-déployable** : env non reproductible, chemins cassés selon le `cwd`, configs contradictoires donnant des résultats OSINT faux, API ouverte, 0% tests, 60+ CSV versionnés. Ce plan corrige **dans l'ordre qui débloque le plus vite** : d'abord rendre le projet installable et déterministe (Phase 0-1), puis le sécuriser et le rendre observable (Phase 2), puis refactorer l'architecture pour le rendre testable et maintenable (Phase 3-4).

**Philosophie :**
*   Aucun big-bang rewrite. Refactoring incrémental, chaque phase laisse le projet dans un état vert (`pytest` + `ruff` passent).
*   Une seule source de vérité pour chaque concern (un `pyproject.toml`, un `config/settings.yaml`, un `paths.py`).
*   Tout ce qui a été `print` devient `logging`, tout ce qui a été `except Exception: return DataFrame()` devient log + exception typée.

### Planning cible (solo)

| Phase | Intitulé | Effort | Cumul | État final |
|---|---|---|---|---|
| **0** | Hygiène & Quick Wins | 4h | 4h | Repo clonable, `.gitignore` propre |
| **1** | Fondations bloquantes | 16h | 20h | `pip install -e .` marche, plus de crash `cwd` |
| **2** | Sécurité & Robustesse | 14h | 34h | API non exploitable, plus de silences |
| **3** | Architecture & Dette | 18h | 52h | Code dédupliqué, package `geopol` |
| **4** | Tests & CI | 14h | 66h | 60%+ coverage, CI GitHub Actions |
| **5** | Docs & Release | 4h | 70h | README, CHANGELOG, release 0.1.0 |

> **Si équipe de 2 :** Phase 1 et 2 en parallèle possible → 5 jours calendaires.

---

## 1. Conventions du plan

Chaque fiche suit ce format :

| Champ | Contenu |
|---|---|
| **ID** | Identifiant unique `P<phase>-<num>` |
| **Titre** | Action explicite |
| **Priorité** | 🔴 Critique / 🟠 Important / 🟡 Amélioration / 🟢 Mineur |
| **Effort** | Heures solo (inclut code + test + doc) |
| **Dépendances** | Fiches préalables |
| **Pourquoi** | Cause racine |
| **Gains** | Bénéfices mesurables |
| **Description** | Étapes concrètes, fichiers touchés, commandes |
| **Critères d'acceptation** | Comment vérifier que c'est fait |

---

## PHASE 0 — HYGIÈNE & QUICK WINS (4h)

> **Objectif :** Rendre le repo clonable sans embarquer 150Mo de bruit. Effet immédiat, risque nul.

### P0-01 — Créer `.gitignore` + nettoyer le repo versionné

*   **Priorité :** 🔴 Critique | **Effort :** 1h | **Dépendances :** Aucune
*   **Pourquoi :** `venv/` (29 libs), `__pycache__/`, `*.pyc`, `data/raw/*.csv` (60+ fichiers), `data/maps/*.html` sont trackés. `pip freeze` montre un venv système pollué, pas l'env projet. Le prochain `git push` pousse 100Mo+.
*   **Gains :** Repo passe de ~150Mo à <1Mo, clone en 2s, plus de conflits binaires.
*   **Description :**
    1.  Créer `/.gitignore` racine :
        ```
        __pycache__/  *.pyc  *.pyo  .pytest_cache/  .mypy_cache/  .ruff_cache/
        venv/  .venv/  env/
        data/raw/*.csv  data/gdelt/*.csv  data/maps/*.html  data/reports/*.csv
        !data/.gitkeep  !data/raw/.gitkeep
        .env  .env.*
        ```
    2.  `git rm -r --cached venv src/**/__pycache__ src/**/__pycache__ -- 2>/dev/null; git rm --cached src/data/raw/*.csv src/data/gdelt/*.csv 2>/dev/null || true`
    3.  `touch data/.gitkeep data/raw/.gitkeep data/gdelt/.gitkeep data/maps/.gitkeep data/reports/.gitkeep && git add .gitignore data/**/.gitkeep`
    4.  Vérifier `git status` ne montre plus `venv`.
*   **Fichiers :** `+/.gitignore`, `data/**/.gitkeep`
*   **Acceptation :** `git ls-files | grep -E "venv|__pycache__|\.pyc"` vide, `du -sh .git` < 5Mo.

### P0-02 — Corriger 5 bugs silencieux à 1 ligne (sans refactor)

*   **Priorité :** 🔴 Critique | **Effort :** 1h | **Dépendances :** Aucune
*   **Pourquoi :** 5 bugs causent des résultats faux ou crashs mais se corrigent en 1 ligne chacun.
*   **Gains :** -50% de crashs en démo, corrélations redevenues correctes.
*   **Description :**
    1.  `src/analysis/correlator.py:45` et `:54` : `if avg_before and avg_after` → `if avg_before is not None and avg_after is not None and avg_before > 0` (2 occurrences).
    2.  `src/analysis/correlator.py:117` : Clamper `goldstein_weight = max(0.0, min(1.0, (10 - goldstein)/20))`.
    3.  `src/ingestion/gdelt_ingestor.py:51` : `http://` → `https://`.
    4.  `src/storage/data_store.py:127` : `pd.read_csv(filepath)` → `pd.read_csv(filepath, parse_dates=["timestamp"])` dans `load_latest_global`.
    5.  `src/api/server.py:20` : `CORS(app)` → `CORS(app, origins=["http://localhost:*", "http://127.0.0.1:*"])`.
*   **Fichiers :** `src/analysis/correlator.py:45,54,117`, `src/ingestion/gdelt_ingestor.py:51`, `src/storage/data_store.py:127`, `src/api/server.py:20`
*   **Acceptation :** `grep -n "if avg_before and" src/analysis/correlator.py` vide, `grep "http://data.gdelt"` vide.

### P0-03 — Supprimer code mort et duplication triviale

*   **Priorité :** 🟡 Amélioration | **Effort :** 1h | **Dépendances :** Aucune
*   **Pourquoi :** `src/utils/helpers.py` vide (0 octet), `src/visualization/dashboard.py:390-421` `_build_map_fragment` jamais appelée, `_build_metrics_banner` définie 2 fois (ligne 481 et 740 — la 2e écrase la 1re).
*   **Gains :** -120 lignes, -1 module fantôme, plus de risque d'éditer la mauvaise `_build_metrics_banner`.
*   **Description :**
    1.  `rm src/utils/helpers.py` + retirer `from utils.helpers import` si présent (grep).
    2.  Dans `dashboard.py` : supprimer `_build_map_fragment` (390-421), garder uniquement `_build_world_map`. Supprimer la première `_build_metrics_banner` (481-507), garder la seconde (740-783) qui gère `regional_data`.
    3.  `grep -r "helpers" src/ tests/` → 0 résultats.
*   **Acceptation :** `ls src/utils/helpers.py` échoue, `grep -c "def _build_metrics_banner" src/visualization/dashboard.py` == 1.

### P0-04 — Standardiser les imports cassés `interactive_shell`

*   **Priorité :** 🟠 Important | **Effort :** 0.5h | **Dépendances :** Aucune
*   **Pourquoi :** `src/agent/interactive_shell.py:13` fait `from llm_analyst import ask` → `ModuleNotFoundError` si lancé depuis racine. Double import `Path`.
*   **Gains :** `python src/agent/interactive_shell.py` ne crash plus.
*   **Description :** Remplacer par `from agent.llm_analyst import ask` + nettoyer imports (`import sys`/`Path` dupliqués). Idem vérifier `api/server.py` double `from pathlib import Path`.
*   **Acceptation :** `python -c "import ast; ast.parse(open('src/agent/interactive_shell.py').read())"` OK, `grep "from llm_analyst" src/` vide.

### P0-05 — Fix mineur `dashboard_main` subprocess fragile

*   **Priorité :** 🟡 Amélioration | **Effort :** 0.5h | **Dépendances :** P0-02
*   **Pourquoi :** `subprocess.Popen([sys.executable, "api/server.py"])` dépend du `cwd`, sans `cwd=`, sans check port occupé.
*   **Gains :** Plus de process fantôme.
*   **Description :** Ajouter `cwd=PROJECT_ROOT` et valider `output_name` via `re.match(r"^[a-z0-9_-]+$", output_name)` avant `Popen`. Logger le PID. À terme ce lancement sera supprimé (Phase 3 CLI).
*   **Acceptation :** `grep -n "subprocess.Popen" src/dashboard_main.py` montre `cwd=`.

---

## PHASE 1 — FONDATIONS BLOQUANTES (16h)

> **Objectif :** Le projet s'installe et s'exécute de façon déterministe depuis n'importe quel `cwd`. Sans cette phase, tout le reste est instable.

### P1-01 — Créer `pyproject.toml` et rendre le projet installable

*   **Priorité :** 🔴 Critique | **Effort :** 3h | **Dépendances :** P0-01
*   **Pourquoi :** Aucun fichier de dépendances. `venv` incomplet (manquent `folium`, `plotly`, `pyyaml`, `ollama`, `flask-cors`, `requests`). `sys.path.insert` hacks partout parce que le code n'est pas un package.
*   **Gains :** `pip install -e .` suffit pour tout installer, `pytest`/`mypy` fonctionnent, onboarding <2min, CI possible.
*   **Description détaillée :**
    1.  Créer `pyproject.toml` à la racine :
        ```toml
        [project]
        name = "geopol-traffic-intelligence"
        version = "0.1.0"
        description = "OSINT air traffic + GDELT correlation engine"
        requires-python = ">=3.11"
        dependencies = [
          "requests>=2.32", "pandas>=2.2", "numpy>=1.26",
          "pyyaml>=6.0", "folium>=0.15", "plotly>=5.22",
          "flask>=3.1", "flask-cors>=4.0", "ollama>=0.3",
        ]
        [project.optional-dependencies]
        dev = ["pytest>=8", "pytest-cov", "responses", "ruff", "mypy", "types-PyYAML"]

        [build-system]
        requires = ["setuptools>=68", "wheel"]
        build-backend = "setuptools.build_meta"

        [tool.setuptools.packages.find]
        where = ["src"]

        [tool.ruff]
        line-length = 100
        target-version = "py311"

        [tool.mypy]
        python_version = "3.11"
        strict = false
        ignore_missing_imports = true

        [tool.pytest.ini_options]
        testpaths = ["tests"]
        ```
    2.  `rm -rf venv && python -m venv venv && venv/bin/pip install -e ".[dev]"`
    3.  Vérifier `venv/bin/pip list | grep -E "folium|plotly|yaml|ollama"` non vide.
    4.  Ajouter `venv/` au `.gitignore` si pas fait.
*   **Fichiers :** `+/pyproject.toml`, `venv/` régénéré (non versionné)
*   **Acceptation :** `venv/bin/pip install -e .` sans erreur, `venv/bin/python -c "import folium, plotly, yaml, ollama, flask_cors"` OK, `venv/bin/pytest --collect-only` 0 erreur.

### P1-02 — Centraliser les chemins filesystem (`paths.py`) et corriger tous les `Path("data/...")`

*   **Priorité :** 🔴 Critique | **Effort :** 4h | **Dépendances :** P1-01
*   **Pourquoi :** 9 fichiers utilisent `Path("data/raw")` relatif → crash selon `cwd`. `api/server.py:31` bricole `_PROJECT_ROOT` différemment de `storage/data_store.py`. Données réelles dans `src/data/raw` mais code pointe vers `data/raw`.
*   **Gains :** Plus de `FileNotFoundError` aléatoire, un seul endroit à changer pour migrer vers `/data` ou S3.
*   **Description détaillée :**
    1.  **Décision à trancher (bloquant) :** `data/` à la racine **OU** `src/data/` ? Recommandation : `data/` à la racine (standard). Si `src/data/` conservé, l'indiquer explicitement. Pour ce plan : on migre vers `data/` racine (déplacer `src/data/*` → `data/*` via `git mv`).
    2.  Créer `src/geopol/paths.py` (après renommage `src` → `src/geopol` en P3-01, en attendant `src/utils/paths.py`) :
        ```python
        from pathlib import Path
        PROJECT_ROOT = Path(__file__).resolve().parents[2]  # src/utils -> src -> root
        DATA_ROOT = PROJECT_ROOT / "data"
        DATA_RAW = DATA_ROOT / "raw"
        DATA_GDELT = DATA_ROOT / "gdelt"
        DATA_REPORTS = DATA_ROOT / "reports"
        MAPS_DIR = DATA_ROOT / "maps"
        CONFIG_PATH = PROJECT_ROOT / "config" / "settings.yaml"
        ```
    3.  Remplacer dans **9 fichiers** :
        *   `src/storage/data_store.py:7` `DATA_DIR = Path("data/raw")` → `from utils.paths import DATA_RAW`
        *   `src/ingestion/gdelt_ingestor.py:33` `GDELT_DATA_DIR = Path("data/gdelt")` → `DATA_GDELT`
        *   `src/visualization/dashboard.py:11`, `map_viewer.py:6`, `timeseries_plotter.py:6` → `MAPS_DIR`
        *   `src/api/server.py:31-35` → `from utils.paths import DATA_RAW, DATA_REPORTS`
        *   `src/collector.py:21` défaut `config/settings.yaml` → `CONFIG_PATH`
        *   `src/dashboard_main.py:16,30,45` → `DATA_RAW`, `DATA_REPORTS`
        *   `src/correlation_main.py:18`, `timeseries_main.py:13`, `global_main.py:45`
    4.  `grep -rn 'Path("data' src/ --include="*.py"` doit être vide après.
    5.  Tester : `cd /tmp && venv/bin/python /path/to/project/src/main.py` (cwd différent) ne lève plus `FileNotFoundError`.
*   **Fichiers :** `+src/utils/paths.py`, 9 fichiers modifiés, `git mv src/data/* data/` si migration
*   **Acceptation :** `grep -rn 'Path("data/' src/` == 0, lancement depuis `/tmp` OK, `pytest` vert.

### P1-03 — Unifier et valider la configuration (`config/settings.yaml`)

*   **Priorité :** 🔴 Critique | **Effort :** 3h | **Dépendances :** P1-02
*   **Pourquoi :** 2 fichiers contradictoires (`config/settings.yaml` = "France" avec bbox `2,45,22,83` fausse, `src/config/settings.yaml` = "Moyen Orient" `2,5,62,83`), + 3 `*_main.py` hardcodent d'autres bbox (`main.py:12` correct, `correlation_main.py:8` fausse, `gdelt_main.py:9` autre). Résultat OSINT faux silencieusement.
*   **Gains :** Une seule vérité, validation au démarrage, plus de bbox inversée.
*   **Description détaillée :**
    1.  Supprimer `src/config/settings.yaml` (garder uniquement `config/settings.yaml` racine).
    2.  Corriger `config/settings.yaml` :
        ```yaml
        zone:
          name: "France"
          lat_min: 41.0
          lon_min: -5.5
          lat_max: 51.5
          lon_max: 10.0
        collection:
          interval_seconds: 300  # 5min, pas 30s (sinon 288 snapshots/jour faux)
          max_snapshots: 288
        paths:
          raw_data: "data/raw"
          maps: "data/maps"
          reports: "data/reports"
        regions:  # optionnel : liste des régions actives
          enabled: ["EU_W", "EU_E", "RU", "ME", "AS_S", "AS_E", "NA", "SA", "AF", "UKR", "TWN", "PG"]
        ```
    3.  Créer `src/utils/config.py` avec `pydantic` :
        ```python
        from pydantic import BaseModel, Field
        import yaml
        from pathlib import Path
        from utils.paths import CONFIG_PATH
        class Zone(BaseModel):
            name: str; lat_min: float = Field(ge=-90, le=90)
            lon_min: float = Field(ge=-180, le=180)
            lat_max: float; lon_max: float
            def model_post_init(self, __ctx): assert self.lat_min < self.lat_max and self.lon_min < self.lon_max
        class Settings(BaseModel):
            zone: Zone; collection: dict; paths: dict
        def load_config(path: Path = CONFIG_PATH) -> Settings:
            return Settings(**yaml.safe_load(path.read_text()))
        ```
    4.  Refactor `src/utils/config_loader.py` pour déléguer à `config.py` (ou le remplacer).
    5.  Refactor `main.py`, `collector.py`, `correlation_main.py`, `gdelt_main.py` pour tous faire `config = load_config(); zone = config.zone` au lieu de hardcoder `LAT_MIN`.
*   **Fichiers :** `config/settings.yaml` (corriger), `-src/config/settings.yaml`, `+src/utils/config.py`, `src/utils/config_loader.py`, 4 `*_main.py`
*   **Acceptation :** `ls src/config/settings.yaml` échoue, `load_config()` lève si bbox inversée, `grep -rn "LAT_MIN.*=" src/*.py` vide (plus de hardcode).

### P1-04 — Corriger `storage/data_store.py` (4 bugs internes)

*   **Priorité :** 🔴 Critique | **Effort :** 3h | **Dépendances :** P1-02, P1-03
*   **Pourquoi :** Module central, 4 bugs : suffixe `__` incohérent, `split("__")` fragile, `parse_dates` manquant, `load_all_flights` sans `verify_integrity`.
*   **Gains :** Dashboard/API ne renvoient plus des timestamps string, plus de collision de noms de fichiers.
*   **Description détaillée :**
    1.  Introduire regex stricte `FLIGHT_RE = re.compile(r"^flights_(?P<ts>\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})(?:__(?P<code>[A-Z_]+))?\.csv$")` au lieu de `split("__")`.
    2.  `save_flights(messages, region_code: str|None)` : valider `region_code` via `re.match(r"^[A-Z_]{2,10}$")`, construire `suffix = f"__{region_code}" if region_code else ""` (pas de double `_`).
    3.  `load_latest_global` : `pd.read_csv(..., parse_dates=["timestamp"])` + utiliser regex pour extraire `code`.
    4.  `load_all_flights` : logger si colonnes manquantes, `pd.concat(..., verify_integrity=False)` mais vérifier `set(df.columns)` identique.
    5.  Ajouter garde `if not messages: raise ValueError` dans `save_flights`.
*   **Fichiers :** `src/storage/data_store.py`
*   **Acceptation :** `save_flights(msgs, suffix="EU_W")` crée `__EU_W.csv` (pas `___EU_W`), `load_latest_global` retourne `timestamp` dtype `datetime64[ns]`.

### P1-05 — Corriger crash `compute_basic_metrics` sur DataFrame vide

*   **Priorité :** 🔴 Critique | **Effort :** 2h | **Dépendances :** P1-04
*   **Pourquoi :** `df["timestamp"].iloc[0]` lève `IndexError` si df vide, `f"{mean:.0f}"` lève `TypeError` si `mean` est `NaN`.
*   **Gains :** Collector ne crash plus en zone vide ou rate-limit.
*   **Description détaillée :**
    1.  Dans `src/analysis/air_traffic_analyser.py:5` :
        ```python
        def compute_basic_metrics(df: pd.DataFrame) -> dict:
            if df.empty:
                return {"total_aircraft":0, "in_flight":0, "on_ground":0, "ground_ratio":0,
                        "altitude_mean":None, "altitude_median":None, "altitude_std":None,
                        "velocity_mean":None, "velocity_median":None,
                        "unique_countries":0, "unique_flights":0, "captured_at":None}
            # puis coercition : alt_mean = float(df["altitude"].mean()) if pd.notna(...) else None
        ```
    2.  Dans `collector.py:66-72` : tester `if metrics["altitude_mean"] is not None` avant `:.0f`.
    3.  Dans `global_ingestor.py:116` : `round(float(x),0) if pd.notna(x) else 0`.
    4.  Ajouter test `test_compute_basic_metrics_empty`.
*   **Fichiers :** `src/analysis/air_traffic_analyser.py`, `src/collector.py`, `src/ingestion/global_ingestor.py`
*   **Acceptation :** `compute_basic_metrics(pd.DataFrame())` ne lève pas, `collector` affiche `0 avions` au lieu de crash.

### P1-06 — Supprimer `sys.path.insert` hacks et passer en package

*   **Priorité :** 🟠 Important | **Effort :** 1h | **Dépendances :** P1-01
*   **Pourquoi :** `sys.path.insert(0, ...)` dans 3 fichiers rend les imports non déterministes.
*   **Gains :** `python -m geopol.collector` marche, IDE/pyright OK.
*   **Description :** Après `pip install -e .`, remplacer `sys.path.insert` + `from ingestion...` par `from geopol.ingestion...` (ou `from src.ingestion...` si pas encore renommé). Vérifier `interactive_shell.py` utilise `from geopol.agent...`.
*   **Acceptation :** `grep -rn "sys.path.insert" src/` vide, `python -m geopol.collector --help` OK.

---

## PHASE 2 — SÉCURITÉ & ROBUSTESSE (14h)

> **Objectif :** Fermer les failles exploitables et rendre les pannes visibles.

### P2-01 — Sécuriser l'API Flask (`server.py`)

*   **Priorité :** 🟠 Important | **Effort :** 4h | **Dépendances :** P1-02
*   **Pourquoi :** `CORS(*)` + `host=0.0.0.0` + `/api/ask` sans validation = prompt injection, DoS, CORS exfiltration.
*   **Gains :** API déployable sur LAN sans risque, conformité OWASP.
*   **Description détaillée :**
    1.  `CORS(app, origins=["http://localhost:5000", "http://127.0.0.1:5000"], supports_credentials=False)` + ajouter `CORS_ALLOWED_ORIGINS` dans `config/settings.yaml`.
    2.  `app.config["MAX_CONTENT_LENGTH"] = 2*1024` (2KB).
    3.  Dans `/api/ask` :
        ```python
        body = request.get_json(force=True, silent=False)
        if not body or "question" not in body: return jsonify(error="..."), 400
        question = str(body["question"]).strip()[:500]
        if len(question) < 3: return jsonify(error="Question trop courte"), 400
        # délimiter le prompt pour limiter l'injection
        full_prompt = f"<DATA>{context}</DATA>\n<QUESTION>{question}</QUESTION>"
        ```
    4.  Ajouter `flask-limiter` : `Limiter(app, default_limits=["30/minute"])` + `@limiter.limit("5/minute")` sur `/api/ask`.
    5.  Passer `host="127.0.0.1"` par défaut, `0.0.0.0` uniquement si `ENV=prod` + auth.
    6.  Ajouter `app.config["JSON_SORT_KEYS"] = False` et headers `X-Content-Type-Options: nosniff`.
*   **Fichiers :** `src/api/server.py`, `config/settings.yaml`, `pyproject.toml` (+ `flask-limiter`)
*   **Acceptation :** `curl -H "Origin: https://evil.com" http://localhost:5000/api/status` → CORS bloqué, `curl -X POST /api/ask -d '{"question":"a"*5000}'` → 413.

### P2-02 — Sécuriser GDELT ingestion (HTTPS + validation ZIP)

*   **Priorité :** 🟡 Moyen (🟠 si prod) | **Effort :** 2h | **Dépendances :** P0-02
*   **Pourquoi :** `http://` MITM, `response.content` non limité, `z.namelist()[0]` sans validation.
*   **Gains :** Plus de MITM, plus de zip-bomb silencieuse.
*   **Description :**
    1.  `GDELT_URL = "https://data.gdeltproject.org/gdeltv2/{ts}.export.CSV.zip"`.
    2.  `requests.get(..., stream=True, timeout=30)` + vérifier `Content-Length` < 10Mo, `Content-Type` contient `zip`.
    3.  `if len(response.content) > 10_000_000: raise ValueError("GDELT file too large")`.
    4.  `with zipfile.ZipFile(BytesIO(content)) as z: if len(z.namelist()) != 1: raise ValueError; info = z.getinfo(namelist[0]); if info.file_size > 50_000_000: raise`.
    5.  Logger `on_bad_lines` count au lieu de `skip` silencieux.
*   **Fichiers :** `src/ingestion/gdelt_ingestor.py`
*   **Acceptation :** `grep "http://data.gdelt" src/` vide, test avec fichier >10Mo lève.

### P2-03 — Remplacer `print` par `logging` structuré

*   **Priorité :** 🟠 Important | **Effort :** 3h | **Dépendances :** Aucune
*   **Pourquoi :** 40+ `print("[Collector] ...")` partout → pas de niveau, pas de timestamp, pas de redirection, invisible en prod.
*   **Gains :** Logs filtrables (`INFO`/`WARNING`), redirigeables vers fichier/Sentry, debuggable.
*   **Description :**
    1.  Créer `src/utils/logging.py` :
        ```python
        import logging
        def setup_logging(level="INFO"):
            logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        ```
    2.  Dans chaque module : `import logging; logger = logging.getLogger(__name__)` + remplacer `print(f"[OpenSky] ...")` par `logger.info("OpenSky fetch", extra={"bbox": ...})`, `print(f"[GDELT] ⚠")` par `logger.warning(...)`.
    3.  Appeler `setup_logging()` dans chaque `main()` et `api/server.py`.
    4.  Conserver 1-2 `print` pour le rapport terminal (`print_report`) mais logger le reste.
*   **Fichiers :** `+src/utils/logging.py`, tous les `src/**/*.py` (40 remplacements)
*   **Acceptation :** `grep -rn 'print(f"\[' src/ --include="*.py" | wc -l` < 5, `grep -rn "logger\." src/ | wc -l` > 20.

### P2-04 — Corriger la gestion d'erreurs (exceptions typées, plus de `except Exception: pass`)

*   **Priorité :** 🟠 Important | **Effort :** 3h | **Dépendances :** P2-03
*   **Pourquoi :** `except Exception: return DataFrame()` masque les pannes, `collector.py` avale tout et boucle infiniment sans alerte.
*   **Gains :** Pannes visibles, retry possible, debug en 1 log au lieu de 1h.
*   **Description :**
    1.  Créer `src/utils/exceptions.py` :
        ```python
        class GeopolError(Exception): pass
        class FetchError(GeopolError): pass
        class ParseError(GeopolError): pass
        ```
    2.  Dans `collector.py` : catcher `requests.RequestException` et `ParseError` séparément, logger `exc_info=True` pour les 500, compter `consecutive_failures` et `break` après 5 échecs.
    3.  Dans `gdelt_ingestor.py` : `except requests.HTTPError` → `logger.warning` + `return DataFrame()`, `except (BadZipFile, ParserError)` → `logger.error` + `raise ParseError`.
    4.  Dans `global_ingestor.py` : idem, ne plus `except Exception` générique.
    5.  Dans `api/server.py` : wrapper `try/except GeopolError` avec `jsonify(error=...) , 500`.
*   **Fichiers :** `+src/utils/exceptions.py`, `src/collector.py`, `src/ingestion/*.py`, `src/api/server.py`
*   **Acceptation :** `grep -rn "except Exception" src/ --include="*.py"` vide ou justifié avec `logger.error`, `grep -rn "return pd.DataFrame()" src/` < 3.

### P2-05 — Ajouter retry/backoff pour OpenSky et GDELT

*   **Priorité :** 🟡 Amélioration | **Effort :** 2h | **Dépendances :** P2-04
*   **Pourquoi :** OpenSky rate-limite (429) sans `Retry-After`, GDELT 404 fréquent (fichier pas encore publié). Actuellement 1 échec = snapshot perdu.
*   **Gains :** +30% de snapshots réussis, moins de trous dans la série temporelle.
*   **Description :**
    1.  Ajouter `tenacity` à `pyproject.toml`.
    2.  Dans `adsb_ingestor.py` :
        ```python
        from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
        @retry(stop=stop_after_attempt(3), wait=wait_exponential(2,10), retry=retry_if_exception_type(requests.RequestException))
        def fetch_flights(...): ...
        ```
    3.  Gérer `429` : `if response.status_code == 429: wait = int(response.headers.get("Retry-After", 10)); time.sleep(wait); raise`.
    4.  Utiliser `requests.Session` avec `HTTPAdapter(max_retries=3)` au lieu de `requests.get` nu.
*   **Fichiers :** `src/ingestion/adsb_ingestor.py`, `src/ingestion/gdelt_ingestor.py`, `pyproject.toml`
*   **Acceptation :** Test mock 429 → retry 3 fois avec backoff, `grep "tenacity" src/` non vide.

---

## PHASE 3 — ARCHITECTURE & DETTE (18h)

> **Objectif :** Dédupliquer, injecter les dépendances, rendre le code testable.

### P3-01 — Transformer `src/` en package `src/geopol/` (renommage)

*   **Priorité :** 🟠 Important | **Effort :** 3h | **Dépendances :** P1-01, P1-06
*   **Pourquoi :** `src/ingestion`, `src/api` ne sont pas un package installable (pas de `src/geopol/__init__.py`). `PYTHONPATH=src` fragile.
*   **Gains :** Imports absolus `from geopol.ingestion.adsb import ...`, `pip install -e .` propre, `mypy` résout les types.
*   **Description :**
    1.  `mkdir -p src/geopol && git mv src/ingestion src/geopol/ && git mv src/analysis src/geopol/ && git mv src/storage src/geopol/ && git mv src/visualization src/geopol/ && git mv src/agent src/geopol/ && git mv src/api src/geopol/ && git mv src/models src/geopol/ && git mv src/utils src/geopol/`
    2.  `touch src/geopol/__init__.py` + chaque sous-package.
    3.  Mettre à jour `pyproject.toml` `[tool.setuptools.packages.find] where=["src"]`.
    4.  Remplacer tous les `from ingestion.` → `from geopol.ingestion.`, `from storage.` → `from geopol.storage.`, etc. (`sed -i` + vérif `grep`).
    5.  Vérifier `venv/bin/python -c "import geopol.ingestion.adsb_ingestor"` OK.
*   **Fichiers :** Toute l'arborescence `src/`
*   **Acceptation :** `ls src/geopol/ingestion/` existe, `grep -rn "from ingestion" src/` vide, `pytest` passe.

### P3-02 — Introduire `DataStore` Protocol et `CsvStore` injectable

*   **Priorité :** 🟠 Important | **Effort :** 4h | **Dépendances :** P1-04, P3-01
*   **Pourquoi :** `storage/data_store.py` est un module de fonctions avec état global `DATA_DIR`, impossible à mocker sans patcher le FS. Changer pour Parquet/SQLite = toucher 8 fichiers.
*   **Gains :** Testabilité (`tmp_path`), swappabilité (Parquet), SRP.
*   **Description :**
    1.  Créer `src/geopol/storage/protocol.py` :
        ```python
        from typing import Protocol
        from pathlib import Path
        import pandas as pd
        from geopol.models.adsb import ADSBMessage
        class DataStore(Protocol):
            def save(self, messages: list[ADSBMessage], region_code: str|None=None) -> Path: ...
            def load(self, path: Path) -> pd.DataFrame: ...
            def load_all(self) -> pd.DataFrame: ...
            def load_latest_per_region(self) -> dict[str, pd.DataFrame]: ...
        ```
    2.  Renommer `data_store.py` → `csv_store.py` et implémenter `class CsvStore(DataStore)` (code de P1-04).
    3.  Injecter `store: DataStore` dans `global_ingestor.fetch_global_snapshot`, `collector.run_collector`, `api/server.py:create_app(store)`.
    4.  `api/server.py` devient factory :
        ```python
        def create_app(store: DataStore = CsvStore()) -> Flask:
            app = Flask(__name__); app.config["store"] = store; ...
        ```
*   **Fichiers :** `+src/geopol/storage/protocol.py`, `~src/geopol/storage/csv_store.py`, `src/geopol/ingestion/global_ingestor.py`, `src/collector.py`, `src/geopol/api/server.py`
*   **Acceptation :** `mypy src/geopol/storage/` passe, `pytest` avec `CsvStore(tmp_path)` vert, `grep "DATA_DIR" src/geopol/storage/` vide.

### P3-03 — Dédupliquer `visualization/dashboard.py`

*   **Priorité :** 🟡 Amélioration | **Effort :** 4h | **Dépendances :** P0-03
*   **Pourquoi :** 2x `_build_metrics_banner`, 2x map logic, 783 lignes dans 1 fichier, CSS/JS inline 300 lignes.
*   **Gains :** -200 lignes, 1 seule source pour les métriques, maintenabilité front.
*   **Description :**
    1.  Fusionner `map_viewer.build_flight_map` et `dashboard._build_world_map` en `src/geopol/visualization/maps.py` avec `def build_map(df, regional_data=None, tiles="CartoDB dark_matter")`.
    2.  Garder une seule `_build_metrics_banner(df, ts, regional_data)` (celle à 3 args).
    3.  Extraire le HTML/CSS/JS inline vers `src/geopol/templates/dashboard.html` (Jinja2) + `src/geopol/static/style.css` + `app.js`. `build_dashboard` ne fait plus que `render_template`.
    4.  `dashboard.py` passe de 783 à ~200 lignes (orchestration uniquement).
*   **Fichiers :** `src/geopol/visualization/dashboard.py`, `+src/geopol/visualization/maps.py`, `+src/geopol/templates/dashboard.html`
*   **Acceptation :** `wc -l src/geopol/visualization/dashboard.py` < 250, `grep -c "def _build_metrics" src/geopol/visualization/dashboard.py` == 1.

### P3-04 — Unifier les 7 `*_main.py` en CLI unique (`Typer`)

*   **Priorité :** 🟡 Amélioration | **Effort :** 4h | **Dépendances :** P1-03, P3-01
*   **Pourquoi :** 7 entrypoints (`main.py`, `collector.py`, `global_main.py`, `gdelt_main.py`, `correlation_main.py`, `timeseries_main.py`, `dashboard_main.py`) avec chacun ses `LAT_MIN` hardcodés, pas de `--help`, pas de `--zone`.
*   **Gains :** UX `geopol collect --zone france --interval 300`, `geopol dashboard`, 1 seul binaire à documenter.
*   **Description :**
    1.  Ajouter `typer>=0.12` à `pyproject.toml`.
    2.  Créer `src/geopol/cli.py` :
        ```python
        import typer
        app = typer.Typer()
        @app.command()
        def collect(zone: str = "france", interval: int = 300, snapshots: int = 288): ...
        @app.command()
        def snapshot(regions: list[str] | None = None): ...  # ex-global_main
        @app.command()
        def correlate(zone: str = "france", window: int = 6): ...
        @app.command()
        def dashboard(port: int = 5000): ...
        @app.command()
        def timeseries(): ...
        if __name__ == "__main__": app()
        ```
    3.  Chaque commande lit `load_config()` et délègue aux fonctions existantes (pas de rewrite).
    4.  Ajouter `[project.scripts] geopol = "geopol.cli:app"` dans `pyproject.toml`.
    5.  Garder les anciens `*_main.py` comme shims `from geopol.cli import app; app()` pendant 1 version, puis déprécier.
*   **Fichiers :** `+src/geopol/cli.py`, `pyproject.toml`, 7 `*_main.py` (shims)
*   **Acceptation :** `geopol --help` liste 5 commandes, `geopol collect --help` montre `--zone`, `--interval`, chaque ancienne main redirige.

### P3-05 — Injecter `HttpClient` dans `adsb_ingestor` / `gdelt_ingestor`

*   **Priorité :** 🟡 Amélioration | **Effort :** 2h | **Dépendances :** P2-05
*   **Pourquoi :** `requests.get` direct → impossible à tester sans `responses` mock global, pas de session réutilisée (pas de keep-alive).
*   **Gains :** Tests unitaires sans réseau, perfs +10% (keep-alive), mock fin.
*   **Description :**
    1.  `def fetch_flights(..., client: requests.Session | None = None)` avec `client = client or requests.Session()`.
    2.  Idem `fetch_gdelt_events(..., client=None)`.
    3.  Dans `global_ingestor.fetch_global_snapshot`, créer une `Session` unique et la passer à chaque `fetch_flights`.
    4.  Tests : `client = Mock(); client.get.return_value = MockResponse; fetch_flights(..., client=client)`.
*   **Fichiers :** `src/geopol/ingestion/adsb_ingestor.py`, `src/geopol/ingestion/gdelt_ingestor.py`, `src/geopol/ingestion/global_ingestor.py`
*   **Acceptation :** `grep "requests\.get" src/geopol/ingestion/` vide (que `client.get`), tests mock sans `responses` possible.

### P3-06 — Nettoyer `api/server.py` cache et `load_data` (perf)

*   **Priorité :** 🟡 Amélioration | **Effort :** 1h | **Dépendances :** P1-02, P3-02
*   **Pourquoi :** `_load_data()` relit **tous** les CSV à chaque `GET /api/status` (60+ fichiers) → latence 1-2s, pas de TTL.
*   **Gains :** Latence API /status 1500ms → 50ms (cache).
*   **Description :**
    1.  Ajouter `cache_ttl = 30s` : `_cache["last_load"] = time.time()` et `if time.time() - last < 30: return`.
    2.  Ne plus faire `load_all_flights` dans `/api/status` (besoin seulement du dernier snapshot).
    3.  Utiliser `store.load_latest_per_region()` au lieu de `glob` manuel.
*   **Fichiers :** `src/geopol/api/server.py`
*   **Acceptation :** `ab -n 100 http://localhost:5000/api/status` p95 < 100ms.

---

## PHASE 4 — TESTS & CI (14h)

> **Objectif :** Passer de 0% à 60% coverage sur le cœur métier, CI qui bloque les régressions.

### P4-01 — Écrire les tests manquants critiques (3 fichiers vides)

*   **Priorité :** 🔴 Critique | **Effort :** 6h | **Dépendances :** P1-04, P1-05, P3-02
*   **Pourquoi :** `tests/test_*.py` = 3 fichiers vides. Aucune régression détectable. `compute_basic_metrics`, `build_timeseries`, `detect_anomalies`, `correlate_event_with_traffic` sont purs et testables en 10 lignes chacun.
*   **Gains :** 60% coverage sur `analysis/` + `storage/`, confiance pour refactorer.
*   **Description détaillée :**
    1.  `tests/conftest.py` : fixtures `df_sample` (10 avions, 2 au sol), `ts_sample` (5 snapshots), `tmp_store` (`CsvStore(tmp_path)`).
    2.  `tests/test_adsb_ingestor.py` (3 tests) :
        *   `test_fetch_flights_success` (mock `responses` ou `client` fake, 2 avions).
        *   `test_fetch_flights_empty_states` → `[]`.
        *   `test_parse_state_filters_no_position` → `None`.
    3.  `tests/test_air_traffic_analyzer.py` (4 tests) :
        *   `test_compute_basic_metrics_empty` → 0/None.
        *   `test_compute_basic_metrics_sample` → `total=10, in_flight=8`.
        *   `test_altitude_distribution` → 4 buckets.
        *   `test_country_breakdown_sorted`.
    4.  `tests/test_data_store.py` (4 tests) :
        *   `test_save_and_load_roundtrip(tmp_path)`.
        *   `test_load_all_flights(tmp_path)` (2 fichiers).
        *   `test_load_latest_per_region(tmp_path)` avec 2 régions.
        *   `test_suffix_validation`.
    5.  `tests/test_timeseries.py` (3 tests) : `test_build_timeseries`, `test_detect_anomalies_zscore`, `test_detect_anomalies_no_variance`.
    6.  `tests/test_correlator.py` (3 tests) : `test_correlate_traffic_delta`, `test_compute_signal_clamped`, `test_avg_before_zero_not_falsy`.
    7.  Lancer `venv/bin/pytest --cov=geopol --cov-report=term-missing` → >60%.
*   **Fichiers :** `tests/conftest.py`, `tests/test_*.py` (5 fichiers)
*   **Acceptation :** `pytest -v` 17 tests verts, `pytest --cov` >60% sur `geopol/analysis` et `geopol/storage`.

### P4-02 — Ajouter `ruff` + `mypy` + `pytest` en pre-commit et CI

*   **Priorité :** 🟠 Important | **Effort :** 3h | **Dépendances :** P1-01
*   **Pourquoi :** Pas de lint, pas de type-check, pas de CI → dérive qualité garantie.
*   **Gains :** Chaque PR bloquée si `ruff`/`mypy`/`pytest` rouge.
*   **Description :**
    1.  Créer `.pre-commit-config.yaml` :
        ```yaml
        repos:
          - repo: https://github.com/astral-sh/ruff-pre-commit
            hooks: [{id: ruff}, {id: ruff-format}]
          - repo: https://github.com/pre-commit/mirrors-mypy
            hooks: [{id: mypy, args: [--ignore-missing-imports]}]
        ```
    2.  `pre-commit install`.
    3.  Créer `.github/workflows/ci.yml` :
        ```yaml
        on: [push, pull_request]
        jobs:
          ci:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with: {python-version: "3.11"}
              - run: pip install -e ".[dev]"
              - run: ruff check src/ tests/
              - run: mypy src/
              - run: pytest --cov=geopol --cov-report=term --cov-fail-under=60
        ```
*   **Fichiers :** `+.pre-commit-config.yaml`, `+.github/workflows/ci.yml`
*   **Acceptation :** `pre-commit run --all-files` vert, `gh workflow view` OK, PR avec `ruff` error bloquée.

### P4-03 — Ajouter tests d'intégration API (`test_api`)

*   **Priorité :** 🟡 Amélioration | **Effort :** 3h | **Dépendances :** P2-01, P3-02
*   **Pourquoi :** API non testée, `/_load_data` dépend du FS réel.
*   **Gains :** Détecte les régressions `CORS`, `MAX_CONTENT_LENGTH`, `create_app`.
*   **Description :**
    1.  `tests/test_api.py` avec `create_app(store=FakeStore)` + `client = app.test_client()`.
    2.  Tests : `test_status_no_data` → 404, `test_status_ok` → 200 + keys, `test_ask_empty_question` → 400, `test_ask_rate_limited` (si limiter mocké).
    3.  Utiliser `pytest-flask` ou `app.test_client()` natif.
*   **Fichiers :** `+tests/test_api.py`, `+tests/fakes.py` (FakeStore)
*   **Acceptation :** `pytest tests/test_api.py -v` 4 tests verts.

### P4-04 — Mesurer et documenter la couverture restante

*   **Priorité :** 🟢 Mineur | **Effort :** 2h | **Dépendances :** P4-01
*   **Pourquoi :** Savoir où on en est, prioriser la suite.
*   **Gains :** Roadmap tests claire.
*   **Description :** `pytest --cov --cov-report=html` + ouvrir `htmlcov/index.html`, lister les modules <50% (probablement `visualization`, `agent`), créer tickets.
*   **Acceptation :** `htmlcov/index.html` généré, README badge `coverage: 60%`.

---

## PHASE 5 — DOCS & RELEASE (4h)

### P5-01 — README, ARCHITECTURE.md, CHANGELOG

*   **Priorité :** 🟡 Amélioration | **Effort :** 2h
*   **Pourquoi :** Pas de README, 7 mains non documentées, config non expliquée.
*   **Gains :** Onboarding <5min, contributeurs autonomes.
*   **Description :**
    1.  `README.md` : `## Installation` (`pip install -e .`), `## Usage` (`geopol collect --help`), `## Config` (bbox), `## API`, `## Tests`.
    2.  `docs/ARCHITECTURE.md` : diagramme `ingestion -> storage -> analysis -> viz`, choix CSV→Parquet futur.
    3.  `CHANGELOG.md` : `0.1.0 — Initial POC`, `0.1.1 — Fix paths, security`.
*   **Acceptation :** `cat README.md | grep "pip install"` non vide, nouveau dev clone et lance `geopol dashboard` en <5min.

### P5-02 — Tag release `0.1.0` et nettoyage final

*   **Priorité :** 🟢 Mineur | **Effort :** 1h | **Dépendances :** Toutes
*   **Pourquoi :** Marquer la baseline avant refactors majeurs.
*   **Description :** `git tag -a v0.1.0 -m "POC baseline" && git push --tags`, vérifier `gh release view`.
*   **Acceptation :** `git tag --list` contient `v0.1.0`.

### P5-03 — Décision `data/` et migration si besoin

*   **Priorité :** 🟢 Mineur | **Effort :** 1h
*   **Pourquoi :** `src/data` vs `data` racine encore ambigu.
*   **Description :** Si P1-02 a migré vers `data/` racine, `git mv` + mettre à jour `README` + `CONFIG`. Sinon documenter `src/data` comme choix et mettre à jour `paths.py`.
*   **Acceptation :** `ls data/raw/` OU `ls src/data/raw/` mais pas les deux, `grep -r "src/data" README.md` cohérent.

---

## 2. Planning Gantt (solo, 9 jours)

```
J1  ████ P0-01..05 + P1-01 (pyproject, .gitignore, quick wins)
J2  ████ P1-02 + P1-03 (paths, config)
J3  ████ P1-04 + P1-05 + P1-06 (storage, metrics, package)
J4  ████ P2-01 + P2-02 (API security, GDELT https)
J5  ████ P2-03 + P2-04 + P2-05 (logging, exceptions, retry)
J6  ████ P3-01 + P3-02 (geopol package, DataStore)
J7  ████ P3-03 + P3-04 (viz dedup, CLI)
J8  ████ P3-05 + P4-01 (HttpClient, tests critiques)
J9  ████ P4-02 + P4-03 + P5-01..03 (CI, API tests, docs)
```

**Chemin critique :** P1-02 → P1-03 → P1-04 → P3-02 → P4-01. Tout retard sur `paths`/`config` décale les tests.

---

## 3. Risques & Mitigations

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Migration `src/data` → `data/` casse les CSV existants | Haute | Moyen | Faire `git mv` + garder symlink `src/data -> ../data` pendant 1 sprint |
| Renommage `src/` → `src/geopol/` casse les imports dans 12 fichiers | Haute | Moyen | Script `sed` + `grep -r "from ingestion"` pour vérifier, `pytest` en garde-fou |
| `pydantic` validation bbox trop stricte bloque la démo | Faible | Faible | Mettre `lat_min < lat_max` en `warning` la 1re semaine, `error` ensuite |
| `flask-limiter` + `ollama` streaming incompatible | Faible | Moyen | Limiter uniquement `/api/ask` (pas `/api/status`), tester le streaming SSE après |
| Couverture 60% trop ambitieuse en 6h | Moyen | Faible | Viser 40% en P4-01, 60% en P4-02 itératif |

---

## 4. Checklist Definition of Done (à cocher à chaque fiche)

*   [ ] `ruff check` vert
*   [ ] `mypy` sans nouvelle erreur
*   [ ] `pytest` vert (pas de régression)
*   [ ] `grep` de non-régression (ex: `grep -rn 'Path("data' src/` vide après P1-02)
*   [ ] Docstring / README mis à jour si API publique changée
*   [ ] Pas de `print` ajouté, pas de `sys.path.insert` ajouté

---

## 5. Ordre d'exécution recommandé (si temps limité)

**Si tu n'as que 1 jour (8h) :** Fais **P0-01 + P0-02 + P1-01 + P1-02 + P1-03 + P1-05** → projet installable, plus de crash, bbox correctes. C'est le MVP qui fait passer la note de 2.5 à 5.5.

**Si tu as 3 jours (24h) :** Ajoute **P1-04 + P2-01 + P2-03 + P4-01 (tests partiels)** → sécu + observabilité + 30% coverage. Note 6.5.

**Si tu as 1 semaine :** Tout jusqu'à **P3-04** → architecture propre, CLI unique. Note 7.5.

---

### Questions pour toi avant de lancer

1.  **Arborescence `data/` :** Tu préfères `data/` à la racine (standard) ou garder `src/data/` ? Je recommande racine, mais je m'adapte.
2.  **CLI :** `geopol` te va comme nom de commande, ou tu veux garder `python -m ...` ?
3.  **Priorité sécu :** L'API doit-elle rester `localhost` uniquement ou être exposée sur le LAN ? Ça change `host` et `CORS`.
4.  **LLM :** `ollama/mistral` reste, ou tu veux le rendre optionnel (l'API doit marcher sans Ollama installé) ?

Dis-moi tes préférences et je lance l'implémentation dans l'ordre ci-dessus.

---

