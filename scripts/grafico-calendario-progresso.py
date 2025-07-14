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

# Prepara dados para gráfico de barras (issues fechadas por dia, agrupadas por milestone)
color_palette = ["indigo", "darkorange", "seagreen", "crimson", "royalblue", "gold", "teal", "purple"]
bars = []
for idx, milestone in enumerate(milestone_day_count.keys()):
    counts = [milestone_day_count[milestone][d] for d in issue_days]
    bars.append(go.Bar(
        x=issue_days,
        y=counts,
        name=milestone,
        marker_color=color_palette[idx % len(color_palette)],
        hovertemplate=f'<b>{milestone}</b><br>Issues fechadas: %{{y}}<br>Dia: %{{x}}<extra></extra>'
    ))

# Gráfico de linha: porcentagem acumulada de issues fechadas
num_total_issues = len(list(all_issues))
acum_closed = np.cumsum([sum(milestone_day_count[m][d] for m in milestone_day_count) for d in issue_days])
percent_closed = [100 * v / num_total_issues if num_total_issues > 0 else 0 for v in acum_closed]
line = go.Scatter(
    x=issue_days,
    y=percent_closed,
    mode='lines+markers',
    name='Porcentagem',
    line=dict(color='black', width=3, dash='dash'),
    marker=dict(symbol='circle', size=8),
    yaxis='y2',
    hovertemplate='<b>Porcentagem Issues Fechadas</b><br>% Fechadas: %{y:.2f}%<br>Dia: %{x}<extra></extra>'
)

# --- Gerar gráfico com Plotly ---
if bars:
    fig = go.Figure(data=bars + [line])
    fig.update_layout(
        barmode='group',
        title='<b>Histograma de Tempo de Ciclo</b>',
        title_x=0.5,
        xaxis_title="Dia de Fechamento",
        yaxis_title="Número de Issues Fechadas",
        yaxis2=dict(
            title="% Issues Fechadas (acumulado)",
            overlaying='y',
            side='right',
            range=[0, 100]
        ),
        legend_title="Milestone",
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
else:
    print("Nenhuma issue fechada encontrada para gerar o gráfico.")

# --- Histograma de Issues Fechadas vs Issues Mergiadas por Data (todas fechadas = mergiadas) ---
print("Gerando histograma considerando que toda issue fechada foi mergiada...")

issues_closed = list(repo.get_issues(state="closed"))
issue_date_count = defaultdict(int)
for issue in issues_closed:
    if issue.closed_at:
        date = issue.closed_at.date()
        issue_date_count[date] += 1

all_dates_issues = sorted(issue_date_count.keys())
issues_total = [issue_date_count[d] for d in all_dates_issues]
issues_merged = issues_total.copy()  # Mesmos valores

bar_total_issues = go.Bar(
    x=[d.strftime('%d/%m/%Y') for d in all_dates_issues],
    y=issues_total,
    name='Issues Fechadas',
    marker_color='royalblue',
    hovertemplate='Data: %{x}<br>Issues Fechadas: %{y}<extra></extra>'
)
bar_merged_issues = go.Bar(
    x=[d.strftime('%d/%m/%Y') for d in all_dates_issues],
    y=issues_merged,
    name='Issues Mergiadas',
    marker_color='darkorange',
    hovertemplate='Data: %{x}<br>Issues Mergiadas: %{y}<extra></extra>'
)

issues_total_sum = sum(issues_total)
cum_total_issues = np.cumsum(issues_total)
percent_cum_total_issues = [100 * v / issues_total_sum if issues_total_sum > 0 else 0 for v in cum_total_issues]
percent_cum_merged_issues = percent_cum_total_issues.copy()

line_total_issues = go.Scatter(
    x=[d.strftime('%d/%m/%Y') for d in all_dates_issues],
    y=percent_cum_total_issues,
    mode='lines+markers',
    name='Percentual Cumulativo Fechadas',
    line=dict(color='royalblue', width=3, dash='dash'),
    marker=dict(symbol='circle', size=8),
    yaxis='y2',
    hovertemplate='Data: %{x}<br>% Cumulativo Fechadas: %{y:.2f}%<extra></extra>'
)
line_merged_issues = go.Scatter(
    x=[d.strftime('%d/%m/%Y') for d in all_dates_issues],
    y=percent_cum_merged_issues,
    mode='lines+markers',
    name='Percentual Cumulativo Mergiadas',
    line=dict(color='darkorange', width=3, dash='dot'),
    marker=dict(symbol='diamond', size=8),
    yaxis='y2',
    hovertemplate='Data: %{x}<br>% Cumulativo Mergiadas: %{y:.2f}%<extra></extra>'
)

fig_issues = go.Figure(data=[bar_total_issues, bar_merged_issues, line_total_issues, line_merged_issues])
fig_issues.update_layout(
    barmode='group',
    title='<b>Histograma de Issues Fechadas vs Mergiadas (todas fechadas = mergiadas)</b>',
    title_x=0.5,
    xaxis_title="Data de Fechamento",
    yaxis_title="Quantidade",
    yaxis2=dict(
        title="% Cumulativo",
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

issues_graph_path = "docs/assets/imgs/graficos/histograma_issues_vs_mergiadas.png"
try:
    output_dir = os.path.dirname(issues_graph_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pio.write_image(fig_issues, issues_graph_path)
    print(f"Gráfico de issues salvo em: {issues_graph_path}")
except Exception as e:
    print(f"Erro ao salvar o gráfico de issues: {e}")

# --- Gráfico Schedule & Progress por Sprint (Milestone) ---
print("Gerando gráfico de Schedule & Progress por sprint (milestone)...")

milestone_names = []
planned_counts = []
done_counts = []

milestones = list(repo.get_milestones(state="all"))
for milestone in milestones:
    # Busca todas as issues da milestone
    issues_all = list(repo.get_issues(milestone=milestone, state="all"))
    issues_closed = list(repo.get_issues(milestone=milestone, state="closed"))
    issues_open = list(repo.get_issues(milestone=milestone, state="open"))
    planned = len(issues_all)  # Tarefas planejadas (committed tasks)
    done = len(issues_closed)  # Tarefas completas
    milestone_names.append(milestone.title)
    planned_counts.append(planned)
    done_counts.append(done)

bar_planned = go.Bar(
    x=milestone_names,
    y=planned_counts,
    name='Tarefas Planejadas',
    marker_color='gray',
    hovertemplate='Sprint: %{x}<br>Planejadas: %{y}<extra></extra>'
)
bar_done = go.Bar(
    x=milestone_names,
    y=done_counts,
    name='Tarefas Completas',
    marker_color='seagreen',
    hovertemplate='Sprint: %{x}<br>Completas: %{y}<extra></extra>'
)

fig_schedule = go.Figure(data=[bar_planned, bar_done])

# Linhas de progresso cumulativo
cum_planned = np.cumsum(planned_counts)
cum_done = np.cumsum(done_counts)
percent_cum_planned = [100 * v / sum(planned_counts) if sum(planned_counts) > 0 else 0 for v in cum_planned]
percent_cum_done = [100 * v / sum(planned_counts) if sum(planned_counts) > 0 else 0 for v in cum_done]

line_planned = go.Scatter(
    x=milestone_names,
    y=percent_cum_planned,
    mode='lines+markers',
    name='Progresso Planejado (%)',
    line=dict(color='blue', width=4, dash='dash'),  # cor azul, linha mais grossa
    marker=dict(symbol='circle', size=10, color='blue'),
    yaxis='y2',
    hovertemplate='Sprint: %{x}<br>% Planejado: %{y:.2f}%<extra></extra>'
)
line_done = go.Scatter(
    x=milestone_names,
    y=percent_cum_done,
    mode='lines+markers',
    name='Progresso Real (%)',
    line=dict(color='orange', width=4, dash='dot'),  # cor laranja, linha mais grossa
    marker=dict(symbol='diamond', size=10, color='orange'),
    yaxis='y2',
    hovertemplate='Sprint: %{x}<br>% Real: %{y:.2f}%<extra></extra>'
)

fig_schedule.add_traces([line_planned, line_done])
fig_schedule.update_layout(
    barmode='group',
    title='<b>Schedule & Progress por Sprint (Milestone)</b>',
    title_x=0.5,
    xaxis_title="Sprint (Milestone)",
    yaxis_title="Quantidade de Tarefas (Issues)",
    yaxis2=dict(
        title="Progresso Cumulativo (%)",
        overlaying='y',
        side='right',
        range=[0, 100]
    ),
    legend_title="Legenda",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="center",
        x=0.5
    ),
    height=700,
    width=1200,
    template="plotly_white"
)

schedule_graph_path = "docs/assets/imgs/graficos/schedule_progress_por_sprint.png"
try:
    output_dir = os.path.dirname(schedule_graph_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pio.write_image(fig_schedule, schedule_graph_path)
    print(f"Gráfico Schedule & Progress salvo em: {schedule_graph_path}")
except Exception as e:
    print(f"Erro ao salvar o gráfico Schedule & Progress: {e}")

# --- Exportação de dados de calendário e progresso ---
print("Exportando dados de calendário e progresso...")
now_str = datetime.now().strftime('%Y%m%d_%H%M%S')

csv_dir = 'data/calendario-progresso/'
os.makedirs(csv_dir, exist_ok=True)
csv_filename = f'metrica-de-calendario-progresso_{now_str}.csv'
csv_path = os.path.join(csv_dir, csv_filename)

csv_header = [
    'Sprint (Milestone)', 'Data Vencimento', 'Qt (Planejado)', 'Qf (Fechadas)', 'Tc (Taxa de Conclusão %)', 'Issues Fechadas (Nº)', 'Título Issue', 'Data Fechamento'
]

csv_rows = []
for milestone in milestones:
    milestone_title = milestone.title
    milestone_due = milestone.due_on.strftime('%Y-%m-%d') if milestone.due_on else ''
    issues_all = list(repo.get_issues(milestone=milestone, state="all"))
    issues_closed = list(repo.get_issues(milestone=milestone, state="closed"))
    Qt = len(issues_all)
    Qf = len(issues_closed)
    Tc = (Qf / Qt * 100) if Qt > 0 else 0
    for issue in issues_closed:
        csv_rows.append([
            milestone_title,
            milestone_due,
            Qt,
            Qf,
            f'{Tc:.2f}',
            issue.number,
            issue.title,
            issue.closed_at.strftime('%Y-%m-%d') if issue.closed_at else ''
        ])

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
print(f"CSV salvo em: {csv_path}")

# --- Exportação dos gráficos (mantendo histórico e versão atual) ---
grafico_dir_hist = 'docs/assets/imgs/graficos/historico/grafico-calendario-progresso/'
grafico_nome_hist = f'grafico-calendario-progresso_{now_str}.png'
grafico_path_hist = os.path.join(grafico_dir_hist, grafico_nome_hist)
os.makedirs(grafico_dir_hist, exist_ok=True)

grafico_dir_atual = 'docs/assets/imgs/graficos/'
grafico_nome_atual = 'grafico-calendario-progresso.png'
grafico_path_atual = os.path.join(grafico_dir_atual, grafico_nome_atual)
os.makedirs(grafico_dir_atual, exist_ok=True)

for path in [grafico_path_hist, grafico_path_atual]:
    try:
        pio.write_image(fig_schedule, path)
        print(f"Gráfico salvo em: {path}")
    except Exception as e:
        print(f"Erro ao salvar o gráfico: {e}")