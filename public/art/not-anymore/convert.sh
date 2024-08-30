#!/bin/bash

for file in *.mov *.mp4; do
    # Check if the file exists (this helps if there are no .mov or .mp4 files in the directory)
    if [ -f "$file" ]; then
        output="${file%.*}_web_720p.mp4"
        echo "Processing $file -> $output"
        ffmpeg -i "$file" \
        -vf "scale=720:720:flags=lanczos,format=yuv420p" \
        -c:v libx264 -preset medium -b:v 1500k \
        -c:a aac -b:a 128k \
        -pix_fmt yuv420p \
        -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
        "$output"
    fi
done