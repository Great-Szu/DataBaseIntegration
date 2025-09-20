def print_backwards(*args, **kwargs):

    for word in args[::-1]:
        print(word[::-1], **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "test", "take", end=' ', file=backwards)
