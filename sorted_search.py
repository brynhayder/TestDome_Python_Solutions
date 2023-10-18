import bisect 

def count_numbers_slow(sorted_list, less_than):
  count = 0
  for x in sorted_list:
    if x < less_than:
      count += 1
    else:
      break
  return count

def count_numbers(sorted_list, less_than):
  return bisect.bisect_left(sorted_list, less_than) 

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2
