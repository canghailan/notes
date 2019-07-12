# 新增虚拟列、索引
```sql
ALTER TABLE `message`.`message` 
ADD COLUMN `v_content_id` VARCHAR(64) GENERATED ALWAYS AS (`content` ->> '$.id') NULL AFTER `uri`;
CREATE INDEX `idx_content_id` ON `message`(`v_content_id`);
```