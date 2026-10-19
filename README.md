# FluentPy Docs

[官网](https://fluentpy.mcxmcl.cn/) · [组件库源码](https://github.com/XDDXMT/FluentPy) · [文档问题](https://github.com/XDDXMT/FluentPy-Docs/issues)

FluentPy 0.7.3 中文文档的独立开源仓库。首页保留项目简介、Qt 接口演示和 C 流程说明，并展示新版工作台截图。包含网站 HTML、CSS、JavaScript、全部静态页面数据、107 个 Fluent 图标、真实 Qt 控件截图和 GIF，以及内容生成、校验和打包脚本。项目采用 [MIT 许可证](LICENSE)。

## 直接预览

```sh
git clone https://github.com/XDDXMT/FluentPy-Docs.git
cd FluentPy-Docs
python -m http.server 8767 --bind 0.0.0.0 --directory dist
```

打开 <http://127.0.0.1:8767/#/introduction>。Windows 可双击 `启动本地文档.bat`。现成的 `dist/` 可独立预览和部署，无需 Node.js、Qt 或 C 编译器；局域网访问使用本机实际 IP。

## 修改与生成

| 位置 | 内容 |
| --- | --- |
| `dist/index.html`、`dist/styles.css`、`dist/app.js` | 布局、主题、导航、搜索、示例与 API 视图 |
| `build_content.py` | 组件内容、分类与源码接口提取 |
| `dist/data.js` | 生成的页面数据，不直接编辑 |
| `dist/assets/` | 本地图片、GIF、SVG 与许可文件 |
| `dist/native-flow.*`、`dist/migration.*` | C 后端说明和 Qt 接口过渡动画 |
| `validate_site.py`、`package_deploy.py` | 校验与完整静态包 |
| `SOURCE.json` | 本次同步对应的组件库提交和文件校验值 |

编辑 HTML、CSS 或 JS 后即可预览。修改文档内容、提取 API 时，需要单独检出组件库：

```sh
git clone https://github.com/XDDXMT/FluentPy.git ../FluentPy
python -m pip install -e ../FluentPy
python -m pip install -r requirements.txt
python build_content.py
python validate_site.py
```

脚本自动寻找相邻的 `FluentPy/`。如源码位于其他目录，先设置 `FLUENTPY_SOURCE_ROOT`：

```powershell
$env:FLUENTPY_SOURCE_ROOT = 'D:\path\to\FluentPy'
python build_content.py
python validate_site.py
```

Linux/macOS 使用 `export FLUENTPY_SOURCE_ROOT=/path/to/FluentPy`。组件库中的 Python 回退可在没有 C 扩展时运行；后端计算以 C 为首选加速，Qt 继续负责界面。

Qt 截图和动图的录制工具集中在[组件库的文档目录](https://github.com/XDDXMT/FluentPy/tree/main/sites/fluentpy-docs)，本仓库保留生成后的媒体。需要重新录制时，在组件库根目录运行 `python sites/fluentpy-docs/capture_workbench_redesign.py` 或对应的 `capture_*.py`，然后重新生成、校验并同步文档。

## 部署

直接将 `dist/` 作为静态站点根目录，或生成包含全部资源和校验清单的压缩包：

```sh
python -m pip install -r requirements.txt
python package_deploy.py --output build/FluentPy-docs-complete.zip
```

包内包含 `dist/`、`部署说明.txt` 和 `SHA256SUMS.txt`。覆盖部署时保留目录结构，将网站根目录指向 `dist/`。正式主页为 <https://fluentpy.mcxmcl.cn/>。服务器无需 Python、Qt 或 Node.js。

## 同步与许可

本仓库由组件库内的 `scripts/export_docs.py` 导出；对应版本见 `SOURCE.json`。组件库内保留文档副本，贡献文档时请明确修改的来源并同步相关内容。

FluentPy 的网站源码及文档采用 MIT，保留原始版权声明与许可文本。Microsoft Fluent System Icons 的许可在 `dist/assets/icons-LICENSE.txt`；第三方声明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。Qt/PySide6 及可选 PyQt6 的许可单独适用，本仓库不分发它们的二进制。
