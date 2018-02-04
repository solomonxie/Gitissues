# gitissues
> Focus on making git issues to a blog or a note, with a whole set of access method such as desktop, iphone and web page.

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

实现主要技巧：
- 将issues映射到其repo的某一特定分支，每个comment为单独md文件
- 图片上传到repo中并引用其raw链接
- 建立每条comment和其md文件的对应表
- 实时监控本地更新，并push到远端；定期查询远端更新，pull到本地。如有冲突，则跳过有冲突的文件，让用户选择方案
