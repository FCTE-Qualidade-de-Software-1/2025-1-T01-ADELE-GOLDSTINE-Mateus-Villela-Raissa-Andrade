# Fase 4 - Executar a avaliação 

## 1. Introdução

Essa fase, tem como objetivo mostrar os resultados da avaliação em relação a compreensibilidade do Agromart, com o foco nos repositórios agromart-web e docs. A avaliação foi conduzida com base nos critérios de qualidade de Manutenibilidade (ISO/IEC 25010) e utilizando a abordagem GQM (Goal – Question – Metric) definida na Fase 2 do projeto. O objetivo principal desta avaliação é medir a clareza e facilidade de entendimento do código-fonte e da documentação técnica, a fim de identificar oportunidades de melhoria. Abaixo , estão os resultados da avaliação. <br>


## 2. Resultados da avaliação 

###  Repositório `agromart-web`

| Métrica | Descrição | Avaliação | Pontuação |
|--------|-----------|-----------|-----------|
| M1 | **Organização modular do código**: Estrutura de pastas bem definida com separação de responsabilidades (`assets`, `components`, `hooks`, `pages`, `routes`, `services`, `styles`, `utils`). | Facilita a localização de arquivos e compreensão do projeto. | 👍 Alto |
| M2 | **Clareza na nomeação de arquivos e componentes**: Componentes como `Button`, `Input`, `SideBar`, `ToastContainer` e `Tooltip` são descritivos. | Os nomes estão de acordo com suas funcionalidades, facilitando o entendimento. | 👍 Alto |
| M5 e M6 | **Proporção de funções com comentários úteis** e **Aderência a padrões de boas práticas**: Repositório arquivado desde 30/08/2022. README genérico sem informações sobre a arquitetura do projeto. Falta de comentários úteis e ausência de lint configurado. | Difícil a compreensão por novos desenvolvedores e não tem evidências de boas práticas. | 🚨 Baixo |

### Avaliação do Repositório `docs`

| Métrica | Descrição | Avaliação | Pontuação |
|--------|-----------|-----------|-----------|
| M3 | **Existência de README, guia e arquitetura**: O repositório possui um `README.md` com a descrição do propósito ("Repositório de documentação dos sistemas e do projeto Agromart"). Inclui seção de arquitetura explicando os três componentes principais (aplicativo móvel, API Dicionário e API principal de cada CSA) e suas interações. Há também instruções sobre uso do GitHub Pages, instalação, desenvolvimento local, build e deploy. | Há uma visão clara da estrutura do sistema e de como utilizá-lo. | 👍 Alto |
| M4 | **Clareza da documentação (escala 1–5)**: Documentação bem estruturada, com títulos e subtítulos organizados, linguagem clara e concisa. A seção de arquitetura é didática e acessível, mesmo para quem não conhece o projeto. Há também tutoriais de instalação e desenvolvimento. | Contribui para a compreensibilidade e usabilidade. | 👍 Alto |

## 3. Oportunidade de melhorias 

Com base na avaliação de compreensibilidade, as seguintes oportunidades de melhoria foram identificadas:

1. **Melhorar a documentação do código no `agromart-web`**  
   O repositório `agromart-web` precisa de um `README.md` detalhado, contendo informações de como rodar o projeto e de comentários úteis no código. A ausência desses elementos dificulta a compreensão do sistema para novos desenvolvedores e compromete a manutenção do código a longo prazo.  
   - A criação de um `README.md` abrangente, com informações sobre a arquitetura, dependências e scripts de execução.  
   - Além disso, a adição de comentários explicativos em funções e componentes complexos melhoraria a compreensibilidade do código.

2. **Implementar ferramentas de análise estática de código (lint) no `agromart-web`**  
   A ausência de ferramentas de lint configuradas no repositório impede a verificação automática de padrões de boas práticas de codificação.  
   - Sugere-se a implementação de um linter (como **ESLint** para JavaScript/TypeScript), com regras bem definidas para manter a consistência do código, identificar possíveis erros e melhorar a compreensibilidade geral.

3. **Atualizar o repositório `agromart-web`**  
   O fato de o repositório estar arquivado e em modo somente leitura indica que ele não está sendo ativamente mantido.  
   - Ainda que a avaliação tenha sido realizada com base na versão existente, a compreensibilidade de um sistema em produção depende de sua atualização contínua.  
   - A reativação e atualização do repositório, com a integração das melhorias propostas, seria um passo relevante para garantir a compreensibilidade e manutenibilidade a longo prazo.

## 4. Ação de melhoria implementada 

Com base nas oportunidades identificadas, a seguinte ação será implementada:

####  Criação de um `README.md` detalhado para o repositório `agromart-web`

Esta ação foi priorizada por seu impacto direto na **compreensibilidade do sistema**, para novos desenvolvedores. A decisão está de acordo com as seguintes métricas:

- **M3: Existência de README, guia e arquitetura**
- **M5: Proporção de funções com comentários úteis**

Ambas apresentaram **pontuação baixa** na avaliação do repositório `agromart-web`.

Um `README.md` bem estruturado cumpre papel fundamental ao:

- Fornecer **contexto inicial** sobre o sistema e seus objetivos;
- Explicar a **estrutura do projeto**, suas dependências e como executá-lo;
- Auxiliar na **onboarding** de novos colaboradores;
- Promover boas práticas de documentação e manutenibilidade.

## 4.1 . Implementação do `README.md` detalhado

# 🌽 Agromart Web

Frontend do sistema Agromart, desenvolvido com React. Este projeto faz parte da plataforma Agromart, voltada à gestão e integração de comunidades que produzem e distribuem alimentos de forma colaborativa (CSAs - Comunidades que Sustentam a Agricultura).

---

## 🚀 Como rodar o projeto localmente

### 1. Pré-requisitos

- [NVM](https://github.com/nvm-sh/nvm) (Node Version Manager)
- Node.js **v18**
- [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/)

### 2. Instalação do Node.js 18 usando NVM

Caso ainda não tenha o NVM instalado, execute:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Depois, feche e reabra o terminal ou rode:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
```

Instale e use o Node.js 18:

```bash
nvm install 18
nvm use 18
```

### 3. Instalar dependências

No diretório raiz do projeto:

```bash
yarn install
```

### 4. Iniciar o projeto

Devido a dependências que usam OpenSSL legado, utilize a flag `--openssl-legacy-provider`:

```bash
NODE_OPTIONS=--openssl-legacy-provider yarn start
```

O projeto será iniciado em: [http://localhost:3000](http://localhost:3000)

---

## 💡 Dica: automatize com um script

Crie um arquivo `start.sh`:

```bash
#!/bin/bash
nvm use 18
NODE_OPTIONS=--openssl-legacy-provider yarn start
```

Dê permissão de execução:

```bash
chmod +x start.sh
```

E execute com:

```bash
./start.sh
```

---

## 📁 Estrutura do projeto

```
agromart-web/
├── public/             # Arquivos públicos e HTML base
├── src/                # Código-fonte
│   ├── assets/         # Imagens, ícones e fontes
│   ├── components/     # Componentes reutilizáveis (UI)
│   ├── hooks/          # Hooks customizados
│   ├── pages/          # Páginas do sistema
│   ├── routes/         # Rotas e navegação
│   ├── services/       # Serviços (ex: chamadas à API)
│   ├── styles/         # Estilos globais
│   └── utils/          # Utilitários e funções auxiliares
├── .env.example        # Exemplo de configuração de variáveis de ambiente
├── package.json        # Dependências e scripts
└── README.md           # Documentação do projeto
```

---

## 🛠️ Scripts úteis

- `yarn start`: inicia o servidor local de desenvolvimento
- `yarn build`: cria a versão de produção do app
- `yarn lint`: roda o linter (se configurado)
- `yarn test`: executa os testes (se houver)

---

## 🧪 Testes

> Ainda não há testes automatizados configurados neste repositório. Contribuições são bem-vindas!

---

## 👥 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'feat: minha feature'`)
4. Push para o repositório (`git push origin feature/minha-feature`)
5. Crie um Pull Request

---

## 📄 Licença

Este projeto segue a licença MIT. Consulte o arquivo [`LICENSE`](./LICENSE) para mais detalhes.

---

## 📫 Contato

Para dúvidas ou sugestões, entre em contato com a equipe responsável ou abra uma *issue* neste repositório.

---

> Projeto mantido como parte da iniciativa AgroMart 🌾


## 5. Conclusão
A avaliação de compreensibilidade do sistema AgroMart mostrou pontos fortes na documentação do repositório docs e na organização modular do agromart-web. Porém, a falta de um README.md detalhado e de comentários no código do agromart-web, e com status de arquivado, representam desafios  para a compreensibilidade e manutenibilidade. A implementação do novo README.md é um passo inicial para amenizar esses problemas e melhorar a experiência de novos desenvolvedores com o projeto.

## 6. ### 8. Detalhamento da Ação de Melhoria Implementada

#### 6.1 Justificativa

A criação de um `README.md` detalhado foi escolhida como ação prioritária por três motivos principais:

1. **Métrica M3**: O `README.md` anterior era genérico (Create React App) e não explicava o projeto AgroMart — pontuação 🚨 Baixa.
2. **Métrica M5**: A falta de documentação e comentários dificultava a compreensão do código — pontuação 🚨 Baixa.
3. **Experiência do desenvolvedor**: O `README.md` é o primeiro contato com o projeto e deve fornecer uma visão clara e rápida do sistema.

#### 6.2 Processo de Implementação

Etapas seguidas:

1. **Análise** do `README.md` original.
2. **Identificação** das seções necessárias com base na estrutura do projeto.
3. **Criação** do novo conteúdo, incluindo:
   - Título e descrição do projeto
   - Tecnologias utilizadas
   - Estrutura do projeto
   - Scripts disponíveis
   - Diretrizes de contribuição
   - Licença
4. **Implementação** do novo arquivo em `/home/ubuntu/agromart-web/README.md`.

#### 6.3 Conteúdo Criado

O novo `README.md`:

- Explica o propósito do projeto (ligar agricultores a consumidores)
- Detalha os diretórios do código (`src/`)
- Oferece orientações práticas sobre execução
- Inclui diretrizes para contribuições colaborativas

#### 6.4 Impacto Esperado

- **M3**: A pontuação sobe de 🚨 Baixa para 👍 Alta.
- **Onboarding facilitado**: Novos devs entenderão o projeto mais rápido.
- **Colaboração padronizada**: As diretrizes ajudam na organização do time.
- **Compreensibilidade aprimorada**: O `README.md` agora cumpre papel de documentação de entrada.


## 7. Planilha de Pontuação das Métricas

| Métrica | Descrição                                      | Repositório   | Método de Avaliação     | Pontuação Antes | Pontuação Após Melhoria | Justificativa                                                                 |
|---------|------------------------------------------------|----------------|--------------------------|------------------|--------------------------|--------------------------------------------------------------------------------|
| M1      | Organização modular do código                 | agromart-web   | Inspeção de pastas       | 👍 Alto          | 👍 Alto                  | Estrutura bem organizada com separação clara de responsabilidades              |
| M2      | Clareza na nomeação de arquivos e componentes | agromart-web   | Avaliação cruzada        | 👍 Alto          | 👍 Alto                  | Nomes descritivos e intuitivos para componentes                                |
| M3      | Existência de README, guia e arquitetura      | agromart-web   | Checklist                 | 🚨 Baixo         | 👍 Alto                  | Criação de `README.md` detalhado e específico do projeto                       |
| M4      | Clareza da documentação                       | docs           | Avaliação com nota        | 👍 Alto          | 👍 Alto                  | Documentação bem estruturada e linguagem clara                                 |
| M5      | Proporção de funções com comentários úteis    | agromart-web   | Contagem manual           | 🚨 Baixo         | ⚠️ Médio                | `README.md` fornece contexto, mas o código ainda carece de comentários         |
| M6      | Aderência a padrões de boas práticas          | agromart-web   | Checklist e lint          | 🚨 Baixo         | 🚨 Baixo                | Ausência de ferramentas de lint configuradas                                   |

## 8. Classificação Final do Sistema

**Classificação: Compreensível**

- Métricas com pontuação **Alta**: M1, M2, M3 (após melhoria), M4 → 4 métricas
- Métricas com pontuação **Baixa**: M6 → 1 métrica

**Critério atendido:** ≥ 4 métricas com pontuação Alta e no máximo 1 Baixa.

A ação de melhoria (README.md detalhado) elevou a classificação de **Parcialmente compreensível** para **Compreensível**.

---

## 9. Recomendações para Melhorias Futuras

1. **Implementar lint (ESLint)** para TypeScript e React → melhora da métrica M6.  
2. **Adicionar comentários explicativos** no código → melhora da métrica M5.  
3. **Criar documentação de arquitetura técnica**, com diagramas.  
4. **Definir padrões de codificação** claros e documentados.  
5. **Incluir testes automatizados** (unitários e de integração) com documentação.

---

## 10. Evidências da Avaliação

Durante a avaliação, foram coletadas as seguintes evidências:


- 🔍 Inspeção de componentes para análise de nomenclatura
- 📄 Análise do conteúdo do site de documentação do AgroMart
- 📝 Novo arquivo `README.md` criado como evidência da ação de melhoria

Todas os indícios estão salvos nos diretórios locais e disponíveis para consulta.



## 11. Referências

- [AgroMart/agromart-web - GitHub Repository](https://github.com/AgroMart/agromart-web)
- [AgroMart/docs - GitHub Repository](https://github.com/AgroMart/docs)
- [AgroMart Docs Website](https://agromart.github.io/docs/)


##  Tabela de Versionamento

<div style="overflow-x:auto">

<table>
  <thead>
    <tr>
      <th>Data</th>
      <th>Versão</th>
      <th>Descrição</th>
      <th>Autor</th>
      <th>Revisor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>12/07/2025</td>
      <td>1.0</td>
      <td>Criação da Fase 4, Execução </td>
      <td><a href="https://github.com/RaissaAndradeS">Raissa</a></td>
      <td>–</td>
    </tr>
  </tbody>
</table>

</div>



