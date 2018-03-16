# slack-basic-lottery
Lottery commands for Slack, written in python 2.7

You need to set up every command in the Slash Command custom integration: https://sbltw.slack.com/apps/A0F82E8CA-slash-commands

They should all use the POST Method, no tokens are needed.


The commands are:

/sbl_list  For checking currently active tickets.

/sbl_get [name] [number of tickets]  For registering tickets, it will use your username if you don't provide a name.

/sbl_draw  For getting a winner.

/sbl_reset  For deleting ALL current tickets.

/sbl_help  To display info.

/sbl_test  To add test entries to the lottery.


You can edit the variables from line 11 to 35 to translate the program to other languages.
