import os

target_folder = input("Target folder location: ")
parent_folder = os.path.dirname(target_folder)
des_folder = os.path.join(parent_folder, 'wav')
print(des_folder)
os.makedirs(des_folder, exist_ok=True)
files = []
for file in os.listdir(target_folder):
    if file.endswith(".flac"):
        size = len(file)
        files.append(file[:size-5])

for file in files:
    input_file = target_folder + "/" + file + ".flac"
    output_file = des_folder + "/" + file + ".wav"
    os.system("ffmpeg -i '{}' '{}'".format(input_file, output_file))

print("done")