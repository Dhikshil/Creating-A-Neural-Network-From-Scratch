import random

def fillList(n, char):
    list_of_chars = []
    if char == "lower":
        lower_bound = 97
        upper_bound = 122
    else:
        lower_bound = 65
        upper_bound = 90
    for x in range(0, n):
        list_of_chars.append(chr(random.randint(lower_bound, upper_bound)))
    return list_of_chars

#print(fillList(10, "upper"))
"""
stack = ["LON", "PAR", "BER", "", "", ""]
top_of_stack = 3

def push(new_value, stack, top_of_stack):
    if top_of_stack != len(stack)
        stack[top_of_stack] = new_value
        top_of_stack += 1
    else:
        print("stack overflow")
    return top_of_stack, stack
"""

num_stack = [1, 6, 5, 3, 9, 0, 2, "", "", ""]
top_of_num_stack  = 7

def push_until_full(stack):
    global top_of_num_stack
    while top_of_num_stack != len(num_stack):
        num = random.randint(0, 9)
        stack[top_of_num_stack] = num
        top_of_num_stack += 1


def createTopPointer(stack):
    index = 0
    if index < len(stack):
        while stack[index] != "":
            index += 1
    return index 

cities = ["MAD", "RON", "LON", "PAR", "BER", "", "", "", "", ""]
cities = ["", "", "", "", "", "", "", "", "", ""]
#cities = ["MAD", "RON", "LON", "PAR", "BER", "POR", "TEN", "TOR", "MAN", "BEN"]

top_of_stack = createTopPointer(cities)

def push(stack, new_value):
    global top_of_stack
    if top_of_stack < len(stack):
        stack[top_of_stack] = new_value
        top_of_stack += 1
    else:
        print("stack overflow")
        
    return stack

def pop(stack):
    global top_of_stack
    if top_of_stack == 0:
        print("underflow error")
    else:
        data = stack[top_of_stack - 1]
        stack[top_of_stack - 1] = ""
        top_of_stack -= 1
    return stack, data


def peak(stack):
    global top_of_stack
    return stack[top_of_stack]

def rle_encode(data):
    data_arr = list(data)
    encoded_data = []
    prev_character = ""
    count = 0
    for character in data_arr:
        if prev_character == character:
            count += 1
        else:
            if prev_character != "":
                encoded_data.append(str(count))
                encoded_data.append(prev_character)
            prev_character = character
            count = 1
    
    encoded_data_str = ""

    for value in encoded_data:
        encoded_data_str += value

    return encoded_data_str

print(rle_encode("AAABBBAAAAAAAAAAAAAAAAAAABBBBBBBBBBBNNNNNNNNNNNDWIIIIIIIIIIIIDddkkkkkkkkkkkaddddddddddddddCCDAA"))

def rle_decode(data):
    data_arr = list(data)
    decoded_str = ""
    for x in range(0, len(data_arr)):
        if x % 2 == 0:
            for i in range(0, int(data_arr[x])):
                decoded_str += data_arr[x + 1]
    return decoded_str




queue = ["BMW", "Mercedes", "Audi", "Porsche", "", "", "", ""]

def shuffleQueue(queue):
    data = queue[0]
    for x in range(0, len(queue)):
        if x < len(queue) - 1:
            queue[x] = queue[x + 1]
    
    return data, queue

data, queue = shuffleQueue(queue)
seats = ["Helen", "Adam", "Lida", "Kwaku", "Priya", "Chan"]

def shuffleSeats(queue, move):
    new_seats = [""] * 6
    for x in range(len(queue)):
        new_seats[x] = (queue[x - move])

    return new_seats

def dict_encoding(values):
    data_dict = {value: idx for idx, value in enumerate(set(values))}
    encoded_data = [data_dict[value] for value in values]
    encoded_data.appned(data_dict)
    return encoded_data

def dict_decoding(data):
    decoding_dict = data[len(data) - 1]
    decoded_data = ""
    for i in range(len(data) - 1):
        decoded_data += decoding_dict[i] + ""
    
    return decoded_data

def emptyList(number):
    return [""] * number

int_stack = [1,2,3,4,5,6,0,0,0,0]
top_of_stack = 6

def autoPush(queue, number):
    global top_of_stack
    for x in range(number):
        if top_of_stack == len(queue):
            print("overflow")
            break
        else:
            queue[top_of_stack] = random.randint(0,20)
            top_of_stack += 1

    return queue

int_stack = [1,2,3,4,5,6,0,0,0,0]
top_of_stack = 6

def sumStack(queue):
    global top_of_stack
    total = 0
    for x in range(0, top_of_stack):
        total += queue[x]

    return total


int_stack = [1,2,3,4,5,6,7,8,9,0]

def reverseStack(queue):
    new_queue = []
    for x in range(len(queue)):
        value = queue[-1 - x]
        if value != 0:
            new_queue.append(value)
    if len(new_queue) != len(queue):
        for x in range(len(queue) - len(new_queue)):
            new_queue.append(0)
    return new_queue

int_stack = [1,2,3,4,5,6,7,8,9,0]
top_of_stack = 9

def searchStack(queue, number):
    global top_of_stack
    for x in range(0, top_of_stack):
        if queue[top_of_stack] == number:
            return x
        else:
            if top_of_stack == 0:
                return -1
            else:
                top_of_stack -= 1

new_seats = [""] * 6


size = 5
queue = [None] * size
head = 0
tail = 0

# helper function to check if queue is empty
def isEmpty():
    global head, tail
    return head == tail

def enqueue(data):
    global tail
    if tail == len(queue) - 1:
        print("full")       

list_of_words = []
with open("emma.txt", "r", encoding="utf-8") as f:
    text = f.read()
    words = text.split()
    for word in words:
        stripped_word = word.strip(".,;:!?—-")
        list_of_words.append(stripped_word)
    
print(list_of_words)

def bad_hash(key, buckets):
    if not key:
        return 0
    return ord(key[0]) % buckets

def good_hash(key, buckets):
    total = 0
    key_list = list(key)
    for letter in key_list:
        total += ord(letter)
    return total % buckets

def weighted_hash(key, buckets):
    total = 0
    key_list = list(key)
    for x in range(0, len(key_list)):
        total += ord(key_list[x]) * (x + 1)
    return total % buckets

def length_hash(key, buckets):
    total = 0
    key_list = list(key)
    for letter in key_list:
        total += ord(letter)
    return (total * len(key)) % buckets

def testHash(func, keys, size):
    results = [0]*size
    keys_used = []
    for i in keys:
        if i not in keys_used:
            hv = func(i, size)
            results[hv] = results[hv] + 1
            keys_used.append(i)
    return results



print(testHash(good_hash, list_of_words, 1000))
print(testHash(weighted_hash, list_of_words, 1000))
print(testHash(length_hash, list_of_words, 1000))

def compareBucketsVar(bucket_1, bucket_2):
    #getting the E(x) of bucket 1
    total = 0
    for values in bucket_1:
        total += values
    Ex_1 = total / len(bucket_1)

    #getting the E(x) of bucket 2
    total = 0
    for values in bucket_2:
        total += values
    Ex_2 = total / len(bucket_2)

    #getting the E(X^2) of bucket 1
    total = 0
    for values in bucket_1:
        total += values ** 2
    Ex2_1 = total / len(bucket_1)

    total = 0
    for values in bucket_2:
        total += values ** 2
    Ex2_2 = total / len(bucket_2)

    Vx_1 = Ex2_1 - (Ex_1 ** 2)
    Vx_2 = Ex2_2 - (Ex_2 ** 2)

    print("variance of hashtable 1: ", Vx_1)
    print("variance of hashtable 2: ", Vx_2)

def compareBucket(bucket):
    #getting the E(x) of bucket 1
    Ex = sum(bucket) / len(bucket) 
    residuals = 0
    for values in bucket:
        residuals += abs(Ex - abs(values))
    return residuals / len(bucket)

 
print(compareBucket(testHash(length_hash, list_of_words, 1000)))
print(compareBucket(testHash(weighted_hash, list_of_words, 1000)))
print(compareBucket(testHash(good_hash, list_of_words, 1000)))
compareBucketsVar(testHash(weighted_hash, list_of_words, 1000), testHash(good_hash, list_of_words, 1000))
compareBucketsVar(testHash(length_hash, list_of_words, 1000), testHash(good_hash, list_of_words, 1000))