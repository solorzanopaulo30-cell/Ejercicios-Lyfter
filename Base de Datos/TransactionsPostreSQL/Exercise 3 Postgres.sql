-- Ejercicio 3: Transacción de retorno de productos
-- Verifica que la factura existe, devuelve el stock de cada producto
-- comprado y marca la factura como Retornada.
-- Todo en un solo bloque: si algo falla, se deshace todo.

DO $$
DECLARE
    v_bill_id INTEGER := 1;
    v_status  VARCHAR(20);
    r         RECORD;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Bills WHERE ID = v_bill_id) THEN
        RAISE EXCEPTION 'La factura % no existe', v_bill_id;
    END IF;

    SELECT Status INTO v_status FROM Bills WHERE ID = v_bill_id;
    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada', v_bill_id;
    END IF;

    FOR r IN SELECT ProductID, Quantity FROM Bills_Products WHERE BillID = v_bill_id LOOP
        UPDATE Products
        SET Stock = Stock + r.Quantity
        WHERE ID = r.ProductID;
    END LOOP;

    UPDATE Bills SET Status = 'Retornada' WHERE ID = v_bill_id;

    RAISE NOTICE 'Factura % retornada', v_bill_id;
END $$;