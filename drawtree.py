def draw_tree(length):
    if length % 2 == 0:
        length += 1
        
    space = length//2
    repeat = 1
    
    while space>0:
        print((" " * space) + ("*" * repeat))
        repeat += 2
        space -= 1
    
    print("*" * length)
    
draw_tree(34)
