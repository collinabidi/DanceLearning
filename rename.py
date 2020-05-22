import os
from shutil import copyfile

def main():
    # go through the files in each sub-folder
    for count, filename in enumerate(os.listdir('./data/lisa/json/')):
        src = './data/lisa/json/' + filename
        dst = './data/lisa/jsonout/lisa_' + str(count) + '.json'
        print("JSON SOURCE " + src)
        print("JSON DEST " + dst)

        if "lisa" in filename:
            a_name = filename.split(".")[0]
        else:
            a_name = filename[7:-5]

        audiosrc = './data/lisa/audio/' + a_name + '.wav'
        audiodest = './data/lisa/audioout/lisa_' + str(count) + '.wav'
        print("AUDIO SOURCE "+audiosrc)
        print("AUDIO DEST "+audiodest + "\n")

        copyfile(src, dst)
        copyfile(audiosrc, audiodest)

if __name__ == "__main__":
    main()