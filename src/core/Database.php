<?php
declare(strict_types=1);

namespace App\Core;

use PDO;

final class Database
{
    private static ?PDO $pdo = null;

    public static function connection(): PDO
    {
        if (self::$pdo === null) {
            $dbPath = dirname(__DIR__, 2) . '/data/landing.db';
            if (!is_dir(dirname($dbPath))) {
                mkdir(dirname($dbPath), 0777, true);
            }
            self::$pdo = new PDO('sqlite:' . $dbPath, null, null, [
                PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES   => false,
            ]);
            self::$pdo->exec('PRAGMA foreign_keys=ON');
        }
        return self::$pdo;
    }
}