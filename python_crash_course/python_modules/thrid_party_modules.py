from art import art, text2art
from translate import Translator



print(art("woman"))
print(art("coffee"))
print(art("random"))
print(art("random"))
print(art("random"))
print(art("random"))

print(text2art("Hello"))

translator = Translator(to_lang="fr")
translation = translator.translate("Hello, I love you.")
print(translation) 
