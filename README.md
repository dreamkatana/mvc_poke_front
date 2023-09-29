
# PokéLista Python
![image](https://github.com/dreamkatana/mvc_poke_front/assets/7691411/a5194f18-170b-44cb-8766-781466249742)

## Visão Geral
Este projeto é uma aplicação Flask que busca dados da API Pokémon e exibe uma lista de 10 Pokémon aleatórios. Também fornece um campo de pesquisa e apresenta estatísticas das consultas.

### Requisitos
- Python 3.7+
- Flask 1.1.2+

### Instruções
1. Clone o repositório para sua máquina local:
   ```
   git clone https://github.com/dreamkatana/mvc_poke_front.git
   ```

### Configuração Docker
Se você estiver usando Docker, siga os comandos abaixo:

1. Construa a imagem Docker (lembre-se de especificar o nome da imagem do projeto do banco de dados, pois ambos os projetos se comunicam):
   ```
   docker-compose build
   ```
   (Referência do projeto de BD: [https://github.com/dreamkatana/mvc_poke_bd2](https://github.com/dreamkatana/mvc_poke_bd2))
2. Inicie os serviços:
   ```
   docker-compose up
   ```

## Contribuição
Contribuições são sempre bem-vindas! Consulte o arquivo `CONTRIBUTING.md` para obter mais detalhes.

## Suporte
Se você encontrar algum problema ou tiver alguma sugestão, por favor, abra uma issue no GitHub.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE.md` para obter mais detalhes.
