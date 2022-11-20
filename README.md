# IAL-Website
Website, desenvolvido em Django, para auxílio no ensino da disciplina: Introdução à Álgebra Linear na UNB (Universidade de Brasília).

Orientado pela professora Luiza Yoko.

Campus FGA-Gama.

## 🖥 Sobre o projeto:

O objetivo desse projeto é construir um website com conteúdos para o ensino de
Introdução à Algebra Linear.

Para realizar essa tarefa foi planejado que o site teria que ser de fácil 
manutenção pois poderá ser contínuado futuramente por outros discentes da UNB, 
que não necessariamente terão plena aptidão com tecnologias complexas de 
desenvolvimento de software. (Se você é um aluno que está contribuindo para 
este projeto, considere ler toda a documentação do mesmo, pois será mais 
fácil de desenvolver)

Então, visto essas condições, optamos por fazer um site utilizando 
[Django](https://www.djangoproject.com/), pois permite a construção de uma API
e de um front-end de forma fácil, unificada e com bons exemplos de documentação
na internet.

Outra ferramenta que foi utilizada para facilitar a instalação das tecnologias
utilizadas, foi o [Docker](https://www.docker.com/) que está aqui com o 
propósito de garantir que com um simples comando, o sistema do site fique 
disponível sem necessitar de configurações adicionais.

Então, resumidamente, para contribuir com esse projeto, os requisitos são 
mínimos. Você precisará entender HTML, CSS, Python e talvez um pouco de 
javascript, visto que estamos evitando ao máximo de utilizar javascript para 
manter a manutebilidade do site da forma mais fácil possível. 
Observe que o site é desenvolvido utilizando Django, então um conhecimento 
básico do framework também é necessário.


---

## 🪛 Instalação

### Dependências

É necessário que se tenha instalado o Docker. 
Não se preocupe com a instalação de outras dependências, 
o Docker irá lidar com as outras dependências do projeto.

Segue a documentação de instalação dessas dependências:

- [Instalação do Docker](https://docs.docker.com/get-docker/)

Assim que o docker for instalado (lembre-se de seguir <b>TODOS OS PASSOS</b> do tutorial de instalação no seu sistema, pois caso contrário você poderá encontrar problemas ao executar os comandos),
 basta executar o comando `docker compose up` na pasta raíz deste projeto. 
A primeira execução desse comando irá demorar alguns minutos pois irá baixar e instalar as dependências

---

## ▶️ Execução

Você terá que configurar as variáveis de ambiente:
 - Crie um arquivo `.env`
   - Preencha as seguintes variáveis
     - ```shell
       ELEPHANT_DB_USER=...
       ELEPHANT_DB_PASSWORD=...
       ELEPHANT_DB_HOST=...
       ELEPHANT_DB_PORT=...
       ELEPHANT_DB_NAME=...
       ```


Após configurar as variáveis de ambiente, basta executar o seguinte comando:

```
docker compose up
```

Após o servidor ser configurado e carregado, a página estará disponível para acesso no endereço `localhost:8000`.

Esse comando é suficiente para executar o projeto.

