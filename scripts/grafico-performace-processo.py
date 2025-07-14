import os
import re
import plotly.graph_objects as go
import plotly.io as pio
from github import Github, GithubException
from datetime import datetime
from collections import defaultdict
import numpy as np
import csv

# --- Configurações do repositório e token ---
GITHUB_TOKEN = os.getenv('GH_TOKEN')  # Token do GitHub via variável de ambiente
REPO_OWNER = "FCTE-Qualidade-de-Software-1"  # Substitua pelo dono do repositório
REPO_NAME = "2025-1-T01-ADELE-GOLDSTINE-Mateus-Villela-Raissa-Andrade"  # Substitua pelo nome do repositório

# Caminho do gráfico gerado
GRAPH_PATH = "docs/assets/imgs/graficos/velocity_graph_hours.png"  # Caminho do gráfico no repositório

# Configurações para labels de tempo
DEFAULT_HOURS_IF_NO_ESTIMATE = 0  # Valor padrão horas, se não houver label

# --- Autenticação ---
if not GITHUB_TOKEN:
    print("Erro: GH_TOKEN não configurado.")
    exit(1)

g = Github(GITHUB_TOKEN)
try:
    repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
    print(f"Conectado ao repositório: {repo.full_name}")
except Exception as e:
    print(f"Erro ao acessar o repositório. Verifique REPO_OWNER, REPO_NAME e GH_TOKEN. Erro: {e}")
    exit(1)

# --- Coletando dados: milestones e issues ---
milestones_data = {}
try:
    milestones = repo.get_milestones(state="all")  # Pega todas as milestones (abertas e fechadas)

    print("Iniciando coleta de dados por milestone...")
    for milestone in milestones:
        total_hours_for_milestone = 0  # Inicializa o total de horas por milestone

        closed_issues = repo.get_issues(state="closed", milestone=milestone)

        for issue in closed_issues:
            # Calcula o tempo de vida da issue em horas
            if issue.closed_at and issue.created_at:
                delta = issue.closed_at - issue.created_at
                issue_hours = delta.total_seconds() / 3600  # horas
            else:
                issue_hours = DEFAULT_HOURS_IF_NO_ESTIMATE
            # Soma o tempo de vida da issue (em horas) para a milestone
            total_hours_for_milestone += issue_hours

        # Armazena o total de horas por milestone
        milestones_data[milestone.title] = total_hours_for_milestone
        print(f"Milestone '{milestone.title}' -> Total de horas: {total_hours_for_milestone}")

except Exception as e:
    print(f"Erro ao coletar dados de milestones/issues. Erro: {e}")
    exit(1)

# --- Coletando dados por Issue fechada ---
print("Iniciando contagem de issues fechadas por dia, agrupadas por milestone...")
closed_issues = repo.get_issues(state="closed")
all_issues = repo.get_issues(state="all")

# Dicionário para issues fechadas por dia e milestone
milestone_day_count = defaultdict(lambda: defaultdict(int))
issue_days = set()

for issue in closed_issues:
    milestone = issue.milestone.title if issue.milestone else "Sem milestone"
    if issue.closed_at:
        day_str = issue.closed_at.strftime('%d/%m/%Y')
        milestone_day_count[milestone][day_str] += 1
        issue_days.add(day_str)

issue_days = sorted(list(issue_days))

# --- Calculando dados para o gráfico principal com TODAS as issues ---
milestones_list = list(repo.get_milestones(state="all"))
milestone_names = []
fechadas_no_prazo = []
fechadas_apos_prazo = []
issues_abertas = []
percent_slippage_by_milestone = []

print("Analisando todas as issues por milestone...")

for milestone in milestones_list:
    # Busca TODAS as issues da milestone (abertas e fechadas)
    all_issues_milestone = list(repo.get_issues(milestone=milestone, state="all"))
    closed_issues_milestone = list(repo.get_issues(milestone=milestone, state="closed"))
    open_issues_milestone = list(repo.get_issues(milestone=milestone, state="open"))
    
    no_prazo = 0
    apos_prazo = 0
    abertas = len(open_issues_milestone)
    due = milestone.due_on if milestone.due_on else None
    
    print(f"Milestone '{milestone.title}': {len(all_issues_milestone)} issues totais, {len(closed_issues_milestone)} fechadas, {abertas} abertas")
    
    # Analisa apenas as issues fechadas para determinar se foram no prazo ou não
    for issue in closed_issues_milestone:
        closed = issue.closed_at
        if closed and due:
            if closed > due:
                apos_prazo += 1
            else:
                no_prazo += 1
        elif closed and not due:
            # Se não há prazo definido, considera como "no prazo"
            no_prazo += 1
    
    milestone_names.append(milestone.title)
    fechadas_no_prazo.append(no_prazo)
    fechadas_apos_prazo.append(apos_prazo)
    issues_abertas.append(abertas)
    
    # Calcula percentual de slippage em relação ao TOTAL de issues da milestone
    total_issues = len(all_issues_milestone)
    percent = (apos_prazo / total_issues * 100) if total_issues > 0 else 0
    percent_slippage_by_milestone.append(percent)
    
    print(f"  - No prazo: {no_prazo}, Fora do prazo: {apos_prazo}, Abertas: {abertas}")
    print(f"  - % Fora do prazo (sobre total): {percent:.2f}%")

# --- Gerar gráfico principal com colunas e linha de porcentagem ---
fig = go.Figure()

# Adicionar colunas para issues no prazo
fig.add_trace(go.Bar(
    x=milestone_names,
    y=fechadas_no_prazo,
    name='Issues Entregues no Prazo',
    marker_color='seagreen',
    hovertemplate='<b>%{x}</b><br>Issues no Prazo: %{y}<br><extra></extra>'
))

# Adicionar colunas para issues fora do prazo
fig.add_trace(go.Bar(
    x=milestone_names,
    y=fechadas_apos_prazo,
    name='Issues Entregues Fora do Prazo',
    marker_color='crimson',
    hovertemplate='<b>%{x}</b><br>Issues Fora do Prazo: %{y}<br><extra></extra>'
))

# Adicionar colunas para issues ainda abertas
fig.add_trace(go.Bar(
    x=milestone_names,
    y=issues_abertas,
    name='Issues Ainda Abertas',
    marker_color='orange',
    hovertemplate='<b>%{x}</b><br>Issues Abertas: %{y}<br><extra></extra>'
))

# Adicionar linha de porcentagem de issues fechadas fora do prazo (sobre o total)
fig.add_trace(go.Scatter(
    x=milestone_names,
    y=percent_slippage_by_milestone,
    mode='lines+markers',
    name='% Issues Fechadas Fora do Prazo (sobre total)',
    line=dict(color='black', width=3, dash='dash'),
    marker=dict(symbol='circle', size=8, color='black'),
    yaxis='y2',
    hovertemplate='<b>%{x}</b><br>% Fora do Prazo: %{y:.2f}%<br><extra></extra>'
))

# Configurar layout do gráfico
fig.update_layout(
    barmode='group',
    title='<b>Histograma de Tempo de Ciclo - Todas as Issues por Milestone</b>',
    title_x=0.5,
    xaxis_title="Milestone",
    yaxis_title="Número de Issues",
    yaxis2=dict(
        title="% Issues Fechadas Fora do Prazo (sobre total de issues)",
        overlaying='y',
        side='right',
        range=[0, 100]
    ),
    legend_title="Legenda",
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.35,
        xanchor="center",
        x=0.5
    ),
    height=900,
    width=1800,
    template="plotly_white"
)

# Salvar o gráfico como imagem
try:
    output_dir = os.path.dirname(GRAPH_PATH)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Diretório criado: {output_dir}")

    pio.write_image(fig, GRAPH_PATH)
    print(f"Gráfico salvo em: {GRAPH_PATH}")
except Exception as e:
    print(f"Erro ao salvar o gráfico: {e}")

print("Calculando métricas de desempenho de processo...")
now_str = datetime.now().strftime('%Y%m%d_%H%M%S')

csv_dir = 'data/desempenho-processo/'
os.makedirs(csv_dir, exist_ok=True)
csv_filename = f'metrica-de-desempenho-processo_{now_str}.csv'
csv_path = os.path.join(csv_dir, csv_filename)

csv_header = [
    'Issue Nº', 'Título', 'Sprint (Milestone)', 'Status', 'Data Criação', 'Data Fechamento', 'Prazo Planejado', 'Lead Time (dias)', 'Slippage (dias)'
]
csv_rows = []
lead_times = []
slippages = []
issue_labels = []

# Incluir TODAS as issues no CSV (abertas e fechadas)
for issue in repo.get_issues(state="all"):
    milestone_title = issue.milestone.title if issue.milestone else ''
    created = issue.created_at
    closed = issue.closed_at
    status = "Fechada" if issue.state == "closed" else "Aberta"
    due = issue.milestone.due_on if issue.milestone and issue.milestone.due_on else None
    
    if closed and created:
        lead_time = (closed - created).days
    else:
        lead_time = 0
    
    if closed and due:
        slippage = (closed - due).days
    else:
        slippage = None
    
    lead_times.append(lead_time)
    slippages.append(slippage if slippage is not None else 0)
    issue_labels.append(f"#{issue.number}")
    
    csv_rows.append([
        issue.number,
        issue.title,
        milestone_title,
        status,
        created.strftime('%Y-%m-%d') if created else '',
        closed.strftime('%Y-%m-%d') if closed else '',
        due.strftime('%Y-%m-%d') if due else '',
        lead_time,
        slippage if slippage is not None else ''
    ])

avg_slippage = np.mean([s for s in slippages if s is not None and s != 0]) if slippages else 0

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
print(f"CSV salvo em: {csv_path}")

# --- Gráfico de Lead Time e Slippage por Issue (apenas fechadas) ---
closed_issues_for_chart = [issue for issue in repo.get_issues(state="closed")]
lead_times_closed = []
slippages_closed = []
issue_labels_closed = []

for issue in closed_issues_for_chart:
    created = issue.created_at
    closed = issue.closed_at
    due = issue.milestone.due_on if issue.milestone and issue.milestone.due_on else None
    
    lead_time = (closed - created).days if closed and created else 0
    slippage = (closed - due).days if closed and due else 0
    
    lead_times_closed.append(lead_time)
    slippages_closed.append(slippage)
    issue_labels_closed.append(f"#{issue.number}")

fig_leadtime = go.Figure()
fig_leadtime.add_trace(go.Bar(
    x=issue_labels_closed,
    y=lead_times_closed,
    name='Lead Time (dias)',
    marker_color='royalblue',
    hovertemplate='Issue: %{x}<br>Lead Time: %{y} dias<extra></extra>'
))
fig_leadtime.add_trace(go.Bar(
    x=issue_labels_closed,
    y=slippages_closed,
    name='Slippage (dias)',
    marker_color='crimson',
    hovertemplate='Issue: %{x}<br>Slippage: %{y} dias<extra></extra>'
))
fig_leadtime.add_trace(go.Scatter(
    x=issue_labels_closed,
    y=[avg_slippage]*len(issue_labels_closed),
    mode='lines',
    name='Slippage Médio',
    line=dict(color='orange', width=4, dash='dash'),
    hovertemplate='Slippage Médio: %{y:.2f} dias<extra></extra>'
))
fig_leadtime.update_layout(
    barmode='group',
    title='<b>Desempenho de Processo: Lead Time e Slippage por Issue</b>',
    title_x=0.5,
    xaxis_title="Issue",
    yaxis_title="Dias",
    legend_title="Legenda",
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.25,
        xanchor="center",
        x=0.5
    ),
    height=700,
    width=1200,
    template="plotly_white"
)

# --- Gráfico de Taxa (%) de Slippage por Milestone ---
fig_taxa = go.Figure()
fig_taxa.add_trace(go.Bar(
    x=milestone_names,
    y=percent_slippage_by_milestone,
    name='Taxa de Slippage (%)',
    marker_color='crimson',
    hovertemplate='Milestone: %{x}<br>Taxa de Slippage: %{y:.2f}%<extra></extra>'
))
fig_taxa.update_layout(
    barmode='group',
    title='<b>Taxa de Slippage (%) por Sprint (Milestone) - Sobre Total de Issues</b>',
    title_x=0.5,
    xaxis_title="Sprint (Milestone)",
    yaxis_title="Taxa de Slippage (%)",
    legend_title="Legenda",
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.25,
        xanchor="center",
        x=0.5
    ),
    height=700,
    width=1200,
    template="plotly_white"
)

# --- Exportação dos gráficos ---
grafico_dir_hist = 'docs/assets/imgs/graficos/historico/grafico-desempenho-processo/'
grafico_nome_hist = f'grafico-desempenho-processo_{now_str}.png'
grafico_path_hist = os.path.join(grafico_dir_hist, grafico_nome_hist)
os.makedirs(grafico_dir_hist, exist_ok=True)

grafico_dir_atual = 'docs/assets/imgs/graficos/'
grafico_nome_atual = 'grafico-desempenho-processo.png'
grafico_path_atual = os.path.join(grafico_dir_atual, grafico_nome_atual)
os.makedirs(grafico_dir_atual, exist_ok=True)

for path in [grafico_path_hist, grafico_path_atual]:
    try:
        pio.write_image(fig, path)
        print(f"Gráfico salvo em: {path}")
    except Exception as e:
        print(f"Erro ao salvar o gráfico: {e}")