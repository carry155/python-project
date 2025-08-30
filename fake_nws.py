# fake news generator
import random

subjects = ["The government", "Scientists", "Celebrities", "Tech companies", "Aliens"]
verbs = ["announce", "discover", "warn about", "investigate", "promote"]
objects = ["a new technology", "a conspiracy", "a health risk", "a secret project", "an alien invasion"]

while True:
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    headline = f"{subject} {verb} {obj}!"
    print(headline)
    input("Press Enter for another fake news headline...")