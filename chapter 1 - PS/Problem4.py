import os

directory_path = '/Users/over/Desktop/for me/chapter 1'

contents = os.listdir(directory_path)

for item in contents:
    print(item)