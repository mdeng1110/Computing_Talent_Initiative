dependencies = {
  "name": "my_cool_software",
  "version": "1.0.0",
  "dependencies": {
    "xmllib": { 
      "version": "0.2.3",
      "name": "xmllib",
      "dependencies" : {
          "parser": {
            "name": "parser",
            "version": "1.2.1"
          },
          
        }
      },
      "parser": {
        "name": "parser",
        "version": "1.4.6"
       }
    }
}

def flatten_dependencies(dependencies):
  dict = {}
  results = dependencies["dependencies"]
  dependency_counter = {}
  for key, value in results.items():
    dependency = value
    if key not in dependency_counter:
      dependency_counter[key] = 1
    else:
      dependency_counter[key] += 1
    
    if dependency.get('dependencies'):
      for k, v in dependency['dependencies'].items():
        if k not in dependency_counter:
          dependency_counter[k] = 1
        else:
          dependency_counter[k] += 1
  
   
  for key, value in results.items():
    if dependency_counter[key] > 1:
      # print(key)
      new_key = '{KEY}@{VERSION}'.format(KEY=key, VERSION=results[key]['version'])
      dict[new_key] = results[key]['version']
      dependency = value
      if dependency.get('dependencies'):
        for k, v in dependency['dependencies'].items():
          new_k = '{KEY}@{VERSION}'.format(KEY=k, VERSION=dependency['dependencies'][k]['version'])
          dict[new_k] = dependency['dependencies'][k]['version']
    else:
      dict[key] = results[key]['version']
      dependency = value
      if dependency.get('dependencies'):
        for k, v in dependency['dependencies'].items():
          new_k = '{KEY}@{VERSION}'.format(KEY=k, VERSION=dependency['dependencies'][k]['version'])
          dict[new_k] = dependency['dependencies'][k]['version']
    # # print("dependency: ", dependency)
    # dict[dependency['name']] = dependency['version']
    # if dependency.get('dependencies'):
    #   print(dependency['dependencies'])
    #   dict[dependency['name']] = dependency['name'] + '@' + dependency['version'] 
  return dict
print(flatten_dependencies(dependencies))
