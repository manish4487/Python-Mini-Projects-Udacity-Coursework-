import os    

def rename_files():
    #1 get files names from folder
    file_list=os.listdir(r"C:\Users\manis\Downloads\prank")    
    print (file_list)
    saved_path=os.getcwd()
    print("current working directory"+saved_path)    
    os.chdir(r"C:\Users\manis\Downloads\prank")
    #2 for each file rename filename
    remove="123456789"    
    table=str.maketrans("","",remove)    
    for file_name in file_list:    
        os.rename(file_name,file_name.translate(table))    


rename_files()
