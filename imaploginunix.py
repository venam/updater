import imaplib
import re
"""
FLAGS:
        \Seen       Message has been read

        \Answered   Message has been answered

        \Flagged    Message is "flagged" for urgent/special attention

        \Deleted    Message is "deleted" for removal by later EXPUNGE

        \Draft      Message has not completed composition (marked as a
                    draft)
        \Recent
"""
def check_the_email(LOCATION):
    try:
        p = imaplib.IMAP4("unixhub.net")
        p.login("email","pass")
        p.select()
        index, data   = p.search(None, 'UnSeen')
        number_of_msg = 0
        sender_array  = []
        subject_array = []

        for num in data[0].split():
            a = p.fetch(num, '(BODY.PEEK[])')[1]
            for b in a[0]:
                if b.startswith("Return-Path:"):
                    number_of_msg+=1
                    c= b
                    c = c.split(">")
                    kk = c[0]
                    kk = kk.split("<")
                    sender_array.append(kk[1])
                    for j in c :
                        stri = re.findall("Subject: (.*)\n",j)
                        if len(stri)>=1:
                            subject_array.append(stri[0])
        old_nb_msg = re.findall("Nb Msg: (.*)\n", open(LOCATION+"config",'r').read() )[0]
        all_emails = open(LOCATION+"config",'r').read().split("Nb Msg: "+old_nb_msg)[1]
        if int(old_nb_msg) != number_of_msg:
            nb = "{0}".format(number_of_msg)
            open(LOCATION+"config.bak","w").write( open(LOCATION+"config", "r").read() )

            if number_of_msg == 0 :
                string = "- No Emails - \n"
            else:
                string = ""
                i = 0
                for a in sender_array:
                    string += "Sender : " + a + "\n"
                    string += "Subject: " + subject_array[i]
                    string += "\n"
                i+=1
            open(LOCATION+"config","w").write( open(LOCATION+"config.bak", "r").read().replace("Nb Msg: "+old_nb_msg+all_emails , "Nb Msg: " + nb + "\n" +string ) )
    except Exception,e:
        print e
