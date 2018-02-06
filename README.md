# gitissues
> Focus on making git issues to a RELIABLE notebook, with a RELIABLE backup solution and a whole set of access method such as desktop, iphone and web page(as blog).

专注于issues博客功能，出发点就不同于桌面已有的和手机上鲜有的应用。

## 特点：
- 每个issues笔记都算为github的contribution，美化profile工作日历
- 自动转md文件并上传到github中的repo，更填改完全对应
- 实时同步网络repo中的issues
- 本地存储性，没联网也可以编辑保存，联网了再自动同步（放心）
- 定期自动备份到多端
- 图片上传到github自带的repo中（市面所有应用都没做到）
- 同时支持desktop和iphone和web page
- 界面和笔记应用相同（如note.app）
- 可以设定某个文集的来源，如github或Bitbucket, 这样可以bitbuckets设置私密文集。
- 还可以同时监控多repo中的issues，集合到一处（为不同来源到issues设置lables或tags）

## 实现主要技巧：
- 将issues映射到其repo的某一特定分支，每个comment为单独md文件
- 图片上传到repo中并引用其raw链接
- 建立每条comment和其md文件的对应表，是个独立文件，对应comment-id和md文件的sha
- 实时监控本地更新，并push到远端；定期查询远端更新，pull到本地。如有冲突，则跳过有冲突的文件，让用户选择方案
- 一个issue转化后是一个文件夹，issue描述和更新信息在README和commit log中;一个comment是文件夹里面的一个md文件.
- 可以设置监控脚本在自己的server服务器上24/7运行，实际上国外server访问github要快很多秒已验证，本地和自己的服务器连接。待考虑是否直接和github连接合适。
- 前期不用python的git库，而是直接调用curl命令实现。容易调试和功能实现，后期再来优化代码。

