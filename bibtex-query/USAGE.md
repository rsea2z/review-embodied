# BibTeX Query Skill - 使用示例

## 功能概述

这个 skill 提供了强大的 BibTeX 文件查询功能：

### ✅ 已实现的功能

1. **单条目查询** - 查询完整的 bib 条目信息
2. **批量查询** - 一次查询多个 citation keys
3. **字段查询** - 只返回指定字段（如 abstract, title）
4. **列出所有 keys** - 查看 bib 文件中的所有条目
5. **列出所有字段** - 查看某条目包含哪些字段
6. **关键词搜索** - 在所有条目中搜索关键词

## 使用示例

### 基本查询

```bash
# 查询单个条目的完整信息
python bibtex-query/scripts/query_bib.py kai2026 test.bib

# 输出：
Entry: @article{kai2026}
  author: Kai Zhang and John Doe
  title: Machine Learning Applications in Medical Imaging
  journal: Journal of AI Research
  year: 2026
  ...
```

### 字段查询

```bash
# 只查询 abstract 字段
python bibtex-query/scripts/query_bib.py kai2026 test.bib --field abstract

# 查询多个字段
python bibtex-query/scripts/query_bib.py kai2026 test.bib --field title --field abstract
```

### 批量查询

```bash
# 一次查询多个条目
python bibtex-query/scripts/query_bib.py kai2026,zhang2025,johnson2024 test.bib

# 批量查询 + 字段过滤
python bibtex-query/scripts/query_bib.py kai2026,zhang2025 test.bib --field abstract
```

### 列表功能

```bash
# 列出所有 citation keys
python bibtex-query/scripts/query_bib.py --list-keys test.bib

# 输出：
Found 3 entries:
  • johnson2024 (@book)
  • kai2026 (@article)
  • zhang2025 (@inproceedings)

# 列出某条目的所有字段
python bibtex-query/scripts/query_bib.py kai2026 test.bib --list-fields

# 输出：
Fields in entry 'kai2026' (@article):
  • abstract
  • author
  • journal
  • keywords
  • pages
  • title
  • volume
  • year
```

### 搜索功能

```bash
# 搜索包含关键词的条目
python bibtex-query/scripts/query_bib.py --search "machine learning" test.bib

# 输出：
Found 1 entries matching 'machine learning':
  • kai2026 (@article) - matched in: title
```

## 错误处理

```bash
# 查询不存在的条目
python bibtex-query/scripts/query_bib.py nonexistent test.bib
# 输出：❌ Entry 'nonexistent' not found in BibTeX file.

# 查询不存在的字段
python bibtex-query/scripts/query_bib.py johnson2024 test.bib --field abstract
# 输出：
⚠️  Entry 'johnson2024' found, but missing fields: abstract
Entry: @book{johnson2024}
  abstract: [NOT FOUND]
```

## 实际应用场景

1. **文献综述** - 批量提取论文摘要
2. **引用管理** - 检查缺失的字段（如 DOI, URL）
3. **检索相关工作** - 通过关键词搜索相关论文
4. **清单管理** - 列出所有已收录的文献

## 技术特点

- UTF-8 编码支持（Windows 兼容）
- 正则表达式精确解析 BibTeX 格式
- 清晰的错误提示和警告信息
- 灵活的命令行参数组合
