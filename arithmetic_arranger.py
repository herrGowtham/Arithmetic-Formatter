def arithmetic_arranger(arithmetic_problems,answer = False):

  problem_list = []
  long_len = []
  temp_list1,temp_list2,temp_list3,temp_list4 = ([] for i in range(4))
  
  if (len(arithmetic_problems) > 5):
    return("Error: Too many problems.")
    
  for problem in arithmetic_problems:
    
    problem_subset = problem.split()
    problem_list.append(problem_subset)
    
    if len(problem_subset[0]) > 4 or len(problem_subset[2]) > 4:
      return("Error: Numbers cannot be more than four digits.")
    
    if '+' not in problem_subset and '-' not in problem_subset:
      return("Error: Operator must be '+' or '-'.")

    if not str.isdigit(problem_subset[0]):
      return("Error: Numbers must only contain digits.")
    if not str.isdigit(problem_subset[2]):
      return("Error: Numbers must only contain digits.")

  for i in range(len(arithmetic_problems)):
    long_len.append(max(len(problem_list[i][0]),len(problem_list[i][2])))
    temp_list1.append(problem_list[i][0].rjust(long_len[i]+2))
    temp_list2.append(problem_list[i][1]+" "+problem_list[i][2].rjust(long_len[i]))
    temp_list3.append("-" * (long_len[i]+2))
    if problem_list[i][1] is '+':
      temp_list4.append(str(int(problem_list[i][0]) + int(problem_list[i][2])).rjust(long_len[i]+2))
    else:
      temp_list4.append(str(int(problem_list[i][0]) - int(problem_list[i][2])).rjust(long_len[i]+2))

  if answer is True:
      return('    '.join(temp_list1)+"\n"+'    '.join(temp_list2)+"\n"+'    '.join(temp_list3)+"\n"+'    '.join(temp_list4))

  else:
    return('    '.join(temp_list1)+"\n"+'    '.join(temp_list2)+"\n"+'    '.join(temp_list3))
