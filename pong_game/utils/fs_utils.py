from os import sep, linesep, pathsep, curdir
import os

class FSUtils():
    
    def __init__(self):
        pass
    
    def get_os_sep(self):
        return sep
    
    def get_os_linesep(self):
        return linesep
    
    def get_os_pathsep(self):
        return pathsep
    
    def get_curdir(self):
        return curdir
    
    def get_cwd(self):
        return os.getcwd()