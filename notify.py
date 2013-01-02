# coding : utf-8
import subprocess, re,time

def check_pkg(LOCATION):
    oldnum=re.findall('PKGS:(.*)\n', open(LOCATION+"config", 'r').read())[0]
    #try:
    #    subprocess.check_output(['sudo','pacman','-Sy'])
    #except:
    #    pass
    try:
        number = subprocess.check_output(['pacman','-Qu'])
        number = number.split("\n")
        i=0

        for a in number:
            i+=1

        if str(i-1) not in oldnum :

            if i==2:
                #change the num
                open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
                open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("PKGS:"+oldnum, "PKGS:"+"1 New Pkg"))
            if i>2:
                open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
                open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("PKGS:"+oldnum, "PKGS:"+str(i-1)+" New pkgs"))

    except:
        if oldnum!="Up-To-Date":
            open(LOCATION+"config.bak","w").write(open(LOCATION+"config", "r").read())
            open(LOCATION+"config","w").write(open(LOCATION+"config.bak", "r").read().replace("PKGS:"+oldnum, "PKGS:"+"Up-To-Date"))
