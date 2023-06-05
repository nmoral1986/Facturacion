import psycopg2


def select(connect, comm):
    cursor = connect.cursor()
    postgreSQL_select_Query = comm

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    product = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in product:
        print("Nombre = ", row[1], )
        print("peso = ", row[2])
        print('Price  = $', row[3])
        print('Price de venta  = $', row[4], "\n")

def connect_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="password",
                                      host="0.0.0.0",
                                      port="5432",
                                      database="nuevadb")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

def insert_data_productos(connect, nam, pes, val, val_vent):
    cursor = connect.cursor()
    cursor.execute('select max(id) from producto')
    product = cursor.fetchall()
    d=product[0][0]+1

    concatenar= (f"""insert into producto(id,nombre,peso,costo,presio_de_venta) values ({d},'{nam}',{pes},{val},{val_vent})""")
    print(concatenar)
    cursor.execute(concatenar)
    connect.commit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = connect_db()
    select(conn, 'select * from producto')
    print("agregar datos a la tabla producto", '\n')
    print("inserte Nombre de producto, peso, valor, valor de venta")
    name=input()
    peso=input()
    valor=input()
    valor_venta=input()
    insert_data_productos(conn, name,peso,valor,valor_venta)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
