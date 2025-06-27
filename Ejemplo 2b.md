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
