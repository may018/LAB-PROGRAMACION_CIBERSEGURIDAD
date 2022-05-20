#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data={
    "usr" : "mayela.brionesnz@uanl.edu.mx"
    "pws" : "********"
}

def EnviarCorreo(message, receipents)
    with open("pws.json") as f:
        data = json.load(f)


    email_msg = MIMEMultipart()
    email_msg["De"] = data["usr"]
    receipents
    email_msg["Hacia"] = ", ".join(receipents)
    email_msg["Cabecera"] = "Hola, envio desde practica"


    email_msg.attach(MIMEText(message, "plain"))
    server = smtplib.SMTP("smtp.office365.com:587")
    server.starttls()

    server.login(data["usr"], data["pws"])



    server.sendmail(email_msg["De"], receipents, email_msg.as_string())
    server.quit()
    print("Se ha enviado exitosamente %s:" % (email_msg["a"]))

def main():

    ayudame =    ("Podras enviar informacion importante e inmediata"
                    "\n Para ingresar tu remitente ingresa -r"
                    "\n Para enviar un mensaje presiona -m")


    verifica = argparse.ArgumentParser(ayudame)
    verifica.add_argument('-r', '--remitente', type=str, 
                            help="Para ingresar tu remitente ingresa")
    verifica.add_argument('-m', '--mensaje', type=str, 
                            help="Para enviar un mensaje presiona")
    argumentos = verifica.parse_args()

    if argumentos.remitente is not None:
        EnviarCorreo(argumentos.mensaje, argumentos.remitente)

if __name__ == "__main__":
    main()