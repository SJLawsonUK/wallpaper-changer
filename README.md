# wallpaper-changer

Python3 app that creates a xml document that can be used in Linux to provide a
desktop background slideshow similar to "cosmos" that is included with the OS

App uses jpg files found recursively in the /home/username/Pictures folder
the jpgs are checked first to ensure they are valid jpg files

tran_time = "5.0"  ... transistion time is set at 5 secs (gives Gnome time to line-up next file)
dura_time = "195.0" ... time between changes

Change the dura_time to suit yourself

The backgrounds.xml file created loops through pictures - just ADD it to your
Appearance Preferences under the Background tab.
