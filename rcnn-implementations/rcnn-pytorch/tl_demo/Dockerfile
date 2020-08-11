FROM python:3.8-alpine

WORKDIR /app
ENV FLASK_APP tl_demo
# locally only
# ENV PORT 5000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache add musl-dev linux-headers g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install numpy

COPY . /app/tl_demo
RUN cd tl_demo && pip3 install -e . && cd ..

# locally only
# EXPOSE 5000

# if development:
# CMD flask run --host=0.0.0.0 -p $PORT
CMD gunicorn -w 4 -b 0.0.0.0:${PORT} --timeout 90 ${FLASK_APP}.wsgi:app   