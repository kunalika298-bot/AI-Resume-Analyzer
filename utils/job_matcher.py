import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jobs = pd.read_csv("dataset/jobs.csv")

def match_jobs(resume_text):

    job_descriptions = jobs['description'].tolist()

    documents = [resume_text] + job_descriptions

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )

    scores = similarity[0]

    jobs['match_score'] = scores * 100

    return jobs.sort_values(
        by='match_score',
        ascending=False
    )