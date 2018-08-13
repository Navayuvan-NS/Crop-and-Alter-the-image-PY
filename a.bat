 
for /r G:\Project\Jerald sir\06.07.18 %%a in (ph.jpg) do (
echo %%a
magick mogrify %%a -resize 1024x1024! %%a
)