from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


job_roles = {
    "Data Scientist": "Python SQL Machine Learning Statistics Pandas",
    "DevOps Engineer": "AWS Docker Kubernetes Linux Git Automation",
    "Backend Developer": "Java Python SQL APIs Database Git",
    "Frontend Developer": "HTML CSS JavaScript React UI",
    "Cloud Architect": "AWS Azure Cloud Docker Kubernetes Networking",
    "Machine Learning Engineer": "Python Machine Learning Deep Learning TensorFlow SQL",
    "Database Administrator": "SQL MySQL PostgreSQL Database Linux"
}


print("==============================================")
print("       🤖 TECH STACK RECOMMENDER")
print("==============================================")

print("\nEnter your skills/interests.")
print("Example: Python, Cloud, Automation\n")

user_input = input("Enter your skills: ")


roles = list(job_roles.keys())
role_skills = list(job_roles.values())

all_documents = role_skills + [user_input]


vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(all_documents)


user_vector = vectors[-1]

role_vectors = vectors[:-1]


similarity_scores = cosine_similarity(
    user_vector,
    role_vectors
)[0]


recommendations = []

for role, score in zip(roles, similarity_scores):
    recommendations.append((role, score))


recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)


print("\n==============================================")
print("       TOP 3 CAREER RECOMMENDATIONS")
print("==============================================")

for i, (role, score) in enumerate(recommendations[:3], start=1):

    print(
        f"{i}. {role} "
        f"-> Similarity Score: {score:.2f}"
    )


print("\nThank you for using Tech Stack Recommender! ")
