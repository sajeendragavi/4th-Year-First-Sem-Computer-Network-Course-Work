import socket
from sys import platform
from subprocess import check_output
import time
import telnetlib
import subprocess
import smtplib  
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("CS-MAIL")

from smtplib import SMTP



def send_part(event):
    from_addr = userNameEnt.get()
    to_addr = receiverEmailEnt.get()
    msg = textMessageArea.get("1.0", "end-1c")

    # #print file_content)


    with SMTP("localhost:25") as smtp:
        noop_answer = smtp.noop()
        if noop_answer == (250, b'Ok'):
            try:
                helo_answer = smtp.helo(name=domainArea.get())
                smtp.sendmail(from_addr, to_addr, msg)

            except SMTP.SMTPRecipientRefused:
                print("ERROR: Recipient refused")
            except SMTP.HeloError:
                print("ERROR: Helo error")
            except SMTP.SMTPSenderRefused:
                print("ERROR: Sender Refused")
            except SMTP.DataError:
                print("ERROR: Data error")

        else:
            print("ERROR: NOOP answer not equal (250, OK)")
            exit()
            
    file_open = open("mail_info.txt")
    file_content = file_open.read().rstrip("\n")
    output_l1 = Label(root,text = file_content)
    output_l1.grid(row=5, column=8, columnspan=3, pady=20, padx=10)
    file_open.close()


userNameLbl = Label(root, text="Sender Email Address")#
userNameEnt = Entry(root)#


userNameLbl.grid(row=0, column=0)
userNameEnt.grid(row=0, column=1, pady=5)

#textArea = Text(root)
#textArea.grid(row=5, column=8, columnspan=3, pady=20, padx=10)



receiverEmailLbl = Label(root, text="Receiver Email Address")  #write message
receiverEmailEnt = Entry(root)

receiverEmailLbl.grid(row=0, column=8)
receiverEmailEnt.grid(row=0, column=9, pady=5, padx=5)


textMessageArea = Text(root)
textMessageArea.grid(row=5, column=0, columnspan=7, pady=20)




#fo = open('mail_info.txt','r')
#msg_out = ""
#for x in fo.readlines():





domainLbl = Label(root, text="domain")
domainLbl.grid(row=0, column=4)

domainArea = Entry(root)
domainArea.grid(row=0, column=5, pady=5)

sendMessageBtn = Button(root, text="Send Message")
sendMessageBtn.grid(row=0, column=10)

sendMessageBtn.bind("<Button-1>", send_part)



root.mainloop()
