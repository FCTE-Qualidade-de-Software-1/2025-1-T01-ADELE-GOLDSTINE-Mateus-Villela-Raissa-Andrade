import os
import plotly.graph_objects as go
import plotly.io as pio
from github import Github, GithubException
from datetime import datetime, timedelta
from collections import defaultdict
import numpy as np
import csv

# --- Configurações do repositório e token ---
GITHUB_TOKEN = os.getenv('GH_TOKEN')  # Token do GitHub via variável de ambiente
REPO_OWNER = "FCTE-Qualidade-de-Software-1"  # Substitua pelo dono do repositório
REPO_NAME = "2025-1-T01-ADELE-GOLDSTINE-Mateus-Villela-Raissa-Andrade"  # Substitua pelo nome do repositório

# Configurações de análise
CONSIDER_WORK_DAYS_ONLY = False  # Considerar apenas dias úteis
EXCLUDE_WEEKENDS = False  # Excluir fins de semana do cálculo
MIN_EFFORT_THRESHOLD = 0.01  # Mínimo de dias para considerar esforço válido

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

def calcular_dias_uteis(data_inicio, data_fim):
    """Calcula apenas dias úteis entre duas datas, excluindo fins de semana"""
    if not data_inicio or not data_fim:
        return 0
    
    if EXCLUDE_WEEKENDS:
        dias_totais = (data_fim - data_inicio).days
        semanas_completas = dias_totais // 7
        dias_restantes = dias_totais % 7
        
        # Contar dias úteis nas semanas completas (5 dias por semana)
        dias_uteis = semanas_completas * 5
        
        # Verificar dias restantes
        data_atual = data_inicio + timedelta(days=semanas_completas * 7)
        for i in range(dias_restantes):
            if (data_atual + timedelta(days=i)).weekday() < 5:  # 0-4 = segunda a sexta
                dias_uteis += 1
        
        return max(dias_uteis, 0.1)  # Mínimo de 0.1 dia
    else:
        return max((data_fim - data_inicio).total_seconds() / (3600 * 24), 0.1)

def calcular_esforco_proporcional(issue, colaboradores_count):
    """Calcula esforço proporcional quando há múltiplos assignees"""
    if issue.state == "closed" and issue.closed_at and issue.created_at:
        tempo_total = calcular_dias_uteis(issue.created_at, issue.closed_at)
        # Dividir esforço proporcionalmente entre colaboradores
        return tempo_total / max(colaboradores_count, 1)
    return 0

print("Iniciando análise de recursos e custos...")
now_str = datetime.now().strftime('%Y%m%d_%H%M%S')

# --- Coletando dados de todas as issues ---
all_issues = list(repo.get_issues(state="all"))
closed_issues = [issue for issue in all_issues if issue.state == "closed"]
milestones = list(repo.get_milestones(state="all"))

# Estruturas de dados para análise
colaborador_data = defaultdict(lambda: {
    'issues_atribuidas': 0,
    'issues_concluidas': 0,
    'esforco_total': 0.0,
    'issues_detalhes': [],
    'milestones': set(),
    'issues_em_andamento': 0,
    'tempo_medio_resolucao': 0.0
})

milestone_data = defaultdict(lambda: {
    'issues_totais': 0,
    'issues_fechadas': 0,
    'esforco_total': 0.0,
    'colaboradores': set()
})

print(f"Analisando {len(all_issues)} issues totais ({len(closed_issues)} fechadas) em {len(milestones)} milestones...")

# --- Processamento das issues ---
for issue in all_issues:
    milestone_name = issue.milestone.title if issue.milestone else "Sem milestone"
    assignees_count = len(issue.assignees) if issue.assignees else 1
    
    # Calcular esforço proporcional
    esforco_issue = calcular_esforco_proporcional(issue, assignees_count)
    
    # Atualizar dados da milestone
    milestone_data[milestone_name]['issues_totais'] += 1
    if issue.state == "closed":
        milestone_data[milestone_name]['issues_fechadas'] += 1
        milestone_data[milestone_name]['esforco_total'] += esforco_issue
    
    # Análise por colaborador
    if issue.assignees:
        for assignee in issue.assignees:
            colaborador_login = assignee.login
            
            # Dados básicos
            colaborador_data[colaborador_login]['issues_atribuidas'] += 1
            colaborador_data[colaborador_login]['milestones'].add(milestone_name)
            milestone_data[milestone_name]['colaboradores'].add(colaborador_login)
            
            # Detalhes da issue
            issue_detail = {
                'number': issue.number,
                'title': issue.title,
                'state': issue.state,
                'milestone': milestone_name,
                'esforco_dias': esforco_issue,
                'created_at': issue.created_at,
                'closed_at': issue.closed_at,
                'assignees_count': assignees_count
            }
            colaborador_data[colaborador_login]['issues_detalhes'].append(issue_detail)
            
            if issue.state == "closed":
                colaborador_data[colaborador_login]['issues_concluidas'] += 1
                colaborador_data[colaborador_login]['esforco_total'] += esforco_issue
            else:
                colaborador_data[colaborador_login]['issues_em_andamento'] += 1
    else:
        # Issues sem assignee - tratamento especial
        colaborador_data["Sem assignee"]['issues_atribuidas'] += 1
        colaborador_data["Sem assignee"]['milestones'].add(milestone_name)
        
        issue_detail = {
            'number': issue.number,
            'title': issue.title,
            'state': issue.state,
            'milestone': milestone_name,
            'esforco_dias': esforco_issue,
            'created_at': issue.created_at,
            'closed_at': issue.closed_at,
            'assignees_count': 0
        }
        colaborador_data["Sem assignee"]['issues_detalhes'].append(issue_detail)
        
        if issue.state == "closed":
            colaborador_data["Sem assignee"]['issues_concluidas'] += 1
            colaborador_data["Sem assignee"]['esforco_total'] += esforco_issue

# --- Cálculo de métricas derivadas ---
colaboradores = list(colaborador_data.keys())
for colaborador in colaboradores:
    data = colaborador_data[colaborador]
    
    # Tempo médio de resolução
    if data['issues_concluidas'] > 0:
        data['tempo_medio_resolucao'] = data['esforco_total'] / data['issues_concluidas']
    
    # Eficiência de alocação (issues por dia de esforço)
    if data['esforco_total'] > MIN_EFFORT_THRESHOLD:
        data['eficiencia_alocacao'] = data['issues_concluidas'] / data['esforco_total']
    else:
        data['eficiencia_alocacao'] = 0
    
    # Taxa de conclusão
    if data['issues_atribuidas'] > 0:
        data['taxa_conclusao'] = (data['issues_concluidas'] / data['issues_atribuidas']) * 100
    else:
        data['taxa_conclusao'] = 0
    
    # Produtividade (issues concluídas por milestone)
    data['produtividade_milestone'] = data['issues_concluidas'] / len(data['milestones']) if data['milestones'] else 0

print(f"Colaboradores analisados: {len(colaboradores)}")

# --- Geração do CSV detalhado ---
csv_dir = 'data/recurso-custo/'
os.makedirs(csv_dir, exist_ok=True)
csv_filename = f'metrica-de-recurso-custo_{now_str}.csv'
csv_path = os.path.join(csv_dir, csv_filename)

csv_header = [
    'Colaborador', 'Issues Atribuídas', 'Issues Concluídas', 'Issues em Andamento',
    'Esforço Total (dias úteis)', 'Tempo Médio Resolução (dias)', 
    'Eficiência (issues/dia)', 'Taxa de Conclusão (%)', 
    'Milestones Envolvidas', 'Produtividade por Milestone'
]
csv_rows = []

# Dados por colaborador
for colaborador in colaboradores:
    data = colaborador_data[colaborador]
    
    csv_rows.append([
        colaborador,
        data['issues_atribuidas'],
        data['issues_concluidas'],
        data['issues_em_andamento'],
        round(data['esforco_total'], 2),
        round(data['tempo_medio_resolucao'], 2),
        round(data['eficiencia_alocacao'], 4),
        round(data['taxa_conclusao'], 2),
        len(data['milestones']),
        round(data['produtividade_milestone'], 2)
    ])

# Resumo geral
total_issues_atribuidas = sum(data['issues_atribuidas'] for data in colaborador_data.values())
total_issues_concluidas = sum(data['issues_concluidas'] for data in colaborador_data.values())
total_esforco = sum(data['esforco_total'] for data in colaborador_data.values())
total_em_andamento = sum(data['issues_em_andamento'] for data in colaborador_data.values())

csv_rows.append(['', '', '', '', '', '', '', '', '', ''])  # Linha em branco
csv_rows.append([
    'RESUMO GERAL',
    total_issues_atribuidas,
    total_issues_concluidas,
    total_em_andamento,
    round(total_esforco, 2),
    round(total_esforco / total_issues_concluidas if total_issues_concluidas > 0 else 0, 2),
    round(total_issues_concluidas / total_esforco if total_esforco > 0 else 0, 4),
    round((total_issues_concluidas / total_issues_atribuidas * 100) if total_issues_atribuidas > 0 else 0, 2),
    len(milestones),
    round(total_issues_concluidas / len(milestones) if milestones else 0, 2)
])

# Adicionar seção de milestones
csv_rows.append(['', '', '', '', '', '', '', '', '', ''])
csv_rows.append(['ANÁLISE POR MILESTONE', '', '', '', '', '', '', '', '', ''])
csv_rows.append(['Milestone', 'Issues Totais', 'Issues Fechadas', 'Taxa Conclusão (%)', 
                'Esforço Total (dias)', 'Esforço Médio (dias)', 'Colaboradores Envolvidos', '', '', ''])

for milestone_name, milestone_info in milestone_data.items():
    taxa_milestone = (milestone_info['issues_fechadas'] / milestone_info['issues_totais'] * 100) if milestone_info['issues_totais'] > 0 else 0
    esforco_medio_milestone = milestone_info['esforco_total'] / milestone_info['issues_fechadas'] if milestone_info['issues_fechadas'] > 0 else 0
    
    csv_rows.append([
        milestone_name,
        milestone_info['issues_totais'],
        milestone_info['issues_fechadas'],
        round(taxa_milestone, 2),
        round(milestone_info['esforco_total'], 2),
        round(esforco_medio_milestone, 2),
        len(milestone_info['colaboradores']),
        '', '', ''
    ])

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
print(f"CSV de recursos e custos salvo em: {csv_path}")

# --- Preparação dos dados para visualização ---
issues_atribuidas = [colaborador_data[col]['issues_atribuidas'] for col in colaboradores]
issues_concluidas = [colaborador_data[col]['issues_concluidas'] for col in colaboradores]
issues_em_andamento = [colaborador_data[col]['issues_em_andamento'] for col in colaboradores]
eficiencia_alocacao = [colaborador_data[col]['eficiencia_alocacao'] for col in colaboradores]
tempo_medio = [colaborador_data[col]['tempo_medio_resolucao'] for col in colaboradores]

# --- Gráfico Principal: Painel de Recursos e Custos Aprimorado ---
fig = go.Figure()

# Barras empilhadas: Issues concluídas vs em andamento
fig.add_trace(go.Bar(
    x=colaboradores,
    y=issues_concluidas,
    name='Issues Concluídas',
    marker_color='seagreen',
    hovertemplate='<b>%{x}</b><br>Issues Concluídas: %{y}<br><extra></extra>'
))

fig.add_trace(go.Bar(
    x=colaboradores,
    y=issues_em_andamento,
    name='Issues em Andamento',
    marker_color='orange',
    hovertemplate='<b>%{x}</b><br>Issues em Andamento: %{y}<br><extra></extra>'
))

# Linha: Eficiência de alocação
fig.add_trace(go.Scatter(
    x=colaboradores,
    y=eficiencia_alocacao,
    mode='lines+markers',
    name='Eficiência (issues/dia útil)',
    line=dict(color='crimson', width=3),
    marker=dict(symbol='circle', size=10, color='crimson'),
    yaxis='y2',
    hovertemplate='<b>%{x}</b><br>Eficiência: %{y:.4f} issues/dia<br><extra></extra>'
))

# Linha: Tempo médio de resolução
fig.add_trace(go.Scatter(
    x=colaboradores,
    y=tempo_medio,
    mode='lines+markers',
    name='Tempo Médio Resolução (dias)',
    line=dict(color='purple', width=2, dash='dash'),
    marker=dict(symbol='diamond', size=8, color='purple'),
    yaxis='y3',
    hovertemplate='<b>%{x}</b><br>Tempo Médio: %{y:.2f} dias<br><extra></extra>'
))

# Configurar layout com múltiplos eixos Y
fig.update_layout(
    barmode='stack',
    title='<b>Painel de Recursos e Custos - Análise Detalhada por Colaborador</b>',
    title_x=0.5,
    xaxis_title="Colaborador",
    yaxis_title="Número de Issues",
    yaxis2=dict(
        title="Eficiência (issues/dia útil)",
        overlaying='y',
        side='right',
        position=1.0,
        range=[0, max(eficiencia_alocacao) * 1.2] if eficiencia_alocacao else [0, 1]
    ),
    yaxis3=dict(
        title="Tempo Médio (dias)",
        overlaying='y',
        side='right',
        position=0.91,
        range=[0, max(tempo_medio) * 1.2] if tempo_medio else [0, 1]
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

# --- Criação dos diretórios e exportação do gráfico ---
grafico_dir_hist = 'docs/assets/imgs/graficos/historico/grafico-recurso-custo/'
grafico_nome_hist = f'grafico-recurso-custo_{now_str}.png'
grafico_path_hist = os.path.join(grafico_dir_hist, grafico_nome_hist)
os.makedirs(grafico_dir_hist, exist_ok=True)

grafico_dir_atual = 'docs/assets/imgs/graficos/'
grafico_nome_atual = 'grafico-recurso-custo.png'
grafico_path_atual = os.path.join(grafico_dir_atual, grafico_nome_atual)
os.makedirs(grafico_dir_atual, exist_ok=True)

# Salvar gráfico principal
for path in [grafico_path_hist, grafico_path_atual]:
    try:
        pio.write_image(fig, path)
        print(f"Gráfico de recursos e custos salvo em: {path}")
    except Exception as e:
        print(f"Erro ao salvar o gráfico: {e}")

# --- Relatório de insights ---
print("\n" + "="*60)
print("📊 RELATÓRIO DE INSIGHTS - RECURSOS E CUSTOS")
print("="*60)

# Top performers
colaboradores_ordenados = sorted(colaboradores, key=lambda x: colaborador_data[x]['eficiencia_alocacao'], reverse=True)
print(f"\n🏆 TOP 3 COLABORADORES MAIS EFICIENTES:")
for i, col in enumerate(colaboradores_ordenados[:3]):
    data = colaborador_data[col]
    print(f"   {i+1}. {col}: {data['eficiencia_alocacao']:.4f} issues/dia ({data['issues_concluidas']} issues concluídas)")

# Colaboradores com maior carga
colaboradores_carga = sorted(colaboradores, key=lambda x: colaborador_data[x]['issues_em_andamento'], reverse=True)
print(f"\n⚠️  COLABORADORES COM MAIOR CARGA ATUAL:")
for i, col in enumerate(colaboradores_carga[:3]):
    data = colaborador_data[col]
    if data['issues_em_andamento'] > 0:
        print(f"   {i+1}. {col}: {data['issues_em_andamento']} issues em andamento")

# Estatísticas gerais
eficiencia_media = np.mean([data['eficiencia_alocacao'] for data in colaborador_data.values()])
tempo_medio_geral = np.mean([data['tempo_medio_resolucao'] for data in colaborador_data.values() if data['tempo_medio_resolucao'] > 0])

print(f"\n📈 ESTATÍSTICAS GERAIS:")
print(f"   • Eficiência média da equipe: {eficiencia_media:.4f} issues/dia")
print(f"   • Tempo médio de resolução: {tempo_medio_geral:.2f} dias")
print(f"   • Taxa de conclusão geral: {(total_issues_concluidas/total_issues_atribuidas*100):.1f}%")
print(f"   • Issues em andamento: {total_em_andamento}")

print("\n✅ Análise de recursos e custos concluída!")
print(f"📊 Gráfico gerado: {grafico_nome_atual}")
print(f"📈 CSV gerado: {csv_filename}")
print("="*60)