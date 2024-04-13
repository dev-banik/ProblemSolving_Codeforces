str=input()
vowels=['a','e','i','o','u','y'] 
result=[letter for letter in str if letter.lower() not in vowels] 
result='.'.join(result) 
result=result.lower()
print('.'+""+result) 