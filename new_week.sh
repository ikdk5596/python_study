#/bin/sh
day=$(date +%A)
pre1=$(date -d '7 day ago' +%m-%d)
pre2=$(date -d '6 day ago' +%m-%d)
pre3=$(date -d '5 day ago' +%m-%d)
pre4=$(date -d '4 day ago' +%m-%d)
pre5=$(date -d '3 day ago' +%m-%d)
pre6=$(date -d '3 day ago' +%d)
day1=$(date -d '0 day' +%m-%d)
day2=$(date -d '1 day' +%m-%d)
day3=$(date -d '2 day' +%m-%d)
day4=$(date -d '3 day' +%m-%d)
day5=$(date -d '4 day' +%m-%d)

folder_name=$pre1\to$pre6

if [ $day == "월요일" ]; then
if [ "$(ls thisweek | grep $day1)" != "$day1" ]; then
	mkdir previous/$folder_name
	mv thisweek/* previous/$folder_name

	git add previous/*

	for dayz in $day1 $day2 $day3 $day4 $day5
	do
		mkdir thisweek/$dayz
		echo "" > thisweek/$dayz/.init
	done


	git add --all thisweek/*
	git commit -m "automatically generated"
	git push origin master
fi
fi
