## Line Counter for TMMC Interview
This is a console application that counts the number of vertical black lines in
an image. The goal is to have a simple, robust app for this task. 

## Assumptions
1. Image is a .jpg.
2. Background is white.
3. Lines are Black. Shades of grey may cause errors that can be played with
by adjusting the value of BLACK_THRESHOLD in count_lines.py
4. Lines are vertical.

## Use
There are two ways to use the application. You can either directly call the .exe in 
the dist directory with an argument, or you can install the required libraries with 
pip install pillow and then run the count_lines python file. 

## Examples
## The below examples assume the image is in the same folder as the executable
count_lines.py img_4.jpg
count_lines.exe img_2.jpg