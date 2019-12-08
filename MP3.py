import numpy as np



def MP3(x):  
    
    x = eval(input('Input n x 2 matrix using np. :  '))  
         
        
    l = len(x)
    
    if l > 12:
        length = 10
        
    else:
        length = l
   
       
    for i in range(length):
        
        c = np.polyfit(x[:,0], x[:,1], i)
        
        p1 = x[:,1]
        p2 = np.polyval(c, x[:,0])
        
        P = np.linalg.norm(p1-p2)
        
        X = [i,P]
        
        if i == 0: 
            
            y = X        
                    
        elif y[1] >= X[1]: 
            
            z = X[0]         
                
                
    c = np.polyfit(x[:,0], x[:,1], z)
    
    print ('Coefficient: ', c)
                
                
                
                
        
        
            
            
            
        
        
        
        
        
        
        
        
    