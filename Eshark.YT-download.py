import youtube_dl
from enum import Enum
from termcolor import colored

# SELECT VIDEO FOR YT
Video = input("What video do you want to download: \n")
print(colored("Video selected:", 'green'), Video)

# SELECT FORMAT FOR DOWNLOAD
format = "Select Format:", "1. m4a (audio only)", "2. mp4_144p", "3. mp4_240p", "4. mp4_360p ", "5. mp4_480p ", "6. mp4_720p ", "7. mp4_1080p", "8. gp3_176_144", "9. gp3_320_240", "10. flv", "11. webm", "12. mp4_640_360", "13. mp4_1280_720 "
print(*format, sep="\n")
format_options = input("Select Format: ")

if format_options != 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print("fail")


class YLFormat(Enum):
    m4a = '140'  # audio only
    mp4_144p = '160'
    mp4_240p = '133'
    mp4_360p = '134'
    mp4_480p = '135'
    mp4_720p = '136'
    mp4_1080p = '137'
    gp3_176_144 = '17'  # 3gp: 176*144
    gp3_320_240 = '36'
    flv = '5'
    webm = '43'
    mp4_640_360 = '18'  # 640 * 360
    mp4_1280_720 = '22'


ylformat = {}

if format_options == "1":
    ylformat = YLFormat.m4a
    print(colored("Selected format:", 'red'), "m4a (audio only)")

elif format_options == "2":
    ylformat = YLFormat.mp4_144p
    print(colored("Selected format:", 'red'), "mp4_144p")
    
elif format_options == "3":
      ylformat = YLFormat.mp4_240p
      print(colored("Selected format:", 'red'), "mp4_240p")
    
elif format_options == "4":
       ylformat = YLFormat.mp4_360
       print(colored("Selected format:", 'red'), "mp4_360p")
  
elif format_options == "5":
    ylformat = YLFormat.mp4_480p
    print(colored("Selected format:", 'red'), "mp4_480p")
    
elif format_options == "6":
    ylformat = YLFormat.mp4_720p
    print(colored("Selected format:", 'red'), "mp4_720p")
    
elif format_options == "7":
    ylformat = YLFormat.mp4_1080p
    print(colored("Selected format:", 'red'), "mp4_1080p")
    
elif format_options == "8":
    ylformat = YLFormat.gp3_176_144
    print(colored("Selected format:", 'red'), "gp3_176_144")
    
elif format_options == "9":
    ylformat = YLFormat.gp3_320_240
    print(colored("Selected format:", 'red'), "gp3_320_240")
    
elif format_options == "10":
    ylformat = YLFormat.flv
    print(colored("Selected format:", 'red'), "Flv")
    
elif format_options == "11":
    ylformat = YLFormat.webm
    print(colored("Selected format:", 'red'), "webm")
    
elif format_options == "12":
    ylformat = YLFormat.mp4_640_360
    print(colored("Selected format:", 'red'), "mp4_640_360")
    
elif format_options == "13":
    ylformat = YLFormat.mp4_1280_720
    print(colored("Selected format:", 'red'), "mp4_1280_720")
    
else:
    print("Invalid input. Please run the script again to try again")
    wait(1)
    end()

def download(url: str, options: dict):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

download_list = [
    (Video, ylformat,),
]

format_conformation = input("Are you sure this is the correct format. \n Y or N:")

if format_conformation == "Y":

    for cur_data in download_list:
        cur_url, tuple_format = cur_data[0], cur_data[1:]
        for format_info in tuple_format:
            if not isinstance(format_info, YLFormat):
                print(f'the format is not correct. format: {format_info}')
                continue
            fmt_name, fmt = format_info.name, format_info.value
            try:
                download(cur_url, dict(format=fmt,
                                       outtmpl=f'%(title)s-{fmt_name}.%(ext)s',
                                       ignoreerrors=True,
                                       quiet=True
                                       ))
            except youtube_dl.utils.DownloadError:
                print(f'download error: {cur_url} | {fmt_name}')
                break
            break
        break
    print("Finished")
    exit()

else:
    print("Run this script to try again.")
    exit()
