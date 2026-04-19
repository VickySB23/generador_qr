# generador_qr

# 📱 Generador de Códigos QR

Este proyecto consiste en una aplicación robusta para la generación de códigos QR estáticos. Está construido bajo principios de **Arquitectura Limpia**, siguiendo la metodología **TDD (Test Driven Development)** y utilizando las tecnologías más modernas del ecosistema Python.

## 🚀 Características

- **Generación en Tiempo Real**: Los códigos se generan directamente en la memoria RAM, sin almacenar archivos temporales en el servidor.
- **Validación Estricta**: Uso de Pydantic para asegurar que solo se procesen URLs válidas.
- **Interfaz Intuitiva**: Frontend interactivo construido con Streamlit.
- **Código Calidad**: Suite de pruebas unitarias con Pytest.
- **Gestión de Paquetes**: Utiliza `uv` para una instalación de dependencias ultra rápida y reproducible.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.13
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Validación**: [Pydantic](https://docs.pydantic.dev/)
- **Generación de QR**: [qrcode](https://pypi.org/project/qrcode/)
- **Pruebas**: [Pytest](https://docs.pytest.org/)
- **Gestor de Entorno**: [uv](https://github.com/astral-sh/uv)

## 📁 Estructura del Proyecto

```text
generador_qr/
├── src/                  # Código fuente
│   ├── api/              # Endpoints y rutas de FastAPI
│   ├── core/             # Lógica de negocio (generación de QR)
│   ├── schemas/          # Modelos de validación (Pydantic)
│   ├── main.py           # Punto de entrada del Backend
│   └── frontend.py       # Interfaz de usuario con Streamlit
├── tests/                # Pruebas unitarias
└── pyproject.toml        # Configuración de dependencias y proyecto

⚙️ Instalación y Configuración
Para poner en funcionamiento este proyecto en tu entorno local, seguí estos pasos:

1. Requisitos previos
Tener instalado uv. Si no lo tenés, podés instalarlo con:

Bash
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
2. Clonar el repositorio y entrar a la carpeta
Bash
git clone [https://github.com/tu-usuario/generador_qr.git](https://github.com/tu-usuario/generador_qr.git)
cd generador_qr
3. Sincronizar el entorno e instalar dependencias
uv se encargará de crear el entorno virtual automáticamente:

Bash
uv sync
🏃 Cómo hacerlo funcionar
Para que la aplicación funcione completa, necesitás tener dos procesos corriendo simultáneamente:

Paso 1: Iniciar el Backend (API)
En una terminal, ejecutá:

Bash
uv run uvicorn src.main:app --reload
La API estará disponible en http://127.0.0.1:8000 y la documentación interactiva en /docs.

Paso 2: Iniciar el Frontend (Interfaz)
En otra terminal, ejecutá:

Bash
uv run streamlit run src/frontend.py
Se abrirá automáticamente tu navegador en http://localhost:8501.

🧪 Ejecución de Pruebas
Para asegurar que todo funcione correctamente después de realizar cambios, ejecutá la suite de tests:

Bash
uv run pytest
📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

Desarrollado por Victoria Sanchez B.