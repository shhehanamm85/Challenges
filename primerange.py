start=int(input("Enter your starting range"))
endl=int(input("Enter ending range"))
prime_list=[]
for num in range(start,endl):
    if num >1:
        pri=True
        for j in range(2,num):
            if num% j==0:
             pri=False
             break
        if pri:
         prime_list.append(num)
if prime_list:
   print("prime numbers of given range are",prime_list)
else:
   print("There is no prime numbers exist in the given range")            

    

               
            
            
                
       
        
                            

                
  
 

    
        


           
 
  
         
      
   
  
  

