# 📘 Mi Lenguaje — Especificación Léxica

**Mi Lenguaje** es un lenguaje de programación didáctico con una sintaxis clara, pensado para el aprendizaje de estructuras básicas de programación: variables, tipos, condicionales, ciclos, operadores y comentarios.

---

## 📌 Estructura general del lenguaje

- Las líneas terminan con un salto de línea (`\n`)
- El uso de `;` al final de línea es opcional y sin efecto
- Se permiten tres formas de definir bloques:
  - Tabulaciones
  - Llaves `{ }`
  - Delimitadores personalizados: `<< >>` y `[[ ]]`
- Las estructuras condicionales pueden usar `then`

---

## 🔠 Reglas para nombres de variables

- Se usa la palabra clave `let` para declarar variables
- Los nombres deben comenzar con una letra
- No se permiten guiones (`-`), guiones bajos (`_`) ni caracteres especiales

### ✅ Ejemplos válidos

```javascript
let año = 2025
let usuario = "daniel"
let deuda = -1500
let saldo = -32.1
```

### ❌ Ejemplos inválidos

```javascript
let _nombre
let -usuario
let @dato
let 3edad
```

---

## 🔢 Tipos de datos permitidos

| Tipo     | Ejemplo                 |
|----------|-------------------------|
| Entero   | `2025`, `-1500`         |
| Decimal  | `7.85`, `-32.1`         |
| Cadena   | `"daniel"`, `'texto'`   |
| Booleano | `true`, `false`         |
| Lista    | `[10, 20, 30]`          |

### Ejemplos de uso

```javascript
let activo = false
let numeros = [10, 20, 30, 40]
```

---

## ➕ Operadores

### Aritméticos

| Operador | Descripción     |
|----------|-----------------|
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División        |
| `%`      | Módulo          |

### Relacionales

| Operador | Descripción        |
|----------|--------------------|
| `==`     | Igual a            |
| `!=`     | Diferente de       |
| `>`      | Mayor que          |
| `<`      | Menor que          |
| `>=`     | Mayor o igual que  |
| `<=`     | Menor o igual que  |

### Lógicos

| Operador | Descripción |
|----------|-------------|
| `&&`     | AND         |
| `\|\|`   | OR          |
| `!`      | NOT         |

### Incrementales y compuestos

| Operador | Acción           |
|----------|------------------|
| `+=`     | Suma y asigna    |
| `-=`     | Resta y asigna   |
| `++`     | Incrementa en 1  |
| `--`     | Decrementa en 1  |

---

## 🔁 Condicionales y ciclos

### Condicionales

```javascript
if (año > 2000) then
    let epoca = "moderna"
elseif (año == 1999) then
    let epoca = "fin del milenio"
else
    let epoca = "antiguo"
```

O con llaves:

```javascript
if (año > 2000) {
    let epoca = "moderna"
} elseif (año == 1999) {
    let epoca = "fin del milenio"
} else {
    let epoca = "antiguo"
}
```

### Ciclos

```javascript
let contador = 5
while (contador < 10) {
    contador += 1
}

do {
    contador -= 1
} while (contador > 0)

for (let j = 1; j <= 5; j++) {
    let mensaje = "iterando"
}

for (item) in (numeros) {
    let valor = item * 2
}
```

---

## 💬 Comentarios

| Forma           | Tipo       |
|-----------------|------------|
| `# texto`       | Una línea  |
| `// texto`      | Una línea  |
| `''' texto '''` | Multilínea |
| `/* texto */`   | Multilínea |

---

## 🔐 Palabras reservadas

No se pueden usar como nombres de variables:

```
let, if, else, elseif, for, while, true, false, in, then, do
```

---

## ⚠️ Advertencias comunes

| Situación                      | Acción/Resultado        |
|--------------------------------|-------------------------|
| Uso de `;` al final de línea   | Ignorado               |
| Separación incorrecta (`= =`)  | Advertencia            |
| Operadores mal formados (`=>`) | Error                  |
| Comentarios mal cerrados       | Error                  |
| Bloques sin delimitación clara | Error                  |

---

## ❌ Errores comunes

| Error                  | Descripción                              |
|------------------------|------------------------------------------|
| `let 9var = ...`       | Nombres no pueden iniciar con números   |
| `let nombre@ = ...`    | Uso de símbolos no permitidos           |
| `if condicion`         | Falta de paréntesis                     |
| Faltan llaves          | Error de estructura de bloque           |

---

## 🚀 Recursos adicionales

![Gráfico autómata](https://github.com/sebastianmend/automata/blob/main/Gr%C3%A1fico%20aut%C3%B3mata%20%20(2).png)


