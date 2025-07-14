# Planejamento do Processo de Medição - Etapa 2

## Introdução

A etapa 5.2 da norma ISO/IEC 15939:2001 [[1](#ref-bib), p.12-15] trata da atividade de planejamento do processo de medição, essencial para garantir que as medições a serem realizadas sejam relevantes, estruturadas e alinhadas com as necessidades de informação da unidade organizacional. Esta atividade é central dentro do ciclo de melhoria contínua proposto pela norma e corresponde à fase de “Planejar” do modelo PDCA. Por meio do planejamento adequado, é possível selecionar medidas compatíveis com os objetivos do projeto, definir procedimentos sistemáticos de coleta e análise de dados e estabelecer critérios claros para avaliar os resultados. O modelo PSM/CID complementa esta abordagem ao fornecer uma estrutura prática para vincular artefatos, atividades e necessidades informacionais à produção de indicadores úteis à gestão.

## Objetivo

O objetivo deste documento é planejar o processo de medição no contexto do projeto, conforme especificado na etapa 5.2 da ISO/IEC 15939:2001 [[1](#ref-bib), p.12]. Pretende-se garantir que todas as decisões de medição — incluindo o que será medido, como será medido e por que será medido — estejam documentadas, justificadas e orientadas por necessidades reais de informação gerencial. O planejamento permitirá a geração de produtos informacionais confiáveis sobre calendário e progresso, desempenho de processo, recursos e custos, servindo como base para dashboards gerenciais.

## Planejamento

### Caracterização da Unidade Organizacional

A unidade organizacional envolvida corresponde à equipe responsável pelo desenvolvimento do projeto acadêmico supervisionado, composta por estudantes da disciplina de Qualidade de Software. Os processos executados incluem planejamento de tarefas, desenvolvimento técnico, acompanhamento de progresso e entrega de artefatos. A unidade opera sob metas pedagógicas, com cronograma previamente definido e critérios de avaliação estabelecidos.

**[Caso existam mais informações sobre a estrutura da equipe, ferramentas utilizadas ou escopo dos processos, inserir aqui para complementar a caracterização.]**

### Identificação das Necessidades Informacionais

Com base no capítulo 5.2.2 da norma ISO/IEC 15939:2001 [[1](#ref-bib), p.13] e nos princípios descritos no PSM CID Measurement Framework, foram identificadas necessidades informacionais específicas que podem ser observadas diretamente a partir de artefatos e dados registrados na plataforma GitHub, como Issues, Pull Requests, Commits e afins. Para tal, as necessidades foram organizadas nas três categorias de informação de enfoque previamente definidas: **calendário e progresso, desempenho de processo, e recursos e custos**. Para cada categoria, como pode ser visto abaixo na [Tabela 1](#tab1), buscou-se elencar algumas das principais necessidades informacionais vinculadas à entidade **Equipe** ou, se pertinente, **organização**.

#### Tabela 1: Potenciais Necessidades Informacionais {#tab1}

| ID  | Objetivo | Constantes | Riscos | Problemas Organizacionais | Necessidade Informacional | Categoria               | Entidade        |
| :-: | :------: | :--------: | :----: | :-----------------------: | :-----------------------: | :---------------------: | :-------------: |
| 1   | Garantir cumprimento de prazos | Cronograma definido | Atrasos nas entregas | Falta de alinhamento de datas | Percentual de tarefas concluídas no prazo | Calendário e Progresso | Equipe          |
| 2   | Monitorar evolução do projeto  | Marcos do projeto   | Mudanças de escopo   | Repriorização de tarefas      | Variação entre prazo planejado e prazo real | Calendário e Progresso | Equipe          |
| 3   | Avaliar aderência ao planejamento | Datas de entrega    | Sobrecarga de atividades | Falta de comunicação         | Número de atividades replanejadas          | Calendário e Progresso | Organizacional  |
| 4   | Medir eficiência do processo    | Volume de tarefas   | Retrabalho            | Falta de padronização         | Taxa de retrabalho                         | Desempenho de Processo | Equipe          |
| 5   | Acompanhar produtividade        | Frequência de entregas | Baixa produtividade | Falta de motivação            | Número de tarefas concluídas por período    | Desempenho de Processo | Equipe          |
| 6   | Identificar gargalos            | Ciclo de execução   | Acúmulo de tarefas    | Falta de recursos             | Tempo médio de execução por tarefa          | Desempenho de Processo | Organizacional  |
| 7   | Controlar alocação de recursos  | Horas disponíveis   | Subalocação           | Falta de registro de esforço   | Horas dedicadas por membro                  | Recursos e Custos      | Equipe          |
| 8   | Estimar custos do projeto       | Orçamento previsto  | Estouro de orçamento  | Falta de controle financeiro   | Custo estimado por entrega                  | Recursos e Custos      | Equipe          |
| 9   | Avaliar eficiência de uso de recursos | Recursos alocados | Desbalanceamento     | Falta de integração de sistemas | Relação entre esforço aplicado e resultado | Recursos e Custos      | Organizacional  |
| 10  | Monitorar carga de trabalho dedicada à documentação  | Total de Tarefas de documentação e periodo | Subestimação do esforço | Baixa especificação das entregas documentais     | Qual o volume de documentação produzida por tarefa que cumprem aos requisitos especificados? | Recursos e Custos      | Equipe          |
| 11  | Quantificar entregas em períodos | Períodos definidos  | Baixa entrega | Falta de acompanhamento        | Total de tarefas finalizadas em determinado período        | Calendário e Progresso | Equipe          |
| 12  | Avaliar relação de tarefas planejadas, realizadas e pendentes | Monitoramento de aderência ao plano de entrega | Acúmulo de pendências | Gargalo de controle de progresso da entrega     | Qual é a taxa de desvio de prazo (slippage) por entrega? | Desempenho de Processo | Organizacional  |

**_Fonte_**: autores

Estas necessidades foram selecionadas com base em sua potencial relevância para a tomada de decisão no contexto do projeto e por sua viabilidade de observação a partir de dados disponíveis em ferramentas de versionamento e colaboração utilizadas pela equipe. Em sequência, prioriza-se três delas, uma para cada categoria de informação, visando aplicá-las no ciclo de medição.

* Priorização

Para o processo de priorização, por se tratar da primeira rodada e o número de integrantes para a análise ser pequena, será utilizado três características para priorização: facilidade no acesso aos dados requisitados, importância para a equipe e esforço estimado na geração do produto de informação (ex.: tabela, gráfico e outros). Cada uma das características serão atribuidas de 1 a 5, sendo 1 o menor grau daquela característica e 5 maior grau e, ao fim, soma-se as notas das características de importância e facilidade de acesso dos dados e subtrai-se o de esforço. Assim, os que possuirem maior pontuação de cada categoria de informação, serão selecionados. Nesse sentido, segue a [Tabela 2](#tab2) abaixo com o resultado das pontuações.

### Tabela 2: Priorização das Necessidades Informacionais {#tab2}

| ID  | Necessidade Informacional                                                 | Categoria               | Facilidade (1–5) | Esforço (1–5) | Importância (1–5) | Pontuação (Facilidade + Importância - Esforço) | Classificação por Categoria |
| :-: | :------------------------------------------------------------------------ | :---------------------: | :-------------: | :-----------: | :----------------: | :--------------: | :--------------------------: |
| 11  | Quantas tarefas foram finalizadas em determinado período?                | Calendário e Progresso  | 5               | 5             | 5                  | 5                | 1 (**Selecionado**)          |
| 1   | Qual o percentual de tarefas concluídas dentro do prazo?                 | Calendário e Progresso  | 5               | 4             | 5                  | 6                | 2                           |
| 2   | Qual foi a variação entre os prazos planejado e real de execução?        | Calendário e Progresso  | 4               | 4             | 4                  | 4                | 3                           |
| 3   | Quantas atividades precisaram ser replanejadas?                          | Calendário e Progresso  | 3               | 3             | 3                  | 3                | 4                           |
| 12  | Qual foi a taxa de desvio de prazo (slippage) por entrega?              | Desempenho de Processo  | 4               | 3             | 5                  | 6                | 1 (**Selecionado**)         |
| 5   | Quantas tarefas foram concluídas em cada período?                        | Desempenho de Processo  | 5               | 4             | 3                  | 4                | 2                           |
| 4   | Qual é a taxa de retrabalho registrada no projeto?                       | Desempenho de Processo  | 3               | 3             | 4                  | 4                | 3                           |
| 6   | Qual é o tempo médio de execução por tarefa?                             | Desempenho de Processo  | 3               | 3             | 4                  | 4                | 4                           |
| 9   | Qual é a relação entre o esforço aplicado e os resultados obtidos?       | Recursos e Custos       | 2               | 3             | 4                  | 3                | 1 (**Selecionado**)         |
| 7   | Quantas horas foram dedicadas por cada membro da equipe?                | Recursos e Custos       | 2               | 2             | 3                  | 3                | 2                           |
| 8   | Qual o custo estimado por entrega realizada?                             | Recursos e Custos       | 2               | 2             | 3                  | 3                | 3                           |
| 10  | Qual o volume de documentação produzida por tarefa que cumpre requisitos? | Recursos e Custos       | 3               | 5             | 4                  | 2                | 4                           |

**_Fonte_**: autores

Baseado na [Tabela 2](#tab2), chega-se às três necessidades de informação de cada categoria a serem selecionadas para medição. Cada uma foi estimada baseada nos critérios de facilidade de obtenção dos dados, esforço associado e importância dada pela equipe, o que acarretou nas seguintes Necessidades Informacionais (Information Needs):

- **Calendário e Progresso**: Quantas tarefas foram finalizadas em determinado período ? (11);
- **Desempenho de Processo**: Qual foi a taxa de desvio de prazo (slippage) por entrega ? (12);
- **Recurso e Custo**: Qual é a relação entre o esforço aplicado e os resultados obtidos ? (9).

### Seleção de Medidas

Seguindo a base estipulada no capítulo 5.2.3 [[1](#ref-bib), p.13] e o padrão encontrado, tanto no documento do PSM/CID Framework [[2](#ref-bib)], as seguintes medidas foram selecionadas para cada necessidade de informação:

### Tabela 3: [Necessidade Informacional 11](#tab1) - Calendário e Progresso {#tab3}

| Tipo               | Nome da Medida ou Indicador              | Fórmula / Descrição                                                                 | Fonte GitHub                     |
|--------------------|-------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------|
| Medida Base        | Data de fechamento das Issues             | Valor extraído de `closed_at` de cada Issue                                          | Issues                           |
| Medida Base        | Milestone atribuída                      | Data de vencimento vinculada em `milestone.due_on`                                   | Issues + Milestones              |
| Medida Derivada    | Quantidade de Issues fechadas por período | `Qf = Σ Issues fechadas entre T_início e T_fim`                                      | Issues                           |
| Medida Derivada    | Taxa de conclusão da sprint               | `Tc = (Qf / Qt) × 100` onde Qt = total planejado para o ciclo                        | Issues + Milestones              |
| Indicador          | Ritmo de entrega por sprint               | Análise temporal da Taxa de Conclusão                                                | Painel de acompanhamento         |

**_Fonte_**: autores

### Tabela 4: [Necessidade Informacional 12](#tab1) - Desempenho de Processo {#tab4}

| Tipo               | Nome da Medida ou Indicador              | Fórmula / Descrição                                                                 | Fonte GitHub                     |
|--------------------|-------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------|
| Medida Base        | Data de criação e fechamento da Issue     | `created_at` e `closed_at`                                                           | Issues                           |
| Medida Base        | Prazo planejado da entrega                | `milestone.due_on` vinculado à Issue                                                 | Issues + Milestones              |
| Medida Derivada    | Lead Time por entrega                     | `LT = closed_at - created_at`                                                        | Issues                           |
| Medida Derivada    | Slippage (desvio de prazo)                | `S = closed_at - milestone.due_on`                                                   | Issues + Milestones              |
| Indicador          | Taxa média de slippage por entrega        | `Ts = (Σ S_i / N)` onde S_i = slippage por Issue i, N = total de entregas avaliadas | Painel de desempenho             |

**_Fonte_**: autores

### Tabela 5: [Necessidade Informacional 9](#tab1) - Recursos e Custos {#tab5}

| Tipo               | Nome da Medida ou Indicador               | Fórmula / Descrição                                                                 | Fonte GitHub                     |
|--------------------|--------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------|
| Medida Base        | Issues atribuídas por colaborador          | Contagem via `assignee`                                                             | Issues                           |
| Medida Base        | Tempo de fechamento por Issue              | `closed_at - created_at`                                                             | Issues                           |
| Medida Derivada    | Esforço médio por entrega                  | `Ef = Σ (closed_at - created_at) / Qf` onde Qf = Issues concluídas                  | Issues                           |
| Medida Derivada    | Esforço total por membro                   | `Em = Σ Effort_issues atribuídas ao membro`                                          | Issues atribuídas por membro     |
| Indicador          | Eficiência de alocação                     | `Ea = (Qt / Em)` onde Qt = entregas por membro, Em = esforço total                  | Painel de esforço e produtividade|

**_Fonte_**: autores



### Definição dos Procedimentos de Coleta, Análise e Reporte

Conforme especificado no capítulo 5.2.4 da ISO/IEC 15939:2001 [[1](#ref-bib), p.14], esta seção apresenta os procedimentos adotados para coleta, armazenamento, análise e comunicação das medidas selecionadas. O processo utiliza exclusivamente os dados disponibilizados pelo GitHub, com coleta automatizada via script Python mantido por [Mateus](https://github.com/MVConsorte), sem apoio de ferramentas externas como planilhas ou serviços paralelos.

#### 1. Coleta de Dados

| Item                          | Procedimento Especificado                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------|
| Fontes de dados              | Issues, Pull Requests e Milestones acessados via GitHub API                               |
| Método de coleta             | Script Python que realiza extração automatizada a partir de cada novo commit              |
| Periodicidade                | Evento de coleta ocorre automaticamente a cada commit registrado no repositório           |
| Verificação inicial          | Inspeção manual da consistência dos dados por membro designado para garantir integridade  |
| Responsável pela coleta      | [Mateus](https://github.com/MVConsorte)                                                   |

#### 2. Armazenamento e Verificação

| Item                          | Procedimento Especificado                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------|
| Repositório de dados         | Arquivos gerados pelo script são mantidos no diretório `/data/` dentro do GitHub do projeto |
| Persistência e rastreabilidade| Cada entrada inclui identificadores únicos (`Issue ID`, `PR ID`, `Milestone`) e timestamps |
| Acesso e permissão           | Arquivos disponíveis para leitura pública via repositório; edições realizadas apenas por script |

#### 3. Análise dos Dados

| Item                          | Procedimento Especificado                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------|
| Funções de medição           | Cálculos diretos em Python para lead time, slippage, esforço médio e eficiência de entrega |
| Modelos de interpretação     | Estatística descritiva, médias por ciclo, variações entre metas planejadas e valores reais |
| Normalização                 | Conversão padronizada de datas em intervalos de tempo (ex: dias corridos, horas úteis)     |
| Validação                    | Verificação automatizada de consistência entre ciclos; alertas para valores fora do padrão histórico |

#### 4. Reporte e Comunicação

| Item                          | Procedimento Especificado                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------|
| Formato dos produtos         | Exportação automática de relatórios tabulares em arquivos `.csv`, organizados por sprint   |
| Frequência de relatório      | Não definido previamente; depende de evento de análise concluída                          |
| Público-alvo                 | Equipe de desenvolvimento e professora orientadora                                        |
| Canal de comunicação         | Via repositório GitHub e publicação no GitHub Pages do projeto                            |
| Responsável pelo reporte     | [Mateus](https://github.com/MVConsorte)                                                   |

#### 5. Configuração e Controle dos Dados

| Item                          | Procedimento Especificado                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------|
| Versionamento                | Realizado automaticamente via commits no repositório, com histórico e diffs ativados       |
| Regras de modificação        | Dados processados não são alterados manualmente; qualquer correção exige nova coleta      |
| Relação entre ciclos         | Cada conjunto de dados é vinculado explicitamente à identificação da Milestone correspondente |


### Definição dos Critérios de Avaliação

Conforme estipulado no capítulo 5.2.5 da ISO/IEC 15939:2001 [[1](#ref-bib), p.14], os critérios de avaliação do processo de medição e dos produtos informacionais gerados visam garantir a relevância, confiabilidade e utilidade das medições no apoio à tomada de decisão gerencial. Esta etapa estabelece os padrões mínimos e desejáveis de qualidade para os resultados da medição, considerando aspectos de completude, aplicabilidade, consistência e conformidade com os planos definidos.

#### 1. Avaliação dos Produtos de Informação

| Critério                            | Descrição                                                                                         | Aplicação ao Projeto                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Clareza interpretativa              | Os indicadores devem ser facilmente compreendidos pelo público-alvo                               | Visualização por gráficos e estrutura de indicadores |
| Conformidade com a necessidade      | O indicador deve responder diretamente à necessidade informacional identificada                   | Ritmo de entrega, slippage e eficiência por membro   |
| Aderência aos dados reais           | Os produtos devem refletir fielmente os dados extraídos sem manipulação ou distorção              | Dados extraídos via GitHub API a cada commit         |
| Capacidade de análise comparativa   | Permitir acompanhamento entre diferentes sprints ou ciclos, destacando tendências e variações     | Análise temporal dos relatórios em `.csv`            |
| Facilidade de disseminação          | Os resultados devem estar disponíveis em formatos acessíveis e visualmente claros                 | Publicação em GitHub Pages e relatórios automatizados |
| Confiança do usuário                | O consumidor da informação confia na origem, na análise e nas interpretações apresentadas         | Garantido por rastreabilidade e código aberto dos scripts |
| Ajuste ao propósito                 | O produto deve ser demonstradamente eficaz na resposta à necessidade informacional específica     | Indicadores alinhados às categorias 11, 12 e 9       |
| Satisfação das premissas do modelo | As premissas técnicas (distribuição dos dados, unidades, escalas) devem ser respeitadas           | Validação automatizada por script Python             |

#### 2. Avaliação do Processo de Medição

| Critério                            | Descrição                                                                                         | Aplicação ao Projeto                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Confiabilidade dos procedimentos    | As tarefas de coleta e análise devem seguir métodos definidos e verificáveis                      | Automação com Python e verificação por [Mateus](https://github.com/MVConsorte) |
| Rastreabilidade dos dados           | As medidas devem ser associadas diretamente aos artefatos de origem                                | Identificação por Issue ID, Milestone, PR            |
| Atualização tempestiva              | O processo deve gerar dados e relatórios no momento oportuno para apoiar decisões                 | Geração automática a cada novo commit                |
| Eficiência                          | Os recursos aplicados à medição devem ser proporcionais ao valor informacional gerado             | Coleta e processamento integrados ao fluxo do projeto |
| Contenção de defeitos               | O processo deve evitar a introdução de erros e tratar rapidamente inconsistências                 | Validação manual inicial e logs de exceção           |
| Satisfação dos usuários             | Os usuários da medição devem considerar os resultados úteis, compreensíveis e aplicáveis          | Reuniões de acompanhamento e aceitação da docente     |
| Conformidade com o plano            | O processo deve seguir o escopo e procedimentos definidos no planejamento               | Etapas 5.1 e 5.2 implementadas segundo a ISO 15939    |
| Capacidade de melhoria contínua     | O processo deve permitir ajustes a partir dos aprendizados obtidos                                | Revisão por ciclos e refinamento iterativo das métricas |

---

Esses critérios formarão a base da validação contínua da prática de medição no projeto, apoiando a confiabilidade dos produtos gerados e a adequação do próprio processo conforme evolui. Eles poderão ser revisados ou adaptados a cada novo ciclo com base em evidências concretas e feedback dos envolvidos.



### Verificação e Validação

De acordo com o capítulo 5.2.6 da ISO/IEC 15939:2001 [[1](#ref-bib), p.14–15], esta etapa garante que o plano de medição definido seja tecnicamente sólido, operacionalmente viável e sustentado pelas partes interessadas. Trata-se de revisar e aprovar os artefatos definidos nas etapas anteriores, assegurando que os recursos estejam disponíveis e que todos os procedimentos estejam claros e consistentes com as necessidades do projeto.

| Ação                           | Descrição                                                                                     | Responsável                      |
|--------------------------------|------------------------------------------------------------------------------------------------|----------------------------------|
| Revisão técnica do plano       | Conferência das medidas, fórmulas e procedimentos definidos nas etapas 5.2.2, 5.2.3 e 5.2.4    | [Mateus](https://github.com/MVConsorte) |
| Validação com partes interessadas | Apresentação do plano à professora orientadora para aprovação formal                        | Equipe + Docente                 |
| Aprovação do processo          | Registro da aprovação via repositório GitHub, validando o início do ciclo de medição          | Professora responsável           |
| Verificação da viabilidade     | Confirmação da disponibilidade dos dados via API, execução dos scripts e teste de coleta inicial | [Mateus](https://github.com/MVConsorte) |
| Liberação para execução        | Após a validação técnica e institucional, inicia-se a coleta automática em cada commit        | GitHub + script Python           |

Esse processo reforça a confiabilidade do plano e dá início formal à execução da medição conforme previsto.

---

### Aquisição e Implementação de Tecnologias de Suporte

Conforme especificado no capítulo 5.2.7 da ISO/IEC 15939:2001 [[1](#ref-bib), p.15], esta etapa consiste em garantir que as ferramentas e recursos técnicos necessários para a execução do plano estejam disponíveis, adequadamente configurados e integrados às rotinas da equipe. O objetivo é viabilizar a automação e a consistência das atividades de coleta, análise e reporte.

| Item                             | Tecnologia ou Procedimento Implementado                                                | Estado Atual     |
|----------------------------------|----------------------------------------------------------------------------------------|------------------|
| Plataforma principal             | GitHub – Repositório central dos dados, Issues, Pull Requests e Milestones            |       |
| Script de medição                | Script em Python – Extrai e processa dados diretamente via API do GitHub              |      |
| Armazenamento dos dados          | Diretório `/data/` no próprio repositório – persistência local com versionamento      |      |
| Visualização dos resultados      | Exportação de `.csv` e publicação dos gráficos em página dedicada via GitHub Pages    |        |
| Automação por evento             | Gatilho de execução do script a cada novo commit                                       |          |

Todas as tecnologias foram implementadas com foco na simplicidade, rastreabilidade e integração direta ao fluxo de trabalho da equipe. Não são utilizadas ferramentas externas (como planilhas ou painéis comerciais), garantindo independência técnica e transparência metodológica.

---

## Referências {#ref-bib}
> [1] [ISO/IEC. *ISO/IEC 15939:2001 – Software engineering — Software measurement process*. Geneva: International Organization for Standardization, 2001.](../assets/pdfs/iso-15939.pdf)
>
> [2] [JONES, Cheryl L.; DRAPER, Geoff; GOLAZ, Bill; JANUSZ, Paul. PSM Continuous Iterative Development Measurement Framework – Part 1: Concepts, Definitions, Principles, and Measures. Version 2.1. Practical Software and Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021.](../assets/pdfs/psm-cid/psm-cid-part1.pdf)

## Bibliografia

> [ISO/IEC. *ISO/IEC 15939:2001 – Software engineering — Software measurement process*. Geneva: International Organization for Standardization, 2001.](../assets/pdfs/iso-15939.pdf).
>
> [MCGARRY, Francis; CARD, David; JONES, Cheryl L.; et al. Practical Software Measurement: Objective Information for Decision Makers. Capítulo 2 – Measurement Information Model. Versão digital. [S.l.]: Software Engineering Institute (SEI), 2002.](../assets/pdfs/measurement-information-model.pdf)


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
      <td>Criação e elaboração da Página de Planejamento do Processo de Medição.</td>
      <td><a href="https://github.com/MVConsorte">Mateus</a></td>
      <td><a href="https://github.com/RaissaAndradeS">Raissa</a></td>
    </tr>
  </tbody>
</table>

</div>