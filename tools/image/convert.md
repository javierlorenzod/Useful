# Useful commands I found using `convert` tool

This tool helps me converting images between formats. Below is a list of useful commands I found using this tool:

- **Converting to EPS format**: info extracted from this [StackOverFlow post]() 
  - Level 2: it provides the best compatibility, and works well with jpeg images.
  - Level 3: it will produce the smallest files. Use it if you can.
  command:
  ```bash
  convert fig.png eps3:fig.eps
  ```
- **Batch converting btw formats**: info extracted from [this StackExchange post](https://superuser.com/questions/71028/batch-converting-png-to-jpg-in-linux)
  1. Solution with loops: `for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done`
  1. Solution without loops: `ls -1 *.png | xargs -n 1 bash -c 'convert "$0" "${0%.*}.jpg"'`
  1. Solution without loops and using multiple jobs (**performance boost!**): `ls -1 *.png | parallel convert '{}' '{.}.jpg'`
  1. Previous solution with stats (**performance boost!**): `ls -1 *.png | parallel --eta convert '{}' '{.}.jpg'`
  1. Same previous-previous solution with GNU parallel syntax: `parallel convert '{}' '{.}.jpg' ::: *.png`
