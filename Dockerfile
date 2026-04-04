FROM node:lts-alpine AS build
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:alpine-slim
EXPOSE 80
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/website/browser /usr/share/nginx/html/web

ENTRYPOINT ["nginx", "-g", "daemon off;"]
