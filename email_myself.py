import smtplib
import base64

def email_hashtags(content):
    informationList = []
    SUBJECT = "Daily Instagram Hashtags"

    with open('../info.txt', 'r') as f:
        for line in f:
            for word in line.split():
                decodedWord = base64.b64decode(word)
                informationList.append(decodedWord)

    # Set UTF-8 after decoding hashed data
    hashedEmail = informationList[0].decode("utf-8")
    hashedAppPassword = informationList[1].decode("utf-8")

    # Set header
    content = 'Subject: {}\n\n{}'.format(SUBJECT, content)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(hashedEmail, hashedAppPassword)
    mail.sendmail(hashedEmail, hashedEmail, content)
    mail.close()
