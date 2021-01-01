def zero_encode(inputbuf):
    newstring = b""
    zero = False
    zero_count = 0            
    for c in inputbuf:
        if c != 0:
            if zero_count != 0:
                newstring = newstring + bytes([zero_count])
                zero_count = 0
                zero = False
 
            newstring = newstring + bytes([c])
            #print("c:",c,"bytes(c):",bytes([c]))
 
        else:
            if zero == False:
                newstring =  newstring + bytes([c])
                zero = True
 
            zero_count = zero_count + 1
    if zero_count != 0:
        newstring = newstring + bytes([zero_count])
 
 
    return newstring
 
def zero_decode(inputbuf):
    newstring = b""
    in_zero = False
    for c in inputbuf:
        if c != 0:
            if in_zero == True:
                zero_count = c
                zero_count = zero_count -1
                while zero_count>0:
 
                    newstring = newstring + bytes([0])
                    zero_count = zero_count -1
                in_zero = False
            else:
                newstring = newstring + bytes([c])
        else:
            newstring = newstring + bytes([c])
            in_zero = True
    return newstring
