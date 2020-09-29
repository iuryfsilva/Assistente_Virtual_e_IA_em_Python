import speech_recognition as reconhecimentoDeFala
import pyttsx3
from config import * #importa tudo que esta dentro do config
from random import choice

reproducao = pyttsx3.init()

def saidaSom(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

print("Ouvindo.......\n----------------\n")
while True:
    respostaErroAleatoria = choice(listaErros)
    reconhecimento = reconhecimentoDeFala.Recognizer()

    with reconhecimentoDeFala.Microphone() as microfone:
        reconhecimento.adjust_for_ambient_noise(microfone)

        while True:
            try:
                audio = reconhecimento.listen(microfone)
                entrada = reconhecimento.recognize_google(audio, language='pt')
                print("Você disse: {}".format(entrada))
                resposta = conversas[entrada]    
                print("Sakamoto-san: {}".format(resposta))
                saidaSom("{}".format(resposta))
                         
            except reconhecimentoDeFala.UnknownValueError:
                saidaSom(respostaErroAleatoria)
            

