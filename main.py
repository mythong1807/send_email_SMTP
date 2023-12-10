import smtplib

my_email = "mythongttt@gmail.com"
my_password = "obqv vnme gafr ssqf"
receiver_list = ["mythonggg@gmail.com", "iampanda18072005@gmail.com", "mythongtt@gmail.com"]

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs=receiver_list[0], msg="Subject:Happy birthday\n\nHappy birthday my bro wish you best things!")
connection.close()