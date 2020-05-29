import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()   
s.login("sendermail@gmail.com", "pass*****") 
message = "Congrats!! Your model is finally trained"
s.sendmail("sendermail@gmail.com", "recievermail@gmail.com", message) 
s.quit()

#note- this is not the actual code that I have used for mailing
#ofcourse- I have changed the email and pass here :)
