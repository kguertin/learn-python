from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Employee Number 21783619736. We hope you had a great day of work. It's time to submit your employee wellness statement")
engine.runAndWait()

print("Enter your employee wellness statement:")
user_input = input("> ")
blob = TextBlob(user_input)

while blob.sentiment.polarity < 0.5:
    print("More positive please: ")
    user_input = input("> ")
    blob = TextBlob(user_input)

print("We appreciate you too!")