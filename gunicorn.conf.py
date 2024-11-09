# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html

bind = '0.0.0.0:8000'

workers = 1
worker_class = 'uvicorn.workers.UvicornWorker'

max_requests = 2000
max_requests_jitter = 400

log_file = '-'
capture_output = True
chdir = '/code'
worker_tmp_dir = '/dev/shm'  # noqa: S108
