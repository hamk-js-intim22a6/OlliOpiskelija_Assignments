import os
import zipfile
import shutil

# Task 1: Generate first 3 text files in subdirectory called example_deleteme
os.makedirs('example_deleteme', exist_ok=True)
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
for filename in filenames:
    with open(f'example_deleteme/{filename}', 'w') as f:
        f.write(f'This is the content of {filename}')

# Task 2: Zip all these files into example.zip
with zipfile.ZipFile('example.zip', 'w') as zipf:
    for filename in filenames:
        zipf.write(f'example_deleteme/{filename}', arcname=filename)

# Task 3: List contents of example.zip
with zipfile.ZipFile('example.zip', 'r') as zipf:
    print("Contents of example.zip:")
    print(zipf.namelist())

# Task 4: Delete all those text files (*.txt)
for filename in filenames:
    os.remove(f'example_deleteme/{filename}')

# Task 5: Extract example.zip
with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('example_deleteme')

# Task 6: Remove example_deleteme and its contents
#shutil.rmtree('example_deleteme')
