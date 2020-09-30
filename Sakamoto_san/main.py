import speech_recognition as reconhecimentoDeFala
import pyttsx3
from config import * #importa tudo que esta dentro do config
from random import choice

reproducao = pyttsx3.init()

def saidaSom(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    print("Hello, what's you full name?") 
    saidaSom("Hello, what's you full name?")
    
    while True:
        respostaErroAleatoria = choice(listaErros)
        reconhecimento = reconhecimentoDeFala.Recognizer()

        with reconhecimentoDeFala.Microphone() as microfone:
            reconhecimento.adjust_for_ambient_noise(microfone)

            while True:
                try:
                    audio = reconhecimento.listen(microfone)
                    userName = reconhecimento.recognize_google(audio, language='en')
                    userName = verificaNome(userName)
                    nameList()
                    apresentacao = "{}".format(verificaNomeExiste(userName))
                    print(apresentacao)
                    saidaSom(apresentacao)
                    
                    # Cria uma lista com cada parte de um nome separada por " "
                    bruteUserName = userName
                    userName = userName.split(" ")
                    userName = userName[0]
                    break
                            
                except reconhecimentoDeFala.UnknownValueError:
                    saidaSom(respostaErroAleatoria)
        break
    
    print("=" * len(apresentacao))
    print("Ouvindo...")
    
    while True:
        respostaErroAleatoria = choice(listaErros)
        reconhecimento = reconhecimentoDeFala.Recognizer()

        with reconhecimentoDeFala.Microphone() as microfone:
            reconhecimento.adjust_for_ambient_noise(microfone)

            while True:
                try:
                    audio = reconhecimento.listen(microfone)
                    entrada = reconhecimento.recognize_google(audio, language='en')
                    print("{}: {}".format(userName, entrada))
                    resposta = conversas[entrada]    
                    print("Sakamoto-san: {}".format(resposta))
                    saidaSom("{}".format(resposta))
                            
                except reconhecimentoDeFala.UnknownValueError:
                    saidaSom(respostaErroAleatoria)
            
if __name__ == '__main__':
    intro()
    saidaSom("Iniciando")
    assistente()
    
