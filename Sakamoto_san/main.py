#-*- coding: utf-8 -*-

#importanto os modulos do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import os

import speech_recognition as reconhecimentoDeFala

bot = ChatBot('Sakamoto_san')

bot.set_trainer(ListTrainer) # definir treinamento

for _file in os.listdir('chats'): # Percorre todos os arquivos em chats
    lines = open('chats/' + _file, 'r').readlines() # vamos ler as linhas
    
    bot.train(lines)


def reconhecimentoDeVoz():
    reconhecimento = reconhecimentoDeFala.Recognizer()

    with reconhecimentoDeFala.Microphone() as microfone:
        reconhecimento.adjust_for_ambient_noise(microfone)

        while True:
            try:
                audio = reconhecimento.listen(microfone)
                entrada = reconhecimento.recognize_google(audio, language='jp')
                return "Você disse: {}".format(entrada)

            except reconhecimentoDeFala.UnknownValueError:
                return "Não entendi..."

print("Ouvindo.......\n----------------\n")

while True:
    fala = reconhecimentoDeVoz()
    print(fala)
