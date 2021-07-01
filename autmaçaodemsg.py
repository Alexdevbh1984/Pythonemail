import pandas as pd
import smtplib
email_meu = "alexribeirobuildtec@gmail.com"
email_dele = "praontemeltrica12345@gmail.com"

smtp = "smtp.gmail.com"

server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_meu, open('senha.txt').read().strip())
 
msg = ('''Deixe o like !e se escreva no canal ''')




server.sendmail(email_meu, email_dele, msg)
server.quit()


print("Sucesso ao enviar o email")