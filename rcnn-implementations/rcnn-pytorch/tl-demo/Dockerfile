FROM python:3.8-alpine

WORKDIR /app
ENV FLASK_APP tl-demo
# locally only
ENV PORT 5000 

RUN pip3 install --upgrade pip
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache add musl-dev linux-headers g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install numpy

COPY . /app/tl-demo
RUN cd tl-demo && pip3 install -e . && cd ..

# locally only
# EXPOSE 5000

RUN echo ${PORT}
RUN echo $PORT
CMD flask run --host=0.0.0.0 -p $PORT