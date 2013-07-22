##Venam updater

This is an updater program that comes with a frontend.
It shows updates about:
* packages
* news
* weather
* mangas
* emails

###How to use
* Open the files configuration.py and update to your needs.
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

###TODO
I'm currently updating the code and adding sub-menus to the interface.
For example, it would be nice to just press 'D' or 'd' to open the available manga to download and then only have to choose between them to start the mangaDL.

