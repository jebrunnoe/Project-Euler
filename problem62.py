start = 2
end = 10000
dic = {}
for n in range(start, end):
   cube_str = str(n ** 3)
   cube_sort = ''.join(sorted(cube_str))
   value = dic.get(cube_sort)
   if value == None: dic[cube_sort] = [n]
   else:
      value.append(n)
      dic[cube_sort] = value
      if len(value) >= 5:
         print value
         break     
 
