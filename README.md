# 🌍 TourGo WebApp

[![Version](https://img.shields.io/badge/Version-1.0-blue)]()

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 


---

TourGo es una landing page simple y elegante desarrollada con **[Reflex](https://reflex.dev)**. esta web está pensada como una interfaz de presentación para servicios turísticos, ideal para mostrar ofertas, detalles de actividades y una sección de reservas.



## Características

- Página de Inicio con formulario de búsqueda
- Página de Descripción con detalles e imágenes
- Página de Reservas con formulario
- Desarrollado 100% en Python con Reflex

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/MyDiDev/TourWebApp.git
cd TourWebApp
````

### 2. Instala Reflex y dependencias

```bash
pip install -r requirements.txt
# o directamente:
pip install reflex
```

> Requiere **Python 3.10+**

---

## 🚀 Ejecutar la Aplicación

```bash
reflex run
```

Esto iniciará el servidor en `http://localhost:3000`


## Contribución

¡Contribuciones son bienvenidas!

- Haz un **Fork** del repositorio.

- Clona tu fork:

   ```bash
   git clone https://github.com/tu_usuario/TourWebApp.git
   ```
- Crea una rama:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
- Realiza tus cambios y commitea:

   ```bash
   git commit -m "Agrega nueva sección"
   ```
- Sube tu rama:

   ```bash
   git push origin feature/nueva-funcionalidad
   ```
- Abre un **Pull Request**.


## Estructura del Proyecto

```
TourWebApp/
│
├── Components/                
│   ├── navbar.py
│   └── footer.py
│
├── DB/                        
│   └── connection.py
│
├── Pages/                     
│   ├── Admin/
│   │   └── mainpage.py
│   ├── Contacts/
│   │   └── mainpage.py
│   ├── Offers/
│   │   └── mainpage.py
│   ├── Schedules/
│   │   └── mainpage.py
│   ├── Transactions/
│   │   └── mainpage.py
│   └── Users/
│       └── mainpage.py
│
├── Uploader/                 
│   ├── uploader.py
│   └── __init__.py
│
├── homepage.py               
├── descriptionpage.py        
├── registerpage.py           
├── paymentpage.py            
├── loginpage.py              
├── adminpage.py              
├── TourWebApp.py             
├── requirements.txt
└── README.md
           
```

## Autor

* [@MyDiDev](https://github.com/MyDiDev)

