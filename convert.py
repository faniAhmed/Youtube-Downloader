import os

def combine_audio(title, foldernum):
    print(title)
    print(foldernum)
    print('\n\n')
    dir = os.getcwd()
    if foldernum == 0:
        os.chdir(dir + "\\" + title)
    else:
        os.chdir(dir + "\\" + title + str(foldernum))
#    char = "|/<>?,:'}{][+_-=)(*&%$#@!~`"
#    for c in char:
#        Ntitle = title.replace(c , "")
    try:
        os.system("ffmpeg -i vid.mp4 -i aud.webm -c copy \""+ title +"\".mkv")
    except:
        os.system("ffmpeg -i vid.webm -i aud.webm -c copy \""+ title +"\".webm")
    os.remove("aud.webm")
    try:
        os.remove("vid.mp4")
    except:
        os.remove("vid.webm")
    for i in range(10):
        try:
            os.rename(title + ".mkv", dir + "\\Download\\" + title + ".mkv")
            break
        except:
            pass
        try:
            os.rename(title + ".mkv", dir + "\\Download\\" + title + "(" + str(i) + ").mkv")
            break
        except:
            pass
    os.chdir(dir)
    if foldernum == 0:
        os.rmdir(dir + "\\" + title)
    else:
        os.rmdir(dir + "\\" + title + str(foldernum))