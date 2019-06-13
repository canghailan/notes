# Log4j钉钉Appender

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Http name="DingTalk" url="https://oapi.dingtalk.com/robot/send?access_token=">
            <ThresholdFilter level="FATAL" />
            <Property name="Content-Type" value="application/json;charset=utf-8" />
            <PatternLayout>
                <pattern>{"msgtype":"markdown","markdown":{"title":"%p","text":"%enc{%m}{JSON}"}}</pattern>
            </PatternLayout>
        </Http>
    </Appenders>
    <Loggers>
        <Root level="error">
            <AppenderRef ref="DingTalk"/>
        </Root>
    </Loggers>
</Configuration>
```

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Date;

public class Main {
    private static final Logger log = LogManager.getLogger();

    public static void main(String[] args) {
        log.fatal("# {}\n 时间： {}", "测试", new Date());
    }
}
```