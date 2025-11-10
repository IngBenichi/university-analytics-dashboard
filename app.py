import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración general
st.set_page_config(
    page_title="University Analytics Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric label {
        color: #31333F !important;
        font-weight: 600 !important;
    }
    .stMetric .css-1xarl3l {
        color: #0e1117 !important;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #0e1117 !important;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
    }
    .stMetric [data-testid="stMetricDelta"] {
        font-weight: 500 !important;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("university_student_data.csv")
    df["Retention Rate (%)"] = df["Retention Rate (%)"].astype(float)
    df["Student Satisfaction (%)"] = df["Student Satisfaction (%)"].astype(float)
    return df


df = load_data()

# Calcular métricas totales por departamento
df["Total Enrolled"] = (
    df["Engineering Enrolled"]
    + df["Business Enrolled"]
    + df["Arts Enrolled"]
    + df["Science Enrolled"]
)

# --- SIDEBAR: Filtros Avanzados ---
st.sidebar.header("🔍 Filtros de Análisis")
st.sidebar.markdown("---")

# Filtro por Año (Multi-select)
years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect(
    "📅 Selecciona Año(s)",
    options=years,
    default=years,
    help="Puedes seleccionar múltiples años para comparar",
)

# Filtro por Semestre
terms = ["All"] + sorted(df["Term"].unique())
selected_term = st.sidebar.selectbox(
    "📚 Selecciona Semestre",
    options=terms,
    help="Filtra por Fall, Spring o muestra ambos",
)

# Filtro por Departamento
departments = st.sidebar.multiselect(
    "🏛️ Departamentos de Interés",
    options=["Engineering", "Business", "Arts", "Science"],
    default=["Engineering", "Business", "Arts", "Science"],
    help="Selecciona los departamentos a visualizar",
)

# Rango de Retención
st.sidebar.markdown("### 📊 Rango de Retención (%)")
retention_range = st.sidebar.slider(
    "Filtrar por tasa de retención",
    min_value=float(df["Retention Rate (%)"].min()),
    max_value=float(df["Retention Rate (%)"].max()),
    value=(
        float(df["Retention Rate (%)"].min()),
        float(df["Retention Rate (%)"].max()),
    ),
    step=0.5,
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Tip:** Usa los filtros para explorar diferentes segmentos de datos"
)

# --- Aplicar Filtros ---
filtered_df = df.copy()

if selected_years:
    filtered_df = filtered_df[filtered_df["Year"].isin(selected_years)]

if selected_term != "All":
    filtered_df = filtered_df[filtered_df["Term"] == selected_term]

filtered_df = filtered_df[
    (filtered_df["Retention Rate (%)"] >= retention_range[0])
    & (filtered_df["Retention Rate (%)"] <= retention_range[1])
]

# --- HEADER ---
st.title("🎓 University Analytics Dashboard")
st.markdown(
    """
    <div style='text-align: center; padding: 10px; background-color: #e8f4f8; border-radius: 10px; margin-bottom: 20px;'>
        <p style='font-size: 18px; color: #1f77b4; margin: 0;'>
            📊 Explora métricas clave de admisión, retención y satisfacción estudiantil de forma interactiva
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Mostrar número de registros filtrados
col_info1, col_info2, col_info3 = st.columns([1, 1, 1])
with col_info2:
    st.info(f"📋 Mostrando **{len(filtered_df)}** de **{len(df)}** registros")

# --- KPIs CON DELTAS ---
st.markdown("### 📈 Indicadores Clave de Rendimiento")

# Calcular métricas actuales y previas para comparación
current_metrics = {
    "applications": int(filtered_df["Applications"].sum()),
    "retention": filtered_df["Retention Rate (%)"].mean(),
    "satisfaction": filtered_df["Student Satisfaction (%)"].mean(),
    "enrolled": int(filtered_df["Total Enrolled"].sum()),
}

# Calcular deltas (comparación con el promedio general)
all_metrics = {
    "applications": int(df["Applications"].sum() / len(df) * len(filtered_df)),
    "retention": df["Retention Rate (%)"].mean(),
    "satisfaction": df["Student Satisfaction (%)"].mean(),
    "enrolled": int(df["Total Enrolled"].sum() / len(df) * len(filtered_df)),
}

col1, col2, col3, col4 = st.columns(4)

with col1:
    delta_app = current_metrics["applications"] - all_metrics["applications"]
    st.metric(
        "📝 Total Solicitudes",
        f"{current_metrics['applications']:,}",
        delta=f"{delta_app:+,}",
        help="Total de solicitudes de admisión en el período seleccionado",
    )

with col2:
    delta_ret = current_metrics["retention"] - all_metrics["retention"]
    st.metric(
        "🎯 Retención Promedio",
        f"{current_metrics['retention']:.1f}%",
        delta=f"{delta_ret:+.1f}%",
        help="Tasa promedio de retención estudiantil",
    )

with col3:
    delta_sat = current_metrics["satisfaction"] - all_metrics["satisfaction"]
    st.metric(
        "😊 Satisfacción Promedio",
        f"{current_metrics['satisfaction']:.1f}%",
        delta=f"{delta_sat:+.1f}%",
        help="Nivel promedio de satisfacción estudiantil",
    )

with col4:
    delta_enr = current_metrics["enrolled"] - all_metrics["enrolled"]
    st.metric(
        "👥 Total Matriculados",
        f"{current_metrics['enrolled']:,}",
        delta=f"{delta_enr:+,}",
        help="Total de estudiantes matriculados",
    )

st.markdown("---")

# --- TABS PARA ORGANIZAR CONTENIDO ---
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Análisis Temporal",
        "🏛️ Departamentos",
        "📈 Correlaciones",
        "📋 Datos Detallados",
    ]
)

# ===== TAB 1: ANÁLISIS TEMPORAL =====
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📉 Tendencias de Retención")

        # Gráfico interactivo de líneas con Plotly
        fig_retention = px.line(
            filtered_df,
            x="Year",
            y="Retention Rate (%)",
            color="Term",
            markers=True,
            title="Evolución de la Tasa de Retención",
            labels={"Retention Rate (%)": "Tasa de Retención (%)", "Year": "Año"},
            color_discrete_map={"Fall": "#ff7f0e", "Spring": "#2ca02c"},
        )
        fig_retention.update_traces(line=dict(width=3), marker=dict(size=10))
        fig_retention.update_layout(
            hovermode="x unified",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_retention, use_container_width=True)

    with col2:
        st.subheader("😊 Satisfacción Estudiantil")

        # Gráfico de barras interactivo
        fig_satisfaction = px.bar(
            filtered_df,
            x="Year",
            y="Student Satisfaction (%)",
            color="Term",
            barmode="group",
            title="Niveles de Satisfacción por Año",
            labels={"Student Satisfaction (%)": "Satisfacción (%)", "Year": "Año"},
            color_discrete_map={"Fall": "#1f77b4", "Spring": "#17becf"},
        )
        fig_satisfaction.update_layout(
            hovermode="x unified",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_satisfaction, use_container_width=True)

    # Gráfico de área para solicitudes
    st.subheader("📝 Tendencias de Solicitudes")
    fig_applications = px.area(
        filtered_df,
        x="Year",
        y="Applications",
        color="Term",
        title="Evolución del Número de Solicitudes",
        labels={"Applications": "Solicitudes", "Year": "Año"},
    )
    fig_applications.update_layout(
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_applications, use_container_width=True)

# ===== TAB 2: ANÁLISIS POR DEPARTAMENTOS =====
with tab2:
    # Preparar datos de departamentos
    dept_cols = {
        "Engineering": "Engineering Enrolled",
        "Business": "Business Enrolled",
        "Arts": "Arts Enrolled",
        "Science": "Science Enrolled",
    }

    # Filtrar solo los departamentos seleccionados
    dept_data = {
        dept: filtered_df[col].sum()
        for dept, col in dept_cols.items()
        if dept in departments
    }

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🥧 Distribución por Departamento")

        # Gráfico de pastel interactivo
        if dept_data:
            fig_pie = go.Figure(
                data=[
                    go.Pie(
                        labels=list(dept_data.keys()),
                        values=list(dept_data.values()),
                        hole=0.4,
                        marker=dict(
                            colors=["#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
                        ),
                        textinfo="label+percent",
                        textfont=dict(size=14),
                        hovertemplate="<b>%{label}</b><br>Estudiantes: %{value}<br>Porcentaje: %{percent}<extra></extra>",
                    )
                ]
            )
            fig_pie.update_layout(
                title="Estudiantes Matriculados por Departamento",
                showlegend=True,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.warning("⚠️ Selecciona al menos un departamento en los filtros")

    with col2:
        st.subheader("📊 Comparativa de Departamentos")

        # Gráfico de barras comparativo
        if dept_data:
            fig_bar = go.Figure(
                data=[
                    go.Bar(
                        x=list(dept_data.keys()),
                        y=list(dept_data.values()),
                        marker=dict(
                            color=list(dept_data.values()),
                            colorscale="Viridis",
                            showscale=True,
                            colorbar=dict(title="Estudiantes"),
                        ),
                        text=list(dept_data.values()),
                        textposition="auto",
                        hovertemplate="<b>%{x}</b><br>Estudiantes: %{y}<extra></extra>",
                    )
                ]
            )
            fig_bar.update_layout(
                title="Total de Estudiantes por Departamento",
                xaxis_title="Departamento",
                yaxis_title="Número de Estudiantes",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    # Tendencias por departamento a lo largo del tiempo
    st.subheader("📈 Evolución por Departamento")

    # Crear DataFrame long format para plotly
    dept_evolution = []
    for dept in departments:
        col_name = dept_cols.get(dept)
        if col_name:
            temp_df = filtered_df[["Year", col_name]].copy()
            temp_df["Department"] = dept
            temp_df.rename(columns={col_name: "Enrolled"}, inplace=True)
            dept_evolution.append(temp_df)

    if dept_evolution:
        dept_evolution_df = pd.concat(dept_evolution, ignore_index=True)

        fig_evolution = px.line(
            dept_evolution_df,
            x="Year",
            y="Enrolled",
            color="Department",
            markers=True,
            title="Tendencias de Matrícula por Departamento",
            labels={"Enrolled": "Estudiantes Matriculados", "Year": "Año"},
        )
        fig_evolution.update_traces(line=dict(width=3), marker=dict(size=8))
        fig_evolution.update_layout(
            hovermode="x unified",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_evolution, use_container_width=True)

# ===== TAB 3: ANÁLISIS DE CORRELACIONES =====
with tab3:
    st.subheader("🔗 Análisis de Correlaciones")

    col1, col2 = st.columns(2)

    with col1:
        # Scatter plot: Retención vs Satisfacción
        fig_scatter1 = px.scatter(
            filtered_df,
            x="Retention Rate (%)",
            y="Student Satisfaction (%)",
            color="Term",
            size="Applications",
            hover_data=["Year"],
            title="Relación: Retención vs Satisfacción",
            labels={
                "Retention Rate (%)": "Tasa de Retención (%)",
                "Student Satisfaction (%)": "Satisfacción (%)",
            },
            trendline="ols",
        )
        fig_scatter1.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_scatter1, use_container_width=True)

    with col2:
        # Scatter plot: Aplicaciones vs Matriculados
        fig_scatter2 = px.scatter(
            filtered_df,
            x="Applications",
            y="Total Enrolled",
            color="Year",
            size="Student Satisfaction (%)",
            hover_data=["Term", "Retention Rate (%)"],
            title="Relación: Solicitudes vs Matriculados",
            labels={
                "Applications": "Solicitudes",
                "Total Enrolled": "Total Matriculados",
            },
            trendline="ols",
        )
        fig_scatter2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_scatter2, use_container_width=True)

    # Matriz de correlación
    st.subheader("🔢 Matriz de Correlación")

    numeric_cols = [
        "Applications",
        "Retention Rate (%)",
        "Student Satisfaction (%)",
        "Engineering Enrolled",
        "Business Enrolled",
        "Arts Enrolled",
        "Science Enrolled",
    ]
    corr_matrix = filtered_df[numeric_cols].corr()

    fig_heatmap = px.imshow(
        corr_matrix,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Correlación entre Variables",
        labels=dict(color="Correlación"),
    )
    fig_heatmap.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

# ===== TAB 4: DATOS DETALLADOS =====
with tab4:
    st.subheader("📋 Tabla de Datos Filtrados")

    # Opciones de visualización
    col1, col2, col3 = st.columns(3)

    with col1:
        show_rows = st.number_input(
            "Filas a mostrar",
            min_value=1,
            max_value=len(filtered_df) if len(filtered_df) > 0 else 100,
            value=min(10, len(filtered_df)) if len(filtered_df) > 0 else 10,
        )

    with col2:
        sort_column = st.selectbox("Ordenar por", options=filtered_df.columns)

    with col3:
        sort_order = st.radio(
            "Orden", options=["Ascendente", "Descendente"], horizontal=True
        )

    # Ordenar datos
    ascending = sort_order == "Ascendente"
    display_df = filtered_df.sort_values(by=sort_column, ascending=ascending).head(
        int(show_rows)
    )

    # Mostrar tabla con estilo
    st.dataframe(
        display_df.style.background_gradient(
            cmap="Blues", subset=["Retention Rate (%)", "Student Satisfaction (%)"]
        ),
        use_container_width=True,
        height=400,
    )

    # Estadísticas descriptivas
    with st.expander("📊 Ver Estadísticas Descriptivas"):
        st.write(filtered_df.describe())

    # Descargar datos
    st.markdown("### 💾 Descargar Datos")
    col1, col2 = st.columns(2)

    with col1:
        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Descargar como CSV",
            data=csv,
            file_name="university_data_filtered.csv",
            mime="text/csv",
            help="Descarga los datos filtrados en formato CSV",
        )

    with col2:
        excel_buffer = pd.ExcelWriter("temp.xlsx", engine="openpyxl")
        filtered_df.to_excel(excel_buffer, index=False)
        excel_buffer.close()

# --- FOOTER ---
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>🎓 <strong>University Analytics Dashboard</strong> | Developed for Data Analytics Project</p>
            <p style='font-size: 14px; margin-top: 10px;'><strong>Integrantes:</strong></p>
            <p style='font-size: 13px;'>👨‍💻 Camilo Benitez | 👨‍💻 Mateo Baca</p>
            <p style='font-size: 12px; margin-top: 10px;'>Última actualización: Noviembre 2025</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
