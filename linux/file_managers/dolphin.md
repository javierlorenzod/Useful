## Invalid protocol when attempting to access SMB share

When this error raises after trying to access an SMB share using its IP (example: `smb://X.X.X.X/`), it is because of the package named *kio-extras* is not installed. It happens in Ubuntu 16.04 LTS (in Kubuntu it does not happen, maybe because it uses KDE as default desktop environment).
[Source](https://forum.kde.org/viewtopic.php?f=224&t=131642)
