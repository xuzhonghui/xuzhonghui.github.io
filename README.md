常规提交：
```python
git status  # 查看当前修改
git add .   # 将当前目录下所有改动加入“暂存区”
git commit -m "本次修改说明"  # 将暂存区内容提交为一个本地版本记录
git push origin main  # 将本地 main 分支的提交推送到 GitHub 的 origin 远程仓库
```

只想提交指定文件：
```python
git add 文件路径
git commit -m "修改某个文件"
git push
```

推送被拒绝:
> 例如看到类似 rejected、fetch first 的提示，先拉取远程更新，再推送：
```python
git pull --rebase origin main   # 先把远程新增提交放到前面，再将你的本地提交重新接到后面，提交历史会更整洁。
git push origin main
```

从 GitHub 拉取最新内容:
```python
# 本地无改动时候直接拉取
git status  
git pull origin main    

# 本地有未提交的修改，但与远程不冲突
# 1、先提交再拉取
git add .
git commit -m "暂存本地修改"
git pull --rebase origin main

# 2、先暂存
git stash   # 暂时收起未提交的本地修改
git pull origin main
git stash pop   # 恢复刚才收起的修改，并删除这份临时暂存

# 如果拉取的时候本地有冲突
git status  # 先查看冲突文件，然后手动处理冲突
git add 冲突文件路径  # 标记冲突已处理
git commit -m "解决合并冲突"  # 二选一： 若使用 git pull origin main（合并方式） 
git rebase --continue   # 二选一： 若使用 git pull --rebase origin main（变基方式 二选一
git push origin main

# 如果不想处理冲突，想撤销拉取过程
git merge --abort   # 二选一： 普通合并拉取时
git rebase --abort  # 二选一： --rebase 拉取时
```

如果要重命名文件
```python
# 常规操作
git mv 旧文件名 新文件名
git commit -m "重命名文件"
git push

# 如果已经在资源管理器里手动重命名过了
git status
git add -A
git commit -m "重命名文件"
git push
```

如果要删除文件
```python
git rm 文件名
git commit -m "删除不再使用的文件"
git push
```

删除或重命名后向反悔
```python
git restore --staged 文件名     # 取消暂存
git restore 文件名  # 将文件恢复到最近一次提交的状态
```