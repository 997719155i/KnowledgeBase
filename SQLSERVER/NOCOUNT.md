# SET NOCOUNT

> 使返回的结果中不包含有关受 Transact-SQL 语句影响的行数的信息。

## 语法

``` sql 
SET NOCOUNT { ON | OFF }
```

## 注释

+ SET NOCOUNT 为 ON 时，不返回计数（表示受 Transact-SQL 语句影响的行数）
  - 更新 @@ROWCOUNT 函数
  - 将不给客户端发送存储过程中的每个语句的 DONE_IN_PROC 信息
+ SET NOCOUNT 为 OFF 时，返回计数。

## 注意

+ 使用 Microsoft SQL Server 提供的实用工具执行查询时，在 Transact-SQL 语句（如 SELECT、INSERT、UPDATE 和 DELETE）结束时将不会在查询结果中显示"nn rows affected"。
+ 如果存储过程中包含的一些语句并不返回许多实际的数据，则该设置由于大量减少了网络流量，因此可显著提高性能。
+ SET NOCOUNT 设置是在执行或运行时设置，而不是在分析时设置。

## 权限

SET NOCOUNT 权限默认授予所有用户。

## 结论

我们应该在存储过程的头部加上SET NOCOUNT ON 这样的话，在退出存储过程的时候加上 SET NOCOUNT OFF这样的话，以达到优化存储过程的目的。