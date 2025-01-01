import yagmail
import random
otp=random.randint(100000,999999)
yag = yagmail.SMTP('ayushmaurya7651@gmail.com', 'wwwc txod jkgj lwuw')
subject = 'Welcome to Wealthify!'
body = ('Your one time password (OTP) is '+str(otp))

yag.send("shownknight5@gmail.com", subject, body)

print(otp)
