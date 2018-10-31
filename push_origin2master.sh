#!/bin/bash
today=$(date +%m-%d)

name=$USER

commit=$name\_upload_on_$today

git pull
git add thisweek/$today/$name\_$today.py
git commit -m "$commit"
git push origin master
