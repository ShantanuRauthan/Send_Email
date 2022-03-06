import smtplib
import ssl
import imghdr
from email.message import EmailMessage  


#defining the email mandate feilds
subject = "This is a Test Email"
receiver_email = "enter receivers email"
sender_email = "enter your email"
password = input("Enter your password: ")
print("")
body = "This is a test email! Testing out automation using python"

message = EmailMessage()      

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(body)


with open('ss.png','rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)   #remove this if you re sening pdf or an application
	file_name = f.name

message.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)


#create a secure connection 
context = ssl.create_default_context()

print("Sending Email..........")

#sending email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email,receiver_email,message.as_string())
print("Success! Email Sent")


