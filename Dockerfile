from python:3.7
ENV TZ=Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./get-pip.py ./
ADD ./py_kafka.py ./
RUN python get-pip.py
RUN pip install kafka
CMD python py_kafka.py