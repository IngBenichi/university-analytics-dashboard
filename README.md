# 🎓 University Analytics Dashboard

## Descripción del Proyecto

**University Analytics Dashboard** es una aplicación web interactiva desarrollada con Streamlit que permite visualizar y analizar métricas clave de admisión, retención y satisfacción estudiantil de una universidad. Este dashboard proporciona herramientas de análisis visual para la toma de decisiones basadas en datos.

## Características Principales

### 📊 Análisis de Datos
- **Filtros Interactivos**: Permite filtrar datos por año académico y semestre
- **KPIs en Tiempo Real**: Muestra métricas clave actualizadas dinámicamente
- **Visualizaciones Múltiples**: Incluye gráficos de línea, barras y pastel

### 📈 Métricas Analizadas
1. **Applications**: Total de solicitudes de admisión
2. **Retention Rate**: Tasa de retención estudiantil (%)
3. **Student Satisfaction**: Nivel de satisfacción estudiantil (%)
4. **Department Enrollment**: Distribución de estudiantes por departamento
   - Engineering (Ingeniería)
   - Business (Negocios)
   - Arts (Artes)
   - Science (Ciencias)

### 📉 Visualizaciones

#### 1. Retention Rate Trends Over Time
Gráfico de líneas que muestra la evolución de la tasa de retención a lo largo del tiempo, diferenciado por semestre.

#### 2. Student Satisfaction by Year
Gráfico de barras que visualiza los niveles de satisfacción estudiantil por año y semestre.

#### 3. Department Enrollment Distribution
Gráfico circular que representa la distribución porcentual de estudiantes matriculados en cada departamento.

## Requisitos del Sistema

### Dependencias
```
streamlit
pandas
matplotlib
seaborn
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
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Interfaz de Usuario

1. **Filtros de Selección**: 
   - Utiliza los selectores en la parte superior para filtrar por año y semestre
   - Selecciona "All" para ver todos los datos

2. **Panel de KPIs**: 
   - Visualiza las métricas principales de forma inmediata

3. **Gráficos Interactivos**: 
   - Desplázate por los diferentes gráficos para analizar tendencias y distribuciones

## Estructura del Código

### `app.py`

```python
# Configuración de la página
st.set_page_config(page_title, page_icon, layout)

# Carga de datos con caché
@st.cache_data
def load_data()

# Filtros interactivos
- Selectores de año y semestre
- Filtrado dinámico del DataFrame

# Visualizaciones
- KPIs: Total Applications, Avg Retention Rate, Avg Satisfaction
- Gráfico de línea: Retention Rate Trends
- Gráfico de barras: Student Satisfaction
- Gráfico circular: Department Enrollment
```

## Funcionalidades Técnicas

### Cache de Datos
Utiliza `@st.cache_data` para optimizar el rendimiento al cargar datos, evitando lecturas repetidas del archivo CSV.

### Diseño Responsive
Configurado con `layout="wide"` para aprovechar mejor el espacio de pantalla en monitores grandes.

### Tipado de Datos
Conversión explícita de columnas a tipos `float` para garantizar operaciones numéricas correctas.

## Personalización

### Modificar Visualizaciones
Los gráficos se crean usando Matplotlib y Seaborn. Puedes personalizar:
- Colores: Modificar parámetros `palette` en seaborn
- Tamaño: Ajustar `figsize` en `plt.subplots()`
- Estilo: Cambiar tipos de gráficos y markers

### Agregar Nuevas Métricas
1. Añade la columna en el archivo CSV
2. Actualiza la función `load_data()` si requiere conversión de tipo
3. Crea nuevas visualizaciones con Matplotlib/Seaborn

## Tecnologías Utilizadas

- **Streamlit**: Framework para crear aplicaciones web de datos
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Biblioteca de visualización de datos
- **Seaborn**: Visualización estadística basada en Matplotlib

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está desarrollado para fines educativos y de análisis universitario.

## Integrantes del Proyecto

👨‍💻 **Camilo Benitez**  
👨‍💻 **Mateo Baca**

## Autor

**IngBenichi**