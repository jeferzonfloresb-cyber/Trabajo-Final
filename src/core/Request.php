<?php
declare(strict_types=1);

namespace App\Core;

final class Request
{
    private array $segments;
    private array $query;
    private array $body;
    private string $method;

    public function __construct()
    {
        $this->method = strtoupper($_SERVER['REQUEST_METHOD'] ?? 'GET');
        $uri = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?? '/';
        $this->segments = array_values(array_filter(explode('/', trim($uri, '/')), fn($s) => $s !== ''));
        $query = [];
        parse_str($_SERVER['QUERY_STRING'] ?? '', $query);
        $this->query = $query;
        $this->body = $_POST;
    }

    public function method(): string
    {
        return $this->method;
    }

    public function segments(): array
    {
        return $this->segments;
    }

    public function query(string $k, $d = null)
    {
        return $this->query[$k] ?? $d;
    }

    public function body(string $k = null, $d = null)
    {
        if ($k === null) {
            return $this->body;
        }
        return $this->body[$k] ?? $d;
    }

    public function jsonBody(): array
    {
        $raw = file_get_contents('php://input');
        if (!$raw) {
            return [];
        }
        $d = json_decode($raw, true);
        return is_array($d) ? $d : [];
    }
}