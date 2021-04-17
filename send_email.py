import smtplib

#create smtp object for the server
smtp_object =smtplib.SMTP('smtp.gmail.com', 587)

#greets the server and establishes a connection

smtp_object.ehlo()

#initiate encryption

smtp_object.starttls()

#never send raw string or email in a script. Any can see it you email and password
#always use getpass when the password has to be entered

import getpass

#password = getpass.getpass ("Password Please:   ")

#need to generate an app password

#setup 2 step verification

email = getpass.getpass("Email:  ")
password = getpass.getpass ("Password: ")
smtp_object.login(email, password)


from_address = email
to_address = email
subject = input("Enter subject line: ")
message = input("Enter body of message: ")
msg = "Subject: "+subject+'\n'+ message


smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()

