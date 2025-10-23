
# 📝 College Event Feedback Analysis

**Future Interns - Data Science & Analytics Internship**  
**Task 3 | Track Code: DS**  
**Intern: KHALID AG MOHAMED ALY**  
**Internship Period: October 16 - November 16, 2025**

---

## 🎯 Objectif du Projet

Analyser les retours d'étudiants suite à un événement universitaire pour :
- Découvrir les tendances de satisfaction
- Identifier les points forts et faibles
- Effectuer une analyse de sentiment avec NLP
- Proposer des améliorations basées sur les données
- Créer des visualisations exploitables

---

## 🛠️ Technologies Utilisées

- **Python** : Langage principal
- **Google Colab** : Environnement de développement
- **Pandas** : Manipulation de données
- **TextBlob / VADER** : Analyse de sentiment (NLP)
- **Seaborn & Matplotlib** : Visualisations
- **WordCloud** : Nuages de mots
- **Google Forms** : Collecte de feedback (CSV export)

---

## 📁 Structure du Projet

```
FUTURE_DS_03/
│
├── README.md
├── data/
│   ├── event_feedback.csv
│   └── processed_feedback.csv
│
├── notebooks/
│   └── feedback_analysis.ipynb
│
├── scripts/
│   ├── data_generator.py
│   ├── sentiment_analyzer.py
│   └── text_processor.py
│
├── reports/
│   ├── feedback_insights.md
│   ├── sentiment_analysis_report.pdf
│   └── recommendations.md
│
└── visuals/
    ├── wordclouds/
    ├── sentiment_distribution.png
    └── satisfaction_trends.png
```

---

## 📊 Dataset - Structure du Feedback

### Colonnes du Survey :

1. **Timestamp** : Date et heure de soumission
2. **Student ID** : Identifiant anonyme
3. **Event Name** : Nom de l'événement
4. **Event Type** : Type (Conférence, Workshop, Culturel, etc.)
5. **Overall Rating** : Note globale (1-5 étoiles)
6. **Venue Rating** : Note du lieu (1-5)
7. **Organization Rating** : Note de l'organisation (1-5)
8. **Content Rating** : Note du contenu (1-5)
9. **Speaker Rating** : Note du speaker/animateur (1-5)
10. **Would Recommend** : Oui/Non
11. **What did you like most?** : Commentaire ouvert
12. **What could be improved?** : Suggestions d'amélioration
13. **Additional Comments** : Commentaires libres
14. **Department** : Département de l'étudiant
15. **Year** : Année d'études
16. **Attendance** : Présentiel/Virtuel

---

## 🔍 Analyses Effectuées

### 1. Analyse Quantitative

**Métriques Calculées :**
- Note moyenne globale et par catégorie
- Taux de recommandation
- Distribution des notes
- Statistiques par département et année
- Comparaison Présentiel vs Virtuel

### 2. Analyse de Sentiment (NLP)

**Techniques Utilisées :**
- **TextBlob** : Polarité et subjectivité
- **VADER** : Analyse de sentiment spécifique aux réseaux sociaux
- Classification : Positif / Neutre / Négatif
- Extraction de mots-clés

**Métriques de Sentiment :**
```python
Polarity: -1 (négatif) à +1 (positif)
Subjectivity: 0 (objectif) à 1 (subjectif)
Compound Score: Score composite VADER
```

### 3. Analyse Textuelle

- **Word Frequency Analysis** : Mots les plus fréquents
- **WordClouds** : Visualisation des thèmes
- **Bigrams & Trigrams** : Phrases récurrentes
- **Topic Modeling** : Thèmes principaux (optionnel)

### 4. Analyse Comparative

- Performance par type d'événement
- Satisfaction par département
- Différences année 1 vs années supérieures
- Présentiel vs Virtuel

---

## 📈 Résultats Clés

### Métriques Globales
```
• Note Moyenne Globale: X.X/5.0
• Taux de Recommandation: XX%
• Nombre de Réponses: XXX
• Sentiment Moyen: X.XX (Positif/Négatif/Neutre)
```

### Distribution des Sentiments
```
😊 Positif: XX%
😐 Neutre: XX%
😞 Négatif: XX%
```

### Top Insights
1. **Point Fort Principal** : [Aspect le plus apprécié]
2. **Point Faible Principal** : [Aspect à améliorer]
3. **Mots-clés Positifs** : excellent, instructif, inspirant, etc.
4. **Mots-clés Négatifs** : désorganisé, ennuyeux, long, etc.

---

## 💡 Recommandations

### Basées sur l'Analyse de Sentiment

✅ **À Maintenir** : Aspects avec sentiment positif > 80%  
⚠️ **À Améliorer** : Aspects avec sentiment négatif > 30%  
🔄 **À Optimiser** : Aspects avec sentiment neutre > 50%

### Recommandations Spécifiques

1. **Organisation**
   - [Recommandation basée sur feedback]
   
2. **Contenu**
   - [Recommandation basée sur feedback]
   
3. **Lieu/Logistique**
   - [Recommandation basée sur feedback]
   
4. **Communication**
   - [Recommandation basée sur feedback]

---

## 🚀 Comment Utiliser ce Projet

### Option 1 : Google Colab (Recommandé)

1. **Ouvrir Google Colab**
   ```
   https://colab.research.google.com
   ```

2. **Créer un nouveau notebook**
   - File → New Notebook

3. **Installer les dépendances**
   ```python
   !pip install textblob vaderSentiment wordcloud
   !python -m textblob.download_corpora
   ```

4. **Importer le code depuis le notebook**
   - Copier le contenu de `notebooks/feedback_analysis.ipynb`

5. **Charger les données**
   ```python
   from google.colab import files
   uploaded = files.upload()
   df = pd.read_csv('event_feedback.csv')
   ```

### Option 2 : Local

```bash
# Installer les dépendances
pip install pandas numpy matplotlib seaborn textblob vaderSentiment wordcloud

# Télécharger les corpus TextBlob
python -m textblob.download_corpora

# Lancer Jupyter
jupyter notebook notebooks/feedback_analysis.ipynb
```

---

## 📊 Visualisations Créées

### 1. Distribution des Notes
- Histogrammes pour chaque catégorie de notation
- Boxplots comparatifs

### 2. Analyse de Sentiment
- Pie chart de la distribution des sentiments
- Bar chart des scores moyens par catégorie
- Evolution temporelle du sentiment

### 3. Word Clouds
- Nuage de mots des commentaires positifs
- Nuage de mots des suggestions d'amélioration
- Nuage général

### 4. Comparaisons
- Heatmap des corrélations entre notes
- Graphiques comparatifs par département
- Analyse présentiel vs virtuel

### 5. Insights Visuels
- Top 10 mots positifs/négatifs
- Fréquence des thèmes mentionnés
- Matrice satisfaction-recommandation

---

## 🧠 Techniques NLP Utilisées

### TextBlob
```python
from textblob import TextBlob

# Analyse de sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
```

**Interprétation :**
- Polarity > 0.1 : Positif
- -0.1 ≤ Polarity ≤ 0.1 : Neutre
- Polarity < -0.1 : Négatif

### VADER
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
compound_score = scores['compound']
```

**Interprétation :**
- Compound ≥ 0.05 : Positif
- -0.05 < Compound < 0.05 : Neutre
- Compound ≤ -0.05 : Négatif

### Preprocessing du Texte
```python
import re
from textblob import TextBlob

def clean_text(text):
    # Minuscules
    text = text.lower()
    # Supprimer ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Supprimer nombres
    text = re.sub(r'\d+', '', text)
    # Supprimer espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    return text
```

---

## 📝 Compétences Développées

✅ Data Cleaning et Preprocessing  
✅ Analyse de Sentiment (NLP)  
✅ TextBlob et VADER  
✅ Traitement du langage naturel  
✅ Visualisation de données textuelles  
✅ Word Clouds  
✅ Extraction d'insights qualitatifs  
✅ Survey Data Analysis  
✅ Statistiques descriptives  
✅ Data Storytelling  

---

## 📚 Ressources d'Apprentissage

### Documentation
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [WordCloud Library](https://github.com/amueller/word_cloud)
- [Pandas Text Analysis](https://pandas.pydata.org/)

### Tutoriels Recommandés
- Natural Language Processing with Python
- Sentiment Analysis for Beginners
- Survey Data Analysis Best Practices

---

## 📧 Contact

**Intern** : KHALID AG MOHAMED ALY  
**LinkedIn** : [https://www.linkedin.com/in/khalid-ag-mohamed-aly/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bu8KIOsoJSHOwG15Pco823A%3D%3D]  
**Email** : alansarymohamed38@gmail.com

---

## 📜 License

Ce projet fait partie du programme de stage Future Interns - Data Science & Analytics Track.

**Internship ID** : FIT/OCT25/DS8272

---

## 🎓 Applications Réelles

### Cas d'Usage :
- **Universités** : Améliorer l'organisation d'événements
- **Entreprises** : Analyse de satisfaction client
- **Conférences** : Évaluation de la qualité
- **Formations** : Feedback sur les cours
- **Événements** : Optimisation de l'expérience

### Impact Business :
- Amélioration de l'engagement étudiant
- Identification rapide des problèmes
- Décisions data-driven
- Meilleure allocation des ressources
- Augmentation de la satisfaction globale

---

## 🏆 Résultats Attendus

Après cette analyse, vous serez capable de :

1. ✅ Collecter et traiter des données de feedback
2. ✅ Effectuer une analyse de sentiment avec NLP
3. ✅ Créer des visualisations impactantes
4. ✅ Extraire des insights actionnables
5. ✅ Formuler des recommandations stratégiques
6. ✅ Présenter les résultats de manière professionnelle

---

## 📊 Exemple de Google Form

### Questions Suggérées :

**Section 1 : Informations Générales**
1. Timestamp (automatique)
2. Identifiant (anonyme)
3. Département (liste déroulante)
4. Année d'études (liste déroulante)
5. Type de participation (Présentiel/Virtuel)

**Section 2 : Évaluations**
6. Note globale (échelle 1-5)
7. Qualité du contenu (échelle 1-5)
8. Organisation (échelle 1-5)
9. Lieu/Plateforme (échelle 1-5)
10. Intervenant(s) (échelle 1-5)

**Section 3 : Recommandation**
11. Recommanderiez-vous cet événement ? (Oui/Non)

**Section 4 : Commentaires Ouverts**
12. Qu'avez-vous le plus apprécié ? (texte long)
13. Que pourrait-on améliorer ? (texte long)
14. Commentaires additionnels (texte long, optionnel)

---

## 💻 Code Snippets Utiles

### Analyse Rapide de Sentiment
```python
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return 'Positif'
    elif polarity < -0.1:
        return 'Négatif'
    else:
        return 'Neutre'

df['Sentiment'] = df['Comments'].apply(analyze_sentiment)
```

### Création de WordCloud
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ' '.join(df['Comments'].dropna())
wordcloud = WordCloud(width=800, height=400, 
                      background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### Extraction des Mots les Plus Fréquents
```python
from collections import Counter
import re

def get_top_words(text, n=10):
    words = re.findall(r'\b\w+\b', text.lower())
    # Supprimer les stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'was', 'were'}
    words = [w for w in words if w not in stop_words and len(w) > 3]
    return Counter(words).most_common(n)
```

---

*Dernière mise à jour : [Date]*  
*Version : 1.0*

🎉 **Bonne chance avec votre analyse de feedback !**
