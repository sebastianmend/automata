```
//Declaración de variables
let anio = 2025
let usuario = "Choclo"
let activo = false
let numeros = [10, 20, 30, 40]
let deuda = -1500
let saldo = -32.1

//Condicionales
if (anio > 2000) {
    let epoca = "moderna"
} 

// Ciclo Repetitivo

while(anio >= 2030){
 anio ++
}

// comentario
```

## Gramática:

```
<PROGRAMA> -> <BLOQUE_DE_CODIGO>

<BLOQUE_DE_CODIGO> -> <SENTENCIA>
<BLOQUE_DE_CODIGO> -> <SENTENCIA> <BLOQUE_DE_CODIGO>

<SENTENCIA> -> <DECLARACION_VARIABLE>
<SENTENCIA> -> <IF>
<SENTENCIA> -> <WHILE>
<SENTENCIA> -> id ++
<SENTENCIA> -> id --
<SENTENCIA> -> <COMENTARIO>

<DECLARACION_VARIABLE> -> let id = <VALOR>
<DECLARACION_VARIABLE> -> let id = <LISTA>

<VALOR> -> string
<VALOR> -> number
<VALOR> -> boolean
<VALOR> -> id + id
<VALOR> -> id - id
<VALOR> -> id * id
<VALOR> -> id / id

<LISTA> -> [ <VALOR_LISTA> ]
<VALOR_LISTA> -> number
<VALOR_LISTA> -> number , <VALOR_LISTA>

<IF> -> if ( <CONDICION> ) { <BLOQUE_DE_CODIGO> }

<WHILE> -> while ( <CONDICION> ) { <BLOQUE_DE_CODIGO> }

<CONDICION> -> id == id
<CONDICION> -> id != id
<CONDICION> -> id > id
<CONDICION> -> id < id
<CONDICION> -> id <= id
<CONDICION> -> id >= id

<COMENTARIO> -> // string
```

## Ecsplicasio

```
───────────────────────── GRAMÁTICA COMENTADA ─────────────────────────
<PROGRAMA>               -> <BLOQUE_DE_CODIGO>              // Punto de entrada

<BLOQUE_DE_CODIGO>       -> <SENTENCIA>                     // Una sola sentencia
<BLOQUE_DE_CODIGO>       -> <SENTENCIA> <BLOQUE_DE_CODIGO>  // Secuencia de sentencias

// --------------- Sentencias de alto nivel ---------------
<SENTENCIA>              -> <DECLARACION_VARIABLE>          // let id = …
<SENTENCIA>              -> <IF>                            // if (…) { … }
<SENTENCIA>              -> <WHILE>                         // while (…) { … }
<SENTENCIA>              -> id ++                           // post-incremento
<SENTENCIA>              -> id --                           // post-decremento
<SENTENCIA>              -> <COMENTARIO>                    // línea que inicia con “//”

// --------------- Declaración de variables ---------------
<DECLARACION_VARIABLE>   -> let id = <VALOR>                // valores simples / expresiones
<DECLARACION_VARIABLE>   -> let id = <LISTA>                // asignación de lista []

// --------------- Valores permitidos ---------------------
<VALOR>                  -> string                          // "Choclo"
<VALOR>                  -> number                          // 2025, -32.1
<VALOR>                  -> boolean                         // true / false
<VALOR>                  -> id + id                         // suma de variables
<VALOR>                  -> id - id                         // resta
<VALOR>                  -> id * id                         // multiplicación
<VALOR>                  -> id / id                         // división

// --------------- Listas numéricas -----------------------
<LISTA>                  -> [ <VALOR_LISTA> ]               // [] obligatorias
<VALOR_LISTA>            -> number                          // un número
<VALOR_LISTA>            -> number , <VALOR_LISTA>          // más números separados por coma

// --------------- Estructuras de control -----------------
<IF>                     -> if ( <CONDICION> ) { <BLOQUE_DE_CODIGO> }
<WHILE>                  -> while ( <CONDICION> ) { <BLOQUE_DE_CODIGO> }

// --------------- Condiciones lógicas --------------------
<CONDICION>              -> id == id
<CONDICION>              -> id != id
<CONDICION>              -> id >  id
<CONDICION>              -> id <  id
<CONDICION>              -> id <= id
<CONDICION>              -> id >= id

// --------------- Comentarios ----------------------------
<COMENTARIO>             -> // string                      // texto libre al final de la línea
───────────────────────────────────────────────────────────

```
