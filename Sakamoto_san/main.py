import speech_recognition as reconhecimentoDeFala
import pyttsx3
from random import choice

listaErros = [
    "Não entendi....",
    "Desculpe, não entendi",
    "Repita novamente por favor"
]

reproducao = pyttsx3.init()

def saidaSom(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def reconhecimentoDeVoz(respostaErroAleatoria):
    reconhecimento = reconhecimentoDeFala.Recognizer()

    with reconhecimentoDeFala.Microphone() as microfone:
        reconhecimento.adjust_for_ambient_noise(microfone)

        while True:
            try:
                audio = reconhecimento.listen(microfone)
                entrada = reconhecimento.recognize_google(audio, language='pt')
                return "Você disse: {}".format(entrada)

            except reconhecimentoDeFala.UnknownValueError:
                return respostaErroAleatoria

print("Ouvindo.......\n----------------\n")

while True:
    respostaErroAleatoria = choice(listaErros)
    fala = reconhecimentoDeVoz(respostaErroAleatoria)
    print(fala)
    saidaSom(fala)

