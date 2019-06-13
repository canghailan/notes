# Log4j钉钉Appender

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Http name="DingTalk" url="https://oapi.dingtalk.com/robot/send?access_token=ed2dd089eaea3309d6c5470882e2a0c5a662976fc2f7a56a4e4006b85bfbc8ad">
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