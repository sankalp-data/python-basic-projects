def is_leap(year):

    if 1900< year <10**5:

        if year%4 != 0:

            return False
        
        elif year%100!=0:

            return True
        
        elif year%400==0:
            
            return True
        
        else:
            return False

    else:
        print("Please enter a year between 1900 and 99999.")
    
    
    return False

print(is_leap())