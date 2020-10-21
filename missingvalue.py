
def MissingDigit(strParam):
  splited_str_=[ (i,v.strip()) for i,v in enumerate(strParam.split("="))  ]
  splited_str= []
  for i,k in splited_str_:
    sub=[]
    for v in k:
      if v.strip() !='':
        sub.append(v)
    splited_str.append((i,''.join(sub)))
  
  splited_op=[]
  for i,v in splited_str:
    if "x" in v and i == 0:
      if "+" in v:
        # x in 0 index and +
        index_x=[(index,v) for index , v in enumerate(v.split("+")) ]
        
        if index_x[0][0] == 0 and "x" in  index_x[0][1]: # index 0[(,)]
          split_ax =index_x[0][1].index('x')
          result = str(int(splited_str[1][1]) - int(index_x[1][1]))[split_ax]
          return result
        elif index_x[1][0] == 1 and "x" in  index_x[1][1]: # index 1[(,)]
          
          split_ax =index_x[1][1].index('x')
          result = str(int(splited_str[1][1]) - int(index_x[0][1]))[split_ax]
          return result

        
      # x in O index and -
      elif "-" in v:
        index_x=[(index,v) for index , v in enumerate(v.split("-")) ]
       
        if index_x[0][0] == 0 and "x" in  index_x[0][1]: # index 0[(,)]

          split_ax =index_x[0][1].index('x')
          result = str(int(splited_str[1][1]) + int(index_x[1][1]))[split_ax]
          return result
        elif index_x[1][0] == 1 and "x" in  index_x[1][1]: # index 1[(,)]
          
          split_ax =index_x[1][1].index('x')
          result = str(-int(splited_str[1][1])+int(index_x[0][1]))[split_ax]
          return result

      # x in O index and *
      elif "*" in v:
        index_x=[(index,v) for index , v in enumerate(v.split("*")) ]
        if index_x[0][0] == 0 and "x" in  index_x[0][1]: # index 0[(,)]

          split_ax =index_x[0][1].index('x')
          result = str(int(splited_str[1][1]) // int(index_x[1][1]))[split_ax]
          return result
        elif index_x[1][0] == 1 and "x" in  index_x[1][1]: # index 1[(,)]
          
          split_ax =index_x[1][1].index('x')
          result = str(int(splited_str[1][1]) // int(index_x[0][1]))[split_ax]
          return result


      # x in 0 index and /
      elif "/" in v:
        index_x=[(index,v) for index , v in enumerate(v.split("/")) ]
        
        if index_x[0][0] == 0 and "x" in  index_x[0][1]: # index 0[(,)]
          split_ax =index_x[0][1].index('x')
          result= str(int(splited_str[1][1]) * int(index_x[1][1]))[split_ax]
          return result

        elif index_x[1][0] == 1 and "x" in  index_x[1][1]: # index 1[(,)]
          split_ax =index_x[1][1].index('x')
          result= str(int(splited_str[1][1]) * int(index_x[0][1]))[split_ax]
          return result
        
      
    elif i == 1  and 'x' in v:
      
      if "+" in splited_str[0][1]:
        op_op=sum ([int(v) for v in splited_str[0][1].split("+") ])
        split_ax =splited_str[1][1].index('x')
        return str(op_op)[split_ax]

      elif "-" in splited_str[0][1]:
        op_op= [int(v) for v in splited_str[0][1].split("-") ]
        split_ax =splited_str[1][1].index('x')
        return str(op_op[0]-op_op[1])[split_ax]
      elif "*" in splited_str[0][1]:
        op_op= [int(v) for v in splited_str[0][1].split("*") ]
        split_ax =splited_str[1][1].index('x')
        return str(op_op[0]*op_op[1])[split_ax]
      elif "/" in splited_str[0][1]:
        op_op= [int(v) for v in splited_str[0][1].split("/") ]
        split_ax =splited_str[1][1].index('x')
        return str(op_op[0]//op_op[1])[split_ax]
    
      
# keep this function call here 
print(MissingDigit(input()))



