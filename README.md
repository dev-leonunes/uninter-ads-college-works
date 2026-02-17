# uninter-ads-college-works

Este repositório reúne **atividades, exercícios e projetos acadêmicos** desenvolvidos ao longo do curso de **Análise e Desenvolvimento de Sistemas (ADS)** na **UNINTER**.

A ideia aqui é manter em um só lugar materiais de disciplinas diferentes (banco de dados, programação, estrutura de dados, big data etc.), com código e scripts que servem tanto para entrega quanto para consulta/estudo.

## Tecnologias e ferramentas

- **Python** (scripts e estruturas de dados)
- **Java / Spring Boot** (projetos completos em repositórios separados)
- **SQL** (modelagem, carga de dados e consultas)
- **Neo4j + Cypher/APOC** (modelagem e consultas NoSQL)
- **PySpark** (processamento distribuído/Big Data)
- **HTML/CSS/JavaScript** (projetos web em repositórios separados)

## Projetos neste repositório

- **banco-de-dados-relacional/**
  - Atividade de **Banco de Dados Relacional**.
  - Contém scripts SQL para criação/população e consultas (ex.: `data.sql`, `dump.sql`, `queries.sql`) e o diagrama em `assets/`.

- **banco-de-dados-nosql/**
  - Atividade de **Banco de Dados NoSQL** usando **Neo4j**.
  - Script `consulta.cypher` com ingestão via **APOC** a partir de JSON e consultas (ex.: hashtag mais popular, usuário com mais retweets).

- **estrutura-de-dados/**
  - Atividades de **Estrutura de Dados** em Python.
  - Implementações com foco em lógica e estruturas clássicas:
    - `hospital_queue.py`: fila de triagem/atendimento com regras de prioridade.
    - `hash_table_placas.py`: tabela hash com encadeamento (lista ligada) para colisões.

- **big-data/**
  - Projeto de **Big Data** com **PySpark**.
  - `main.py` baixa um dataset (ZIP/CSV) e executa análises com RDD (`map`, `reduceByKey`) sobre reviews do IMDb.

## Repositórios relacionados

Alguns trabalhos maiores (principalmente aplicações completas) estão em repositórios próprios. Links e contexto:

- [dev-leonunes-portfolio](https://github.com/dev-leonunes/dev-leonunes-portfolio)
  - Portfólio pessoal da disciplina de **Programação Web**.
  - Projeto estático com **HTML/CSS**, com foco em layout, responsividade e organização de páginas.

- [python-get-started (pasta ADS-college)](https://github.com/dev-leonunes/python-get-started/tree/main/ADS-college)
  - Repositório de estudos iniciais em Python.
  - A pasta **ADS-college** reúne exercícios de **Lógica de Programação e Algoritmos** e um projeto final, com evolução gradual dos conceitos.

- [cofrinho-java-uninter](https://github.com/dev-leonunes/cofrinho-java-uninter)
  - Projeto final de **Programação Orientada a Objetos**.
  - Implementa um “cofrinho” de moedas em **Java**, praticando POO (classes, herança/polimorfismo, encapsulamento) e regras de negócio.

- [the-legend-of-zelda-v2](https://github.com/dev-leonunes/the-legend-of-zelda-v2)
  - Projeto de **Linguagem de Programação Aplicada**.
  - Jogo em **Python** inspirado em _The Legend of Zelda_, explorando POO, estados do jogo, sprites e áudio (ex.: **Pygame**).

- [gestao-estoque-app](https://github.com/dev-leonunes/gestao-estoque-app)
  - Projeto de **Atividades Extensionistas**.
  - Sistema web full-stack para **gestão de produtos e movimentações de estoque**:
    - **Frontend:** React + Vite (TypeScript)
    - **Backend:** NestJS + TypeORM + PostgreSQL (TypeScript)

- [gestao-tarefas-app](https://github.com/dev-leonunes/gestao-tarefas-app)
  - Trabalho final de **Desenvolvimento Web Back-end**.
  - API **REST** para gerenciamento de tarefas (CRUD), com **Java + Spring Boot** e persistência em **PostgreSQL** (Spring Data JPA/Hibernate).
