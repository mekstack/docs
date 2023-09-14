FROM python:latest AS build
RUN pip install tox
WORKDIR /app
COPY ./ ./
RUN tox

FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
