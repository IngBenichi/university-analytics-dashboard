import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración general
st.set_page_config(page_title="University Analytics Dashboard", page_icon="🎓", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("university_student_data.csv")
    df["Retention Rate (%)"] = df["Retention Rate (%)"].astype(float)
    df["Student Satisfaction (%)"] = df["Student Satisfaction (%)"].astype(float)
    return df

df = load_data()

# Título
st.title("🎓 University Analytics Dashboard")
st.markdown("Explora métricas clave de admisión, retención y satisfacción estudiantil.")

# --- Filtros interactivos ---
years = sorted(df["Year"].unique())
terms = sorted(df["Term"].unique())

col1, col2 = st.columns(2)
selected_year = col1.selectbox("Select Year", options=["All"] + list(map(str, years)))
selected_term = col2.selectbox("Select Term", options=["All"] + terms)

# --- Filtrado dinámico ---
filtered_df = df.copy()
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == int(selected_year)]
if selected_term != "All":
    filtered_df = filtered_df[filtered_df["Term"] == selected_term]

# --- KPIs ---
st.subheader("📈 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", int(filtered_df["Applications"].sum()))
col2.metric("Avg Retention Rate", f"{filtered_df['Retention Rate (%)'].mean():.1f}%")
col3.metric("Avg Satisfaction", f"{filtered_df['Student Satisfaction (%)'].mean():.1f}%")

# --- Gráfico 1: Retention Rate Over Time ---
st.subheader("Retention Rate Trends Over Time")
fig1, ax1 = plt.subplots(figsize=(8,4))
sns.lineplot(data=df, x="Year", y="Retention Rate (%)", hue="Term", marker="o", ax=ax1)
ax1.set_ylabel("Retention Rate (%)")
st.pyplot(fig1)

# --- Gráfico 2: Satisfaction by Year ---
st.subheader("Student Satisfaction by Year")
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.barplot(data=df, x="Year", y="Student Satisfaction (%)", hue="Term", ax=ax2, palette="Blues_d")
ax2.set_ylabel("Satisfaction (%)")
st.pyplot(fig2)

# --- Gráfico 3: Department Enrollment (Pie) ---
st.subheader("Department Enrollment Distribution")
dept_totals = df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.pie(dept_totals, labels=dept_totals.index, autopct="%1.1f%%", startangle=90)
ax3.axis("equal")
st.pyplot(fig3)

st.markdown("---")
st.caption("Developed for University Data Analytics Project.")
