for AB in range(10, 100):
    result = AB * AB 
    
    if result % 100 == AB and result<1000:
        print(result)