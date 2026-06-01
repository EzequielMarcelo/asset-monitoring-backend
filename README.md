# Asset Telemetry Monitoring Backend

Sistema de monitoramento de ativos por telemetria, com alertas baseados em regras.

A solução proposta contempla uma arquitetura completa para ingestão de dados de telemetria, avaliação de regras e geração de alertas.

## Objetivos

O sistema foi projetado para permitir:

- Cadastro de ativos.
- Cadastro das variáveis associadas a cada ativo.
- Cadastro de regras de alerta associadas às variáveis monitoradas.

Além da implementação, o projeto apresenta uma proposta arquitetural para os componentes responsáveis por:

- Ingestão e armazenamento das leituras de telemetria emitidas pelos ativos.
- Avaliação das regras.
- Geração de alertas.
- Consulta ao histórico de leituras e
  alertas.
- Integrações e componentes necessários para uma solução escalável.

O foco principal é demonstrar boas práticas de modelagem, organização de código, persistência de dados e definição de uma arquitetura escalável para monitoramento de ativos em tempo real.

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Docker
- Docker Compose

## Como executar o projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado:

- Docker
- Docker Compose
- Git

### Clonando o repositório

```bash
https://github.com/EzequielMarcelo/asset-monitoring-backend
```

```bash
cd asset-monitoring-backend
```

### Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/asset_monitoring
```

### Subindo a aplicação com Docker

O projeto já está configurado para rodar via Docker Compose.

```bash
docker compose up --build
```

A aplicação estará disponível em:

```text
http://localhost:8000
```

---

## Documentação da API

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## Modelo de Dados

### Asset

Representa um ativo monitorado.

### Variable

Representa uma variável associada a um ativo.

Exemplos:

- Temperatura
- Pressão
- Umidade

### Rule

Define condições para geração de alertas.

Exemplos:

- Temperatura > 80°C
- Pressão < 10 PSI

---

## Arquitetura Final

A arquitetura proposta para um ambiente produtivo contempla:

1. Recebimento de telemetria através de API ou broker de mensagens.
2. Armazenamento das leituras em banco de dados.
3. Processamento assíncrono para avaliação das regras.
4. Geração de alertas quando condições forem atendidas.
5. Disponibilização de consultas históricas.

Fluxo simplificado:

```text
Ativo
  ↓
Ingestão de Telemetria
  ↓
Banco de Dados
  ↓
Motor de Regras
  ↓
Alertas
```

---
