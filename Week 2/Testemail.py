# Send an email with gmail

username = 'email@gmail.com'
password = 'password'
toemail= 'otheremail@gmail.com'
fromEmail = 'email@gmail.com'
message = 'Heres an email'
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(username,password)
server.sendmail(fromEmail,toemail,message)