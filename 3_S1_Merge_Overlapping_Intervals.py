def merge_overlapping_intervals(intervals):
  result = []
  if len(intervals) <= 1:
    return intervals
  # loop from 1 to length of intervals
  # perform any applicable merges between current_list and next_list
  # update current_list with next_list
  
  for i in range(1, len(intervals)):
    if intervals[i - 1][1] > intervals[i][0]:
      intervals[i - 1].append(1)
      
      if intervals[i - 1][0] < intervals[i][0]:
        intervals[i][0] = intervals[i - 1][0]
    else:
      intervals[i - 1].append(0)
  
  intervals[-1].append(0)
  
  for interval in intervals:
    if interval[2] == 0:
      result.append(interval[0:2])

  # for each list interval check if the element at current_list[2] is a 1
  # or a 0. If it is a 1, then merge the current_list interval with the next
  # list interval and append to result, if its a 0 then there is no merge
  # merge necessary, so append the result
  # for idx, interval in enumerate(intervals):
  #   # print(intervals[i])
  #   if interval[2] == 1:
  #     # print(intervals[i])
  #     current = interval
  #     next_list = intervals[idx + 1]
  #     if current[2] == 1 and next_list[2] == 1:
  #         result.append([min(current[0:2]), max(next_list[0:2])])
  #     elif current[2] == 1 and next_list[2] == 0:
  #       if len(result) > 0:
  #         tmp = result.pop()
  #         result.append([min(tmp), max(current[0:2])])
  #         tmp = result.pop()
  #         result.append([min(tmp), max(next_list[0:2])])
  #       else:
  #         result.append([min(current[0:2]), max(next_list[0:2])])
  #     intervals.pop(0)
  #   else:
  #     result.append(interval[0:2])
  return result

# print(merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]]))   
# print(merge_overlapping_intervals([[1,3],[2,6],[15,18], [16,20]]))
# print(merge_overlapping_intervals([[1,15],[5,25],[15,40], [20,50], [55,60]]))