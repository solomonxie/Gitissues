# gitissues
Based on Github Issues for the excellence of its writing experience,
this program aims to help user generate entire blog site or sites
without concerns of any technical  requirements.
It lets the user fully focused on writing itself, and the program will keep eyes
on the updates 24/7 and generate/update personal blog site automatically.
What the program does is it retrives data through Github API,
and organize the content into different categories automatically and
generate entire static website in HTML and also in the format of
trending site generators like, Jekyll, Gitbooks, Readthedocs, Hugo nad Hexo.

## Branches

Master branch is for development (weird but convenient for personal use)
Stable brances are as snapshots for properly working versions.


## Docker Version

```sh
make build && make run && make into
```


## Architecture

Docker build --> generate credentials into envfile --> docker run with envfile --> docker cmd entry -->
crontab -> all_in_one.py
