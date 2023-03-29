#!/bin/bash

for file in /path/to/input/folder/*.mp4
do
  base=$(basename "$file" .mp4)
  mkdir "/path/to/output/folder/$base"

  duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file")
  segment_duration=5
  segments=$((duration / segment_duration))

  for i in $(seq 1 $segments)
  do
    start=$((i * segment_duration))
    ffmpeg -i "$file" -ss 00:00:$start -t 00:00:$segment_duration -c copy "/path/to/output/folder/$base/$base-$i.mp4"
  done
done
