from flet import *
import sqlite3
conn = sqlite3.connect('db/dbone.db',check_same_thread=False)

tb = DataTable(
	columns=[
		DataColumn(Text("actions")),
		DataColumn(Text("Marca")),
		DataColumn(Text("Modelo")),
		DataColumn(Text("Patente")),
		DataColumn(Text("Comprador")),
		DataColumn(Text("Telefono")),
		DataColumn(Text("gender")),
	],
	rows=[]

	)


def showdelete(e):
	try:
		myid = int(e.control.data)
		c = conn.cursor()
		c.execute("DELETE FROM users WHERE id=?", (myid,))
		conn.commit()
		print("success delete")
		tb.rows.clear()	
		calldb()
		tb.update()

	except Exception as e:
		print(e)


id_edit = Text()
name_edit = TextField(label="Marca")
age_edit = TextField(label="Modelo")
contact_edit = TextField(label="Patente")
gender_edit = RadioGroup(content=Column([
		Radio(value="man",label="man"),
        Radio(value="woman",label="woman"),

	]))
email_edit = TextField(label="Comprador")
address_edit = TextField(label="Telefono")


def hidedlg(e):
	dlg.visible = False
	dlg.update()


def updateandsave(e):
	try:
		myid = id_edit.value
		c = conn.cursor()
		c.execute("UPDATE users SET Marca=?, Modelo=?, Patente=?, gender=?, Comprador=?, Telefono=? WHERE id=?", (name_edit.value, contact_edit.value, age_edit.value, gender_edit.value, email_edit.value, address_edit.value, myid))
		conn.commit()
		print("success Edit ")
		tb.rows.clear()	
		calldb()
		dlg.visible = False
		dlg.update()
		tb.update()
	except Exception as e:
		print(e)

dlg = Container(
	bgcolor="blue200",
	padding=10,
			content=Column([
				Row([
				Text("Edit Form",size=30,weight="bold"),
				IconButton(icon="close",on_click=hidedlg),
					],alignment="spaceBetween"),
				name_edit,
				age_edit,
				contact_edit,
				Text("Select Gender",size=20,weight="bold"),
				gender_edit,
				email_edit,
				address_edit,
				ElevatedButton("Update",on_click=updateandsave)

				])
)




def showedit(e):
	data_edit = e.control.data
	id_edit.value = data_edit['id']
	name_edit.value = data_edit['Marca']
	age_edit.value = data_edit['Modelo']
	contact_edit.value = data_edit['Patente']
	gender_edit.value = data_edit['gender']
	email_edit.value = data_edit['Comprador']
	address_edit.value = data_edit['Telefono']

	dlg.visible = True
	dlg.update()


def calldb():
	c = conn.cursor()
	c.execute("SELECT * FROM users")
	users = c.fetchall()
	print(users)
	if not users == "":
		keys = ['id', 'Marca', 'Modelo', 'Patente', 'gender', 'Comprador', 'Telefono']
		result = [dict(zip(keys, values)) for values in users]
		for x in result:
			tb.rows.append(
				DataRow(
                    cells=[
                        DataCell(Row([
                        	IconButton(icon="create",icon_color="blue",
                        		data=x,
                        		on_click=showedit

                        		),
                        	IconButton(icon="delete",icon_color="red",
                        		data=x['id'],
                        	on_click=showdelete

                        		),
                        	])),
                        DataCell(Text(x['Marca'])),
                        DataCell(Text(x['Modelo'])),
                        DataCell(Text(x['Patente'])),
                        DataCell(Text(x['email'])),
                        DataCell(Text(x['Comprador'])),
                        DataCell(Text(x['Telefono'])),
                    ],
                ),

		)


calldb()





dlg.visible = False
mytable = Column([
	dlg,
	Row([tb],scroll="always")
	])