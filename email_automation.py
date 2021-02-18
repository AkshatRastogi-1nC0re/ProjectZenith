import smtplib


def send_mail(list_emails, message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("","")
    server.sendmail('project.zenith11@gmail.com',list_emails,message)
