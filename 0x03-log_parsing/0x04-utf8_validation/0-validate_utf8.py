def validUTF8(data):

    trailing_bytes = 0

    for num in data:
        
        num = num & 0xFF

        if trailing_bytes > 0:
    
            if (num >> 6) != 0b10:
                return False
            trailing_bytes -= 1
        else:

            if num >> 7 == 0:
        
                trailing_bytes = 0
            elif (num >> 5) == 0b110:
        
                trailing_bytes = 1
            elif (num >> 4) == 0b1110:
                
                trailing_bytes = 2
            elif (num >> 3) == 0b11110:
    
                trailing_bytes = 3
            else:
                return False 

    return trailing_bytes == 0


data1 = [197, 130, 1] 
data2 = [235, 140, 4]  
data3 = [240, 144, 128, 128] 

print(validUTF8(data1))  
print(validUTF8(data2)) 
print(validUTF8(data3))  