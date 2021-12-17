import os

os.chdir("M:\Projects")
repo_name = "N/A"
description = "N/A"
repo_name = input("Enter the name of the project: ")
description = input("Enter the description of the project: ")
os.system(f"gh repo create {repo_name} --public --clone-d {description} ")
os.system("cd " + repo_name )
os.system("code .") 