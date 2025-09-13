<h1 align="center">maliang-table</h1>

<p align="center"><a title="Official Website" href="https://xiaokang2022.github.io/maliang/">https://xiaokang2022.github.io/maliang/</a></p>

<p align="center">Extension package of <code>maliang</code> for supporting table</p>

<p align="center">
<a href="https://github.com/Xiaokang2022/maliang-table/releases"><img alt="Version" src="https://img.shields.io/github/v/release/Xiaokang2022/maliang-table?include_prereleases&logo=github&label=Version" title="Latest Version" /></a>
<a href="https://pypistats.org/packages/maliang-table"><img alt="Downloads" src="https://img.shields.io/pypi/dm/maliang-table?label=Downloads&logo=pypi&logoColor=skyblue" title="Downloads" /></a>
<a href="https://pepy.tech/project/maliang-table"><img alt="Total Downloads" src="https://img.shields.io/pepy/dt/maliang-table?logo=pypi&logoColor=gold&label=Total%20Downloads" title="Total Downloads" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table"><img alt="Size" src="https://img.shields.io/github/languages/code-size/Xiaokang2022/maliang-table?label=Size&logo=github" title="Code Size"/></a>
<br/>
<a href="https://github.com/Xiaokang2022/maliang-table/watchers"><img alt="Watchers" src="https://img.shields.io/github/watchers/Xiaokang2022/maliang-table?label=Watchers&logo=github&style=flat" title="Watchers" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table/forks"><img alt="Forks" src="https://img.shields.io/github/forks/Xiaokang2022/maliang-table?label=Forks&logo=github&style=flat" title="Forks" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Xiaokang2022/maliang-table?label=Stars&color=gold&logo=github&style=flat" title="Stars" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Xiaokang2022/maliang-table?label=Issues&logo=github" title="Issues" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Xiaokang2022/maliang-table?label=Pull%20Requests&logo=github" title="Pull Requests" /></a>
<a href="https://github.com/Xiaokang2022/maliang-table/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/Xiaokang2022/maliang-table?label=Discussions&logo=github" title="Discussions" /></a>
</p>

<p align="center">
    <a href="https://star-history.com/#Xiaokang2022/maliang-table&Date">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Xiaokang2022/maliang-table&type=Date&theme=dark" />
            <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Xiaokang2022/maliang-table&type=Date" />
            <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Xiaokang2022/maliang-table&type=Date" />
        </picture>
    </a>
</p>


## 📦 Installation

```shell
pip install maliang-table
```

### 👀 Preview

```python
import maliang
from maliang import table

root = maliang.Tk()
tk_table = table.TkTable(root, data=[[f"Row {r}, Col {c}" for c in range(100)] for r in range(100)])
tk_table.enable_bindings()
tk_table.pack(expand=True, fill="both")
root.mainloop()
```
