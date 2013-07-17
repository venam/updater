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

def check_the_email(LOCATION,domain,user,passwd):
    try:
        p = imaplib.IMAP4(domain)
        p.login(user,passwd)
        p.select()
        index, data   = p.search(None, 'UnSeen')
        number_of_msg = 0
        sender_array  = []
        subject_array = []

        for num in data[0].split():
            k = p.fetch(num, '(BODY.PEEK[])')[1][0][1]
            k = k.split("\n")
            for a in k:
                a = a.rstrip()
            for internal in k:
                if internal.startswith("From:"):
                    sender_array.append(internal)
                if internal.startswith("Subject:"):
                    subject_array.append(internal)
        number_of_msg = len(subject_array)

        old_nb_msg = re.findall("Nb Msg: (.*)\n", open(
            LOCATION+"config",'r').read()
            )[0]
        all_emails = open(LOCATION+"config",'r').read().split("Nb Msg: "+old_nb_msg)[1]
        if int(old_nb_msg) != number_of_msg:
            nb = "{0}".format(number_of_msg)
            #backup the configs
            open(LOCATION+"config.bak","w").write(
                open(LOCATION+"config", "r").read()
                )
            if number_of_msg == 0 :
                string = "- No Emails - \n"
            else:
                string = ""
                i = 0
                for a in sender_array:
                    string +=  a + "\n"
                    string +=  subject_array[i] + "\n"
                    i+=1
            open(LOCATION+"config","w").write(
                open(LOCATION+"config.bak", "r").read().replace(
                    "Nb Msg: "+old_nb_msg+all_emails , "Nb Msg: " + nb + "\n" +string
                    )
                )

    except Exception,e:
        print e
