import smtplib


def send_mail(list_emails, message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("project.zenith11@gmail.com","testing@123")
    server.sendmail('project.zenith11@gmail.com',list_emails,message)