ICS32 Assignment 4: Extending the platform

Created by:
Junyu Li
junyul24@uci.edu


Features of programs:
In programs like Slack, Discord, and Facebook Messenger, keywords can be entered into chat conversations that trigger some sort of automatic inclusion or formatting. 
In computer science, this process is called transclusion, which refers to the process of using a linking syntax to connect or include content from one source into the content of another. 
For this assignment, you will enhance the post writing feature you created in assignment three by adding support for keyword transclusion.

This assignment includes the following files:
a4.py : Use this file as the main program.
ui.py: Use this file to interact with the user.
Profile.py : Provide Post class and Profile class. 
ds_protocol.py: Adaptation of the DSP Protocol.
ds_client.py: Module for connecting to DSP serve and sending messages.
WebAP.pyI: a class contain some methods.
LastFM.py: a class for downloading API information from LastFM website.
OpenWeather.py: a class for downloading API information from OpenWeather website.

Purpose of this program:
This is an interactive tool that will inspect the contents of a folder. The user can use this program to see the contents of a directory or create and delete files.
This program support five command line argument 'L', 'C', 'D', 'R', and 'Q'. "L" is to list the content of a directory, while "Q" quits the program.
This program also support further file operations if the user input L. 
Further options of the 'L' command(not necessary):
    -r : Output directory content recursively.
    -f : Output only files, excluding directories in the results.
    -s : Output only files that match a given file name.
    -e : Output only files that match a given file extension.
For 'C' command, it will create a new file in the specified directory with the specified name and the ‘dsu’ extension.
For 'D' command, it allows the user to delete a DSU file.
For 'R' command, it will print the all contents of a DSU file. 
For 'O' command, it will read and print a piece of information given by the input.
For 'E' command, it will edit the DSU file only after the user use C command or O command.
For 'P' command, it will print information stored in the DSU file only after the user use C command or O command.
For 'V' command, it will allow user to publish information online.

How to use this program:
To use this program, user must input all information in one line, separated by spaces.
The user input for this program will take the following format:
[COMMAND] [INPUT] [[-]OPTION] [INPUT]
[COMMAND] part and [INPUT] part must have content, which means you must input at least two strings.
For 'L' command, you can type up to five strings, for example, you can input this: L /home/algol/ics32/lectures/ -r -e txt
Remember, -f option does not require user to input [INPUT] part, while -s and -e option require user to input [INPUT] part.
For 'C' command, the user must input '-n' as an additional operation, which measn while inputing 'C' command, user must input 4 strings.
For 'D' and 'R' command, the user only be allowed to input two strings as one input.
For 'O' command, it is implemented similar to the 'R' command.
For 'E' command, it will have this format:
	-usr [USERNAME]
	-pwd [PASSWORD]   
	-bio [BIO] 
	-addpost [NEW POST] 
	-delpost [ID]
For 'P' command, it will have this format:
	-usr Prints the username stored in the profile object
	-pwd Prints the password stored in the profile object
	-bio Prints the bio stored in the profile object
	-posts Prints all posts stored in the profile object with their ID (using list index is fine)
	-post [ID] Prints post identified by ID
	-all Prints all content stored in the profile object