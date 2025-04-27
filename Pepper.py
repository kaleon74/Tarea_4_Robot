#! /usr/bin/env python
# -- encoding: UTF-8 --


import qi
import os
import sys
import math
import time
import almath
import motion
import argparse


#Definimos la funcion que me permite que Pepper hable 
    
#Presentacion del emprendimiento
def presentacion(animated_speech_service,animation_player_service):
    	os.system("clear")
    	#Texto de Tablet
	animation_player_service.run("animations/Stand/Gestures/Hey_3") 
    	print("Hola, Soy Pepper👋 , asistente de AK WATCH 🤖 y quien te ayudara a escoger el mejor accesorio para elevar tu estilo ⌚ ")
    	animated_speech_service.say("Hola Mucho gusto soy Pepper, tu asistente y Bienvenido a AK WATCH ") #Texto dicho 
    	time.sleep(3)
        return
    
#Se muestra la pagina del emprendimiento     
def pagweb(tablet_service):
    	os.system("clear")
	tablet_service.showImage("http://192.168.0.101:8000/PaginaWEB.jpg")  # Pagina WEB
	time.sleep(2)
	return

def pedido(animated_speech_service,tablet_service,animation_player_service):
	os.system("clear")
	tablet_service.hide()
	animated_speech_service.say("Gracias, por tu Compra, SOMOS AK WATCH")
	time.sleep(3)
	print("Gracias 🫂 por  la compra en las proximas hora llegara tu pedido 📦")
	animation_player_service.run("animations/Stand/Gestures/Hey_3")
	animated_speech_service.say("SIGUENOS, lo mejor solo AQUI")
    	tablet_service.showImage("http://192.168.0.101:8000/follow.jpg")
	return

#Sesion principal de funcionamiento
def main(session):
	
	navigation_service = session.service("ALNavigation")
	motion_service = session.service("ALMotion")
	posture_service = session.service("ALRobotPosture")
	speech_service = session.service("ALTextToSpeech")
	speech_recognition_service = session.service("ALSpeechRecognition")
	animated_speech_service = session.service("ALAnimatedSpeech")
	behavior_service = session.service("ALBehaviorManager")
	tablet_service = session.service("ALTabletService")
	animation_player_service = session.service("ALAnimationPlayer")
	audio_service = session.service("ALAudioDevice")
	system_service = session.service("ALSystem")
	camara_service = session.service("ALVideoDevice")
	photo_service = session.service("ALPhotoCapture")
	
	
	tablet_service.hide()
	

	#Se ejecuta la presentacion del emprendimiento.
	os.system ("clear")
	presentacion(animated_speech_service,animation_player_service)
	pagweb(tablet_service)
	
	#Pregunta por el producto que desea 
	opcion=0
	j=0
	eleccion=0
	imag_relojh=["http://192.168.0.101:8000/RelojCaballero/reloj1.jpg",
        "http://192.168.0.101:8000/RelojCaballero/reloj2.jpg"]

	imag_relojm=["http://192.168.0.101:8000/rRelojDama/reloj1.jpg",
        "http://192.168.0.101:8000/rRelojDama/reloj2.jpg"]

        imag_joyeria=["http://192.168.0.101:8000/Joyeria/joya1.jpg",
        "http://192.168.0.101:8000/Joyeria/joya2.jpg"]

        imag_audi=["http://192.168.0.101:8000/Audifonos/audi1.jpg",
        "http://192.168.0.101:8000/Audifonos/audi2.jpg"]

	while j==0:
		animation_player_service.run("animations/Stand/Gestures/Thinking_1")
		print("Y Dime que Producto te interesa 👀 \n 1. Relojes 🕒\n 2.Joyeria 💍•\n 3.Audifonos\n 4.Salir :D")
    		animated_speech_service.say("En AK Watch tenemos lo mejor, que producto te interesa, Relojes Opcion 1, Joyeria Opcion 2 y Audifonos Opcion 3")
		opcion = input()    
    		if opcion==1:
			animated_speech_service.say("Lo mejor en relojeria claro que si, que Buscas, Opcion 1 Reloj para Caballero, Opcion 2 reloj para Dama")
			print("¿Que Buscas🔎\n 1.Reloj Para Dama👑\n 2. Reloj para Caballero👨")
			animation_player_service.run("animations/Stand/Gestures/Enthusiastic_5")
			eleccion= input()
			if eleccion==1:
				print("Estos son nuestros diseños 😊")
				animated_speech_service.say("CLARO,aqui tienes los diseños que manejamos para DAMA")
        			for img in imag_relojm:
            				tablet_service.showImage(img)
            				time.sleep(3)
				j=1
			elif eleccion==2:
				print("Estos son nuestros diseños �^�^�^�")
                                animated_speech_service.say("CLARO,aqui tienes los diseños que manejamos para CABALLERO")
                                for img in imag_relojh:
                                        tablet_service.showImage(img)
                                        time.sleep(3)
				j=1
    		elif opcion==2:
			print("Estos son nuestros diseños �^�^�^�")
			animated_speech_service.say("CLARO,aqui Joyeria que resalta tu estilo")
        		for img in imag_joyeria:
            			tablet_service.showImage(img)
				time.sleep(2)
			#opcion = 4
			j = 1
			
    		elif opcion==3:
			print("Estos son nuestros diseños �^�^�^�")
			animated_speech_service.say("Los mejores audifonos aqui, a continuacion te los muestro")
        		for img in imag_audi:
            			tablet_service.showImage(img)
            			time.sleep(2)
			j=1
		elif opcion==4:
			j==1
			
    		else:
        		print("Por favor digíte una opción Valida ✅")
        		animated_speech_service.say("Por favor digíte una opción válida, gracias")
        		tablet_service.hide()

        pedido(animated_speech_service,tablet_service,animation_player_service)
      
#Funcion principal para la sesion y conexion con Pepper

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        #IP = raw_input("BIenvenido a la aplicación de Pepper, por favor ingrese la direccion IP")
        IP="127.0.0.1"
        parser.add_argument("--ip", type=str, default=IP,
                                                help="La IP de Pepper. Ambos deben estar conectados a la misma red")
        parser.add_argument("--port", type=int, default=9559,
                                                help="Siempre va a ser el mismo 9559")
        args = parser.parse_args()
        session = qi.Session()
        try:
                session.connect("tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
                print ("Problema al conectarse\"" + args.ip + "\" en el puerto " + str(args.port))
                sys.exit(1)
        main(session)

