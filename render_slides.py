import gizeh as gz

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def render_welcome_slide(t):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text1 = gz.text("Welcome to YouTube Wrapped!", fontfamily="Charter",
                   fontsize=75, fontweight='bold', fill=WHITE, xy=(29 * 21.9, 280))

   text2 = gz.text("Let's review what you watched!", fontfamily="Charter",
                   fontsize=75, fontweight='bold', fill=WHITE, xy=(29 * 22.1, 380))

   text1.draw(surface)
   text2.draw(surface)
   return surface.get_npimage()


def render_stats_slide(t, num_videos, num_channels):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text1 = gz.text("2020 was a busy year for you!", fontfamily="Charter",
                   fontsize=75, fontweight='bold', fill=WHITE, xy=(29 * 21.9, 170))

   text2 = gz.text(f"You watched {num_videos} different videos", fontfamily="Charter",
                   fontsize=55, fontweight='bold', fill=WHITE, xy=(34 * 19.1, 320))

   text3 = gz.text(f"across {num_channels} different channels!", fontfamily="Charter",
                   fontsize=55, fontweight='bold', fill=WHITE, xy=(32 * 19.1, 380))

   text4 = gz.text("Let's look at your top 5 most watched videos!", fontfamily="Charter",
                   fontsize=55, fontweight='bold', fill=WHITE, xy=(45 * 14.1, 520))

   text1.draw(surface)
   text2.draw(surface)
   text3.draw(surface)
   text4.draw(surface)
   return surface.get_npimage()


def render_ranking_slide(t, rank):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text = gz.text(f"#{rank}", fontfamily="Charter",
                  fontsize=130, fontweight='bold', fill=WHITE, xy=(2 * 315, 340))

   text.draw(surface)
   return surface.get_npimage()


def render_side_banner_videos(t, rank, video_name, num_views, banner_str):
   surface = gz.Surface(min(len(banner_str)*16, 1280), 100, bg_color=(1, 1, 1))

   text = gz.text(banner_str, fontfamily="Charter",
                  fontsize=30, fontweight='bold', fill=BLACK, xy=(10, 55), h_align="left")

   text.draw(surface)
   return surface.get_npimage()


def render_channels_intro(t):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text = gz.text("Now let's have a look at your top 5 channels!", fontfamily="Charter",
                  fontsize=55, fontweight='bold', fill=WHITE, xy=(45 * 14.2, 350))

   text.draw(surface)
   return surface.get_npimage()


def render_side_banner_channels(t, rank, channel, num_videos, banner_str):
   surface = gz.Surface(min(len(banner_str)*16, 1280), 100, bg_color=(1, 1, 1))

   text = gz.text(banner_str, fontfamily="Charter",
                  fontsize=30, fontweight='bold', fill=BLACK, xy=(10, 55), h_align="left")

   text.draw(surface)
   return surface.get_npimage()


def render_thanks_slide(t):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text = gz.text("Thanks for watching!", fontfamily="Charter",
                  fontsize=80, fontweight='bold', fill=WHITE, xy=(20 * 32, 350))

   text.draw(surface)
   return surface.get_npimage()


def render_video_too_long(t):
   surface = gz.Surface(1280, 720, bg_color=(0, 0, 0))

   text1 = gz.text("Sorry :(", fontfamily="Charter",
                   fontsize=70, fontweight='bold', fill=WHITE, xy=(32 * 20, 280))

   text2 = gz.text("The video is too long", fontfamily="Charter",
                   fontsize=70, fontweight='bold', fill=WHITE, xy=(32 * 20, 380))

   text1.draw(surface)
   text2.draw(surface)
   return surface.get_npimage()