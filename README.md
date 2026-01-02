# MLOps House Price Predictor

Un pipeline "End-to-End" de Machine Learning para predecir precios de viviendas en California. Este proyecto demuestra buenas prácticas de **MLOps** integrando entrenamiento de modelos, APIs REST, Contenedores y Dashboards interactivos.

## 🛠️ Tecnologías

- **Python 3.10**: Lenguaje base.
- **Scikit-Learn**: Entrenamiento del modelo (Random Forest).
- **FastAPI**: API REST para servir las predicciones.
- **Streamlit**: Interfaz de usuario (Frontend) interactiva.
- **Docker**: Containerización para despliegue portable.
- **Joblib**: Serialización del modelo.

## Estructura del Proyecto 📂 

```bash
mlops-price-predictor/
├── src/
│   ├── api.py           # Aplicación FastAPI
│   ├── app.py           # Dashboard Streamlit
│   └── train_model.py   # Script de entrenamiento
├── Dockerfile           # Configuración de Docker
├── requirements.txt     # Dependencias
└── model.joblib         # Modelo entrenado (generado)
```

## Cómo Ejecutar 🚀 

### Opción 1: Localmente (Python)

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Entrenar el modelo (si no existe):**
    ```bash
    python src/train_model.py
    ```

3.  **Iniciar la API (Backend):**
    ```bash
    uvicorn src.api:app --reload
    ```
    *La API estará disponible en: http://localhost:8000/docs*

4.  **Iniciar la App (Frontend):**
    ```bash
    streamlit run src/app.py
    ```
    *Abrir en navegador: http://localhost:8501*

### Opción 2: Con Docker 🐳

1.  **Construir la imagen:**
    ```bash
    docker build -t house-price-predictor .
    ```

2.  **Correr el contenedor:**
    ```bash
    docker run -p 8000:8000 house-price-predictor
    ```

## 📊 Endpoints de la API

- `GET /`: Health check.
- `POST /predict`: Recibe un JSON con las características de la casa y devuelve el precio estimado.

---
*Proyecto desarrollado como parte de demostración de capacidades de Ingeniería de Datos y MLOps.*
