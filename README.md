# Luna Robotics 月神机器人 · 官网

为星际探索造通用人形机器人。月球 · 火星 · 人类的下一个家园。

## 目录结构

```
company-website/
├── index.html              主站首页 — 太空人形机器人方向
├── btc-training/index.html 宝信图灵认证（BTC）第二期专题页
├── deploy.py               本地服务器部署脚本
└── .gitignore
```

## 本地预览

```bash
python deploy.py                    # 默认 8080 端口，自动打开浏览器
python deploy.py --port 9000        # 指定端口
python deploy.py --no-browser       # 不自动打开浏览器
```

访问：
- 主站首页 `http://127.0.0.1:8080/index.html`
- BTC 专题 `http://127.0.0.1:8080/btc-training/index.html`

## 线上地址

https://huangwei361.github.io/luna-robotics/

- 主站首页 `https://huangwei361.github.io/luna-robotics/`
- BTC 专题 `https://huangwei361.github.io/luna-robotics/btc-training/`

## 更新流程

```bash
git add .
git commit -m "描述"
git push origin main
```

GitHub Pages 会自动重新构建，通常 1-2 分钟生效。

## 技术说明

- 纯静态 HTML + CSS，无构建步骤，无第三方依赖
- 深空主题配色：`#050A18` 底色 / 火星橙 `#E27B58` / 荧光绿 `#64FFDA`
- 响应式布局，移动端自动折叠导航
- 星空背景使用纯 CSS 动画实现

## 内容说明

BTC 专题页内容依据《宝信图灵认证（BTC）第二期通知》（2026年11月6日）整理，
认证等级、考核方式、考试安排等均来自通知原文。
