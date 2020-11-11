# 临时表

## 创建临时表

1. ``` sql
   create table #临时表名(字段1 约束条件,
   						字段2 约束条件,
   						.....)
   create table ##临时表名(字段1 约束条件,
   						字段2 约束条件,
   						.....)
   ```

2. ``` sql
   select * into #临时表名 from 你的表;
   select * into ##临时表名 from 你的表;
   ```

**注**：以上的"#"代表局部临时表，"##"代表全局临时表

## 查询临时表

``` sql 
select * from #临时表名;
select * from ##临时表名;
```

## 删除临时表

``` sql
drop table #临时表名;
drop table ##临时表名;
```

