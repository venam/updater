import os

p = os.popen("ps -eo pcpu,pid,user,args | sort -k 1 -r|grep /updater.py|awk 'NF='4'{ print $2}'")
p = p.read()
p = p.split('\n')
for a in p:
    try:
        os.kill(int(a),15)
    except:
        print "No such process"

