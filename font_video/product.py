#ja
!ffmpeg -i video.mp4 -vf "subtitles=subs_ja.srt:force_style='FontName=Noto Sans CJK JP'" -c:a copy output_ja.mp4

#zh
!ffmpeg -i video.mp4 -vf "subtitles=subs_zh.srt:force_style='FontName=Noto Sans CJK JP'" -c:a copy output_zh.mp4

#ko
!ffmpeg -i video.mp4 -vf "subtitles=subs_ko.srt:force_style='FontName=Noto Sans CJK JP'" -c:a copy output_ko.mp4