import smtplib
import ssl


def send_email(msg, password):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(msg['From'], password)
    result = server.send_message(msg)
    server.quit()
    return result


def build_email(src, dest, sub, msg):
    from time import sleep
    sleep(10)  # To demonstrate why we want a stub for this function
    return {'From': src, 'To': dest, 'Subject': sub, 'Message': msg}
