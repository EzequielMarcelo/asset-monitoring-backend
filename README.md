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
