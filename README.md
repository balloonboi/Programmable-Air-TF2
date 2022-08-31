# Programmable-Air-TF2
Python and C++ Code to allow the Programmable Air Arduino project to interact with the video game Team Fortress 2 by Valve Software.

# Instructions for Installation
Follow the instructions to get Arduino set up for your Programmable Air unit, listed on the Programmable Air GitHub. (https://github.com/Programmable-Air/Code)

Make note of the COM port that your board is listed under, you will need it to run the program.

Flash the modified FactoryFirmware.ino provided in this repository to your Programmable Air board, using the Arduino IDE.

Download the provided Python script, it should work with any Python version.

# Prerequisites for Launch
Before launching Team Fortress 2 for the first time, locate the folder for the game itself. You can do the following in-game with the developer console, but this makes it easier.

Locate your Team Fortress 2 internal folder, this can be done directly from the Steam client by right clicking on TF2 in the games menu, then "Browse local files", it will come up with your Team Fortress 2 folder, do not close this window for the rest of this tutorial.

In your Team Fortress 2/tf/cfg folder, locate the file autoexec.cfg, if it does not exist, create it manually.

All you need to add is one line to autoexec, that being 
```con_logfile logfilename.log```

Replace logfilename with whatever you would like to name it, but do not include spaces. Make sure it ends with .log as the file extension.

# Launching the Script
Go ahead and launch Team Fortress 2, this will create the log file we set up in the previous step.

Once it loads and you are on the main menu, launch the Python script with your method of choice, making sure your Programmable Air board is plugged into your PC before you do, otherwise it will crash.

It will ask for your Steam username, enter it as it is seen on your profile, it is case-sensitive.

It will then ask for the COM port for your Programmable Air board, it is most likely a single digit number, and it is the same that is seen in the Arduino IDE, type it in here.

Finally, it will open a window and ask for your logfile, it will have the same name you selected in Prerequisites, and be in your Team Fortress 2/tf folder, select it.

If everything went well, it should be up and running, which you can test by opening itemtest, or joining any Community or Casual servers, it will work on any server.

Enjoy!
