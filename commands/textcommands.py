import re

def modify_text(message):
  try:
    command_type = message.split()[0]
    target = (message.split()[1])
    text = (message.split(":")[1]).lstrip()

    if (target[-1] != ":"):
      return ('Invalid input, missing arguments!')
    else:
      target = target[:-1]

  except IndexError:
    return('Invalid input, missing arguments!')
  
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
      text = text.replace(target, (""))
      text = text.replace("  ", (" "))
      return (text)
    
    case _:
      return ("Invalid command to modify the text with!")
