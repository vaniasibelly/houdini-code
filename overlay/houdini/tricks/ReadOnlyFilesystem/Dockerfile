# Use a imagem oficial do Ubuntu
FROM ubuntu:22.04

# Evita perguntas interativas durante a instalação (trava o build)
ENV DEBIAN_FRONTEND=noninteractive

# Tenta limpar o cache e usar mirrors mais estáveis, se necessário
RUN apt-get clean && \
    apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Configura o diretório de trabalho
WORKDIR /

# Cria o ambiente virtual e instala pacotes
RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip

# Copia o script
COPY read_only_filesystem.py /read_only_filesystem.py

# Comando padrão
CMD ["venv/bin/python", "/read_only_filesystem.py"]
