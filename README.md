
# Clash订阅添加自定义规则

### 问题：clash使用梯子的订阅地址会定时自动更新并覆盖本地的.yaml配置文件，想加入自定义配置规则时则因此机制会被覆盖掉。

`解决方案1：clash premium 有一个proxy-providers方案参考：` [Proxy Providers](https://github.com/Dreamacro/clash/wiki/configuration#proxy-providers)

`解决方案2：方案1配置之后不生效，也没时间去读源码和折腾，遂来个简单粗暴的法子，使用脚本将订阅中自动更新下来的配置文件内容替换或追加自定义的规则，具体步骤如下：`

* 1、使用python写一个替换、追加规则的代码，替换的情况适用于在订阅的配置文件里有但规则与实际需求不同，需要追加的是订阅规则文件里没有的情况，下面是模板代码，根据实际情况可以修改。

* 2、创建shell脚本runUpdateClashRules.sh，用来运行上面的python代码，注意目录替换。

* 3、创建launchd定时任务配置文件com.updateclashrules.plist，并将它放到~/Library/LaunchAgents目录下，执行launchctl load -w com.updateclashrules.plist。

* 4、验证，tail -f /Users/roc/.config/clash/UpdateClashRules.log查看是否按照预定的时间间隔执行任务并尝试访问规则里的域名确认生效。


