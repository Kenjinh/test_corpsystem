FROM node:18-slim

WORKDIR /app

COPY . .

RUN npm install -g pnpm
RUN pnpm install

EXPOSE 4173

CMD ["pnpm", "run", "preview"]