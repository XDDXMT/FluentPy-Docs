# FluentPy Docs

[官网](https://fluentpy.mcxmcl.cn/) · [中文文档](https://fluentpy.mcxmcl.cn/docs/) · [组件库源码](https://github.com/XDDXMT/FluentPy) · [部署包](https://github.com/XDDXMT/FluentPy-Docs/releases/latest) · [文档问题](https://github.com/XDDXMT/FluentPy-Docs/issues)

FluentPy 官网和中文文档的源码仓库。文档包括入门教程、组件用法、API 与性能说明，也收录实际运行的 Qt 工作台截图和交互动图。项目采用 [MIT 许可证](LICENSE)。

## 本地预览

```console
git clone https://github.com/XDDXMT/FluentPy-Docs.git
cd FluentPy-Docs
python preview_site.py
```

在 [本地首页](http://127.0.0.1:8768/) 和 [本地文档](http://127.0.0.1:8768/docs/) 查看完整网站。预览使用仓库里的静态资源，只需要 Python。可用 `--port` 指定端口。

单独预览文档时，可以双击 Windows 下的 `启动本地文档.bat`，或运行以下命令后打开 [文档简介](http://127.0.0.1:8767/#/introduction)。

```console
python -m http.server 8767 --bind 127.0.0.1 --directory dist
```

## 修改文档

| 路径 | 内容 |
| --- | --- |
| [docs/](docs/) | Markdown 组件指南、构建和发布说明 |
| [home/dist/](home/dist/) | 展示主页及资源 |
| [dist/](dist/) | 文档站的界面、页面数据、配图与图标 |
| [build_content.py](build_content.py) | 生成页面数据、提取组件 API |
| [tools/](tools/) | Qt 控件截图和动图录制 |
| [validate_site.py](validate_site.py) | 检查文档资源、链接和示例代码 |

编辑网页正文时修改 `build_content.py`，然后重新生成 `dist/data.js`。提取 API、运行文档示例或录制配图时，脚本会使用相邻的 FluentPy 源码。

```console
git clone https://github.com/XDDXMT/FluentPy.git ../FluentPy
python -m pip install -e ../FluentPy
python -m pip install -r requirements.txt
python build_content.py
python validate_site.py
node --test tests/icon-catalog.test.cjs
```

已有组件库检出时可使用该目录。源码在其他位置时，将 `FLUENTPY_SOURCE_ROOT` 设为其绝对路径。

重新录制工作台静态截图可运行 `python -m tools.capture_workbench_redesign`。录制后运行 `python build_content.py` 和 `python validate_site.py`。各组件的录制入口在 [tools/](tools/) 内。

## 部署

[文档 Releases](https://github.com/XDDXMT/FluentPy-Docs/releases) 提供完整网站和独立文档 ZIP。也可以从当前检出生成部署包。

```console
python home/package_site.py --output build/releases/FluentPy-Website.zip
python -m pip install -r requirements.txt
python package_deploy.py --output build/releases/FluentPy-Docs.zip
```

完整网站包部署到站点根目录，首页在 `/`，文档在 `/docs/`。独立文档包的 `dist/` 可作为文档目录。两个包都附带部署说明和 SHA-256 校验清单，服务器可直接提供静态文件。

## 许可

FluentPy 的网站和文档采用 [MIT](LICENSE)。Microsoft Fluent System Icons 的许可在 [图标许可证](dist/assets/icons-LICENSE.txt)，Qt、PySide6 和可选 PyQt6 使用各自的许可证。查看 [第三方声明](THIRD_PARTY_NOTICES.md)。
