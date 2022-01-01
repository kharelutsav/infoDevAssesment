s = "egg"
t = "add"

index_s = {}
index_t = {}
state = True

if len(s) == len(t):
    for index in range(len(s)):
        index_s[s[index]] = [index] if not s[index] in index_s else index_s[s[index]] + [index]
        index_t[t[index]] = [index] if not t[index] in index_t else index_t[t[index]] + [index]
    for (os, ot) in zip(index_s, index_t):
        if index_s[os] != index_t[ot]:
            state = False
            break
        
    print(state)
    
else:
    print(False)
    
    
# s = "egg"
# t = "add"

# index_s = {}
# index_t = {}

# if len(s) == len(t):
#     for index in range(len(s)):
#         index_s[s[index]] = [index] if not s[index] in index_s else index_s[s[index]] + [index]
#         index_t[t[index]] = [index] if not t[index] in index_t else index_t[t[index]] + [index]
#         state = True if index_s[s[index]] == index_t[t[index]] else False
#         if state == False:
#             break
#     print(state)
# else:
#     print(False)
