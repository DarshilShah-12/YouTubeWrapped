from bs4 import BeautifulSoup
import moviepy.editor as mpy
from pytube import YouTube
from moviepy.editor import *
import shutil
from render_slides import render_ranking_slide, render_stats_slide, render_thanks_slide, render_welcome_slide, render_video_too_long, render_side_banner_videos, render_side_banner_channels, render_channels_intro, WHITE, BLACK

VIDEO_SIZE = (1280, 720)

path = 'C:/Users/whats/Desktop/youtube_watch_history.txt'

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

# Format videos

if (not os.path.isdir("compile_videos")):
   os.mkdir("compile_videos")
if (not os.path.isdir("test")):
   os.mkdir("test")

def trackNum(num, slide):
   slide.write_videofile(f"compile_videos/{num}.mp4", fps=30)
   slide.close()
   return num + 1

num = 100

welcome_slide = mpy.VideoClip(render_welcome_slide, duration=5)
stats_slide = mpy.VideoClip(lambda t: render_stats_slide(t, len(arr_videos), len(arr_channels)), duration=5)

welcome_slide.audio = CompositeAudioClip([AudioFileClip("music/music_1.mp3")])
# welcome_slide.write_videofile(f"compile_videos/{num}.mp4", fps=30)
num = trackNum(num, welcome_slide)

stats_slide.audio = CompositeAudioClip([AudioFileClip("music/music_2.mp3")])
# stats_slide.write_videofile(f"compile_videos/{num}.mp4", fps=30)
num = trackNum(num, stats_slide)

for i in range(len(top_5_videos) - 1, -1, -1):
   ranking_slide = mpy.VideoClip(lambda t: render_ranking_slide(t, i + 1), duration=5)

   video_name = top_5_videos[i][0]
   num_views = top_5_videos[i][1]
   banner_str = f"#{i + 1}: {video_name} ({num_views} views)"
   side_banner_for_video = mpy.VideoClip(lambda t: render_side_banner_videos(t, i + 1, video_name, num_views, banner_str), duration=15)

   link = data_dic[top_5_videos[i][0]][0]
   print(link)
   length = YouTube(link).length

   if (length > 1800):  # 30 minutes
      video = mpy.VideoClip(render_video_too_long, duration=5)
   else:
      if (YouTube(link).streams.get_by_itag(22)):
         YouTube(link).streams.get_by_itag(22).download(output_path="test", filename="tmp")
      else:
         YouTube(link).streams.first().download(output_path="test", filename="tmp")
      video = mpy.VideoFileClip("test/tmp.mp4", target_resolution=(720, 1280))
      start_time = round(video.duration / 2) - 7.5
      video = video.subclip(start_time, start_time + 15)

   if (length > 1800):
      if (i == len(top_5_videos) - 1):
         video.audio = CompositeAudioClip([AudioFileClip("music/music_3.mp3")])
      else:
         video.audio = CompositeAudioClip([AudioFileClip("music/music_2.mp3")])

   composite_clip = mpy.CompositeVideoClip([video, side_banner_for_video.set_position((max(1280 - len(banner_str)*16, 0), 600))],
                                           size=VIDEO_SIZE).on_color(color=BLACK, col_opacity=1).set_duration(15)

   if (i == len(top_5_videos) - 1):
      ranking_slide.audio = CompositeAudioClip([AudioFileClip("music/music_3.mp3")])
   else:
      ranking_slide.audio = CompositeAudioClip([AudioFileClip("music/music_1.mp3")])

   num = trackNum(num, ranking_slide)
   num = trackNum(num, composite_clip)
   video.close()

channels_intro = mpy.VideoClip(render_channels_intro, duration=5)
channels_intro.audio = CompositeAudioClip([AudioFileClip("music/music_1.mp3")])
num = trackNum(num, channels_intro)

for i in range(len(top_5_channels) - 1, -1, -1):
   ranking_slide = mpy.VideoClip(lambda t: render_ranking_slide(t, i + 1), duration=5)

   channel = top_5_channels[i][0]
   num_videos = top_5_channels[i][1]
   banner_str = f"#{i + 1}: {channel} ({num_videos} videos)"
   side_banner_for_channel = mpy.VideoClip(lambda t: render_side_banner_channels(t, i + 1, channel, num_videos, banner_str), duration=15)

   link = channel_videos[top_5_channels[i][0]]
   print(link)
   length = YouTube(link).length

   if (length > 1800):  # 30 minutes
      video = mpy.VideoClip(render_video_too_long, duration=5)
   else:
      if (YouTube(link).streams.get_by_itag(22)):
         YouTube(link).streams.get_by_itag(22).download(output_path="test", filename="tmp")
      else:
         YouTube(link).streams.first().download(output_path="test", filename="tmp")
      video = mpy.VideoFileClip("test/tmp.mp4", target_resolution=(720, 1280))
      start_time = round(video.duration / 2) - 7.5
      video = video.subclip(start_time, start_time + 15)

   if (length > 1800):
      if (i == len(top_5_videos) - 1):
         video.audio = CompositeAudioClip([AudioFileClip("music/music_3.mp3")])
      else:
         video.audio = CompositeAudioClip([AudioFileClip("music/music_2.mp3")])

   composite_clip = mpy.CompositeVideoClip([video, side_banner_for_channel.set_position((max(1280 - len(banner_str)*16, 0), 600))],
                                           size=VIDEO_SIZE).on_color(color=BLACK, col_opacity=1).set_duration(15)

   if (i == len(top_5_videos) - 1):
      ranking_slide.audio = CompositeAudioClip([AudioFileClip("music/music_2.mp3")])
   else:
      ranking_slide.audio = CompositeAudioClip([AudioFileClip("music/music_1.mp3")])

   num = trackNum(num, ranking_slide)
   num = trackNum(num, composite_clip)
   video.close()

thanks_slide = mpy.VideoClip(render_thanks_slide, duration=5)
thanks_slide.audio = CompositeAudioClip([AudioFileClip("music/music_1.mp3")])
num = trackNum(num, thanks_slide)

# Stitch videos

clips = []

for file in sorted(os.listdir("compile_videos")):
   print(file)
   clips.append(mpy.VideoFileClip(os.path.join("compile_videos", file)))

final_video = concatenate_videoclips(clips)
final_video.write_videofile("your_youtube_wrapped.mp4", fps=30)

shutil.rmtree("compile_videos")
shutil.rmtree("test")