#!/bin/bash

name=嘻嘻要哈哈
channel=猜数字
echo "您好， $name, 欢迎来到$channel!"
#number=$((RANDOM % 10 + 1))
#echo $number
while true
do
number=$((RANDOM % 10 + 1))
#echo $number
echo "请输入一个1-10之间的数字"
read guess
if [[ $guess -eq $number ]]; then
	echo "恭喜你猜对了！是否继续？ （y/n）: "
	read choice
	if [[ $choice = "y" ]] || [[ $choice = "Y" ]]; then
		continue
	else
		break
	fi
elif [[ $guess -lt $number ]]; then
	echo "小了"
else
	echo "大了"
fi
done
