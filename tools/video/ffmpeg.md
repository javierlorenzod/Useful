# ffmpeg

- **FFMPEG (libx264) “height not divisible by 2”**

  Solution: 
  ```bash
  ffmpeg -r 1 -i test_%03d.png -vcoded libx264 intention_1sec.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"
  ```
