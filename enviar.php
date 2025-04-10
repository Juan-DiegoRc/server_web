<?php

enviar($_POST['nombre'],$_FILES['adjunto']['name']);

function enviar($nombre,$adjunto){
    if(isset($_POST)){
    
    if($adjunto) {

    $dir_subida = 'otros/';
    $archivo = $dir_subida . basename($adjunto);
    //Se sube 
    move_uploaded_file(from: $_FILES['adjunto']['tmp_name'], to: $archivo);
    } 
}
}
?>