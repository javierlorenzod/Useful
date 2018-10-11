# MPV (a media player)
## RAW videos
- Convert RAW video to MP4
```bash
mpv -demuxer=rawvideo 
  --demuxer-rawvideo-mp-format=<bayer_format_or_whatever_you_need>
  <video_filename>
  --demuxer-rawvideo-w=<video_width> 
  --demuxer-rawvideo-h=<video_height>  
  --demuxer-rawvideo-fps=<video_fps>
  --screenshot-png-compression=<selected_compression> 
  -o <output_video_filename> 
  --of=mp4
```
