import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

print(r.recognize_google(audio, language='ko-KR'))
if r.recognize_google(audio, language='ko-KR') == '멈춰':
    print("멈춰")