-- create trigger
CREATE TRIGGER quantity_order
AFTER INSERT ON orders
FOR EACH ROW
UPDATE item SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
