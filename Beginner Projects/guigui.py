import PySimpleGUI as sg
import speech_recognition as sr


r = sr.Recognizer()

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout, margins=(150, 100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        harvard = sr.AudioFile('ocean.wav')
        with harvard as source:
            audio = r.record(source)
        window = sg.Window(sg.Text(r.recognize_google(audio)))

window.close()
