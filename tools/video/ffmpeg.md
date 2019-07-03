# ffmpeg

- **FFMPEG (libx264) “height not divisible by 2”**

  Solution (from [this stackoverflow question](https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2)): 
  ```bash
  ffmpeg -r 1 -i test_%03d.png -vcoded libx264 intention_1sec.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"
  ```
