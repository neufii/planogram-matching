import os

image_files = []
os.chdir(os.path.join("image"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("image" + "/" + filename)
os.chdir("..")

with open("train.txt", "w") as outfile:
    for image_file in image_files:
        outfile.write(image_file)
        outfile.write("\n")
    outfile.close()

with open("val.txt", "w") as outfile:
    for image_file in image_files:
        outfile.write(image_file)
        outfile.write("\n")
    outfile.close()
