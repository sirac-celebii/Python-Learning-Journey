import os

extension_map = {
     ".mp3" : "Audios",
     ".flac" : "Audios",
     ".ogg" : "Audios",
     ".wav" : "Audios",

     ".mp4" : "Videos",
     ".avi" : "Videos",
     ".mpg" : "Videos",
     ".mov" : "Videos",

     ".c" : "Code",
     ".cpp" : "Code",
     ".java" : "Code",
     ".py" : "Code",
     ".ipynb" : "Code",
     ".js" : "Code",
     ".ts" : "Code",
     ".cs" : "Code",
     ".swift" : "Code",
     ".pl" : "Code",
     ".html" : "Code",
     ".css" : "Code",
     ".go" : "Code",
     ".php": "Code",
     ".rb" : "Code",
     ".rs" : "Code",
     ".R" : "Code",

     ".sql" : "Databases",
     ".db" : "Databases",
     ".sqlite" : "Databases",
     ".sqlite3" : "Databases",
     
     ".sh" : "Scripts",

     ".exe" : "Apps",
     ".msi" : "Apps",
     ".bat" : "Apps",

     ".rar" : "Compressed",
     ".zip" : "Compressed",
     ".zipx" : "Compressed",
     ".z" : "Compressed",
     ".7z" : "Compressed",

     ".txt" : "Documents",
     ".doc" : "Documents",
     ".docx" : "Documents",
     ".wps" : "Documents",
     ".wpd" : "Documents",
     ".csv" : "Documents",
     ".xls" : "Documents",
     ".xlsx" : "Documents",

     ".pdf" : "PDF Files",
     ".htm" : "PDF Files",

     ".ppt" : "Presentations",
     ".pptx" : "Presentations",

     ".jpg" : "Images",
     ".jpeg" : "Images" ,
     ".gif" : "Images",
     ".avif" : "Images",
     ".png" : "Images"
}

files = []

path = input("Path -> ")

#Find the files from the directory
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        files.append(file)

# Create folders
for file in files:
    file_name, extension = os.path.splitext(file)

    if extension in extension_map.keys():
        folder_name = extension_map[extension]
    else:
        folder_name = "Others"

    new_folder_path = os.path.join(path, folder_name)

# Move the files to the related folder
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    source = os.path.join(path, file)
    destination = os.path.join(new_folder_path, file)

    os.replace(source, destination)

  

