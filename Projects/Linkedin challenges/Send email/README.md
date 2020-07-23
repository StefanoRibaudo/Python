## Send an email challenge

### Desciption
The aim of this challenge is to write a function that sends an email.

### Solution
I used modules smtplib and ssl to establish connection and send the email. Since this code sends the email from a dummy account, its password is protected in a compiled module.

### Usage
send_email(receiver_email,subject,message) sends an email to receiver_email with appropriate subject and message.