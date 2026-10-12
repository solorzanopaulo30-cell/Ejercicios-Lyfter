# Ejercicio de Normalización: Cars

## Tabla original

| VIN | Make | Model | Year | Color | Owner_ID | Owner_Name | Owner_Phone | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

## 1FN

La tabla queda igual, con la llave primaria compuesta (VIN, Owner_ID).

| VIN | Make | Model | Year | Color | Owner_ID | Owner_Name | Owner_Phone | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

Justificación: la tabla cumple la 1FN porque cada celda tiene un solo valor y la llave primaria es compuesta: (VIN, Owner_ID). El VIN se repite (el mismo auto aparece con dos dueños), y un dueño podría tener varios autos, así que se necesita la pareja para identificar cada fila.

## 2FN

Cars (PK: VIN)

| VIN | Make | Model | Year | Color |
| --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

Owners (PK: Owner_ID)

| Owner_ID | Owner_Name | Owner_Phone |
| --- | --- | --- |
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

Car_Owners (PK: VIN, Owner_ID. FK: ambas)

| VIN | Owner_ID | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- |
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de la llave (VIN, Owner_ID).

- Solo de VIN: Make, Model, Year y Color. Pasan a Cars. En la tabla original, el mismo auto repetía estos cuatro datos en sus dos filas.
- Solo de Owner_ID: Owner_Name y Owner_Phone. Pasan a Owners.
- De las dos: Insurance_Company e Insurance_Policy, porque el mismo auto tiene un seguro distinto para cada dueño (Alice con ABC y Bob con XYZ). Quedan en Car_Owners.

## 3FN

Models (PK: Model_ID)

| Model_ID | Make | Model_Name |
| --- | --- | --- |
| 1 | Honda | Accord |
| 2 | Honda | CR-V |
| 3 | Chevrolet | Volt |

Cars (PK: VIN. FK: Model_ID)

| VIN | Model_ID | Year | Color |
| --- | --- | --- | --- |
| 1HGCM82633A | 1 | 2003 | Silver |
| 5J6RM4H79EL | 2 | 2014 | Blue |
| 1G1RA6EH1FU | 3 | 2015 | Red |

Owners y Car_Owners quedan igual que en la 2FN.

Justificación: en la 3FN encuentro una dependencia transitiva en Cars: VIN → Model → Make. El modelo determina la marca (un Accord siempre es Honda), y Honda se repite en dos modelos. Creo la tabla Models con Model_ID como llave primaria, y Cars guarda solo Model_ID como llave foránea. En Owners no hay dependencias transitivas, porque Owner_Name y Owner_Phone dependen directamente de Owner_ID. En Car_Owners tampoco, porque el seguro depende de la pareja completa (VIN, Owner_ID), y Insurance_Company e Insurance_Policy no dependen una de la otra (una compañía ofrece varias pólizas).

## Notas

- Supuesto: un auto puede tener varios dueños y un dueño puede tener varios autos, por eso Car_Owners tiene llave compuesta aunque en estos datos Owner_ID no se repita.
- Supuesto: cada modelo pertenece a una sola marca.
- El auto con VIN 1HGCM82633A aparece con dos dueños, cada uno con su propio seguro.# Ejercicio de Normalización: Cars

## Tabla original

| VIN | Make | Model | Year | Color | Owner_ID | Owner_Name | Owner_Phone | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

## 1FN

La tabla queda igual, con la llave primaria compuesta (VIN, Owner_ID).

| VIN | Make | Model | Year | Color | Owner_ID | Owner_Name | Owner_Phone | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

Justificación: la tabla cumple la 1FN porque cada celda tiene un solo valor y la llave primaria es compuesta: (VIN, Owner_ID). El VIN se repite (el mismo auto aparece con dos dueños), y un dueño podría tener varios autos, así que se necesita la pareja para identificar cada fila.

## 2FN

Cars (PK: VIN)

| VIN | Make | Model | Year | Color |
| --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

Owners (PK: Owner_ID)

| Owner_ID | Owner_Name | Owner_Phone |
| --- | --- | --- |
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

Car_Owners (PK: VIN, Owner_ID. FK: ambas)

| VIN | Owner_ID | Insurance_Company | Insurance_Policy |
| --- | --- | --- | --- |
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de la llave (VIN, Owner_ID).

- Solo de VIN: Make, Model, Year y Color. Pasan a Cars. En la tabla original, el mismo auto repetía estos cuatro datos en sus dos filas.
- Solo de Owner_ID: Owner_Name y Owner_Phone. Pasan a Owners.
- De las dos: Insurance_Company e Insurance_Policy, porque el mismo auto tiene un seguro distinto para cada dueño (Alice con ABC y Bob con XYZ). Quedan en Car_Owners.

## 3FN

Models (PK: Model_ID)

| Model_ID | Make | Model_Name |
| --- | --- | --- |
| 1 | Honda | Accord |
| 2 | Honda | CR-V |
| 3 | Chevrolet | Volt |

Cars (PK: VIN. FK: Model_ID)

| VIN | Model_ID | Year | Color |
| --- | --- | --- | --- |
| 1HGCM82633A | 1 | 2003 | Silver |
| 5J6RM4H79EL | 2 | 2014 | Blue |
| 1G1RA6EH1FU | 3 | 2015 | Red |

Owners y Car_Owners quedan igual que en la 2FN.

Justificación: en la 3FN encuentro una dependencia transitiva en Cars: VIN → Model → Make. El modelo determina la marca (un Accord siempre es Honda), y Honda se repite en dos modelos. Creo la tabla Models con Model_ID como llave primaria, y Cars guarda solo Model_ID como llave foránea. En Owners no hay dependencias transitivas, porque Owner_Name y Owner_Phone dependen directamente de Owner_ID. En Car_Owners tampoco, porque el seguro depende de la pareja completa (VIN, Owner_ID), y Insurance_Company e Insurance_Policy no dependen una de la otra (una compañía ofrece varias pólizas).

## Notas

- Supuesto: un auto puede tener varios dueños y un dueño puede tener varios autos, por eso Car_Owners tiene llave compuesta aunque en estos datos Owner_ID no se repita
- Supuesto: cada modelo pertenece a una sola marca
- El auto con VIN 1HGCM82633A aparece con dos dueños, cada uno con su propio seguro