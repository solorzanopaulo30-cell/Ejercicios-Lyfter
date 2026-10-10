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

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de