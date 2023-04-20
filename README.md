# discord-bot
Discord bot built with the purpose of practicing developing. Bot has a variety of functions, such as:
-   Set which roles in your server can use certain bot commands
    -   Only Admins can use admin commands
    -   Users with a server role associated with the following **type of role**:
        -   full can use all commands except admin ones
        -   game can only use game commands
        -   text can only use text commands
-   Check **Bot Capabilities** for others

## IMPORTANT
Bot commands are to be prefixed with: !
-   `For example, if you want to run help, do
    -   *!help*
Bot commands aside from admin ones are not available once bot joins the server (currently seeking to update this for admins). To use the set of commands associated to a type of command above, admins must do the following:
-   In your server, create a role with an **alphanumeric** name
-   An admin must run the command *!setup_role "type of role" "name of created role"*
    -   For example, an admin creates the role Authors in their server and want them to only use text commands, thus they will need to run 
    -   *!setup_role text Authors
    -   Then assign everyone (including themselves) who you want to have access to text commands with the Authors role in Discord

An explanation of Admin commands are as follows:
-   *!setup_role*
    -   Format: *!setup_role "type of role" "name of created role"*
    -   Description: associates one of the 3 type of role to a role within the Discord server
-   *!remove_role*
    -   Format: *!remove_role "type of role"*
    -   Description: removes the association of a server role to a type of role  
-   *!list_roles*
    -   Format: *!list_roles*
    -   Description: bot lists the 3 type of role and their associated server role
-   *!help*
    -   Format: *!help*
    -   Description: bot brings up help screen

## Bot Capabilities:
-   Text commands such as:
    -   ...
    -   ...

-   Ability to play games such as TicTacToe and Rock Paper Scissors against another person or bot

