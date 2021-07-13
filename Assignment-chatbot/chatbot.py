import pyttsx3
import speech_recognition as sr
import random

""" Python small chatbot for some college information
    eg questions:-
        1. Hello
        2. Who is HOD of Physics Department
        3. Where is PPS Department 
"""

def sayText(text):
    tts = pyttsx3.init()
    tts.setProperty('rate', 150)
    tts.say(text)
    print(text + "\n")
    tts.runAndWait()


def recognitionText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except:
        sayText("Sorry I did'nt Understand...")


def checker(text, find):
    for x in find:
        if text.__contains__(x):
            return x
        else:
            continue


entering = ['hi', 'hello there', 'hello', 'hey', 'hey', 'hai']
exiting = ['okay thanks', 'bye', 'good day', 'thanks']
secondary = ['Physics', 'physics', 'chemistry',
    'Chemistry', 'pps', 'PPS', 'Maths', 'maths']
main = ['HOD', 'department', 'Department']


while True:
    text = recognitionText()

    checkerMain = checker(text, main)
    checkerSecondary = checker(text, secondary)

    if text in entering:
        sayText(random.choice(entering))

    elif checkerMain == 'department' or checkerMain == 'Department':

        if checkerSecondary == 'Physics' or checkerSecondary == 'physics':
            sayText('Physics Department is in A Block')
        elif checkerSecondary == 'chemistry':
            sayText('Chemistry Department is in D Block')
        elif checkerSecondary == 'maths' or checkerSecondary == 'Maths':
            sayText('Maths Department is in B Block')
        elif checkerSecondary == 'pps' or checkerSecondary == 'PPS':
            sayText('PPS Department is in C Block')
        else:
            sayText('I don\'t know the answer...exiting')
            break

    elif checkerMain == 'HOD':

        if checkerSecondary == 'Physics' or checkerSecondary == 'physics':
            sayText('Ram is HOD of physics department')
        elif checkerSecondary == 'chemistry' or checkerSecondary == 'Chemistry':
            sayText('Sita is HOD of chemistry department')
        elif checkerSecondary == 'maths' or checkerSecondary == 'Maths':
            sayText('Kailash is HOD of maths department')
        elif checkerSecondary == 'pps' or checkerSecondary == 'PPS':
            sayText('Kavita is HOD of PPS department')
        else:
            sayText('I don\'t know the answer...exiting')
            break

    elif text in exiting:
        sayText(random.choice(exiting))
        break
    
    else:
        sayText('I don\'t know the answer...exiting')
        break