FROM python:3.11-slim

# ENV PYPI_MIRROR=https://pypi.doubanio.com/simple
ENV PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple
ENV TZ=Asia/Shanghai

WORKDIR /opt/server
COPY . /opt/server/

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
    && apt-get update && apt-get install -y gcc libpq-dev

RUN pip install -i $PYPI_MIRROR --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

CMD ["python", "manage.py", "runserver"]
