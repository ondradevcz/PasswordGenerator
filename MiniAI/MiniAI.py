import random
from Data import *

convo_text = ""
l_convo_text = ""

print("Dobrý den, moje jméno je MiniAI")

def Respond():
    global l_convo_text  # Declare l_convo_text as global
    if any(ending in l_convo_text for ending in l_end_convo):
        print("Děkuji za konverzaci a tvůj čas, měj se.")
        # KONEC
    elif any(greeting in l_convo_text for greeting in l_greetings):
        print(random.choice(l_ai_greetings))
        StartKonverzace()
    else:
        print("Nerozumím, zkus to znova")
        StartKonverzace()

def StartKonverzace():
    global convo_text, l_convo_text  # Declare both convo_text and l_convo_text as global
    convo_text = input("Piš zde: ")
    l_convo_text = convo_text.split()
    print(l_convo_text)
    Respond()
    return convo_text, l_convo_text

StartKonverzace()