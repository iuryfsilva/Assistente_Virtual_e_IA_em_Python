import speech_recognition as reconhecimentoDeFala
reconhecimento = reconhecimentoDeFala.Recognizer()
with reconhecimentoDeFala.Microphone() as microfone:
    reconhecimento.adjust_for_ambient_noise(microfone)
    
    while True:
        audio = reconhecimento.listen(microfone)
        
        fala = reconhecimento.recognize_google(audio, language = 'jp')
        
        print('Você disse: ', fala)