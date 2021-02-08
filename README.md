# Aggregate Your Data
As YouTube no longer provides access to a user's watch history through their latest API (forum [here](https://issuetracker.google.com/issues/35172816)), I had to resort to other more creative but cumbersome methods of obtaining this watch history in a reasonable manner. I have outlined the method I used below.

1. While logged in to your YouTube/Google account, go to the following url: [https://www.youtube.com/feed/history](https://www.youtube.com/feed/history). It will take you to a lazy-loading page that contains all of your watch history.
2. Scroll like you've never scrolled before. At least that's what I did when I first started this project. It took about 2 hours and a bit of my sanity to scroll through my entire watch history for the year 2020 alone. Since then, I've found a pretty neat Google Chrome extension ([Scroll it!](https://chrome.google.com/webstore/detail/scroll-it/nlndoolndemidhlomaokpfbicfnjeeed)) that will speed up the process for you somewhat. You don't necessarily have to scroll to the previous year if you don't want to. I think scrolling even a couple months should be able to provide a somewhat interesting summary.
3. Once you are satisfied with your scrolling efforts, press *F12*, or *Inspect Element*. Select the top-most **\<html\>** tag, right-click and select **Edit as HTML**. Select all and copy into a text file. Depending on the number of videos you've loaded in the previous step, it could potentially take a couple of minutes between each step.
4. Save the text file.

# Run It Yourself
1. Clone this repository.
2. Ensure you have all the Python packages list in *requirements.txt* installed. Otherwise, you can simply run `pip install -r requirements.txt`.
3. Update **line 10** of *main.py* with the path to the text file containing your data, as described in the above section **Aggregate Your Data**.
3. Run *main.py*. After a couple minutes of automated downloading, splicing and stitching of multiple videos, your video summary can be found under *your_youtube_wrapped.mp4*.

# YouTube Wrapped

This is a simple video automation project I took on over this past winter break. Having been recently inspired by the *2020 Wrapped* feature on Spotify, I decided to implement a similar feature for YouTube, another platform on which I spend large quantities of time.

Although this application is nowhere near as flashy as its audible counterpart, I had to jump over a few hurdles throughout the process that piqued my interest and made the project a fun challenge.

Sample frames from the output video are shown below.

![welcome](/sample_frames/welcome.png)

![stats](/sample_frames/stats.png)

![channel_intro](/sample_frames/channel_intro.png)

![ranking](/sample_frames/ranking.png)

![clip](/sample_frames/clip.png)

![thanks_for_watching](/sample_frames/thanks_for_watching.png)
