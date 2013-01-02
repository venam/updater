# coding: utf-8
import mechanize
import re
import time

class check_the_mails():
    def __init__(self,email,passwd,ID,LOCATION):
        self.email  = email
        self.passwd = passwd
        self.ID     = ID
        self.LOCATION = LOCATION

    def run(self):
        br=mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_gzip(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3')]
        try:
            br.open("https://mid.live.com/si/login.aspx?wa=wsignin1.0&rpsnv=11&ct=1338648316&rver=6.1.6206.0&wp=MBI&wreply=http%3a%2f%2fdu107w.dub107.mail.live.com%2fm%2f%3frru%3dinbox%26lc%3d1033%26mlc%3den-US&lc=1033&id=64855&mspco=1", timeout=20)
            br.select_form(nr=0)
            br.form['LoginTextBox']=self.email
            br.form['PasswordTextBox']=self.passwd
            br.submit()
            br.open("http://sn118w.snt118.mail.live.com/md/folders.aspx")
            try:
                number = re.findall('Inbox (.*)</a></td>',br.response().read())
                number = number[0].replace('&#40;','&#41;').replace('&#41;','')
                if number!="" :
                    #open msg and show first msg
                    br.open("http://sn118w.snt118.mail.live.com/md/folder.aspx?fid=00000000-0000-0000-0000-000000000001")
                    msg=re.findall('bold;\">(.*)</a></td>',br.response().read())[0]
                    msg = msg.replace('&#58;',':')
                    msg = msg.replace('&#233;','e')
                    msg = msg.replace('&#39;', "'")
                    msg = msg.replace('&#33;', "!")
                    msg = msg.replace('&#38;',"&")
                    for i in xrange(10000):
                        msg=msg.replace('&#'+str(i)+";",'')

            except:
                msg = "None"
                number= '0'

            msg_old = re.findall(self.ID+':(.*)\n', open(self.LOCATION+"config", 'r').read())[0]
            number_old = re.findall(self.ID+'N:(.*)\n', open(self.LOCATION+"config", 'r').read())[0]
            if number_old!=number:
                #change the num
                open(self.LOCATION+"config.bak","w").write(open(self.LOCATION+"config", "r").read())
                open(self.LOCATION+"config","w").write(open(self.LOCATION+"config.bak", "r").read().replace(self.ID+"N:"+number_old, self.ID+"N:"+number))
            if msg_old!=msg:
                #change the msg
                open(self.LOCATION+"config.bak","w").write(open(self.LOCATION+"config", "r").read())
                open(self.LOCATION+"config","w").write(open(self.LOCATION+"config.bak", "r").read().replace(self.ID+":"+msg_old, self.ID+":"+msg))
        except:
            time.sleep(2)
            checkmail(self.email,self.passwd,self.ID)

