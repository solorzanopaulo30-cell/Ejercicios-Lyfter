-- Ejercicio 2: Transacción de compra
-- Valida el usuario y el stock, inserta la factura con sus líneas
-- y reduce el stock. Todo en un solo bloque: si algo falla, se deshace todo.


DO $$ 
DECLARE 
	v_user_id INTEGER := 1;
BEGIN
	IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = v_user_id) THEN
		RAISE EXCEPTION 'El usuario % no existe', v_user_id;
	END IF;

	RAISE NOTICE 'Usuario % encontrado', v_user_id;
END $$;



--------------------------------------------------------------


DO $$
DECLARE
    v_user_id     INTEGER := 1;
    v_product_ids INTEGER[] := ARRAY[1, 3];
    v_quantities  INTEGER[] := ARRAY[2, 1];
    v_stock       INTEGER;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        SELECT Stock INTO v_stock FROM Products WHERE ID = v_product_ids[i];

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto % no existe', v_product_ids[i];
        END IF;

        IF v_stock < v_quantities[i] THEN
            RAISE EXCEPTION 'Stock insuficiente del producto %: hay %, se piden %', v_product_ids[i], v_stock, v_quantities[i];
        END IF;
    END LOOP;

    RAISE NOTICE 'Validaciones correctas';
END $$;


-------------------------------------------------------------------------------------------


DO $$
DECLARE
    v_user_id     INTEGER := 1;
    v_product_ids INTEGER[] := ARRAY[1, 3];
    v_quantities  INTEGER[] := ARRAY[2, 1];
    v_stock       INTEGER;
    v_bill_id     INTEGER;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        SELECT Stock INTO v_stock FROM Products WHERE ID = v_product_ids[i];

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto % no existe', v_product_ids[i];
        END IF;

        IF v_stock < v_quantities[i] THEN
            RAISE EXCEPTION 'Stock insuficiente del producto %: hay %, se piden %', v_product_ids[i], v_stock, v_quantities[i];
        END IF;
    END LOOP;

    INSERT INTO Bills (UserID) VALUES (v_user_id)
    RETURNING ID INTO v_bill_id;

    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        INSERT INTO Bills_Products (BillID, ProductID, Quantity)
        VALUES (v_bill_id, v_product_ids[i], v_quantities[i]);
    END LOOP;

    RAISE NOTICE 'Factura % creada', v_bill_id;
END $$;


------------------------------------------------------------------------------------------------


DO $$
DECLARE
    v_user_id     INTEGER := 1;
    v_product_ids INTEGER[] := ARRAY[1, 3];
    v_quantities  INTEGER[] := ARRAY[2, 1];
    v_stock       INTEGER;
    v_bill_id     INTEGER;
BEGIN
    -- 1. Confirmar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    -- 2. Comprobar que hay existencias suficientes de cada producto
    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        SELECT Stock INTO v_stock FROM Products WHERE ID = v_product_ids[i];

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto % no existe', v_product_ids[i];
        END IF;

        IF v_stock < v_quantities[i] THEN
            RAISE EXCEPTION 'Stock insuficiente del producto %: hay %, se piden %', v_product_ids[i], v_stock, v_quantities[i];
        END IF;
    END LOOP;

    -- 3. Insertar la factura con el usuario relacionado y sus líneas
    INSERT INTO Bills (UserID) VALUES (v_user_id)
    RETURNING ID INTO v_bill_id;

    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        INSERT INTO Bills_Products (BillID, ProductID, Quantity)
        VALUES (v_bill_id, v_product_ids[i], v_quantities[i]);
    END LOOP;

    -- 4. Reducir el stock según la cantidad comprada
    FOR i IN 1..array_length(v_product_ids, 1) LOOP
        UPDATE Products
        SET Stock = Stock - v_quantities[i]
        WHERE ID = v_product_ids[i];
    END LOOP;

    RAISE NOTICE 'Factura % creada', v_bill_id;
END $$;


ALTER TABLE Bills ADD COLUMN Status VARCHAR(20) NOT NULL DEFAULT 'Completada';

