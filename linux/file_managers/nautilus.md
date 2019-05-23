- **Create new blank file in Nautilus (>=3.6)**: create a blank file inside `~/Templates/`. If you want a custom location,
change in `~/.config/user-dirs.dirs` the variable `XDG_TEMPLATE_DIR` to your custom directory. After this, you only need to launch the command `nautilus -q` in the terminal or `source ~/.config/user-dirs.dirs` and reopen nautilus file manager.
- **Add shortcut for terminal opening in current nautilus folder** ([source](https://stackoverflow.com/questions/48840027/ubuntu-open-terminal-in-current-folder-with-shortcut)):
  1. Open a terminal and go to `~/.local/share/nautilus/scripts`.
  1. Create a file called Terminal with the following content:
  ```bash
  # !/bin/sh
  gnome-terminal
  ```
  1. Make it executable and then close any Nautilus instance:
  ```bash
  chmod +x Terminal
  nautilus -q
  ```
  1. Create (or edit) the `~/.config/nautilus/scripts-accels` file adding these lines:
  ```bash
  F4 Terminal
  ; Commented lines must have a space after the semicolon
  ; Examples of other key combinations:
  ; <Control>F12 Terminal
  ; <Alt>F12 Terminal
  ; <Shift>F12 Terminal
  ```
