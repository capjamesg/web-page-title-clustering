import string
from nltk.corpus import stopwords
from collections import defaultdict

INTERSECTION_THRESHOLD = 0

stopwords = set(stopwords.words("english"))

titles = []

titles = sorted(titles)
original_titles = titles.copy()
titles = [title.lower().translate(str.maketrans("", "", string.punctuation)) for title in titles]
titles = [title.split(" ") for title in titles]
titles = [[word for word in title if word not in stopwords] for title in titles]
titles = [set(title) for title in titles]

similar_titles = defaultdict(defaultdict)

from tqdm import tqdm

for original_title, title in tqdm(zip(original_titles, titles), total=len(titles)):
    for other_title, other_words in zip(original_titles, titles):
        if original_title == other_title:
            continue

        similar_titles[original_title][other_title] = len(title.intersection(other_words))

for title in similar_titles:
    similar_titles[title] = dict(sorted(similar_titles[title].items(), key=lambda x: x[1], reverse=True))

results = similar_titles["How I decide what coffee to drink [Diagram]"]

for title, score in list(results.items())[:5]:
    print(f"{title}: {score}")
