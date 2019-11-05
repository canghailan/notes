```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
python -m pip install --upgrade pip
pip install pipenv
```

```shell
set PIPENV_VENV_IN_PROJECT=1 & pipenv install --skip-lock
```

```shell
PIPENV_PYPI_MIRROR=https://mirrors.aliyun.com/pypi/simple
PIPENV_VENV_IN_PROJECT=1
PIPENV_SKIP_VALIDATION=1
```