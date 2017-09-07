import os
def renameFile(fileName):
    filePre = "D:\\laungue\\studynotes\\yyWang"
    #os.chdir(os.path.dirname(filePre))
    os.rename(filePre, fileName)
    print filePre

if __name__ == '__main__':
    #D:\laungue\studynotes\yiyuanwang\aaa.txt
    renameFile("D:\\laungue\\studynotes\\yy")