for /r G:\06.07.18 %%a in (sgn.jpg) do (
echo %%a
magick mogrify %%a -resize 1024x1024! %%a
)