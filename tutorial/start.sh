#!/usr/bin/config bash
set -e

# 第一种启动方式，适用于测试开发阶段
python -m flask --app flaskr run --host=127.0.0.1 --port=8080 --debugger --reload

# 第二种启动方式，pip包形式启动
#waitress-serve --call 'flaskr:create_app'