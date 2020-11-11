# sys.sysobjects (Transact-SQL)

>  在数据库中创建的每个对象（例如表，约束、默认值、日志、规则以及存储过程）都对应一行

查询所有的表名

``` sql
select Name as 表名 from sysobjects where xtype='U'
select Name as 表名 from sysobjects where xtype='u' and status>=0
```



查询所有的存储过程名称

``` sql
select Name as 存储过程名称 from sysobjects where xtype='P'
```



| 列名称           | 数据类型     | 说明                                                         |
| :--------------- | :----------- | :----------------------------------------------------------- |
| name             | **sysname**  | 对象名称                                                     |
| id               | **int**      | 对象标识号                                                   |
| xtype            | **char(2)**  | 对象类型。 可以是以下对象类型之一：<br>**U = 用户表**<br>**P = 存储过程**<br>AF = 聚合函数 (CLR) C = CHECK 约束   D = 默认值或 DEFAULT 约束   F = FOREIGN KEY 约束   L = 日志   FN = 标量函数   FS = 程序集  (CLR) 标量函数  FT = 程序集 (CLR) 表值函数  IF = 内联表函数  IT = 内部表    PC = Assembly (CLR) 存储过程  PK = PRIMARY KEY 约束（类型为 K）  RF = 复制筛选存储过程  S = 系统表  SN = 同义词  SQ = 服务队列  TA = 程序集 (CLR) DML 触发器  TF = 表函数  TR = SQL DML 触发器  TT = 表类型   UQ = UNIQUE 约束（类型为 K）  V = 视图  X = 扩展存储过程 |
| uid              | **smallint** | 对象所有者的架构 ID。 对于从旧版 SQL Server 升级的数据库，架构 ID 等于所有者的用户 ID。 如果用户数和角色数超过 32,767，则发生溢出或返回 NULL。  ** * * 重要 * 提示 * **如果使用以下任意 SQL Server DDL 语句，则必须使用[sys.databases](https://docs.microsoft.com/zh-cn/sql/relational-databases/system-catalog-views/sys-objects-transact-sql?view=sql-server-ver15)目录视图，而不是 sys.sys对象。  创建 \| ALTER \| DROP USER  创建 \| ALTER \| DROP ROLE  创建 \| ALTER \| DROP 应用程序角色  CREATE SCHEMA  ALTER AUTHORIZATION ON OBJECT |
| info             | **smallint** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| **status**       | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| base_schema_ver  | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| replinfo         | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| parent_obj       | **int**      | 父对象的对象标识号。 例如，表 ID（如果父对象是触发器或约束）。 |
| crdate           | **datetime** | 对象的创建日期。                                             |
| ftcatid          | **smallint** | 注册为使用全文检索的所有用户表的全文目录标识符，对于没有注册的所有用户表则为 0。 |
| schema_ver       | **int**      | 在每次更改表的架构时都会增加的版本号。 始终返回 0。          |
| stats_schema_ver | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| type             | **char(2)**  | 对象类型。 可以是以下其中一个值：  AF = 聚合函数 (CLR)  C = CHECK 约束  D = 默认值或 DEFAULT 约束  F = FOREIGN KEY 约束  FN = 标量函数  FS = 程序集 (CLR) 标量函数  FT = 程序集 (CLR) 表值函数 IF = 内联表函数  IT - 内部表  K = PRIMARY KEY 或 UNIQUE 约束  L = 日志  P = 存储过程  PC = Assembly (CLR) 存储过程  R = 规则  RF = 复制筛选存储过程  S = 系统表  SN = 同义词  SQ = 服务队列  TA = 程序集 (CLR) DML 触发器  TF = 表函数  TR = SQL DML 触发器  TT = 表类型  U = 用户表  V = 视图  X = 扩展存储过程 |
| userstat         | **smallint** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| sysstat          | **smallint** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| indexdel         | **smallint** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| refdate          | **datetime** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| 版本             | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| deltrig          | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| instrig          | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| updtrig          | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| seltrig          | **int**      | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |
| category         | **int**      | 用于发布、约束和标识。                                       |
| cache            | **smallint** | 标识为仅供参考。 不支持。 不保证以后的兼容性。               |