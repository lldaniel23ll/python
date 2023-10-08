import smtplib

user = 'djimenezsoza@gmail.com'
password = 'dn^v$!!z!qe4@'
sender = 'lldaniel23ll@protonmail.com'
message = 'Hi, this is a test'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server. login(user, password)
server.sendmail(user, sender, message)
server.quit()

print ("Email sended succesfully!")