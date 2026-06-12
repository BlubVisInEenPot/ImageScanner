import os

def doesFile_Exist(sourceFile, targetDir):
    filename = os.path.basename(sourceFile)
    target_path = os.path.join(targetDir, filename)
    if os.path.exists(target_path):
        return True
    else:
        return False


print(doesFile_Exist("Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten\images.tiff", "Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten"))