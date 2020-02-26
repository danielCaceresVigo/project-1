def sort(arr):
    sortedar = {0:arr[0]}
    pointer = 0
    for x in range(1, len(arr)):
        while(pointer in sortedar):
            if(arr[x] < sortedar[pointer]):
                pointer = pointer*2+1
            else:
                pointer = pointer*2+2
        sortedar[pointer] = arr[x]
        pointer = 0
    printedrt = False
    for x in range(len(arr)):
       
        parent = pointer = 0
        while(pointer in sortedar):
            if(pointer*2+1 in sortedar):
                parent = pointer
                pointer = pointer * 2+1
            elif(pointer*2+2 in sortedar):
                if(parent *2+1 == pointer):
                    print(sortedar[pointer])
                    if(pointer != 0):
                        del sortedar[pointer]
                elif(pointer == 0 and printedrt == False):
                    printedrt = True
                    print(sortedar[pointer])
                parent = pointer
                pointer = pointer*2+2
            else:
                if(pointer != 0):
                    print(sortedar[pointer])
                    del sortedar[pointer]
                break;