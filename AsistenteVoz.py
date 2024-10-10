import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# Escuchar nuestro microfono y devolver el audio como texto
def transformarAudioEnTexto():
    # Almacenar el reconocedor en una variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google (corrección del nombre del parámetro)
            pedido = r.recognize_google(audio, language='es-CO')

            # Prueba de que pudo transformar la voz en texto
            print(f"Dijiste: {pedido}")

            # Devolver el pedido
            return pedido

        # En caso de que no comprenda
        except sr.UnknownValueError:

            # Prueba de que no comprendió el audio
            print("Ups! No entendí")

            # Devolver error
            return "Sigo esperando"

        # En caso de recibir el pedido
        except sr.RequestError:

            # Prueba de que no hay servicio
            print("Ups! No hay servicio")

            # Devolver error
            return "Sigo esperando"

        # Error inesperado
        except:
            # Prueba de que algo salió mal
            print("Ups! Algo ha salido mal")

            # Devolver error
            return "Sigo esperando"


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronuncias mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedirDia():
    # Crear variable de datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario que tenga los nombres de los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Vierenes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Diacir dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")


# Informar que hora es
def pedirHora():
    # Crear variable con datos del a hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} y {hora.minute}'
    print(hora)

    # Decir la hora
    hablar(hora)


# Funcion saludo inicial
def saludoInicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 >= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir saludo
    hablar(f"Hola, {momento}, soy elena, tu asistente personal. Dime que necesitas")


# Funcion central del asistente
def pedirCosas():
    # Activar el saludo iniciar
    saludoInicial()

    comenzar = True
    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformarAudioEnTexto().lower()

        if 'abrir youtube' in pedido:
            hablar('Okey, estoy abriendo YouTube')
            webbrowser.open('https://www.YouTube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Okey, voy a abrir tu navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedirDia()
            continue
        elif 'qué hora es' in pedido:
            pedirHora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedía dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar("Buscando en internet")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
        elif 'reproducir' in pedido:
            hablar("Ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'adiós' in pedido: 
            hablar("Está bien... Me voy a descansar, cualquier cosa me avisas")
            break


pedirCosas()
