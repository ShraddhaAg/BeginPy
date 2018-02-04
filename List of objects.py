object file
# files can be opened using the open("insert file name here",'mode') function
    # modes may be r : opens file to read, position at the beg; default mode
    #              w : opens file to write (makes new if file doesn't exists), truncates file, pointer at beg
    #              a : opens file to append, pointer at the end
    #             r+ : opens file to read and write, pointer at the beg
    #             w+ : opens file (new) to read and write; truncates if something already exists, pointer at beg
    #             a+ : open file to read and write, pointer at the end


            # functions: 1. read(<size>): returns a string from file of size as passed from the file position; if size not passed will return string having contents of file till eof is reached
            #            2. close()
            #            3. truncate() : will clear the contents of the file
            #            4. write("stuff") : writes stuff to the file
            #            5. seek(offset, from_what) : offset is the number of positions wanted to move ; from_what defines the refrence pointe
                                                    # for refrence point: 0 : means from beginning (default)
                                                                        # 1: means from the current position
                                                                        # 2: means from end of file
                                                    # seek function is useless in w mode as the file gets truncated, also it doesn't work in append mode, but does work in append mode only for reading from the changed position when opened for reading as well that is a+
                                                    # doesn't work for writing
            #            6. readline(<size>) : just like read but limits the maximum amount returned as a string to when a new line is encountered
            
