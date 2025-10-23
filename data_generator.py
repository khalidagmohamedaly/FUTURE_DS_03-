"""
Script pour générer des données de feedback d'événement universitaire
Future Interns - Task 3: College Event Feedback Analysis
Author: KHALID AG MOHAMED ALY
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)

# Nombre de réponses
n_responses = 200

# Définir les options
events = ['Tech Conference 2025', 'Career Workshop', 'Cultural Fest', 
          'Entrepreneurship Summit', 'AI & ML Seminar']
event_types = ['Conférence', 'Workshop', 'Culturel', 'Séminaire', 'Compétition']
departments = ['Computer Science', 'Engineering', 'Business', 'Arts', 'Science', 'Law']
years = ['1st Year', '2nd Year', '3rd Year', '4th Year']
attendance_types = ['Présentiel', 'Virtuel']

# Commentaires positifs templates
positive_comments = [
    "Excellent événement, très instructif et bien organisé.",
    "J'ai beaucoup appris, les intervenants étaient passionnants.",
    "Parfaite organisation, contenu de qualité et networking intéressant.",
    "Très inspirant, je recommande vivement cet événement.",
    "Super expérience, les sujets abordés étaient pertinents.",
    "Brillant ! Les speakers étaient experts et accessibles.",
    "Organisation impeccable, contenu riche et diversifié.",
    "Fascinant du début à la fin, très enrichissant.",
    "Excellente initiative, j'ai découvert de nouvelles perspectives.",
    "Incroyable événement, parfaitement adapté aux étudiants.",
]

# Commentaires neutres templates
neutral_comments = [
    "Bon événement dans l'ensemble, quelques aspects à améliorer.",
    "Intéressant mais pourrait être plus interactif.",
    "Correct, conforme à mes attentes générales.",
    "Pas mal, certaines sessions étaient meilleures que d'autres.",
    "Décent, bon contenu mais organisation perfectible.",
    "Satisfaisant, aurait pu être plus dynamique.",
    "Bien mais assez classique, rien d'exceptionnel.",
    "Moyen, certains aspects étaient intéressants.",
    "Ok, conforme à mes attentes sans grande surprise.",
    "Acceptable, quelques bons moments.",
]

# Commentaires négatifs templates
negative_comments = [
    "Décevant, mal organisé et contenu peu pertinent.",
    "Trop long et ennuyeux, manque de dynamisme.",
    "Désorganisé, mauvaise gestion du temps.",
    "Pas à la hauteur des attentes, speakers peu engageants.",
    "Mauvaise organisation, problèmes techniques récurrents.",
    "Contenu superficiel, manque de profondeur.",
    "Événement mal planifié, beaucoup de temps perdu.",
    "Peu intéressant, pas assez interactif.",
    "Décevant comparé à l'année dernière.",
    "Mauvaise qualité audio, difficile de suivre.",
]

# Suggestions d'amélioration templates
improvements = [
    "Améliorer la gestion du temps, certaines sessions étaient trop longues.",
    "Plus d'interactivité et de sessions pratiques seraient appréciées.",
    "Meilleure coordination et communication avant l'événement.",
    "Lieu plus spacieux, il y avait trop de monde.",
    "Améliorer la qualité technique (audio, vidéo).",
    "Plus de pauses entre les sessions.",
    "Diversifier les sujets et les formats de présentation.",
    "Meilleure signalétique et orientation sur place.",
    "Nourriture de meilleure qualité.",
    "Plus de temps pour le networking.",
    "Sessions plus courtes et plus dynamiques.",
    "Meilleure sélection des intervenants.",
]

def generate_ratings(overall_sentiment):
    """Génère des notes cohérentes basées sur le sentiment global"""
    if overall_sentiment == 'positive':
        base = 4
        variance = 1
    elif overall_sentiment == 'neutral':
        base = 3
        variance = 1
    else:  # negative
        base = 2
        variance = 1
    
    ratings = {
        'Overall': min(5, max(1, int(np.random.normal(base, variance/2)))),
        'Venue': min(5, max(1, int(np.random.normal(base, variance/2)))),
        'Organization': min(5, max(1, int(np.random.normal(base, variance/2)))),
        'Content': min(5, max(1, int(np.random.normal(base, variance/2)))),
        'Speaker': min(5, max(1, int(np.random.normal(base, variance/2))))
    }
    
    return ratings

def get_comment(overall_rating):
    """Sélectionne un commentaire basé sur la note globale"""
    if overall_rating >= 4:
        return random.choice(positive_comments)
    elif overall_rating >= 3:
        return random.choice(neutral_comments)
    else:
        return random.choice(negative_comments)

# Générer le dataset
data = []

# Date de l'événement (il y a 1 semaine)
event_date = datetime.now() - timedelta(days=7)

for i in range(n_responses):
    # Timestamp de la réponse (entre le jour de l'événement et maintenant)
    days_after = random.randint(0, 7)
    hours_after = random.randint(0, 23)
    timestamp = event_date + timedelta(days=days_after, hours=hours_after)
    
    # Sélectionner des attributs aléatoires
    event_name = random.choice(events)
    event_type = random.choice(event_types)
    department = random.choice(departments)
    year = random.choice(years)
    attendance = random.choice(attendance_types)
    
    # Déterminer le sentiment global (70% positif, 20% neutre, 10% négatif)
    sentiment_rand = random.random()
    if sentiment_rand < 0.70:
        sentiment = 'positive'
    elif sentiment_rand < 0.90:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    
    # Générer les notes
    ratings = generate_ratings(sentiment)
    
    # Recommandation basée sur la note globale
    would_recommend = 'Oui' if ratings['Overall'] >= 3 else 'Non'
    
    # Générer les commentaires
    liked_most = get_comment(ratings['Overall'])
    
    # Suggestions d'amélioration (plus fréquentes pour notes basses)
    if ratings['Overall'] <= 3 or random.random() < 0.4:
        improvements_text = random.choice(improvements)
    else:
        improvements_text = "Rien de particulier, tout était bien." if random.random() < 0.5 else random.choice(improvements)
    
    # Commentaires additionnels (optionnels, 50% de chance)
    if random.random() < 0.5:
        additional = "Merci pour cet événement !" if sentiment == 'positive' else \
                    "Continuez vos efforts." if sentiment == 'neutral' else \
                    "Beaucoup à améliorer."
    else:
        additional = ""
    
    # Ajouter l'enregistrement
    data.append({
        'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'Student ID': f'STU{str(i+1).zfill(4)}',
        'Event Name': event_name,
        'Event Type': event_type,
        'Overall Rating': ratings['Overall'],
        'Venue Rating': ratings['Venue'],
        'Organization Rating': ratings['Organization'],
        'Content Rating': ratings['Content'],
        'Speaker Rating': ratings['Speaker'],
        'Would Recommend': would_recommend,
        'What did you like most?': liked_most,
        'What could be improved?': improvements_text,
        'Additional Comments': additional,
        'Department': department,
        'Year': year,
        'Attendance': attendance
    })

# Créer le DataFrame
df = pd.DataFrame(data)

# Trier par timestamp
df = df.sort_values('Timestamp').reset_index(drop=True)

# Sauvegarder le dataset
output_path = '../data/event_feedback.csv'
df.to_csv(output_path, index=False)

print("✅ Dataset de feedback d'événement généré avec succès!")
print(f"📊 Nombre de réponses: {len(df)}")
print(f"📁 Fichier sauvegardé: {output_path}")

print(f"\n📋 Aperçu des données:")
print(df.head(10))

print(f"\n📊 STATISTIQUES GLOBALES")
print("="*70)
print(f"📅 Période de feedback: {df['Timestamp'].min()} à {df['Timestamp'].max()}")
print(f"⭐ Note moyenne globale: {df['Overall Rating'].mean():.2f}/5.0")
print(f"👍 Taux de recommandation: {(df['Would Recommend'] == 'Oui').sum() / len(df) * 100:.1f}%")

print(f"\n📊 DISTRIBUTION DES NOTES")
print("="*70)
print("\nNote Globale:")
print(df['Overall Rating'].value_counts().sort_index())

print("\n📊 RÉPARTITION")
print("="*70)
print("\n🎓 Par Département:")
print(df['Department'].value_counts())

print("\n📚 Par Année:")
print(df['Year'].value_counts())

print("\n🏢 Par Type de Participation:")
print(df['Attendance'].value_counts())

print("\n🎯 Par Événement:")
print(df['Event Name'].value_counts())

# Calculer des statistiques avancées
print(f"\n📈 STATISTIQUES PAR CATÉGORIE")
print("="*70)
rating_cols = ['Overall Rating', 'Venue Rating', 'Organization Rating', 
               'Content Rating', 'Speaker Rating']
print(df[rating_cols].describe().round(2))

# Identifier les réponses positives, neutres et négatives
positive = df[df['Overall Rating'] >= 4]
neutral = df[df['Overall Rating'] == 3]
negative = df[df['Overall Rating'] <= 2]

print(f"\n😊 Feedback Positifs (4-5 étoiles): {len(positive)} ({len(positive)/len(df)*100:.1f}%)")
print(f"😐 Feedback Neutres (3 étoiles): {len(neutral)} ({len(neutral)/len(df)*100:.1f}%)")
print(f"😞 Feedback Négatifs (1-2 étoiles): {len(negative)} ({len(negative)/len(df)*100:.1f}%)")

# Créer un fichier d'information
info_text = f"""
# Dataset Information - College Event Feedback

## Overview
- **Total Responses**: {len(df)}
- **Response Period**: {df['Timestamp'].min()} to {df['Timestamp'].max()}
- **Events**: {df['Event Name'].nunique()}
- **Departments**: {df['Department'].nunique()}
- **Academic Years**: {df['Year'].nunique()}

## Key Metrics
- **Average Overall Rating**: {df['Overall Rating'].mean():.2f}/5.0
- **Recommendation Rate**: {(df['Would Recommend'] == 'Oui').sum() / len(df) * 100:.1f}%
- **Positive Feedback**: {len(positive)} ({len(positive)/len(df)*100:.1f}%)
- **Neutral Feedback**: {len(neutral)} ({len(neutral)/len(df)*100:.1f}%)
- **Negative Feedback**: {len(negative)} ({len(negative)/len(df)*100:.1f}%)

## Columns Description
1. **Timestamp**: Date and time of response submission
2. **Student ID**: Anonymous student identifier
3. **Event Name**: Name of the event attended
4. **Event Type**: Type of event (Conference, Workshop, etc.)
5. **Overall Rating**: Overall satisfaction rating (1-5 stars)
6. **Venue Rating**: Rating of the venue/location (1-5)
7. **Organization Rating**: Rating of event organization (1-5)
8. **Content Rating**: Rating of content quality (1-5)
9. **Speaker Rating**: Rating of speaker/presenter (1-5)
10. **Would Recommend**: Whether student would recommend (Yes/No)
11. **What did you like most?**: Open-ended positive feedback
12. **What could be improved?**: Open-ended suggestions
13. **Additional Comments**: Any additional comments (optional)
14. **Department**: Student's academic department
15. **Year**: Student's year of study
16. **Attendance**: Type of participation (In-person/Virtual)

## Data Quality
- No missing values in required fields
- Ratings range from 1 to 5
- Realistic distribution of sentiments
- Coherent feedback patterns

## Usage
Perfect for:
- Sentiment analysis practice
- NLP text processing
- Survey data analysis
- Event feedback evaluation
- Improvement recommendations
"""

with open('../data/feedback_dataset_info.txt', 'w') as f:
    f.write(info_text)

print("\n📄 Informations du dataset sauvegardées: ../data/feedback_dataset_info.txt")
print("\n🎉 PROCESSUS TERMINÉ!")
