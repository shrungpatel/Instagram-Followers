# Instagram-Followers
A simple Python script which tells you the list of people that do not follow you back on Instagram.

# How to run and use the script
## Download your Instagram data
Go to the menu bar in the top right of your profile section and go to "My Activtiy".
Click on "Download your information".
You will be asked about how much information you want to download where you should click on the option saying only some.
  Scroll down till you see connections and click on "Followers and Following".
Request your download and wait for an email containing the zip file.
There might be a lot of files in that folder but only two are relevant for us (followers and following).
## Run the script
Open the script in your preferred Python IDE. https://www.onlinegdb.com/online_python_compiler is one that is easy to work with.
Upload the two JSON files and run the .py file.
That's it!

# Background
I initially wrote a program in Java in the summer of 2021 to find this out. The program was a little different in that you would need to open up the desktop version of Instagram and Ctrl-A/Cmd-A to copy your following/followers and paste into its respective file. When I tried doing this in 2024, it turned out that Instagram removed this feature so I had to find an alternative which led me to the "download your information" section. Instagram does not have an API for the public to use so it is a little inconvinent to run the script.
Yes the script is only 4 lines long, that's the beauty of set comprehensions in Python (although I guess the code is not that fun to read because of it).
