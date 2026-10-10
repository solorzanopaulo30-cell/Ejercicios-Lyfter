# Ejercicio de Normalización

## Tabla original

| ORDER_ID | CUSTOMER_NAME | CUSTOMER_PHONE | ADDRESS | ITEM_ID | ITEM_NAME | PRICE | QUANTITY | SPECIAL_REQUEST | DELIVERY_TIME |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 4th Avenue | 102 | Fries | $3 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

## 1FN

La tabla queda igual, con la llave primaria compuesta (ORDER_ID, ITEM_ID).

La tabla original ya cumple la 1FN: cada celda tiene un solo valor y la llave primaria es compuesta, (ORDER_ID, ITEM_ID), porque ORDER_ID y ITEM_ID se repiten por separado, pero la pareja no.

## 2FN

Orders (PK: ORDER_ID)

| ORDER_ID | CUSTOMER_NAME | CUSTOMER_PHONE | ADDRESS | DELIVERY_TIME |
| --- | --- | --- | --- | --- |
| 001 | Alice | 123-456-7890 | 123 Main St | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 5:00 PM |

Items (PK: ITEM_ID)

| ITEM_ID | ITEM_NAME | PRICE |
| --- | --- | --- |
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

Order_Items (PK: ORDER_ID, ITEM_ID)

| ORDER_ID | ITEM_ID | QUANTITY | SPECIAL_REQUEST |
| --- | --- | --- | --- |
| 001 | 101 | 2 | No onions |
| 001 | 102 | 1 | Extra ketchup |
| 002 | 103 | 1 | Extra cheese |
| 002 | 102 | 2 | None |
| 003 | 105 | 1 | No croutons |
| 004 | 106 | 1 | None |

En la 2FN reviso qué columnas dependen solo de una parte de la llave (ORDER_ID, ITEM_ID). Las que dependen solo del pedido pasan a Orders, las que dependen solo del producto pasan a Items, y las que necesitan ambas (quantity y special_request) quedan en Order_Items, con la llave compuesta.

## 3FN

Customers (PK: CUSTOMER_ID)

| CUSTOMER_ID | CUSTOMER_NAME | CUSTOMER_PHONE |
| --- | --- | --- |
| 1 | Alice | 123-456-7890 |
| 2 | Bob | 987-654-3210 |
| 3 | Claire | 555-123-4567 |

Orders (PK: ORDER_ID, FK: CUSTOMER_ID)

| ORDER_ID | CUSTOMER_ID | ADDRESS | DELIVERY_TIME |
| --- | --- | --- | --- |
| 001 | 1 | 123 Main St | 6:00 PM |
| 002 | 2 | 456 Elm St | 7:30 PM |
| 003 | 3 | 789 Oak St | 12:00 PM |
| 004 | 3 | 464 Georgia St | 5:00 PM |

Items y Order_Items quedan igual que en la 2FN.

En la 3FN encuentro una dependencia transitiva: customer_name y customer_phone no dependen directamente de order_id, sino del cliente. Los muevo a una tabla Customers con customer_id como llave primaria, y Orders guarda solo customer_id como llave foránea. Así, los datos de cada cliente aparecen una sola vez.

## Notas

- ADDRESS se queda en Orders y no pasa a Customers, porque Claire tiene una dirección distinta en cada pedido: es la dirección de entrega, no del cliente.
- El pedido 002 aparecía con dos direcciones (456 Elm St y 4th Avenue). Lo tomé como un error de datos y dejé 456 Elm St.