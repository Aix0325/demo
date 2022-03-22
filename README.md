# BATCH MODIFY ARTICLE STATUS

根据links.txt 和条件筛选 批量修改文章 post_status 的值

## 条件

- post_status = "publish"
- post_type = "post"

## 编译

```shell
pyinstaller -F main.py -i favicon.ico -n "Article Batch Modify"
```

## 我是Aix
  