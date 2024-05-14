FROM node:19-alpine

WORKDIR /client

COPY ./package*.json .

COPY  . .

RUN yarn install

EXPOSE 3000

CMD ["yarn", "run", "dev"]