import re

def modify_text(command_type, target, text):
  match (command_type):

    case "find":
      return (
        'There are ' + str(text.count(target)) + ' occurances of "' + target 
        + '" in the provided text:\n\n' 
        + text.replace(target, ("**"+target+"**"))
      )
    
    case "replace":
      try:
        in_text = target.split("-")[0]
        to_replace = target.split("-")[1]
      except IndexError:
        return ('Invalid input, missing arguments!')
      text = text.replace(in_text, (to_replace))
      text = text.replace("  ", (" "))
      return (text)
    
    case "remove":
      text = text.replace(target, (text))
      text = text.replace("  ", (" "))
      return (text)
    
    case _:
      return ("Invalid command to modify the text with!")
