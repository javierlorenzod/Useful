# APT (Advanced Package Tool)
## apt-mark tool
- In order to prevent updating of specific package, you could use `apt-mark` as follows ([source](https://askubuntu.com/questions/18654/how-to-prevent-updating-of-a-specific-package)):
```bash
sudo apt-mark hold <package-name> # UPDATE --> OFF
sudo apt-mark unhold <package-name> # UPDATE --> ON
```
