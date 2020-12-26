# Download Panopto Video Using Python

A tool to download Panopto video using Python and FFmpeg.

The key idea of this tool is using FFmpeg to download `index.m3u8`, which is loaded while opening the Panopto video page. Although FFmpeg provided command line tools to download .m3u8 directly, it is hard to remember, so this tool is written to facilitate downloading.

Please feel free to raise issues and suggestions. As this is a kind of crawling, use at your own risk.

# Configuration
### For Window and Mac
1. Download FFmpeg from https://ffmpeg.org/download.html
2. (Window) Extract `ffmpeg.exe` / (Mac) Install FFmpeg and find out the location of ffmpeg file
3. Download my script and amend the `ffmpeg_path` and `video_folder_path` to fit your computer

### For Linux
1. Install FFmpeg
```
sudo add-apt-repository universe
sudo apt update
sudo apt install ffmpeg
```
2. Download my script and amend the `video_folder_path` to fit your computer

# How to Use

I have tested on Chrome only.

For each video you would like to download, follow these steps:
1. In the Panopto video page, press `F12` to open developer tools
2. Go to the Network tab, refresh the page, and search `index.m3u8` in search box
3. Press on `index.m3u8`, go to Headers tab and copy the Request URL
4. Modify the python script and add a key-value pair in the `video` dictionary. Key is the file name you want to store and value is the copied URL


# Idea
You can download video / `.m3u8` using FFmpeg by command line tool. Example command is as follow:
`"D:\ffmpeg" -protocol_whitelist file,http,https,tcp,tls,crypto -i "https://YourURL/index.m3u8" -c copy "D:\Video\filename.mp4"`

I have packed it into a Python file so that I can download multiple videos at the same time without remembering the complicated command.

# Limitation
Finding the `index.m3u8` URL is tedious, but I don't know how to automate this. The main problem is getting loaded resource URL in a webpage, which seems cannot be done by requests and selenium. Please tell me if you have any idea. Many thanks.
