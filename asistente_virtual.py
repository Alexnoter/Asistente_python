import pyttsx3  #para que nos pueda hablar
import speech_recognition as sr      #para que nos escuche as es para abrebiar nombre
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia




#opciones de voz / idiomas
'''
con esto sabremos cuantas voces tengo en el dispositivo

engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
'''
#le estamos dando todas las direccion de las voces
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'






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
            pedido = r.recognize_google(audio, language="es-es")

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


#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3 engine por estandar motor
    engine =pyttsx3.init()

    #le decimos con que voz de asistente queremos escuchar
    engine.setProperty('voices', id2)

    # pronunciar mensaje say = decir
    engine.say(mensaje)
    engine.runAndWait()



#informar el dia de la semana
def pedir_dia():

    # Crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variables para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')



#informar que hora es
def pedir_hora():

    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #Decir la hora
    hablar(hora)



# saludo inicialss
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 12:
        momento = 'buenos dias'
    else:
        momento = 'Buenas tardes'


    #saludo
    hablar(f'{momento}, soy helena, tu asistente personal. porfavor dime en que te puedo ayudar')




#la funcion central del asistente
def pedir_cosas():

    #activar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abrir navegador' in pedido:
            hablar('claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'dime la hora' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            #esto es pa buscar en internet
            pywhatkit.search(pedido)
            hablar('esto es lo que encontre')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea estoy en eso')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip() #strip elimina los espacios en blanco
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'la encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue

        elif 'adiós' in pedido:
            hablar('Me voy a descansar cualquier cosa me avisas')
            break

pedir_cosas()

