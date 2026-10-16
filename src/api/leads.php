<?php
require_once dirname(__DIR__).'/core/Database.php';
require_once dirname(__DIR__).'/core/Request.php';

use App\Core\Database;
use App\Core\Request;

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET,POST,OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD']==='OPTIONS'){ http_response_code(204); exit; }

$db = Database::connection();
$db->exec("CREATE TABLE IF NOT EXISTS leads(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,email TEXT NOT NULL,telefono TEXT,interes TEXT,mensaje TEXT,created_at DATETIME DEFAULT CURRENT_TIMESTAMP)");

$r = new Request();
if($r->method()==='POST'){
  $d = $r->jsonBody();
  if(empty($d['nombre'])||empty($d['email'])){ http_response_code(422); echo json_encode(['success'=>false,'error'=>'nombre y email requeridos']); exit; }
  $st=$db->prepare("INSERT INTO leads(nombre,email,telefono,interes,mensaje) VALUES(?,?,?,?,?)");
  $st->execute([$d['nombre'],$d['email'],$d['telefono']??null,$d['interes']??null,$d['mensaje']??null]);
  echo json_encode(['success'=>true,'id'=>$db->lastInsertId()]);
  exit;
}
if($r->method()==='GET'){
  $st=$db->query("SELECT * FROM leads ORDER BY id DESC LIMIT 100");
  echo json_encode(['success'=>true,'data'=>$st->fetchAll()]);
  exit;
}
http_response_code(405); echo json_encode(['success'=>false,'error'=>'METHOD_NOT_ALLOWED']);
