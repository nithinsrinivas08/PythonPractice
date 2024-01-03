user_in = input('Please enter 3 numbers : ')
string_tokens = user_in.split(', ')
int_tokens = []
for i in string_tokens :
    int_tokens.append(int(i))

a,b,c = int_tokens
result = a + b - c
print(result)