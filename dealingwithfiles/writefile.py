"""
    read file content --->
    write content to the file ---> open file for writing --> starting from the beginning of the file
    remove old content
    append content to the file --> open file for append --> starting from the end of the file
    keep old content

    ---- to deal with files
    --> open file --> specify mode
    --> r --> reading
    ---> w --> writing 000> if file doesn't exists ---> will try to create it
    ---> a ---> append
    open(filename, mode)

    do operation
        read ---> read , readlines
        write ---> write , writelines
    close file
    close
    ------------------simple text files -----------------------
    "read , save log message "
    'storage wise '
    'configuration file '
"""
try:
    fileobject = open("mycv.txt", 'w')  # return with TextIOWrapper object
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write('My name is Noha\n')
    fileobject.write('I works at ITI\n')
    """ write lines"""
    fileobject.writelines(['Ahmed\n', 'Ali', 'test'])
    "write content starting from specific byte "
    fileobject.seek(10)
    fileobject.write("#"*100)

    fileobject.close()  # close the stream
