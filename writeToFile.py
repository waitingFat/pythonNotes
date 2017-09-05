def write_to_file(file_name,text):
    with open(file_name,"w")as f:
        f.write(text+"\n")
if __name__ == "__main__":
        write_to_file("newFile" ,"first edit my python file")
