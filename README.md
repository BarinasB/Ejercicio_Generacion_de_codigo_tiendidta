 
 Ejercicio  Generacion automatica de codigo tiendita  
 
 cordial saludo profe 
 para la ejecucion del codigo se debe proceder a ejercutar el script entity_codegen.py  
 
 Como procedimiento se modelaron las entidades correspondientes al negocio de la tiendita como se puede evidenciar en la siguiente imagen 
 
 ![image](https://user-images.githubusercontent.com/90980492/201242872-6f7a53a2-6527-44ac-b4f5-02f3862ce59e.png)

 se colocaron las entidades en el archivo tiendita.ent de la forma que establecen las librerias jinja y textx

 se procedio a crear las plantillas de generacion de codigo para la capa de controladores web y de repositorio de base de datos, en los archivos 
 
 repositories.template 
 restserv.template 
 
 se modifico el script de entity_codegen.py para incluir la generacion de archivos con las plantillas
 
 la capa de controladores rest esta basada en flask 
 la capa de repositorio de base de datos esta basada en el ORM SQLALCHEMY
 los archivos de controlador tienen el sufijo controller y los archivos de repositorio tienen el sufijo repo  
 
Integrantes 

Brayan Estiven Barinas PErdomo cod 20221099001 <br/>
Juan David Gutierrez Rodriguez cod 20221099004  <br/>
Ferney Alonso Moreno Pineda cod 20221099011
 
 

