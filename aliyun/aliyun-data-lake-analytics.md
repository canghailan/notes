```sql
msck repair database xxx
```

OSS分区表
```sql
CREATE EXTERNAL TABLE `yt_log`.`web` (
	`app_key` string COMMENT 'from deserializer',
	`device_id` string COMMENT 'from deserializer',
	`event` string COMMENT 'from deserializer',
	`metrics` string COMMENT 'from deserializer',
	`user_details` string COMMENT 'from deserializer',
	`__source__` string COMMENT 'from deserializer',
	`__time__` int COMMENT 'from deserializer',
	`__topic__` string COMMENT 'from deserializer',
	`__useragent__` string COMMENT 'from deserializer'
)
PARTITIONED BY (
	`year` string,
	`month` string,
	`day` string
)
STORED AS `JSON`
LOCATION 'oss://yt-log/logstore/yitong/web'
TBLPROPERTIES (
	'io.compression.snappy.native' = 'true',
	'recursive.directories' = 'true',
	'skip.header.line.count' = '0',
	'text.compression' = 'snappy'
)

-- ALTER TABLE `yt_log`.`web` ADD
-- PARTITION (year='2020', month='01', day='08') 
-- LOCATION 'oss://yt-log/logstore/yitong/web/2020/01/08/';

-- SHOW PARTITIONS `yt_log`.`web`;
```

SQL优化
1. 使用WITH子句提前进行简单查询
2. IN优于JOIN、EXISTS
3. 查询条件注意数据类型一致
4. 查询结果较复杂时，拆分为多条简单SQL