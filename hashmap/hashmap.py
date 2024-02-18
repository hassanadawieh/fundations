

string = "I am berlin I live in berlin  berlin is a great city A lot of people live there"

def solution(input)-> str:
    hashmap = {}

    for word in input.split(" "):
      hashmap[word] = hashmap.get(word , 0) + 1
    return hashmap    

print(solution(string))    
