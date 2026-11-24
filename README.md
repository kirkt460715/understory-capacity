# 林下经营申报资料

本项目整理林地和林分状态、林下经营申请、季节监测、已批准活动与经营收益，供林下经营项目复核生态容量和共同资源使用情况。

## 资料

`data/manifest.json` 说明本地合成资料字段。申请、地块、监测和经营记录保留不同的主体、期间和统计单位。

字段含义及有效期约定见[资料口径](资料口径.md)。

## 本地检查

使用 Python 3.11 或更新版本，无需安装第三方依赖。

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```
