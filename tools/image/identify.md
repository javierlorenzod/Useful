- **Find all images with certain pixel size**: info extracted from [this post in Ask Ubuntu](https://askubuntu.com/questions/238136/how-to-find-all-images-with-a-certain-pixel-size-using-commandline)
  - 2 ways of doing it (in this example, the size found is less than 300 in height and width):
    1. `find . -iname "*.jpg" -type f -exec identify -format '%w %h %i' '{}' \; | awk '$1<300 || $2<300'`
    1. `find . -iname "*.jpg" -type f | xargs -I{} identify -format '%w %h %i' {} | awk '$1<300 || $2<300'`
