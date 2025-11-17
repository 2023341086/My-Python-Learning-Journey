
def scores_statistic():  
   numbers = []
   print("请输入10个成绩：")
   for i in range(0,10):
       n=i+1
       num = int(input("成绩"+str(n)+":" ))
       numbers.append(num)
   print("\n输入的成绩: "+str(numbers))

   total = 0
   for num in numbers:
       total += num
   print("数字总和: "+str(total))

   max_num = numbers[0]
   for num in numbers:
       if num > max_num:
           max_num = num
   print("最大数字: "+str(max_num))
 
   for num in numbers:
       if num >=60:
           continue
       print("检测出的不及格的成绩："+str(num))

scores_statistic()


