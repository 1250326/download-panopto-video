import os
from multiprocessing import Pool

def downloading(pack):
        (video, key) = pack
        video_folder_path = "/Users/yourUserName/Desktop/video/"
        content = "ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i \"%s\" -c copy \"%s%s.mp4\""%(video[key], video_folder_path, key)
        print("processing:", key)
        os.system(content)
        
if  __name__ == '__main__':

    ####### Control to use multiprocessing or not #######
    multi = True
    #####################################################
    
    video = {
        "filename" : "https://lecturecapture.fakeUniversity.hk/Panopto/Content/someCodes/index.m3u8",
    }

    if multi == False:
        for key in video.keys():
            downloading((video, key))
    else:
        pool = Pool() # no. of CPU used
        pool.map(downloading, [(video, key) for key in video.keys()])