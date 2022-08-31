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

# How it works (For those still reading)
The initial program flashed to the Programmable Air unit is a modified version of the default firmware, with extra presets for data sent over serial.
The two I added were the functions pump() and vent().
Both work by recieving data over serial, pump() takes two arguments, the first one being the power of the pump (any integer between 0 and 100) and the second one being the amount of time to turn the pump on for, in seconds.
vent() simply uses the release valve to vent air to the atmosphere. It has one argument, that being the amount of time (in seconds) to vent for.
That's all I added to the stock firmware, I wanted to touch C++ as little as possible.

Finally, the Python script.
I wrote this entirely myself. The first thing it does is set the port to communicate with the Arduino over serial. It then creates two variables, one named kills and one named deaths. It then opens the file that contains the Team Fortress 2 console log, with read and write permissions, and encoded with UTF-8. The encoding in UTF-8 is technically not required, however the program will crash when special Unicode characters are encountered if you don't include it.
It creates an if statement to look for "x killed" in the console log to see if you killed anyone in game. If it finds this line, it will add 1 to the variable "kills", and print the current amount of kills to console.
After that, it sends the keyword vent() over serial to the Arduino, with the number afterwards being replaced with the amount of kills you currently have in this life. Therefore, the more kills you get in a life, the more it will vent to atmosphere and release pressure.
As an added measure, it deletes the line to avoid detection of the same kill multiple times.

After that is an else if statement, very similar to the one for kills, but this time it looks for deaths using the keyword "killed x". If it finds this, it adds to the variable deaths, the same as before, then prints the amount to console. It acts different from the kill detection starting here. It will send the keyword pump() over serial, with the power of the pump being determined with how many kills you got in that life. Being that the power is determined on a scale from 0 to 100, I had it go down with the amount of kills. It divides the amount of kills you got by 5, then subtracts that from the maximum power of 100 to determine the power of the pump when it is turned on. In practice, this means that if you get 20 kills in a life, the pump power will be set to 0. 10 kills will equal 50 percent power, 5 for 75 percent, and so on. Then for determining the amount of time the pump is turned on for, it simply uses the amount of deaths you have gotten this game. The more you die in a game, the longer the pump will turn on for. Finally, it resets the amount of kills in the variable kills to 0, to make sure that the vents do not get too generous. This is the main distinction between the two, kills reset after every life, deaths do not, and persist for the entire time the script is active.
It finishes up by doing the same line deletion as before, to prevent detection of one death as several.
Detection for kills/deaths is repeated every 100 milliseconds.

This code is not perfect, I am terrible at programming and Python is the only language I'd consider myself to be any good at. There is room for optimization and improvement, and if you have any suggestions or issues, dm me and I will see about adding/fixing them.
