from bs4 import BeautifulSoup

path = 'path/to/watch/history/file'

with open(path, encoding="utf8") as f:
   soup = BeautifulSoup(f, "html.parser")

tmp = soup.find_all('a', attrs={'id':'video-title'})

video_dic = {}
data_dic = {}
channel_dic = {}
channel_videos = {}

min_views = 2000000000000
min_view_video = ""

for i in range(len(tmp)):
   data = tmp[i]["aria-label"].split()
   # video = tmp[i]["title"].strip()
   video = ' '.join(tmp[i]["title"].strip().split())
   link = "https://youtube.com" + tmp[i]["href"].strip()

   title = ""
   channel = ""
   length = 0
   views = 0

   while (data):
      if (data[-1] == "views"):
         j = 0
         while (j < len(data[-2])):
            if (data[-2][j] == ","):
               data[-2] = data[-2][:j] + data[-2][j + 1:]
            else:
               j += 1
         views = int(data[-2])
         del (data[-1])
         del (data[-1])
      elif (data[-1] == "seconds"):
         length += int(data[-2])
         del (data[-1])
         del (data[-1])
      elif (data[-1] == "minutes," or data[-1] == "minutes"):
         length += int(data[-2]) * 60
         del (data[-1])
         del (data[-1])
      elif (data[-1] == "hours," or data[-1] == "hours"):
         length += int(data[-2]) * 60 * 60
         del (data[-1])
         del (data[-1])
      elif (data[-1] == "days," or data[-1] == "days"):
         length += int(data[-2] * 60 * 60 * 24)
         del (data[-1])
         del (data[-1])
      else:
         while (len(title[:-1].split()) != len(video.split())):
            title += data[0] + " "
            del (data[0])
         del (data[0])
         while (data):
            channel += data[0] + " "
            del (data[0])
         channel = channel[:-1]

   if (video not in data_dic):
      data_dic[video] = [link, channel, length]

   if (channel in channel_dic):
      channel_dic[channel] += 1
   else:
      channel_dic[channel] = 1

   if (channel not in channel_videos and length < 60*60):
      channel_videos[channel] = link

   if (video in video_dic):
      video_dic[video] += 1
   else:
      video_dic[video] = 1

   if (views > 0 and views < min_views):
      min_views = views
      min_view_video = video


arr_videos = []

for key in video_dic:
   arr_videos.append([key, video_dic[key]])

arr_videos.sort(key=lambda x: x[1], reverse=True)

# Number of different videos
print("Number of different videos:", len(arr_videos))
print()

arr_channels = []
for key in channel_dic:
   arr_channels.append([key, channel_dic[key]])

arr_channels.sort(key=lambda x: x[1], reverse=True)

# Number of different channels
print("Number of different channels:", len(arr_channels))
print()

# Top 5 videos
top_5_videos = arr_videos[:5]
print(top_5_videos)
print()

# Top 5 channels
top_5_channels = arr_channels[:5]
print(top_5_channels)
print()

# Lowest viewed video
print("Lowest viewed video:", min_view_video, "(" + str(min_views) + " views)")
print()