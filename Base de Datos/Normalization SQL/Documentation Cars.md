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

| VIN | Owner_ID |
| --- | --- |
| 1HGCM82633A | 101 |
| 1HGCM82633A | 102 |
| 5J6RM4H79EL | 103 |
| 1G1RA6EH1FU | 104 |

Car_Insurance (PK: VIN, Insurance_Company, Insurance_Policy. FK: VIN)

| VIN | Insurance_Company | Insurance_Policy |
| --- | --- | --- |
| 1HGCM82633A | ABC Insurance | Fire & Theft |
| 1HGCM82633A | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | DEF Insurance | Collision |
| 1G1RA6EH1FU | GHI Insurance | Basic Legal |

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de la llave (VIN, Owner_ID).

- Solo de VIN: Make, Model, Year y Color. Pasan a Cars. En la tabla original, el mismo auto repetía estos cuatro datos en sus dos filas.
- Solo de Owner_ID: Owner_Name y Owner_Phone. Pasan a Owners.
- Insurance_Company e Insurance_Policy: el seguro se aplica al vehículo y no a la persona, así que depende solo del VIN y no de la pareja (VIN, Owner_ID). Pasan a Car_Insurance, que identifica cada póliza del vehículo con (VIN, Insurance_Company, Insurance_Policy).
- De las dos: ninguna. Por eso Car_Owners solo guarda la llave y registra quién es dueño de qué auto.

## 3FN

Models (PK: Model_ID)

| Model_ID | Make | Model_Name | Year |
| --- | --- | --- | --- |
| 1 | Honda | Accord | 2003 |
| 2 | Honda | CR-V | 2014 |
| 3 | Chevrolet | Volt | 2015 |

Cars (PK: VIN. FK: Model_ID)

| VIN | Model_ID | Color |
| --- | --- | --- |
| 1HGCM82633A | 1 | Silver |
| 5J6RM4H79EL | 2 | Blue |
| 1G1RA6EH1FU | 3 | Red |

Insurance_Companies (PK: Company_ID)

| Company_ID | Company_Name |
| --- | --- |
| 1 | ABC Insurance |
| 2 | XYZ Insurance |
| 3 | DEF Insurance |
| 4 | GHI Insurance |

Insurance_Policies (PK: Policy_ID. FK: Company_ID)

| Policy_ID | Policy_Name | Company_ID |
| --- | --- | --- |
| 1 | Fire & Theft | 1 |
| 2 | Full Cover | 2 |
| 3 | Collision | 3 |
| 4 | Basic Legal | 4 |

Car_Policies (PK: VIN, Policy_ID. FK: ambas)

| VIN | Policy_ID |
| --- | --- |
| 1HGCM82633A | 1 |
| 1HGCM82633A | 2 |
| 5J6RM4H79EL | 3 |
| 1G1RA6EH1FU | 4 |

Owners y Car_Owners quedan igual que en la 2FN.

Justificación: en la 3FN reviso las dependencias entre columnas que no son la llave.

- En Cars: Make, Model_Name y Year describen al modelo y no al auto físico (VIN → Model → Make, Model_Name, Year). Creo la tabla Models con Model_ID como llave primaria, y Cars guarda solo Model_ID y Color, que sí es propio de cada auto.
- En Car_Insurance: una póliza pertenece a una compañía (Policy → Company). Si muchos autos usaran la póliza Full Cover, el nombre de la compañía se repetiría en cada uno. Creo Insurance_Companies e Insurance_Policies, con Company_ID como llave foránea en las pólizas. Car_Policies relaciona cada vehículo con sus pólizas.
- En Owners: no hay dependencias transitivas, porque Owner_Name y Owner_Phone dependen directamente de Owner_ID.

## Notas

- Supuesto: un auto puede tener varios dueños y un dueño puede tener varios autos, por eso Car_Owners tiene llave compuesta aunque en estos datos Owner_ID no se repita.
- Supuesto: cada modelo tiene una sola marca y un solo año.
- La póliza se aplica al vehículo y no a la persona. El auto con VIN 1HGCM82633A tiene dos pólizas en los datos, por eso el seguro va en una tabla aparte (Car_Policies) y no en una columna de Cars. Si cada auto tuviera una sola póliza, bastaría con una columna Policy_ID en Cars.
- Al separar el seguro del dueño, ya no se registra qué dueño contrató cada póliza.