# Build caddy with cloudflare plugin
ARG PYTHON_VERSION=3.13.2-alpine3.21
ARG CADDY_BUILDER_VERSION=2.9-builder-alpine
ARG CADDY_SERVER_VERSION=2.9.1-alpine
FROM caddy:${CADDY_BUILDER_VERSION} AS builder
RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare \
    --with github.com/caddyserver/forwardproxy=github.com/klzgrad/forwardproxy@naive
FROM caddy:${CADDY_SERVER_VERSION}

# Build the base image for naive proxy
FROM python:${PYTHON_VERSION}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV XDG_DATA_HOME=/naive_base/caddy/caddy_certs
EXPOSE 443/tcp
EXPOSE 443/udp
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
WORKDIR /naive_base
COPY . /naive_base/
RUN addgroup -S naive_group && adduser -S naive_user -G naive_group
RUN mkdir /naive_base/caddy/caddy_certs && \
    chmod +x /usr/bin/caddy && \
    apk update && apk add --no-cache libcap && \
    setcap cap_net_bind_service=+ep /usr/bin/caddy && \
    chown -R naive_user:naive_group /naive_base && \
    chmod -R ug+rwx /naive_base/caddy && \
    rm -rf /var/cache/apk/*
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt
USER naive_user
CMD ["python", "main.py"]