import pyttsx3  #para que nos pueda hablar
import speech_recognition as sr      #para que nos escuche as es para abrebiar nombre
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia





#escuchar nuestro microfono y devolver en audio como texto
def transformar_audio_en_texto():

    #almacenar el reconecedor(reconnizer) en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera / humbral de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print("ya puedes hablar")

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            #prueba de que entendio lo que le dijimos
            print("dijiste: " + pedido)

            #devuelve pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            #devolver error
            return "sigo esperando"

        #en caso de no resolver el pedido, es decir que grabo pero no lo puede transformar
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        #error inesperado
        except:
            # prueba de que no comprendio el audio
            print("ups, algo a salido mal")

            # devolver error
            return "sigo esperando"


transformar_audio_en_texto()





