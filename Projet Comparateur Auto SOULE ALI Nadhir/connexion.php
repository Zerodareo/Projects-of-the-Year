<?php

$host = 'localhost';
$bdd = 'inventory';
$user = 'root';
$pwd = 'root';

try{ // Essayer
	$co = new PDO('mysql:host='.$host.';dbname='.$bdd, $user, $pwd);
}
catch(Exception $e){ // Capter l'erreur
	die( $e->getMessage() );
}

?>