
"""
    read file content --->
    write content to the file ---> open file for writing --> starting from the beginning of the file
    remove old content
    append content to the file --> open file for append --> starting from the end of the file
    keep old content

    ---- to deal with files
    --> open file --> specify mode
    --> r --> reading
    ---> w --> writing
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
    fileobject=open("names.txt", 'r')  #return with TextIOWrapper object
except Exception as e:
    print(e)
else:
    print(fileobject)
    # read file content
    # data = fileobject.read()  # read file content into one string
    # print(data)
    # read file content line by line
    # line = fileobject.readline()
    # print(line)
    # line = fileobject.readline()
    # print(line)
    """ read file lines """
    lines = fileobject.readlines()
    print(lines)  # read file content into a list .
    fileobject.seek(0) # return with cursor to the beginning of the file
    data = fileobject.read()
    print(f'data={data}#')

    fileobject.close()  # close the stream




