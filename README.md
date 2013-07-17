##Venam updater

This is an updaater program that comes with a frontend.
It shows updates about:
* packages
* news
* weather
* mangas
* emails

###How to use
* Install the mechanize module.
* Open the files updater-frontend.py and updater.py anc change : `LOCATION` by the location of the config file.
* Update the updater.py file to your needs.
* Add a symlink to uppdater.py and updater-frontend.py to your bin or create a script in you bin dir starting the program.
* You can use this as an example. :
<pre>
#!/bin/bash
python2 /home/raptor/.my_updater/killer.py;
python2 /home/raptor/.my_updater/pythondaemon.py /home/raptor/.my_updater/updater.py;
</pre>
* Start the frontend script.
* Quit the frontend by pressing `q` or `Q`
* Kill the updater.py daemon by using the killer.py script

###Scrot
![Srcot](https://raw.github.com/venam/updater/master/scrot.png)
