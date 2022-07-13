INSERT INTO public.producto(
	id, nombre, categoria, precio)
	VALUES 
	( 'galletas 1' , 'comida para perros','1500'),
	( 'galletas 2' , 'comida para perros','2500'),
	( 'galletas 3' , 'comida para perros','500'),
	( 'galletas 4' , 'comida para perros','100'),
	( 'galletas 5' , 'comida para perros','2000'),
	( 'galletas 6' , 'comida para perros','4500');


INSERT INTO public.usuario(
	codigo, nombre, email, contrasena)
	VALUES
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1234'),
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1235'),
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1236'),
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1237'),
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1238'),
	( 15986662, '1', 'Arnoldo' , 'a.ramos1@ducocu.cl','1239');



INSERT INTO public.contacto(
	codigo, run, dv, nombres, apellido_paterno, apellido_materno, email, telefono, asunto)
	VALUES 
	( 15986662, '1', 'Arnoldo' , 'Ramos', 'Acevedo', 'a.ramos1@ducocu.cl', '+56964735999', 'compra galletas para perro1'),
	( 12986664, 'k', 'Maria' , 'Ramos', 'Acevedo', 'a.ramos2@ducocu.cl', '+56964735999', 'compra galletas para perro2'),
	( 9986664, '1', 'Arnoldo' , 'Ramos', 'Acevedo', 'a.ramos3@ducocu.cl', '+56964735999', 'compra galletas para perro3'),
	( 15986564, '1', 'Arnoldo' , 'Ramos', 'Acevedo', 'a.ramos4@ducocu.cl', '+56964735999', 'compra galletas para perro4'),
	( 23986664, 'k', 'Arnoldo' , 'Ramos', 'Acevedo', 'a.ramos5@ducocu.cl', '+56964735999', 'compra galletas para perro5'),
	( 3986664, '7', 'Arnoldo' , 'Ramos', 'Acevedo', 'a.ramos6@ducocu.cl', '+56964735999', 'compra galletas para perro6');