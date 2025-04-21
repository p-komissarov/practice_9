def is_palindrome(num):
    return str(num) == str(num)[::-1]

for start in range(100000, 1000000):
    if not is_palindrome(str(start)[-5:]):
        continue
    
    if not is_palindrome(str(start + 1)[-5:]):
        continue
    
    if not is_palindrome(str(start + 2)[1:5]):
        continue
    
    if is_palindrome(start + 3):
        print(f"Начальный пробег: {start}")
        break