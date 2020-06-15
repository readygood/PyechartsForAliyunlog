#!/bin/bash

/home/python3/.pyenv/shims/aliyunlog log get_log_all --project="prod-slb-xb" --logstore="java-zuul" --query="*|SELECT COUNT(*) as count" --from_time="yesterday 00:00:00" --to_time="yesterday 23:59:59" >> zuultotaldata
/home/python3/.pyenv/shims/aliyunlog log get_log_all --project="prod-slb-xb" --logstore="java-zuul" --query="status > 399|SELECT COUNT(*) as count" --from_time="yesterday 00:00:00" --to_time="yesterday 23:59:59" >> zuulerrordata
/home/python3/.pyenv/shims/aliyunlog log get_log_all --project="prod-slb-xb" --logstore="java-zuul" --query="status < 400|SELECT COUNT(*) as count" --from_time="yesterday 00:00:00" --to_time="yesterday 23:59:59" >> zuulnormaldata
