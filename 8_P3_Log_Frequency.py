test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]
def log_stats(logs):
  logs_dict = {}
  for log in logs:
    log = log.split(":")
    log_level = log[0].split("]")[0][1:]
    error_code = log[0].split()[1]
    category = " ".join(log[0].split()[2:])
    description = log[1].lstrip()
    #print(log_level)
    if log_level not in logs_dict:
      logs_dict[log_level] = {}
    
    if error_code not in logs_dict[log_level]:
      logs_dict[log_level][error_code] = {}
    
    if category not in logs_dict[log_level][error_code]:
      logs_dict[log_level][error_code][category] = {}

    if description not in logs_dict[log_level][error_code][category]:
      logs_dict[log_level][error_code][category][description] = 1
    else:
      logs_dict[log_level][error_code][category][description] += 1
      
  return logs_dict
# [WARNING]   403        Forbidden: No token in request parameters'
# {Log Level}{Error Code} {Category}       {Description :value(number of times it appeared)}
# have a list of strings
# loop over the string to create dictionary of dictionaries
# work on the string to create dictionaries.  turn string to dict. 
