# Documentação: criar-variavel-grupo-azure-cli.py

Este script permite a gestão de grupos de variáveis dentro do Azure DevOps através da Azure DevOps CLI.

## Bibliotecas Utilizadas:
- `sys`: Utilizada para obter argumentos do comando que invoca o script.
- `azure.devops.connection`: Fornece métodos para estabelecer conexões com o Azure DevOps.
- `msrest.authentication`: Fornece métodos para autenticação.

## Funções:

### 1. get_variables_from_file(file_name)
- **Argumentos**: file_name (Nome do arquivo que contém as variáveis).
- **Retorno**: Dicionário com pares chave-valor das variáveis.
- **Descrição**: Lê um arquivo que contém variáveis no formato `key=value` e retorna um dicionário.

### 2. get_variable_group(client, project, group_name)
- **Argumentos**:
  - client (Cliente do Azure DevOps)
  - project (Nome do projeto no Azure DevOps)
  - group_name (Nome do grupo de variáveis)
- **Retorno**: ID do grupo de variáveis ou None.
- **Descrição**: Retorna o ID do grupo de variáveis se ele existir.

### 3. get_variables_from_group(client, project, group_id)
- **Argumentos**:
  - client (Cliente do Azure DevOps)
  - project (Nome do projeto no Azure DevOps)
  - group_id (ID do grupo de variáveis)
- **Retorno**: Dicionário com as variáveis do grupo.
- **Descrição**: Recupera as variáveis associadas ao grupo de variáveis.

### 4. create_variable_group(client, project, group_name, variables)
- **Argumentos**:
  - client (Cliente do Azure DevOps)
  - project (Nome do projeto no Azure DevOps)
  - group_name (Nome do grupo de variáveis)
  - variables (Dicionário com variáveis a serem adicionadas)
- **Retorno**: ID do grupo de variáveis criado ou None.
- **Descrição**: Cria um novo grupo de variáveis no Azure DevOps.

## Fluxo Principal (main):
- Obtenção dos argumentos do comando (TOKEN, ORG_URL, PROJECT, GROUP_NAME).
- Estabelece uma conexão com o Azure DevOps.
- Verifica se o grupo de variáveis já existe.
- Se o grupo existir:
  - Recupera as variáveis do grupo existente.
  - Verifica se há novas variáveis a serem adicionadas.
  - Atualiza o grupo com as novas variáveis, se houver.
- Se o grupo não existir:
  - Cria um novo grupo de variáveis.

## Utilização:

Para utilizar o script, é necessário invocá-lo através do comando abaixo, substituindo os placeholders pelos valores apropriados:

```
python criar-variavel-grupo-azure-cli.py [TOKEN] [ORG_URL] [PROJECT] [GROUP_NAME]
```

**Nota**: O arquivo `variables.txt` deve estar no mesmo diretório do script e conter as variáveis no formato `key=value`.

## Considerações:

- A autenticação é feita utilizando um token básico do tip PAT.
- O script assume que as variáveis estão armazenadas no arquivo `variables.txt` no formato `key=value`.
- A descrição padrão para os grupos de variáveis criados pelo script é "Variavel de grupo criada por script".

OBS.:
É importante garantir que as bibliotecas necessárias estejam instaladas e que você tenha as devidas permissões no Azure DevOps para criar e modificar grupos de variáveis.

# Documentação: exportar-variavel-grupo-azure-cli.py

Este script facilita a exportação de grupos de variáveis do Azure DevOps para um arquivo de texto.

## Bibliotecas Utilizadas:
- Estamos usando as mesmas biblioteca do script anterio descrito.

## Funções:

### 1. escape_unwanted_sequences(value)
- **Argumentos**: value (string que pode conter sequências indesejadas).
- **Retorno**: String com sequências indesejadas substituídas por suas versões "escapadas".
- **Descrição**: Substitui `\n` por `\\n` e `\t` por `\\t` em uma string.

### 2. save_variables_to_file(file_name, variables)
- **Argumentos**: 
  - file_name (Nome do arquivo onde as variáveis serão salvas)
  - variables (Dicionário com variáveis a serem salvas).
- **Retorno**: Nenhum.
- **Descrição**: Salva as variáveis em um arquivo de texto no formato `key=value`.

### 3. get_variable_group(client, project, group_name)
- **Argumentos**:
  - client (Cliente do Azure DevOps)
  - project (Nome do projeto no Azure DevOps)
  - group_name (Nome do grupo de variáveis)
- **Retorno**: ID do grupo de variáveis ou None.
- **Descrição**: Retorna o ID do grupo de variáveis se ele existir.

### 4. get_variables_from_group(client, project, group_id)
- **Argumentos**:
  - client (Cliente do Azure DevOps)
  - project (Nome do projeto no Azure DevOps)
  - group_id (ID do grupo de variáveis)
- **Retorno**: Dicionário com as variáveis do grupo.
- **Descrição**: Recupera as variáveis associadas ao grupo de variáveis.

## Fluxo Principal (main):
- Obtenção dos argumentos do comando (TOKEN, ORG_URL, PROJECT, GROUP_NAME).
- Estabelece uma conexão com o Azure DevOps.
- Verifica se o grupo de variáveis existe.
- Se o grupo existir:
  - Recupera as variáveis do grupo existente.
  - Salva as variáveis em um arquivo chamado `GROUP_NAME_variables.txt`.
- Se o grupo não existir:
  - Exibe uma mensagem informando que o grupo não foi encontrado.

## Utilização:

Para utilizar o script, você deve chamar o mesmo com o seguinte comando, substituindo os placeholders pelos valores corretos:

```
python exportar-variavel-grupo-azure-cli.py [TOKEN] [ORG_URL] [PROJECT] [GROUP_NAME]
```

**Nota**: Após a execução, se o grupo de variáveis for encontrado, as variáveis serão salvas em um arquivo denominado `GROUP_NAME_variables.txt` no mesmo diretório do script.

## Considerações:

- A autenticação é feita usando um token básico.
- O script considera e manipula a possibilidade de haver caracteres como `\n` ou `\t` nas variáveis, escapando-os adequadamente.
- Os erros são tratados e as mensagens correspondentes são exibidas no console.

Certifique-se de ter as bibliotecas necessárias instaladas e as devidas permissões no Azure DevOps para acessar grupos de variáveis.