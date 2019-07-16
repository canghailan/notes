import os
import time

dbs = [
    {
        "source": {
            "user": "",
            "password": "",
            "host": "",
            "port": 5432,
            "database": ""
        },
        "target": {
            "user": "",
            "password": "",
            "host": "",
            "port": 5432,
            "database": ""
        }
    }
]

pg_dump = '''
pg_dump \
--dbname='postgresql://{user}:{password}@{host}:{port}/{database}' \
--exclude-table=pg_ts_custom_word \
--verbose \
--no-owner \
--no-privileges \
--format=c \
--file='{backup}'
'''

pg_restore = '''
pg_restore \
--dbname='postgresql://{user}:{password}@{host}:{port}/{database}' \
--verbose \
--no-owner \
'{backup}'
'''

if not os.path.exists("db"):
    os.makedirs("db")

for db in dbs:
    backup = "db/pg-{database}.dump".format(**db["source"])
    if os.path.exists(backup):
        os.remove(backup)

    dump = pg_dump.format(**dict({"backup": backup}, **db["source"]))
    print(dump)

    t0 = time.time()
    os.system(dump)
    t1 = time.time()

    restore = pg_restore.format(**dict({"backup": backup}, **db["target"]))
    print(restore)

    t2 = time.time()
    os.system(restore)
    t3 = time.time()

    print(f"dump    {t1 - t0}s")
    print(f"restore {t3 - t2}s")
    print(f"total   {t3 - t0}s")


'''
CREATE EXTENSION "plpgsql";
CREATE EXTENSION "zhparser";
CREATE TEXT SEARCH CONFIGURATION chinese (PARSER = zhparser);
ALTER TEXT SEARCH CONFIGURATION chinese ADD MAPPING FOR n,v,a,i,e,l WITH simple;
CREATE EXTENSION "uuid-ossp";
'''