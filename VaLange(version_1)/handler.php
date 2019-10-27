<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
/*
Tested working with PHP5.4 and above (including PHP 7 )

 */
require_once './vendor/autoload.php';

use FormGuide\Handlx\FormHandler;


$pp = new FormHandler();

$validator = $pp->getValidator();
$validator->fields(['nom','prénom','email'])->areRequired()->maxLength(50);
$validator->field('institution')->maxLength(6000);
$validator->field('email')->isEmail();
$validator->field('agree')->maxLength(6000);
$validator->field("nom_de_l'enfant")->maxLength(6000);
$validator->field('genre')->maxLength(6000);
$validator->field('age')->maxLength(6000);
$validator->field('localisation')->maxLength(6000);
$validator->field('langue_français')->maxLength(6000);
$validator->field('langue_anglais')->maxLength(6000);
$validator->field('langue_italien')->maxLength(6000);
$validator->field('langue_portugais')->maxLength(6000);
$validator->field('langue_autre')->maxLength(6000);
$validator->field('genre_de_discours')->maxLength(6000);


$pp->attachFiles(['file']);


$pp->sendEmailTo('contactvalange@gmail.com'); // ← Your email here

echo $pp->process($_POST);
