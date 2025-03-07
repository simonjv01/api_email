import smtplib, ssl



host = "smtp.gmail.com"
port = 465

username = "sjvargas01@gmail.com"
password = ""

receiver = "sjvargas01@gmail.com"
context = ssl.create_default_context()

message = """
Subject: Test Email"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)