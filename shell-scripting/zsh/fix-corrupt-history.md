To fix zsh history after it became corrupt due to a machine shutdown, it is needed to follow these steps, extracted from [this post](https://superuser.com/questions/957913/how-to-fix-and-recover-a-corrupt-history-file-in-zsh):

```zsh
# Move previous history to a backup file
mv .zsh_history .zsh_history_bad
# Find all the printable strings in the corrupt file and save them in the new history file
strings .zsh_history_bad > .zsh_history
# Read the history file and append the contents to the history list (not sure)
fc -R .zsh_history
```
