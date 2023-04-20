import re

def readfile(filename):
  textfile = open(filename, 'r')
  data = textfile.read()
  textfile.close()
  return data

# Used to determine if user has a specific role, req_role are user provided and are those stored in roles
# user_discord_roles are provided in a format that can be viewed in examples/discord_roles.txt
# Check if user has a specific role using regex
def checkUserRole(req_role, user_discord_roles):
  my_regex = r"(?<=name=')" + req_role + r"(?=')"
  if re.search(my_regex, user_discord_roles):
    return True
  else:
    return False

# server_role either user provided (!set_role) or empty ("", in !remove_role)
# return false if type_role provided is not one of the 3 required
def setTypeRole(roles, type_role, server_role):
  match (type_role):
    case 'full':
      roles[0] = server_role
    case 'game':
      roles[1] = server_role
    case 'text':
      roles[2] = server_role
    case _:
      return False