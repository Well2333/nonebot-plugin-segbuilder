<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="docs/images/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="docs/images/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-segbuilder

_✨ 为不同的适配器提供更通用且简易的消息段构建方式 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Well2333/nonebot-plugin-segbuilder.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-segbuilder">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-segbuilder.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

跨平台太复杂？不同的适配器区别太大？saa 太难不会用？

别担心，`nonebot-plugin-segbuilder` 将是你的不二之选！

## 📖 介绍

`nonebot-plugin-segbuilder` 是帮助**开发者**快速构建跨平台消息段的应用的工具。相较于 saa ([nonebot-plugin-send-anything-anywhere](https://github.com/felinae98/nonebot-plugin-send-anything-anywhere)) 包办了消息构建与发送，本插件仅实现了消息段构建，更加符合 NoneBot2 原生的编写流程，同时也更易拓展与理解。

但与之相对的，面对与 QQ 消息类型相差越大的平台，这种发送方式的兼容性也会越差，而本插件由于仅负责了消息段构建而不少问题是发送时才会抛出，因此本插件的使用体验下限将远低于 saa。但如果你能接受一定程度的平台相关处理或仅在类 qq 的平台(如 OB11 和 OB12)，本插件的上限也将高于 saa。

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-segbuilder

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分**去掉本插件**, 否则小概率可能造成加载失败

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-segbuilder

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-segbuilder

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-segbuilder

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-segbuilder

</details>

</details>

## 🎉 使用

详见 docs (绝赞咕咕咕中)

## 🙏 感谢

在此感谢以下开发者(项目)对本项目做出的贡献：

- [nonebot-plugin-send-anything-anywhere](https://github.com/felinae98/nonebot-plugin-send-anything-anywhere): 项目的灵感来源以及部分实现的参考
- [nonebot-plugin-template](https://github.com/A-kirami/nonebot-plugin-template): 项目的 README 模板
