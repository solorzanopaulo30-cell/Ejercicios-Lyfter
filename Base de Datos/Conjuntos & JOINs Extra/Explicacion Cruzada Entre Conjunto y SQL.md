## 1. Explicación cruzada entre conjuntos y SQL

Analice la operación de conjuntos All - Odd.



## Explique cómo una operación similar se puede representar en SQL con JOINs.

Resultado: $\{2, 4, 6, 8, 10\}$ (corresponde a los números pares del conjunto All al excluir los impares).

## ¿Qué tipo de JOIN usaría?
Tipo de JOIN: LEFT JOIN (conocido como Anti-Join).

Cómo se hace: Se unen las tablas con LEFT JOIN y se filtra con WHERE tabla_derecha.id IS NULL para obtener solo los registros de la izquierda que no tienen coincidencia.