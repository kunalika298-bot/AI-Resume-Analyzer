import pandas as pd

skills_df = pd.read_csv("dataset/skills.csv")

skills_list = skills_df['skills'].tolist()

def extract_skills(text):

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills