# 🎓 University Analytics Dashboard

## Descripción del Proyecto

**University Analytics Dashboard** es una aplicación web interactiva desarrollada con Streamlit que permite visualizar y analizar métricas clave de admisión, retención y satisfacción estudiantil de una universidad. Este dashboard proporciona herramientas de análisis visual para la toma de decisiones basadas en datos.

## Características Principales

### 🎯 Dashboard Interactivo Avanzado
- **Sidebar con Filtros Múltiples**: Multi-selección de años, semestres, departamentos y rangos personalizados
- **Sistema de Tabs Organizado**: 4 pestañas especializadas para diferentes tipos de análisis
- **KPIs Dinámicos con Comparaciones**: Indicadores con deltas automáticos que muestran cambios
- **Gráficos Interactivos Plotly**: Visualizaciones con zoom, hover, pan y líneas de tendencia
- **Descarga de Datos**: Exportación en CSV y Excel de datos filtrados
- **Diseño Responsive**: Optimizado para diferentes tamaños de pantalla

### � Análisis por Pestañas

#### 1️⃣ Análisis Temporal
- Tendencias de retención con gráficos de línea interactivos
- Niveles de satisfacción estudiantil por año con barras agrupadas
- Evolución de solicitudes con gráficos de área

#### 2️⃣ Análisis por Departamentos
- Distribución con gráfico de dona (donut chart)
- Comparativa de departamentos con barras coloreadas
- Evolución temporal de matrícula por departamento

#### 3️⃣ Análisis de Correlaciones
- Scatter plots con líneas de tendencia OLS
- Relación Retención vs Satisfacción
- Relación Solicitudes vs Matriculados
- Matriz de correlación (heatmap) interactiva

#### 4️⃣ Datos Detallados
- Tabla interactiva con ordenamiento dinámico
- Coloreado condicional de métricas clave
- Estadísticas descriptivas expandibles
- Botones de descarga en múltiples formatos

### 📈 Métricas Analizadas
1. **📝 Total Solicitudes**: Número total de aplicaciones de admisión
2. **🎯 Retención Promedio**: Tasa de retención estudiantil (%)
3. **😊 Satisfacción Promedio**: Nivel de satisfacción estudiantil (%)
4. **👥 Total Matriculados**: Suma de estudiantes en todos los departamentos
5. **🏛️ Distribución por Departamento**:
   - Engineering (Ingeniería)
   - Business (Negocios)
   - Arts (Artes)
   - Science (Ciencias)

## Requisitos del Sistema

### Dependencias
```
streamlit
pandas
matplotlib
seaborn
plotly
openpyxl
statsmodels
scikit-learn
```

### Requisitos de Datos
El proyecto requiere un archivo CSV llamado `university_student_data.csv` con las siguientes columnas:
- `Year`: Año académico
- `Term`: Semestre (Fall/Spring)
- `Applications`: Número de solicitudes
- `Retention Rate (%)`: Tasa de retención
- `Student Satisfaction (%)`: Nivel de satisfacción
- `Engineering Enrolled`: Estudiantes en Ingeniería
- `Business Enrolled`: Estudiantes en Negocios
- `Arts Enrolled`: Estudiantes en Artes
- `Science Enrolled`: Estudiantes en Ciencias

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/IngBenichi/university-analytics-dashboard.git
cd university-analytics-dashboard
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Preparar los Datos
Asegúrate de tener el archivo `university_student_data.csv` en el directorio raíz del proyecto.

## Uso

### Ejecutar la Aplicación

**Opción 1** (recomendada si tienes problemas con PATH):
```bash
python -m streamlit run app.py
```

**Opción 2** (si streamlit está en PATH):
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Guía de Uso del Dashboard

#### 🔍 Sidebar - Panel de Filtros
1. **Selección de Años**: Multi-selecciona uno o varios años para análisis comparativo
2. **Filtro de Semestre**: Elige Fall, Spring o ambos
3. **Departamentos de Interés**: Selecciona qué departamentos visualizar
4. **Rango de Retención**: Ajusta el slider para filtrar por tasa de retención específica

#### 📊 Indicadores Clave (KPIs)
- Visualiza 4 métricas principales en tiempo real
- Los **números en verde/rojo** indican cambios positivos o negativos
- Cada métrica incluye tooltip informativo al pasar el mouse

#### 📑 Sistema de Tabs
- **Tab 1 - Análisis Temporal**: Visualiza tendencias históricas
- **Tab 2 - Departamentos**: Analiza distribución y evolución por área
- **Tab 3 - Correlaciones**: Explora relaciones entre variables
- **Tab 4 - Datos Detallados**: Tabla interactiva con opciones de descarga

#### 💡 Interactividad en Gráficos
- **Hover**: Pasa el mouse sobre los gráficos para ver valores exactos
- **Zoom**: Haz clic y arrastra para hacer zoom en áreas específicas
- **Pan**: Usa el modo "pan" para moverte por el gráfico
- **Reset**: Doble clic para restablecer la vista original
- **Descargar**: Botón de cámara para guardar gráficos como imágenes

## Estructura del Proyecto

```
university-analytics-dashboard/
│
├── app.py                          # Aplicación principal de Streamlit
├── requirements.txt                # Dependencias del proyecto
├── university_student_data.csv     # Datos fuente (CSV)
└── README.md                       # Documentación
```

## Arquitectura del Código

### `app.py` - Componentes Principales

```python
# 1. Configuración inicial
st.set_page_config(page_title, page_icon, layout, sidebar_state)

# 2. Estilos CSS personalizados
- Estilos para métricas (fondo, colores, sombras)
- Diseño responsive y tipografía

# 3. Carga de datos con caché
@st.cache_data
def load_data()
    - Lee CSV
    - Convierte tipos de datos
    - Calcula totales

# 4. Sidebar - Filtros avanzados
- Multi-select para años
- Selectbox para semestres
- Multi-select para departamentos
- Slider para rango de retención

# 5. KPIs con deltas
- Cálculo de métricas actuales vs promedio
- 4 indicadores principales con comparación

# 6. Sistema de Tabs
Tab 1: Análisis Temporal
    - Gráfico de línea (Retención)
    - Gráfico de barras (Satisfacción)
    - Gráfico de área (Solicitudes)

Tab 2: Departamentos
    - Gráfico de dona (Distribución)
    - Barras comparativas
    - Evolución temporal

Tab 3: Correlaciones
    - Scatter plots con trendlines
    - Matriz de correlación (heatmap)

Tab 4: Datos Detallados
    - Tabla interactiva con sorting
    - Estadísticas descriptivas
    - Botones de descarga (CSV/Excel)

# 7. Footer con información del equipo
```

## Funcionalidades Técnicas Avanzadas

### 🚀 Optimización de Rendimiento
- **Cache de Datos**: `@st.cache_data` para carga rápida del CSV
- **Carga Diferida**: Los gráficos se generan solo cuando se accede a cada tab
- **Filtrado Eficiente**: Operaciones optimizadas con Pandas

### 🎨 Diseño y UX
- **Layout Wide**: `layout="wide"` para aprovechar pantallas grandes
- **CSS Personalizado**: Estilos mejorados para métricas y textos
- **Sidebar Expandido**: `initial_sidebar_state="expanded"` por defecto
- **Tooltips Informativos**: Ayudas contextuales en cada elemento

### 📊 Visualizaciones Interactivas con Plotly
- **Hover Details**: Información detallada al pasar el mouse
- **Zoom & Pan**: Exploración interactiva de gráficos
- **Trendlines OLS**: Líneas de tendencia con regresión lineal
- **Export Charts**: Descarga de gráficos como imágenes PNG
- **Color Scales**: Paletas de colores profesionales

### 📈 Análisis Estadístico
- **Correlaciones**: Matriz completa de correlaciones entre variables
- **Regresión Lineal**: Análisis de tendencias con statsmodels
- **Estadísticas Descriptivas**: Media, mediana, desviación estándar, etc.

### 💾 Exportación de Datos
- **CSV**: Exportación simple y compatible
- **Excel**: Formato profesional con openpyxl
- **Filtros Aplicados**: Los archivos descargados reflejan los filtros activos

## Personalización y Extensión

### 🎨 Modificar Apariencia

#### Cambiar Colores
```python
# En el bloque CSS personalizado (línea ~15)
.stMetric {
    background-color: #tu-color;  # Cambia el fondo de las métricas
}
```

#### Ajustar Paletas de Colores en Gráficos
```python
# Ejemplo para gráficos Plotly
color_discrete_map={"Fall": "#tu-color1", "Spring": "#tu-color2"}
```

### 📊 Agregar Nuevas Visualizaciones

1. **Añade un nuevo Tab**:
```python
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tab1", "Tab2", "Tab3", "Tab4", "Nuevo Tab"])

with tab5:
    st.subheader("Tu Nueva Visualización")
    # Tu código aquí
```

2. **Crea gráficos con Plotly Express**:
```python
import plotly.express as px
fig = px.line(data, x="columna_x", y="columna_y")
st.plotly_chart(fig, use_container_width=True)
```

### 📁 Agregar Nuevas Métricas
1. Añade la columna en `university_student_data.csv`
2. Si necesita conversión de tipo, actualiza `load_data()`:
```python
df["Nueva Métrica"] = df["Nueva Métrica"].astype(float)
```
3. Crea un nuevo KPI o visualización según necesites

## Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Streamlit** | 1.51.0+ | Framework web interactivo |
| **Pandas** | Latest | Manipulación y análisis de datos |
| **Plotly** | Latest | Visualizaciones interactivas |
| **Matplotlib** | Latest | Gráficos estáticos de respaldo |
| **Seaborn** | Latest | Visualización estadística |
| **Statsmodels** | Latest | Análisis estadístico y regresión |
| **Scikit-learn** | Latest | Machine learning y análisis |
| **OpenPyXL** | Latest | Exportación a Excel |

## 🐛 Solución de Problemas

### Error: "streamlit" no se reconoce como comando
**Solución**: Usa `python -m streamlit run app.py` en lugar de `streamlit run app.py`

### Error: ModuleNotFoundError
**Solución**: Asegúrate de instalar todas las dependencias:
```bash
pip install -r requirements.txt
```

### Error: FileNotFoundError para CSV
**Solución**: Verifica que `university_student_data.csv` esté en el mismo directorio que `app.py`

### Los números en los KPIs no se ven
**Solución**: Ya está solucionado en la última versión con CSS mejorado

### Error: statsmodels no encontrado
**Solución**: Instala statsmodels:
```bash
pip install statsmodels scikit-learn
```

## 🚀 Roadmap - Futuras Mejoras

- [ ] Autenticación de usuarios
- [ ] Exportación de reportes PDF
- [ ] Predicciones con Machine Learning
- [ ] Comparación entre múltiples universidades
- [ ] API REST para integración con otros sistemas
- [ ] Dashboard en tiempo real con actualización automática
- [ ] Modo oscuro / claro seleccionable

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de Contribución
- Mantén el código limpio y bien documentado
- Sigue las convenciones de PEP 8 para Python
- Añade tests cuando sea posible
- Actualiza el README si añades nuevas funcionalidades

## Licencia

Este proyecto está desarrollado para fines educativos y de análisis universitario.

## 📸 Capturas de Pantalla

### Vista Principal
El dashboard muestra KPIs dinámicos con comparaciones en tiempo real y un sistema de tabs organizado para diferentes tipos de análisis.

### Filtros Interactivos
El sidebar permite multi-selección de años, departamentos y rangos personalizados para análisis específicos.

### Visualizaciones Avanzadas
Gráficos interactivos con Plotly que incluyen hover details, zoom, pan y líneas de tendencia estadísticas.

## 📊 Casos de Uso

1. **Análisis de Tendencias**: Identifica patrones en retención y satisfacción estudiantil
2. **Comparación de Departamentos**: Evalúa el rendimiento relativo entre áreas académicas
3. **Predicción de Matrículas**: Usa datos históricos para proyectar inscripciones futuras
4. **Reportes Ejecutivos**: Genera visualizaciones para presentaciones a stakeholders
5. **Toma de Decisiones**: Basa estrategias institucionales en datos concretos

## 🎓 Contexto Académico

Este proyecto fue desarrollado como parte de un análisis de datos universitarios, demostrando:
- Habilidades en visualización de datos interactiva
- Dominio de frameworks modernos (Streamlit, Plotly)
- Capacidad de crear dashboards profesionales
- Análisis estadístico aplicado a métricas educativas

## 📝 Licencia

Este proyecto está desarrollado para fines educativos y de análisis universitario.

## 👥 Integrantes del Proyecto

👨‍💻 **Camilo Benitez**  
👨‍💻 **Mateo Baca**

## 👤 Autor

**IngBenichi**  
**bacas07**

GitHub: [@IngBenichi](https://github.com/IngBenichi)
GitHub: [@IngBenichi](https://github.com/bacas07)
