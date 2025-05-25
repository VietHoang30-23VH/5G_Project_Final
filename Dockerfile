FROM debian:bookworm-slim AS builder

RUN apt-get update && \
    apt-get install -y build-essential flex bison libpcap-dev libssl-dev libtirpc-dev wget zlib1g-dev

WORKDIR /opt

RUN wget https://github.com/openargus/clients/archive/refs/tags/v5.0.0.tar.gz && \
    tar -xvzf v5.0.0.tar.gz && \
    cd clients-5.0.0/ && \
    ./configure && make -j$(nproc) && make install

FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y libpcap0.8 libssl3 libtirpc3 zlib1g python3 python3-pip && \
    pip3 install --no-cache-dir numpy pandas plotly dash sqlalchemy dash-core-components \
    dash-html-components dash-bootstrap-components dash_iconify joblib xmlrpc xlrd
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/ra /usr/local/bin/ra



CMD ["/usr/local/sbin/argus", "-i", "any", "-P", "561"]