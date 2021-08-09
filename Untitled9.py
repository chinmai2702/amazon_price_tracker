from tkinter import *
import requests
from bs4 import BeautifulSoup
import smtplib


window = Tk()
window.title("AMAZON  PRICE  TRACKER")
window.geometry('1100x300')

txt = Entry(window,width=80)
txt1 = Entry(window,width=15)
txt2 = Entry(window,width=50)

lbl = Label(window, text="Welcome")
lbl0 = Label(window,text="")
lbl1 = Label(window,text="")
lbl2 = Label(window,text="")
lbl3 = Label(window,text="")
lbl4 = Label(window,text="")
lbl5 = Label(window,text="")
lbl6 = Label(window,text="Enter you email : ")
lbl7 = Label(window,text="Paste the url here :  ")
lbl8 = Label(window,text="Enter your price :  ")

lbl.grid(column=0, row=0)
lbl0.grid(column=0, row=1)
lbl1.grid(column=0, row=2)
lbl2.grid(column=0, row=3)
lbl3.grid(column=0, row=4)
lbl4.grid(column=0, row=5)
lbl5.grid(column=0, row=6)
lbl6.grid(column=0, row=7)
txt2.grid(column=0, row=8)
lbl7.grid(column=0, row=10)
txt.grid(column=0, row=11)
lbl8.grid(column=0, row=12)
txt1.grid(column=0, row=13)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()    
    server.login('chinmai0227@gmail.com', 'qcgqdqdgnxcvtxaf')    
    subject = 'PRICES FALL DOWN'    
    body = 'check the amazon link '+ txt.get()    
    msg = f"Subject: {subject}\n\n{body}"    
    server.sendmail('chinmai0227@gmail.com', txt2.get(), msg)    
    server.quit()

def con(p):
    s=''
    for i in p:
        if i!=',':
            s=s+i
        else:
            pass
    return s        

def clicked():
    url = txt.get()    
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    by = soup.find(id="bylineInfo").get_text()
    price = soup.find(id='priceblock_dealprice').get_text()
    detail = soup.find(id="acrCustomerReviewText").get_text()
    merchant = soup.find(id='merchant-info').get_text()    
    res=""
    cprice = price[2:]    
    pr=float(con(cprice))    
    maxpr = float(txt1.get())
    if pr < maxpr:
        send_mail()
        res = res+"Email has been sent!!"

    lbl.configure(text= res)    
    lbl1.configure(text= title.strip())    
    lbl2.configure(text= 'BY: '+by)    
    lbl3.configure(text= "OUR PRICE: "+price)    
    lbl4.configure(text= "RATINGS: "+detail)    
    lbl5.configure(text= merchant.strip())
    

btn = Button(window, text="Click Here", command=clicked)
btn.grid(column=0, row=15)
window.mainloop()
