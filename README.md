# Cyberoam_automatic_login

Logging into Cyberoam each time you transfer your data limit can be annoying especially when you have some download going on and that gets interrupted. So these python files are an attemt to bring you out of the torment of Cyberoam. Now you can login just once and the script will log you in automatically each time your limit is exceeded.

This repo contains following files: <br />
1. id_extractor_script.py <br />
2. login.py <br />
3. logout.py

#####1. id_extractor_script.py
This script can be used to make a folder containing differnt login IDS. In this script Brute force method is used to check the password against each ID. You will be prompted to enter a password and after that a list of all the possible ID's that can be used for login will be created which will be used by the login.py script.

#####2. login.py
This script is for logging you into Cyberoam. You will have to enter the passwors in string form in the array in this file so that it can log you in Cyberoam by picking up some random ID from the IDS folder which you created by using id_extractor_script.py.

#####3. logout.py
This script is for logging you out from Cyberoam. But before running it make sure you have ended the login.py script by using Keyboard interrupt.

##### IDS Folder
This folder will not be present at first. It will come in form by running id_extractor_script.py against different passwords to give you a list of possible ID's you can use for each password.


### Making logging in more simpler
Instead of going to the folder containing login.py each time you want to log in, you can make an alias for running the script from anywhere in your terminal. Follow these steps: <br />
1. Open terminal and open bash_profile file.<br />
2. You can use any of the editor like vim or sublime. like I use sublime so I will type like this:<br />
ask@macpro$subl ~/.bash_profile <br />
3. In that you will use this following line to create an alias:<br />
alias alias_name="python 'address_of_file/login.py'"<br />
Replace alias_name with your desired alias and address_of_file with the file address where you kept the file.<br />
You can make alias for both login and logout for simplifying the login and logout process.
4. Save bash_profile.
5. Restart you terminal. If you don't restart then you won't be able to use the alias.<br />
6. You are good to go.<br />

### Common Mistakes
1. Not entering the filenames present in IDS folder in the array in login.py.<br />
2. If you are using alias then you will have to give full adresses everywhere thaey are used in these scripts.<br />
