import os
def RewriteCss(css, Name):
    download_folder = os.path.expanduser("~/Downloads")
    file_path = os.path.join(download_folder, Name + ".css")
    with open(file_path, "w") as file:
        for i in css:
            if i == "}":
                file.write(i + "\n \n")
            elif i == ";" or i == "{":
                file.write(i + "\n")
            else:
                file.write(i)
    print(f"Contenu écrit dans {file_path}")
        
n = input("Entrez le nom du fichier qui sera enregistré dans /download ...")
css = input("Entrez CSS : ")
RewriteCss(css, n)
