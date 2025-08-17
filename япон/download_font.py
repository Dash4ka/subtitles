#скачиваю шрифт
!wget "https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip"
!unzip NotoSansCJKjp-hinted.zip
!mkdir -p ~/.fonts
!cp *.otf ~/.fonts/
!fc-cache -fv  # Обновляем кэш шрифтов