import re

def modify_text(message):
  try:
    command_type = message.split()[0]
    scope = (message.split()[1])
    target = (message.split()[2])
    text = (message.split(":")[1]).lstrip()

    if (target[-1] != ":"):
      return ('Invalid input, missing arguments!')
    else:
      target = target[:-1]

  except IndexError:
    return('Invalid input, missing arguments!')
  
  match (command_type):
    #-------------------------------------------------------------------------
    case "find":
      my_regex = checkScope(scope, target)
      if my_regex == False:
        return('Invalid input, incorrect scope!')
      
      if scope == "case_spec":
        num_occurances = str(len(re.findall(my_regex, text)))
        return_text = replaceFunction(my_regex, ("**"+target+"**"), text, True)
      else:
        num_occurances = str(len(re.findall(my_regex, text, re.IGNORECASE)))
        return_text = replaceFunction(my_regex, ("**"+target+"**"), text)

      return (
        'There are ' + num_occurances + ' occurances of "' + target 
        + '" in the provided text:\n\n' + return_text
      )
    
    #-------------------------------------------------------------------------
    case "replace":
      try:
        in_text = target.split("-")[0]
        to_replace = target.split("-")[1]
      except IndexError:
        return ('Invalid input, missing arguments!')
      
      my_regex = checkScope(scope, in_text)
      if my_regex == False:
        return('Invalid input, incorrect scope!')
      
      if scope == "case_spec":
        return_text = replaceFunction(my_regex, to_replace, text, True)
      else:
        return_text = replaceFunction(my_regex, to_replace, text)
      
      return (return_text)
    
    #-------------------------------------------------------------------------
    case "remove":    
      my_regex = checkScope(scope, target)
      if my_regex == False:
        return('Invalid input, incorrect scope!')
      
      if scope == "case_spec":
        return_text = replaceFunction(my_regex, "", text, True)
      else:
        return_text = replaceFunction(my_regex, "", text)
      
      return_text = replaceFunction("  ", " ", return_text)
      return (return_text)
    
    #-------------------------------------------------------------------------
    case _:
      return ("Invalid command to modify the text with!")
    

# func below taken from stackoverflow, works to replace a string keeping the case of the original word
# https://stackoverflow.com/questions/24893977/whats-the-best-way-to-regex-replace-a-string-in-python-but-keep-its-case
def replaceFunction(in_text, to_replace, text, case=None):
  if case:
    return re.sub(in_text, to_replace, text)
  
  def func(match):
    g = match.group()
    if g.islower(): return to_replace.lower()
    if g.istitle(): return to_replace.title()
    if g.isupper(): return to_replace.upper()
    return to_replace      
  return re.sub(in_text, func, text, flags=re.I)

def checkScope(scope, target):
  match (scope):
    case "all":
      return (target)
    case "spec":
      return ("\\b" + target + "\\b")
    case "case_spec":
      return ("\\b" + target + "\\b")
    case _:
      return False

