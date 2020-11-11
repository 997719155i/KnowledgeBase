``` sql
TRUNCATE TABLE name
```



**注**：

	+ 对于由 FOREIGN KEY 约束引用的表，不能使用 TRUNCATE TABLE，而应使用不带 WHERE 子句的 DELETE 语句
	+ TRUNCATE TABLE 不能用于参与了索引视图的表
	+ 由于 TRUNCATE TABLE 不记录在日志中，所以它不能激活触发器
	+ 使用TRUNCATE语句进行删除的数据不能够回滚，而使用DELETE语句进行删除的数据可以进行回滚