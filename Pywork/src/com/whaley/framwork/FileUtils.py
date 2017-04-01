# -*- coding: utf-8 -*-
'''
Created on 2017年3月23日

@author: hc
'''

import os 

class FileUtils():
    @staticmethod
    def renameFileRecursive( destDir,suffix):
        for parent ,dirnames,filenames in os.walk(destDir):
            for dirname in dirnames:
                print "parent is :"+parent
                print "dirname is :"+dirname
            for filename in filenames:
                print "filename is "+ filename
                
                if(os.path.isfile(os.path.join(parent,filename))) :
                    print "the full name of the file is:" + os.path.join(parent,filename)
                    newFile = filename.split(".")[0]+suffix
                    os.rename(os.path.join(parent,filename), os.path.join(parent,newFile))
    @staticmethod               
    def renaemFiles(destDir,suffix): 
        for  filename in os.listdir(destDir):     
            if(os.path.isdir(os.path.join(destDir,filename))):
                print "dir is :"+  os.path.join(destDir,filename)
            if(os.path.isfile(os.path.join(destDir,filename))):
                print "file is :"+  os.path.join(destDir,filename)
                newFile = filename.split(".")[0]+suffix
                os.rename(os.path.join(destDir,filename), os.path.join(destDir,newFile))



if __name__ =="__main__":
    #fileUtils = FileUtils();
    FileUtils.renaemFiles(r"C:\Users\hc\Desktop\gd", ".jpg")
    #fileUtils.renameFileRecursive(r"C:\Users\hc\Desktop\1", ".jpg")
    
    
