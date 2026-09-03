# 部署到 GitHub Pages 指南

以下步骤在项目根目录运行（假设当前目录为 `/Users/everythinggoestonowhere/材料`）：

1) （可选）准备打包目录并规范文件名：

```bash
python3 scripts/normalize_and_package.py . site
```

2) 安装并初始化 Git（若尚未）：

```bash
git init
git add .
git commit -m "Initial commit: prepared for GH Pages"
```

3) 如果有大文件（PSD 等），安装 Git LFS 并追踪：

```bash
brew install git-lfs   # macOS
git lfs install
git lfs track "*.psd"
git add .gitattributes
git add <large files>
git commit -m "Add large files via LFS"
```

4) 在 GitHub 上创建新仓库（例如 `jiaxinxing-site`），然后添加远程并推送：

```bash
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

5) GitHub Actions 已在 `.github/workflows/gh-pages.yml` 中配置为在 `main` push 时部署到 `gh-pages` 分支。若你希望部署到 `docs/`，请修改 `publish_dir`。

6) 验证：在仓库页面打开 `Settings -> Pages`，查看 `gh-pages` 分支是否为发布源，访问 `https://<username>.github.io/<repo>/`。

如果你希望我替你把仓库推到 GitHub（需提供仓库 URL 并允许我执行 push），请确认授权并提供目标仓库地址。否则请按以上步骤在本机完成最后推送。
