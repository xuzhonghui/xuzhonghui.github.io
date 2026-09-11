---
layout: post
title: "从零搭建并维护 GitHub Pages 个人博客"
date: 2026-09-11
categories: [技术, GitHub Pages]
tags: [GitHub Pages, Jekyll, Markdown, 博客]
---

本文记录本博客从零搭建、发布到日常维护的完整流程。博客使用 GitHub Pages + Jekyll，不需要购买服务器，也不需要手动部署后端服务。

## 1. 成品与工作方式

本博客的公开地址为：

<https://xuzhonghui.github.io/>

日常工作方式很简单：

1. 在本地仓库中新增或修改 Markdown 文章；
2. 使用 Git 提交并推送到 GitHub；
3. GitHub Pages 自动构建网站；
4. 等待一两分钟后刷新网站查看效果。

当前博客使用“左侧分类树 + 右侧正文”的单页阅读方式：点击左侧文章时，正文会在右侧载入；每篇文章仍保留独立链接，方便分享。

## 2. 第一次创建博客

### 2.1 创建仓库

在 GitHub 新建一个 Public（公开）仓库。

本博客使用的是**用户站点仓库**。用户站点仓库名称必须精确等于：

```text
用户名.github.io
```

当前 GitHub 用户名为 `xuzhonghui`，因此仓库名必须是：

```text
xuzhonghui.github.io
```

对应的网站地址固定为：

```text
https://xuzhonghui.github.io/
```

用户站点与普通项目站点的区别是：用户站点没有仓库名这一层 URL 路径，因此访问地址更简洁。

### 2.2 启用 GitHub Pages

在仓库页面执行：

1. 点击 `Settings`；
2. 点击左侧 `Pages`；
3. 在 `Build and deployment` 中选择 `Deploy from a branch`；
4. Branch 选择 `main`，文件夹选择 `/(root)`；
5. 点击 `Save`。

每次推送到 `main` 分支后，GitHub Pages 都会自动重新构建。

### 2.3 最小 Jekyll 配置

仓库根目录的 `_config.yml` 是站点配置文件，核心内容如下：

```yml
title: 小羊哥
description: 记录技术、想法与生活
url: "https://xuzhonghui.github.io"
baseurl: ""
theme: jekyll-theme-minimal
lang: zh-CN
```

用户站点必须将 `baseurl` 保持为空字符串。因为网站已经位于域名根目录，不能再填写 `/xuzhonghui` 或其他仓库路径。

## 3. 当前仓库结构

```text
xuzhonghui.github.io/
├─ _config.yml                 # 网站基础配置
├─ index.html                  # 首页：向布局传递文章数据
├─ _layouts/
│  └─ home.html                # 首页布局、分类树与单页文章加载逻辑
├─ _posts/                     # 所有博客文章
│  ├─ 2026-09-10-MyFirstBlog.md
│  └─ 2026-09-11-HowToUsePages.md
├─ assets/
│  ├─ css/
│  │  └─ style.scss            # 炭灰主题与响应式样式
│  └─ images/
│     └─ avatar.jpg            # 侧边栏头像
└─ README.md
```

几个以 `_` 开头的目录是 Jekyll 的约定：

- `_posts`：Jekyll 会将其中符合命名规则的 Markdown 文件编译成文章；
- `_layouts`：存放页面布局模板；
- `_config.yml`：定义站点标题、地址、主题等全局配置。

## 4. 新建一篇文章

### 4.1 文件名规则

在 `_posts` 目录中新建文件，名称必须采用下面格式：

```text
YYYY-MM-DD-英文文章标识.md
```

例如：

```text
_posts/2026-09-15-github-pages-guide.md
```

日期影响文章的发布时间与排序；英文标识会成为文章 URL 的一部分。建议使用小写英文和连字符。

### 4.2 文章模板

复制以下模板即可开始写作：

```md
---
layout: post
title: "文章标题"
date: 2026-09-15
categories: [技术, GitHub Pages]
tags: [Jekyll, 博客]
---

这里是第一段正文。首页或搜索摘要通常会使用文章开头的内容。

## 一级标题

正文内容。

### 二级标题

更多正文内容。
```

`layout: post` 不要删除，它表示这是一篇博客文章。

## 5. 分类、子分类与文章目录

当前博客侧边栏会根据 `categories` 自动生成可折叠的文件夹树。

### 5.1 两级分类

```yml
categories: [技术, GitHub Pages]
```

显示效果：

```text
▾ 技术
  ▸ GitHub Pages
    ─ 文章标题
```

### 5.2 三级、四级或更多分类

分类层级没有固定上限。例如：

```yml
categories: [技术, JavaScript, 前端工程化, 构建工具]
```

会生成：

```text
▾ 技术
  ▸ JavaScript
    ▸ 前端工程化
      ▸ 构建工具
        ─ 文章标题
```

侧边栏默认展开第一个顶级分类，其余分类可点击三角按钮展开或收起。

### 5.3 未分类文章

不建议省略分类。至少填写一个顶级分类：

```yml
categories: [未分类]
```

常用分类示例：

```yml
categories: [技术, Python]
categories: [技术, Windows]
categories: [生活, 随笔]
categories: [读书, 技术书]
```

## 6. 文章排版与自动大纲

当前博客会为**所有文章自动生成位于左侧文章目录栏与正文之间的大纲**。不需要在 Markdown 中手写“目录”，也不需要手动添加锚点。

只要使用 Markdown 标题，系统会自动提取 `##`、`###` 和 `####` 标题，并在桌面端的文章目录栏与正文之间生成固定大纲。阅读正文时，大纲不会随页面向下滚动；点击任一大纲项会平滑跳转到对应段落。左侧的“隐藏大纲 / 显示大纲”按钮可由读者自行切换大纲可见性，且选择会保存在当前浏览器中。

```md
## 准备工作

### 安装工具

### 创建仓库

## 发布网站
```

显示层级为：

```text
准备工作
  安装工具
  创建仓库
发布网站
```

使用建议：

- `##` 用于文章主要章节；
- `###` 用于主要章节下的小节；
- `####` 只用于确实需要的更细层级；
- 不要从 `##` 直接跳到 `####`，避免大纲层级断裂；
- 文章的 Front Matter 标题由页面标题显示，不会重复出现在右侧大纲中；
- 浏览器宽度不足时，大纲会自动隐藏，保证手机端阅读空间。

## 7. 插入静态图片、GIF 和视频

### 7.1 图片与 GIF

建议为每篇文章创建独立资源目录：

```text
assets/images/posts/github-pages-guide/
├─ cover.png
└─ demo.gif
```

在文章中引用时使用：

```md
![封面说明]({{ site.baseurl }}/assets/images/posts/github-pages-guide/cover.png)

![操作演示]({{ site.baseurl }}/assets/images/posts/github-pages-guide/demo.gif)
```

图片与 GIF 的 Markdown 写法相同。GIF 文件通常较大，建议尽量压缩，或使用动画 WebP。

### 7.2 本地 MP4 视频

短视频可放在：

```text
assets/videos/demo.mp4
```

然后在文章中使用 HTML：

```html
<video controls width="100%" preload="metadata">
  <source src="{{ site.baseurl }}/assets/videos/demo.mp4" type="video/mp4">
  你的浏览器不支持视频播放。
</video>
```

### 7.3 视频平台嵌入

大视频推荐上传到哔哩哔哩、YouTube 等平台，再嵌入播放器。这样不会让 Git 仓库和 Pages 流量快速膨胀。

GitHub Pages 更适合文章、图片和短演示；不适合托管大量或高清的视频文件。

## 8. 本地修改、提交与发布

在 Windows PowerShell 中进入仓库：

```powershell
cd E:\GitHubProjects\xuzhonghui
```

仓库重命名为用户站点后，本地远程地址应为：

```powershell
git remote set-url origin https://github.com/xuzhonghui/xuzhonghui.github.io.git
git remote -v
```

查看改动：

```powershell
git status
```

确认改动无误后，依次执行：

```powershell
git add .
git commit -m "新增 GitHub Pages 使用指南"
git push origin main
```

命令含义：

- `git add .`：将当前目录的修改加入待提交列表；
- `git commit -m "说明"`：创建一次本地版本记录；
- `git push origin main`：将本地提交推送至 GitHub 的 `main` 分支。

推送后可在仓库的 `Actions` 标签页查看构建状态。构建成功后，再访问博客地址：

<https://xuzhonghui.github.io/>

## 9. 日常文章管理建议

### 9.1 写作前

1. 确定文章标题、日期和分类；
2. 创建符合规则的文件名；
3. 先写 Front Matter；
4. 再开始正文。

### 9.2 写作后

1. 检查标题层级；
2. 检查图片路径；
3. 检查分类是否放在正确层级；
4. 使用 `git status` 查看变更；
5. 提交并推送；
6. 等待 Pages 构建后访问网页确认。

### 9.3 修改旧文章

直接修改 `_posts` 中对应 Markdown 文件即可。若文件名中的日期或英文标识改变，文章的独立链接也会改变；已经分享出去的旧链接可能失效，因此通常只修改标题和正文，不轻易修改文件名。

### 9.4 删除文章

删除对应的 `_posts/YYYY-MM-DD-name.md` 文件后，提交并推送。删除前建议先保留本地备份，或通过 Git 提交记录恢复。

## 10. 主题与页面维护

当前界面的主要文件是：

- `assets/css/style.scss`：颜色、间距、字体、侧栏宽度、移动端样式；
- `_layouts/home.html`：头像、站点名称、可折叠文件夹树、文章异步加载；
- `index.html`：向分类树提供文章标题、URL 与分类数据。

如果只想改颜色、间距或字体，优先修改 `assets/css/style.scss`。如果要改侧边栏的 HTML 结构或文章点击方式，再修改 `_layouts/home.html`。

### 10.1 大纲栏宽度与响应式规则

桌面端开启大纲后，页面从左到右依次为“文章目录栏 / 本页大纲 / 正文”。本页大纲默认宽度为 `200px`，读者可以拖拽大纲栏右侧的分隔边框，在 `140px` 至 `320px` 间自行调整宽度；选择会保存在当前浏览器中。

三栏布局由 `assets/css/style.scss` 中的 CSS 变量控制：

```scss
:root {
  --toc-width: 200px;
}

body.toc-visible .blog-shell {
  grid-template-columns: 288px var(--toc-width) minmax(0, 1fr);
}
```

三个值的含义是：

```text
左侧文章目录栏 | 中间文章大纲栏 | 右侧正文区域
288px          | 可拖拽调整      | 剩余全部宽度
```

如果要修改新访客看到的默认宽度，调整 `--toc-width` 的 `200px` 即可。大纲栏越宽，正文可用宽度越小；建议日常使用保持在 `160px` 至 `200px` 左右。

当浏览器宽度小于或等于 `1280px` 时，样式会自动隐藏大纲栏，页面恢复为“文章目录栏 / 正文”的双栏布局；宽度大于 `1280px` 时，读者可以通过左侧的“隐藏大纲 / 显示大纲”按钮控制其可见性。

修改主题前建议先提交一次 Git：

```powershell
git add .
git commit -m "备份当前博客样式"
```

这样效果不满意时，可以方便地回退到此前版本。

## 11. 常见问题排查

### 11.1 页面样式没有更新

1. 先确认 GitHub Actions / Pages 构建成功；
2. 使用 `Ctrl + F5` 强制刷新浏览器；
3. 或使用无痕窗口重新访问；
4. 检查 `assets/css/style.scss` 是否保存并已推送。

### 11.2 图片不显示

检查三项：

1. 图片是否已放入仓库并提交；
2. 文件名大小写是否完全一致；
3. 引用路径是否包含 `{{ site.baseurl }}`。

当前是用户站点，图片可以直接从域名根目录引用。为兼容未来的站点迁移，仍建议统一写成：

```md
{{ site.baseurl }}/assets/images/...
```

在用户站点中，`site.baseurl` 是空字符串，因此最终路径就是 `/assets/images/...`。

### 11.3 新文章没有出现在侧边栏

检查：

1. 文件是否在 `_posts` 目录；
2. 文件名是否满足 `YYYY-MM-DD-name.md`；
3. Front Matter 是否由两行 `---` 正确包围；
4. `date` 是否是未来日期；
5. GitHub Pages 构建是否成功。

### 11.4 页面链接或样式全部失效

重点检查 `_config.yml` 的 `baseurl`。本博客是用户站点，必须保持为空：

```yml
baseurl: ""
```

如果误写成 `/xuzhonghui` 或其他内容，CSS、头像、图片与文章链接都可能指向错误地址。

## 12. 推荐的维护习惯

- 一篇文章对应一次或少数几次清晰的 Git 提交；
- 提交信息写清楚，例如“新增 Windows 文件管理文章”；
- 图片按文章单独分目录存放；
- 分类不要频繁改名，避免文章目录混乱；
- 定期使用 `git status` 检查未提交内容；
- 修改主题前先创建提交作为可恢复的版本点；
- 文章多起来后，可考虑新增“关于我”“归档”“标签”等页面。

至此，你只需要专注于 Markdown 写作与 Git 提交，GitHub Pages 会负责把仓库内容自动发布为博客网站。