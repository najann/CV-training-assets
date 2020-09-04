FROM node:14-alpine3.10

WORKDIR /usr/src/app
ENV NODE_ENV production
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]