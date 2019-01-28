# Recovery
- **How to reset or revert a specific file to a specific revision using Git** (obtained from [this post](https://stackoverflow.com/questions/215718/reset-or-revert-a-specific-file-to-a-specific-revision-using-git):)
```bash
git checkout [commit_hash] --file1/to/restore file2/to/restore ... fileN/to/restore
```
`commit_hash` refers to the unique identification  of each commit, obtained from `git log`. If you want to revert to the previous commit of `commit_hash`
use after `[commit_hash]~N` where N is the number of previous commits to revert.
