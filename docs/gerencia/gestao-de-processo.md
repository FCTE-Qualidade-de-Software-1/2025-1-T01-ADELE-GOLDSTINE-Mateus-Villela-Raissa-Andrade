# Gestão de Processo

## Introdução

A gestão de processo é fundamental para garantir a qualidade e o sucesso dos projetos de software. Baseando-se na ISO/IEC 15939 e no princípio do PSM/CID, este documento apresenta a estruturação da gerência de processo, vinculados às práticas e diretrizes para o gerenciamento eficaz da medição de processos, promovendo a melhoria contínua e o alinhamento com os objetivos organizacionais (ou equipe). A motivação para adotar esse padrão internacional reside na necessidade de estabelecer métodos claros e confiáveis para coletar, analisar e utilizar dados, possibilitando decisões informadas e o aprimoramento dos resultados ao longo do ciclo de vida do software. Além disso, essa prática contribui para a coerência e coesão no própria gestão do projeto, além de mensurar o quão eficaz e adequada são as práticas e artefatos de um processo. Assim, essa página se concetra em estabelecer a gerência de processo vinculados ao projeto da disicplina de Qualidade de Software 1 (2025.1).

## Objetivos 

**Objetivo Geral**: Documentação e rastreabilidade da Gestão de processo e artefatos associados, visando a aplicação do Processo de medição de software proposto pela ISO/IEC 15939:2001.

**Objetivos Específicos**:
    
- Execução das etapas do Processo de medição que a gestão do processo.
- Implementação de três produtos de informação com integração ao Git/Github para monitoramento de processo.
- Avaliação dos resultados obtidos.

## Referencial teórico

O processo de medição, conforme definido na norma ISO/IEC 15939:2001, representa uma metodologia estruturada voltada ao apoio e melhoria contínua da **gestão de processos organizacionais** ([1](#ref-bib), p.7-8). Sua aplicação está centrada na coleta, análise e comunicação de dados que representam tanto os produtos desenvolvidos quanto os processos implementados pela unidade organizacional ([1](#ref-bib), p.7). Ao fazer isso, a medição se torna uma ferramenta gerencial que proporciona **tomada de decisão objetiva, monitoramento de desempenho e avaliação da qualidade**.

Segundo a norma, o processo de medição é constituído por quatro atividades principais que espelham o ciclo de melhoria contínua PDCA (Plan-Do-Check-Act ou, traduzido, Planejar-Fazer-Checar-Agir) e pode ser visualizado abaixo e em [Figura 1](#fig1) ([[1](#ref-bib)], p.7, 4.2):

- **5.1 Estabelecer e sustentar o compromisso de medição**  
  Visa garantir envolvimento da alta gestão e alocação de recursos para a execução sustentável da medição.
  
- **5.2 Planejar o processo de medição**  
  Engloba identificar necessidades de informação, selecionar medidas, definir procedimentos e critérios.

- **5.3 Executar o processo de medição**  
  Abrange coleta, armazenamento, análise de dados e geração dos produtos de informação.

- **5.4 Avaliar a medição**  
  Promove melhoria do processo com base em avaliações de eficácia e repositório de experiências.

#### **Figura 1**: Modelo de Processo de medição de software {#fig1}

![Modelo de Processo de medição de software](../assets/imgs/imagem-pdca-adaptado.jpeg)

**_Fonte_**: Retirado da ISO/IEC 15939:2001 ([1](#ref-bib), p. 9).

Essas atividades não são estanques, mas formam um ciclo iterativo de gestão, reforçando o vínculo entre **informação gerencial necessária** e os **produtos de informação** construídos com base em medidas adequadas.

### Principais Termos e Definições 

Alguns termos relevantes para o contexto segundo a ISO/IEC 15939:2001 ([[1](#ref-bib)], p.1-6):

- **atributo**: propriedade ou característica de uma entidade que pode ser distinguida quantitativamente ou qualitativamente por um humano ou automatizações.
- **entidade**: objeto que deve ser caracterizado através da medição dos seus atributos.
- **Medida Base**: medida definida em termos de um atributo e o método para quantificá-lo (independentes funcionalmente entre si).
- **Medida Derivada**: medida que é definida como uma função de dois ou mais valores
- **Medida**: variável à qual se atribui valor após operação de medição.
- **Indicador**: medida que fornece uma estimativa ou avaliação de atributos específicos derivados de um modelo acerca de necessidades informacionais (Information Needs) definidas.
- **Produto Informacional**: conjunto de indicadores e suas interpretações que satisfazem a(s) necessidade(s) informacional(is).
- **Necessidade Informacional**: conhecimento necessário para gerir objetivos, riscos e problemas.
- **Medição**: conjunto de operações que têm por objetivo determinar o valor de uma medida
- **Processo de medição**: conjunto de atividades para estabelecer, planejar, executar e avaliar a medição dentro de um contexto organizacional.
- **Modelo**: algoritmo ou cálculo que combina uma ou mais medidas de base e/ou derivadas com critérios de decisão associados.
- **Escala**: conjunto ordenado de valores, contínuos ou discretos, ou um conjunto de categorias às quais o atributo é atribuído.
- **Unidade de medida**: determinada quantidade, definida e adoptada por convenção, com a qual se comparam outras quantidades do mesmo tipo para exprimir a sua grandeza em relação a essa quantidade.
- **Valor**: resultado numérico ou categórico atribuído a uma medida de base, medida derivada ou indicador.

O processo é estruturado por meio do **Modelo de Informação de Medição**, que conecta diretamente os atributos observáveis dos elementos organizacionais às **necessidades informacionais** dos interessados (gerenciamento, técnica, qualidade). Isso permite uma abordagem sistemática na seleção de métricas e indicadores relevantes, com rastreabilidade desde a origem da necessidade até sua representação quantitativa e analítica.

Além disso, o processo é compatível com a abordagem CID/PSM, que organiza os artefatos da medição em níveis operacionais e estratégicos, desde o planejamento até a melhoria, reforçando o papel central da medição como parte da engenharia organizacional e da governança de qualidade.

## Metodologia

### Estabelecimento e comprometimento com a medição

### Planejamento de Processo de medição

### Execução de processo de medição

### Avaliação de processo de medição

## Considerações e Conclusão

## Referencia Bibliográfica {#ref-bib}
> [1] [ISO/IEC. *ISO/IEC 15939:2001 – Software engineering — Software measurement process*. Geneva: International Organization for Standardization, 2001.](../assets/pdfs/iso-15939.pdf).

## Bibliografia
> [ISO/IEC. *ISO/IEC 15939:2001 – Software engineering — Software measurement process*. Geneva: International Organization for Standardization, 2001.](../assets/pdfs/iso-15939.pdf).

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
      <td>11/07/2025</td>
      <td>1.0</td>
      <td>Criação da Página principal de Gestão de Processo com as seções definidas e feito a Introdução e Objetivo.</td>
      <td><a href="https://github.com/MVConsorte">Mateus</a></td>
      <td><a href="https://github.com/RaissaAndradeS">Raissa</a></td>
    </tr>
    <tr>
      <td>11/07/2025</td>
      <td>1.1</td>
      <td>Adição do Referencial teórico.</td>
      <td><a href="https://github.com/MVConsorte">Mateus</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

</div>