# Visualização Dinâmica de Boltzmann Machine

Este projeto implementa uma visualização dinâmica de uma **Boltzmann Machine (BM)** utilizando Python e FastAPI. A visualização é gerada como um **GIF** dinâmico, mostrando a interação entre unidades visíveis e ocultas ao longo do tempo.

![boltzmann](https://github.com/user-attachments/assets/cc66a93c-0aa2-4509-97b3-c75fc8dfbd86)

## Descrição

As **Boltzmann Machines** são redes neurais estocásticas que podem ser usadas para modelar sistemas de probabilidade. Elas são compostas por unidades visíveis e ocultas, com conexões entre elas, e podem ser usadas para aprender representações e realizar inferências.

Para mais informações sobre as Boltzmann Machines, consulte a [Wikipedia](https://en.wikipedia.org/wiki/Boltzmann_machine).

## Funcionalidades

* **Geração de Visualização**: O projeto cria uma representação gráfica da Boltzmann Machine com unidades visíveis e ocultas.
* **GIF Dinâmico**: A visualização é salva como um GIF animado, mostrando as interações entre as unidades ao longo de várias iterações.
* **API FastAPI**: O projeto expõe uma API usando o FastAPI para gerar e fornecer a visualização em tempo real.

## Requisitos

* Python 3.8 ou superior
* FastAPI
* Uvicorn
* NetworkX
* Matplotlib
* Pillow

Você pode instalar as dependências com o seguinte comando:

```bash
pip install fastapi uvicorn networkx matplotlib pillow
```

## Como Usar

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd seu-repositorio
```

3. Execute o servidor FastAPI:

```bash
uvicorn app:app --reload
```

4. Acesse a API no navegador:

```bash
http://127.0.0.1:8000/boltzmann
```

Isso irá gerar e exibir a visualização da Boltzmann Machine em formato GIF.

## Estrutura do Projeto

```
seu-repositorio/
│
├── app.py            # Código principal do FastAPI e lógica da Boltzmann Machine
├── requirements.txt  # Dependências do projeto
└── README.md        # Este arquivo de documentação
```

## Contribuição

Contribuições são bem-vindas! Se você tiver melhorias ou correções para o projeto, por favor, abra uma **issue** ou um **pull request**.

## Licença

Este projeto está licenciado sob a MIT License.

## Como adicionar no GitHub

1. Crie um repositório no GitHub
2. Adicione o arquivo `README.md` no repositório
3. Comite e envie as alterações para o repositório remoto
