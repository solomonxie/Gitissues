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
- 图片上传到某个独立的专门放媒体文件的repo中，和文章等都不一样，并引用其raw链接
- 建立每条comment和其md文件的对应表，是个独立文件，对应comment-id和md文件的sha
- 实时监控本地更新，并push到远端；定期查询远端更新，pull到本地。如有冲突，则跳过有冲突的文件，让用户选择方案
- 一个issue转化后是一个文件夹，issue描述和更新信息在README和commit log中;一个comment是文件夹里面的一个md文件.
- 可以设置监控脚本在自己的server服务器上24/7运行，实际上国外server访问github要快很多秒已验证，本地和自己的服务器连接。待考虑是否直接和github连接合适。
- 前期不用python的git库，而是直接调用curl命令实现。容易调试和功能实现，后期再来优化代码。
- 每次访问issues完成之后，都先把整个repo的md文件形成打包备份文件存到电脑某个位置，然后整体删除，再将所有issues保存到repo。 这样考虑是减少了python对比remote和本地的文件变动移动等不方便，成本太大也没必要，因为既然访问api时已经获取了所有内容那就干脆顺便全存下来好了。文件变动追踪这种事还是交给最擅长的git来做。
  但是这样每次都删除再更新，相当于每次的commit都是一整批。这样的话每篇文章都没有自己的history可供追踪回溯。
  也许可以每次都下载issues列表，然后抓取新列表时和本次的对比，对比哪些issues是更新过的才去下载、更新，哪些是没有的就直接下载创建新文件。
  comment不用逐条追踪，它的变动都跟随着issues走就够了，要不然逻辑太复杂不值得，而且issue本身是一个整天文件，完全可以追踪溯源每条comment的更删改变化。comment在这里相当于一篇文章里的一个章节罢了。所以当初没有把每个comment提取出来做一个文章是理智的。即使有些comments自身是一整篇完整文章非常长，但是也不影响。如果真有需要完全可以独立出来作为一个新issue，或者直接变成md文件放到另外的文件夹或另外的repo中去。
  两个issues list对比的python方法，目前思路是：将每个列表里的update-time都取出来放到一个数组里，这样就有新、旧两个数组。用python自带的数组什么方法，或元祖或集合的什么方法，合并两个数组并得到不同的项目，然后再用这些不同的项目（即产生变化的项目）去找到对应的issue序号，进行下载。
  目前想到的是，将两个list合并到一个set()集，去掉duplicates，然后分别用两个list对比集，把没有重复的保留出来。不知道有没有原生的更好的方法。
```python
a = ['a', 'b', 'c', 'd', 'a', 'a']
b = [x for x in a if a.count(x) == 1]
print b
```
- 经过试验，其实是可以整天删除仍保存某个文件的追踪的，前提是文件名没有变。实际上文件名变了的话，即使没有删除再写入，而是直接给文件改个名字，它也会断掉追踪轨迹。倒是把一个文件先删除，不提交，然后再拷贝进来新文件（创建日期等都不一样但内容一样或有改动），只要名字和路径没有变，就有迹可循。如果只凭这点还是可以整天删除再整天复制进来的。因为在删除所有文件后，只要不提交，拷贝进来的新内容，如果是和以前同名同路径，git就认为没有变动，不会提交
