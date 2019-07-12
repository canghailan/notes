# 查询、结束连接
```sql
select * from pg_stat_activity;
SELECT pg_terminate_backend(1);
```


# 查询所有表
```sql
select * from pg_tables where schemaname = 'public';
```

# 查询所有表行数
```sql
SELECT
	array_to_string ( ARRAY ( SELECT unnest ( array_agg ( q ) ) ), E'\n' || 'union all' || E'\n' ) 
FROM
	( SELECT 'select ''' || tablename || ''' as tab, count(*) cnt from ' || tablename AS q FROM pg_tables WHERE schemaname = 'public' AND tableowner = 'base' ) AS t;
```


# 创建只读账号
```sql
CREATE ROLE xxx WITH LOGIN ENCRYPTED PASSWORD 'password';
-- GRANT CONNECT ON DATABASE db TO xxx;
-- GRANT USAGE ON SCHEMA public TO xxx;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO xxx;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
   GRANT SELECT ON TABLES TO xxx;

GRANT xxx TO yyy;
```