# provaider_id, provaider_name, provaider_address, provaider_industry, provaider_location,
# provaider_postal_code, provaider_email, provaider_notes, provaider_telephone,
# provaider_created, provaider_status
create_provaiders_table = """
    CREATE TABLE provaiders(
      provaider_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      provaider_name VARCHAR(40) NOT NULL,
      provaider_address VARCHAR(60) NOT NULL,
      provaider_industry VARCHAR(20),
      provaider_location VARCHAR(20),
      provaider_postal_code INT,
      provaider_email VARCHAR(20),
      provaider_notes VARCHAR(60),
      provaider_telephone INT,
      provaider_created datetime NOT NULL,
      provaider_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""
# one to one: one product from one provaider!
create_products_table = """
    CREATE TABLE products(
      product_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      provaider INT DEFAULT NULL,
      product_name VARCHAR(40) NOT NULL,
      product_sku_num VARCHAR(20) NOT NULL,
      product_description VARCHAR(60) NOT NULL,
      product_price decimal,
      product_discount INT,
      product_tax INT,
      product_pvp decimal,
      product_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      product_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_services_table = """
    CREATE TABLE services(
      service_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      service_name VARCHAR(40) NOT NULL,
      service_sku_num VARCHAR(20) NOT NULL,
      service_description VARCHAR(60) NOT NULL,
      service_price decimal,
      service_discount INT,
      service_tax INT,
      service_pvp decimal,
      service_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      service_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_offers_table = """
    CREATE TABLE offers(
      offer_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      products INT DEFAULT NULL,
      offer_name VARCHAR(40) NOT NULL,
      offer_description VARCHAR(60) NOT NULL,
      offer_price decimal,
      offer_discount INT,
      offer_tax INT,
      offer_pvp decimal,
      offer_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      offer_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_budgets_table = """
    CREATE TABLE budgets(
      budget_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      products INT DEFAULT NULL,
      budget_name VARCHAR(40) NOT NULL,
      budget_description VARCHAR(60) NOT NULL,
      budget_price decimal,
      budget_discount INT,
      budget_tax INT,
      budget_pvp decimal,
      budget_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      budget_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_bills_table = """
    CREATE TABLE bills(
      bill_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      products INT DEFAULT NULL,
      bill_name VARCHAR(40) NOT NULL,
      bill_description VARCHAR(60) NOT NULL,
      bill_price decimal,
      bill_discount INT,
      bill_tax INT,
      bill_pvp decimal,
      bill_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      bill_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_orders_table = """
    CREATE TABLE orders(
      order_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      products INT DEFAULT NULL,
      order_name VARCHAR(40) NOT NULL,
      order_description VARCHAR(60) NOT NULL,
      order_price decimal,
      order_discount INT,
      order_tax INT,
      order_pvp decimal,
      order_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      order_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

create_delivery_notes_table = """
    CREATE TABLE delivery_notes(
      dn_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      products INT DEFAULT NULL,
      dn_name VARCHAR(40) NOT NULL,
      dn_description VARCHAR(60) NOT NULL,
      dn_price decimal,
      dn_discount INT,
      dn_tax INT,
      dn_pvp decimal,
      dn_last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      dn_status BOOLEAN NOT NULL DEFAULT '1'
    );
"""

################################################
############### TABLE INSERTS ##################
################################################
insert_provaider = """
( NULL, 'name', 'addr', 'indust', 'loc', 08000, 'mail@str', 'notes', 6006060, now(), 1);
"""

insert_products = """
( NULL, 'name', '123AA89-99z', 'description', 1.99, 20, 16, 200.42, NULL, 1)
"""

insert_services = """
(NULL, 'name', 12345AA-ff3R, 'description', 17.42, 20, 16, 200.42, 0)
"""

insert_offers = """
(NULL, 10, 'name', 'description', 17.42, 25, 16, 200.17, 1)
"""

insert_budgets = """
(NULL, 10, 'name', 'description', 17.42, 20, 16, 200.42, 0)
"""

insert_bills = """
(NULL, 10, 'name', 'description', 17.42, 20, 16, 200.42, 1)
"""

insert_orders = """
(NULL, 10, 'name', 'description', 17.42, 20, 16, 200.42, 1)
"""

insert_dn = """
(NULL, 10, 'name', 'description', 17.42, 20, 16, 200.42, 1)
"""
