# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "test", "take", end='\t')
    print("Another String")


print()
print("hello", "test", "take", end='', sep='\n**\n')
print_backwards("hello", "test", "take", end='', sep='\n**\n')
print("!")
print()
print("test")
