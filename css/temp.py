import os

# Set the path to your target folder
folder_path = os.getcwd()+'\css'

# List only files in the folder (exclude directories)
files = [f for f in os.listdir(folder_path) 
         if os.path.isfile(os.path.join(folder_path, f))]

# Print the list of files
print("Files in folder:")
for file in files:
    print(file)