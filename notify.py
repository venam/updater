# coding : utf-8
import os,re

def check_pkg(LOCATION):
    oldnum=re.findall('PKGS:(.*)\n', open(
        LOCATION+"config", 'r').read()
        )[0]
    try:
        p = os.popen("pacman -Qu |wc -l")
        p = p.read()
        p = p.rstrip()

        if ':'+p+' New pkg' not in oldnum :
            if p!= '0':
                open(LOCATION+"config.bak","w").write(
                    open(LOCATION+"config", "r").read()
                    )
                open(LOCATION+"config","w").write(
                    open(LOCATION+"config.bak", "r").read().replace(
                        "PKGS:"+oldnum, "PKGS:"+p+" New Pkg"
                        )
                    )
            else:
                open(LOCATION+"config.bak","w").write(
                    open(LOCATION+"config", "r").read()
                    )
                open(LOCATION+"config","w").write(
                    open(LOCATION+"config.bak", "r").read().replace(
                        "PKGS:"+oldnum, "PKGS:"+"Up-To-Date")
                        )
    except Exception,e:
        print e
