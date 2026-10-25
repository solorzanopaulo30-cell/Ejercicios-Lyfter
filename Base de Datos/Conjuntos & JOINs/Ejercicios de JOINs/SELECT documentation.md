# Ejercicio de JOINs: documentación del SELECT

## Orden en que se escribe un SELECT

SELECT columnas FROM tabla [JOIN ... ON ...] [WHERE ...] [GROUP BY ...] [HAVING ...] [ORDER BY ...] [LIMIT ...]

## ORDER BY, LIMIT y GROUP BY

| Cláusula | Para qué sirve | Sintaxis | Ejemplo | Detalles importantes |
| --- | --- | --- | --- | --- |
| ORDER BY | Ordena las filas del resultado por una o más columnas | ORDER BY columna ASC o DESC | SELECT * FROM Products ORDER BY Price DESC; | ASC (de menor a mayor) es el valor por defecto. Sin ORDER BY el orden de las filas no está garantizado. Se pueden usar varias columnas separadas por coma. En SQLite, los NULL se consideran menores que cualquier valor. |
| LIMIT | Limita cuántas filas devuelve la consulta | LIMIT n OFFSET m | SELECT * FROM Products ORDER BY Price DESC LIMIT 3; | Va siempre al final. OFFSET m salta las primeras m filas (sirve para paginar). Junto con ORDER BY da el "top N". Sin ORDER BY no se sabe cuáles filas salen. |
| GROUP BY | Junta las filas que tienen el mismo valor en una columna y devuelve una fila por grupo | GROUP BY columna HAVING condición | SELECT Brand, SUM(Stock) FROM Products GROUP BY Brand; | Se usa con funciones de agregado (COUNT, SUM, AVG, MIN, MAX). WHERE filtra filas antes de agrupar y HAVING filtra los grupos después. Una columna sin agregar que no esté en el GROUP BY: SQLite lo permite, pero su valor sale de una fila cualquiera del grupo, y otros motores dan error. |

## Tres tipos de JOIN

Un JOIN junta filas de dos tablas. La condición ON dice qué columnas deben coincidir, normalmente una llave foránea con una llave primaria.

| Tipo | Qué devuelve | Sintaxis | Ejemplo | Filas sin pareja |
| --- | --- | --- | --- | --- |
| INNER JOIN | Solo las filas que tienen pareja en las dos tablas | FROM A INNER JOIN B ON A.col = B.col | SELECT Products.Name, Categories.Name FROM Products INNER JOIN Categories ON Products.Category_ID = Categories.ID; | Se descartan las de cualquiera de las dos tablas. Escribir solo JOIN equivale a INNER JOIN. |
| LEFT JOIN | Todas las filas de la tabla izquierda (la que va antes del JOIN), tengan pareja o no | FROM A LEFT JOIN B ON A.col = B.col | SELECT Products.Name, Categories.Name FROM Products LEFT JOIN Categories ON Products.Category_ID = Categories.ID; | Si una fila de la izquierda no tiene pareja, las columnas de la derecha salen NULL. Con LEFT JOIN, poner una condición en ON o en WHERE da resultados distintos. |
| RIGHT JOIN | Todas las filas de la tabla derecha (la que va después del JOIN), tengan pareja o no | FROM A RIGHT JOIN B ON A.col = B.col | SELECT Products.Name, Categories.Name FROM Products RIGHT JOIN Categories ON Products.Category_ID = Categories.ID; | Si una fila de la derecha no tiene pareja, las columnas de la izquierda salen NULL. SQLite lo soporta desde la versión 3.39.0 (2022). Antes se resolvía cambiando el orden de las tablas y usando LEFT JOIN. |

## Fuentes

- Documentación de SQLite, SELECT: https://www.sqlite.org/lang_select.html
- Notas de la versión 3.39.0 de SQLite (soporte de RIGHT y FULL OUTER JOIN): https://www.sqlite.org/releaselog/3_39_0.html