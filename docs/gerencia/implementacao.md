# Implementação - Etapa 3

Segundo o planejado na [etapa anterior](../planejamento.md), segue-se para a execução das medições estipuladas, visando aplicar os procedimentos para coletar e processar os dados e, por consequência, produzir os produtos informacionais que alimentam os dashboards e futuros relatórios de gestão. Nesse sentido, as atividades consistem em quatro etapas principais, descritas conforme a norma ISO/IEC 15939:2001 (cláusula 5.3) e adaptadas às condições do projeto.

---

## 1. Incorporar os Procedimentos de Medição

A coleta e análise dos dados foram integradas às rotinas naturais do projeto por meio do uso do GitHub como plataforma central de desenvolvimento. A medição ocorre como parte do ciclo técnico da equipe, com atenção aos seguintes pontos:

- Utilização padronizada de **Issues**, **Pull Requests** e **Milestones**, de modo a garantir rastreabilidade dos artefatos.
- Aplicação de boas práticas no uso de labels, atribuições (`assignee`) e vinculação a entregas (`milestone`), conforme previsto no plano de medição.
- Execução automatizada dos scripts de medição em Python a cada novo commit registrado no repositório.

## 2. Coletar os Dados

A coleta é realizada automaticamente por meio de script Python desenvolvido e mantido por [Mateus](https://github.com/MVConsorte), com base na GitHub API. Os dados extraídos incluem:

- Metadados de Issues: `created_at`, `closed_at`, `assignee`, `labels`, `milestone`.
- Metadados de PRs: autor, timestamps, número de revisões.
- Ciclos de entrega: agrupamento por Milestone/Sprint.

Os dados brutos são armazenados no diretório `/data/` do repositório, com persistência automática e controle por commit. A verificação inicial da consistência dos dados é feita manualmente, garantindo integridade antes da análise.

## 3. Analisar os Dados e Desenvolver os Produtos Informacionais

As medidas derivadas e indicadores são calculados com base nas fórmulas definidas no planejamento (etapa 5.2.3), organizados por categoria de necessidade informacional:

- **Calendário e progresso**: taxa de conclusão de sprints, ritmo de entrega.
- **Desempenho de processo**: lead time, slippage médio por entrega.
- **Recursos e custos**: esforço médio por entrega, eficiência de alocação por membro.

Os resultados são organizados em arquivos `.csv`, permitindo visualização estruturada dos dados. Além disso, gráficos interpretativos são gerados automaticamente e publicados junto aos relatórios, com foco em facilitar a análise comparativa entre ciclos.

## 4. Comunicar os Resultados

Os produtos informacionais são disponibilizados publicamente por meio de:

- Repositório GitHub do projeto (`/reports/`).
- Publicação via GitHub Pages, com visualizações gráficas vinculadas.

A divulgação dos resultados garante transparência e promove o uso ativo dos indicadores na gestão do projeto.

---

**_Referência Normativa:_** ISO/IEC 15939:2001 – Software Engineering — Software Measurement Process.

---
## Tabela de Versionamento

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
      <td>13/07/2025</td>
      <td>1.0</td>
      <td>Criação e escrita da Página de Implementação.</td>
      <td><a href="https://github.com/MVConsorte">Mateus</a></td>
      <td><a href="https://github.com/RaissaAndradeS">Raissa</a></td>
    </tr>
  </tbody>
</table>

</div>
