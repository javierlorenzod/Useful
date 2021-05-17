#!/bin/bash

echo "Converting video ${0} to ${1}"

mpv \
  -demuxer=rawvideo \
  --demuxer-rawvideo-mp-format=bayer_rggb8 \
  "${1}" \
  --demuxer-rawvideo-w=640 \
  --demuxer-rawvideo-h=480  \
  --demuxer-rawvideo-fps=30 \
  -o "${2}" \
  --of=mp4
