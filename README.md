Estudiante:   Karla Daniela Luque Navarrete

Aplicación gráfica de gestión para un restaurante, desarrollada como evolución del proyecto de las semanas anteriores de Programación Orientada a Objetos.

## Objetivo de la Semana 15

La aplicación incorpora el manejo básico de eventos mediante un botón asociado con `command=` y un callback. El callback coordina el registro de una venta y delega la validación y persistencia a `RestauranteServicio`.

## Funcionalidades

- Inicio de sesión.
- Gestión de productos: registrar, consultar, actualizar y eliminar.
- Consulta de usuarios.
- Registro de ventas relacionando un usuario existente con un producto existente.
- Persistencia de ventas en `datos/ventas.json`.
- Visualización de ventas mediante `Treeview`.
- Actualización inmediata de la tabla después de registrar una venta.
- Logo e íconos integrados desde `assets/`.

## Flujo de eventos de ventas

```text
Usuario
  ↓
Botón "Registrar venta"
  ↓
command=self.registrar_venta
  ↓
callback registrar_venta()
  ↓
RestauranteServicio.registrar_venta()
  ↓
validación de usuario y producto
  ↓
ventas.json
  ↓
actualización del Treeview
  ↓
respuesta visual al usuario
```

La interfaz coordina la interacción, mientras que las reglas y la persistencia permanecen en la capa de servicios.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   ├── logo.png
│   ├── icono_productos.png
│   ├── icono_usuarios.png
│   └── icono_ventas.png
└── main.py
```

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

Credenciales de prueba incluidas en `datos/usuarios.json`:

- Usuario: `admin`
- Contraseña: `admin`


El proyecto mantiene la arquitectura modular de las semanas anteriores. La Semana 15 agrega únicamente la operación de ventas y el manejo básico de eventos solicitado.

## Usuarios de prueba

- Administrador: usuario `admin`, contraseña `admin`
- Juan Perez: correo `juan@gmail.com`, contraseña `1234`
- Maria Lopez: correo `maria@gmail.com`, contraseña `1234`

Estos usuarios permiten probar la selección de usuario en la sección Ventas.
