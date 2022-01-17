import sys, os

class noDirectoryFound(Exception):
    def __init__(self, directory):
        self.directory = directory

    def __str__(self) -> str:
        return super().__str__(f"{self.directory} cannot be found")


def setParent(directory:str) -> str:
    """
    creates a path like string object based on some parent folder
    for instance if the path is a/b/c/d
    and setParent("c") is run, then a/b/c will be returned
    returns a noDirectoryFound exception if location isnt in directory
    """
    cwd = os.getcwd()
    if sys.platform == "win32":
        delimeter = "\\"
    else:
        delimeter = "/"
        
    split_cwd =  cwd.split(delimeter)

    if directory not in split_cwd:
        raise noDirectoryFound(directory)
    
    location = split_cwd.index(directory)
    new_path =  delimeter.join(split_cwd[:location+1])
    return new_path

def addToPath(path:str)-> bool:
    """
    add string  to system path
    """
    try:
        sys.path.insert(0,path)
        return True
    except Exception as e:
        return False

def addParentToPath(directory: str)-> list:
    """
    find directory if a parent and create a and add that as path variable to sys.path
    """
    addToPath(setParent(directory=directory))
    return sys.path



if "__main__" ==__name__:
    print(addParentToPath("Dev"))    


