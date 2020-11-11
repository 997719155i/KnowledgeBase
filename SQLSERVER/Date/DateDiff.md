# 语法

``` sql
DATEDIFF(datepart,startdate,enddate)
```

*startdate* 和 *enddate* 参数是合法的日期表达式。

# 实例

``` sql
SELECT DATEDIFF(day,'2008-12-29','2008-12-30') AS DiffDate
```

| DiffDate |
| :------- |
| 1        |

```sql
SELECT DATEDIFF(day,'2008-12-28','2008-12-30') AS DiffDate
```

| DiffDate |
| :------- |
| 2        |

```sql
SELECT DATEDIFF(day,'2008-12-30','2008-12-29') AS DiffDate
```

| DiffDate |
| :------- |
| -1       |