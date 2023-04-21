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
-   For example, if you want to run help, do
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
Text commands such as:
-   !*modTxt*
    -   Format: *!modText "command_type" "scope" "target": "text"*
    -   Description: bot either modifies or determine details of provided text
        -   *"command_type"*, one of:
            -   **find** (find # of occurences of "target" in a "text", returns it with all occurences highlighted)
            -   **replace** ("target" takes format of "in_text"-"to_replace", replaces all occurences of "in_text" with "to_replace")
        -   *"scope"*, one of:
            -   **all** (all possible matches)
            -   **spec** (only the specific word)
            -   **case_spec** (only the specific word, case sensitive)
        -   *"target"*
            -   word we wish to do something with
            -   **EXCEPT** when using command type **replace**, then "target" takes the format of "in_text"-"to_replace"
        -   *"text"*
            -   text we wish to modify or analyze

    -   Examples:
        -   We want to find all occurences of mike in a text (including in stuff like mikeimator or so), we do:
            -   !modTxt find all mike: "text"
        -   We want to replace Mike (case sensitive) and only Mike in a text with Adam
            -   !modTxt replace case_spec Mike-Adam: "text"
    

-   Ability to play games such as TicTacToe and Rock Paper Scissors against another person or bot

