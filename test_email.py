# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# set the text file
textfile = "my_email_content.txt"

# Open the plain text file whose name is in textfile for reading.
with open(textfile, "r", encoding="utf-8") as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

me = "harry1318945@gmail.com"
you = "harry.j.wilson@icloud.com"
msg["Subject"] = f"The contents of {textfile}"
msg["From"] = me
msg["To"] = you

# Send the message via Google's real SMTP server
# 587 is the standard port for TLS secure mail
with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()  # Secures the connection

    # Use your Gmail address and your 16-character App Password
    s.login(me, "qvev shkz kcet crza")
    s.send_message(msg)


print("Sent")
