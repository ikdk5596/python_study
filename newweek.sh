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

if [ $day == "수요일" ]; then
if [ "$(ls thisweek | grep $day1)" != "$day1" ]; then
	mkdir previous/$folder_name
	mv thisweek/* previous/$folder_name

	for pres in $pre1 $pre2 $pre3 $pre4 $pre5
	do
		git add previous/$folder_name/$pres
	done


	for dayz in $day1 $day2 $day3 $day4 $day5
	do
		mkdir thisweek/$dayz
		git add thisweek/$dayz
	done

	git commit -m "automatically created"
	git push origin master
fi
fi