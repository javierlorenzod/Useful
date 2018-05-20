# One-line scripting
1. Formatting the output of `make` command with colors (to distinguish between errors, warnings and notes), using egrep:
```shell
make | GREP_COLOR='01;31' egrep --color=always 'error|$' | GREP_COLOR='01;31' egrep -i --color=alw│ e. wrong detections).");                                                                                       
ays 'warning|$'
```
2. To find several files (in the example, PNG images) with specific name format and do whatever you want to do with them (in the example, convert them to JPG images), use the following example which uses command line tool **find**:
```shell
find . -type f -name "*.png" -not -name "*heatmaps.png" -print | while read f; do
  mogrify -format jpg $f
done
```
3. To deactivate globbing in order to use * as a character:
```shell
set -f
```
To activate it:
```shell
set +f
```
4. To get the return value of a function in C (obtained from [this answer in StackOverflow](https://stackoverflow.com/questions/8626109/how-can-i-get-what-my-main-function-has-returned):
```shell
./<binary_filename>
echo $?
```
