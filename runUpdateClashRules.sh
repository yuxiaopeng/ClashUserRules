#!/bin/sh

# 进入clash配置文件所在目录
cd /Users/[replace your user home directory]/.config/clash/ &&
# 记录一下开始时间
echo `date` >> ./UpdateUserRules.log &&
# 执行python脚本
/usr/bin/python3 UpdateUserRules.py
# 运行完成
echo 'update clash config file finished' >> ./UpdateUserRules.log