import os
from shutil import copyfile

def main():
    audio_names = sorted([fname.split(".")[0] for _, fname in enumerate(os.listdir('./data/lisa/original_audio'))])
    json_names = sorted([fname.split(".")[0] for _, fname in enumerate(os.listdir('./data/lisa/json'))])
    print("audio length: {}".format(len(audio_names)))
    print("json  length: {}".format(len(json_names)))

    for count, filename in enumerate(os.listdir('./data/lisa/json/')):
        a_name = filename.split(".")[0]
        if a_name not in audio_names:
            print("{} is not in the audio names!".format(a_name))
            #new_name = a_name + ".json"
            #print("{} --> {}".format(filename, new_name))
            #os.rename("./data/lisa/json/" + filename, "./data/lisa/json/" + new_name)


        

if __name__ == "__main__":
    main()
