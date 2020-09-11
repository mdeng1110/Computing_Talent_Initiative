def server_time_check(task_config, task_times):
  sum = 0
  count = 0
  task_config = task_config.split()
  task_times = task_times.split() 
  for n in task_times:
      sum += int(n)
      if sum < int(task_config[1]):
        count += 1
      else:
        break
  return count

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")

print(server_time_check(task_config, task_times))
