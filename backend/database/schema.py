CLIENTS = "CREATE TABLE IF NOT EXISTS CLIENTS (" \
                          "client_id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "name text NOT NULL," \
                          "last_name text NOT NULL," \
                          "identity_card text," \
                          "email text," \
                          "phone_1 text," \
                          "phone_2 text," \
                          "address text NOT NULL" \
                          ");"

VEHICLES_TYPE = "CREATE TABLE IF NOT EXISTS VEHICLES_TYPE (" \
                          "vehicle_type_id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "brand text NOT NULL," \
                          "model text NOT NULL," \
                          "year integer NOT NULL" \
                          ");"


VEHICLES = "CREATE TABLE IF NOT EXISTS VEHICLES (" \
                          "vehicle_id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "client_id integer NOT NULL," \
                          "vehicle_type_id integer NOT NULL," \
                          "identity text NOT NULL," \
                          "color text NOT NULL, " \
                          "FOREIGN KEY (client_id) REFERENCES CLIENTS (client_id)" \
                          "FOREIGN KEY (vehicle_type_id) REFERENCES VEHICLES_TYPE(vehicle_type_id)" \
                          ");"

REPAIRS = "CREATE TABLE IF NOT EXISTS REPAIRS (" \
                          "repair_id integer PRIMARY KEY UNIQUE NOT NULL," \
                          "vehicle_id integer NOT NULL," \
                          "mileage real NOT NULL, " \
                          "client_observations TEXT," \
                          "mechanical_observations TEXT," \
                          "date_entry TEXT NOT NULL," \
                          "date_exit TEXT," \
                          "other_observations TEXT," \
                          "price REAL," \
                          "status integer NOT NULL," \
                          "FOREIGN KEY (vehicle_id) REFERENCES vehicle (vehicle_id)" \
                          "); """
