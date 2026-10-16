<?php
declare(strict_types=1);

namespace App\Core;

final class Router
{
    private array $routes = [];

    public function get(string $p, callable $h): void { $this->routes['GET'][$p] = $h; }
    public function post(string $p, callable $h): void { $this->routes['POST'][$p] = $h; }
    public function put(string $p, callable $h): void { $this->routes['PUT'][$p] = $h; }
    public function delete(string $p, callable $h): void { $this->routes['DELETE'][$p] = $h; }

    public function dispatch(Request $r): void
    {
        $m = $r->method();
        $seg = $r->segments();
        $path = '/' . implode('/', $seg);
        $table = $this->routes[$m] ?? [];
        foreach ($table as $pattern => $handler) {
            if ($this->match($pattern, $path, $params)) {
                call_user_func($handler, $r, ...array_values($params));
                return;
            }
        }
        http_response_code(404);
        echo json_encode(['success' => false, 'error' => 'NOT_FOUND']);
        exit;
    }

    private function match(string $pattern, string $path, &$params): bool
    {
        $params = [];
        $pats = explode('/', trim($pattern, '/'));
        $paths = explode('/', trim($path, '/'));
        if (count($pats) !== count($paths) && !str_contains($pattern, '{')) {
            return false;
        }
        for ($i = 0; $i < max(count($pats), count($paths)); $i++) {
            $pat = $pats[$i] ?? null;
            $pth = $paths[$i] ?? null;
            if ($pat === null || $pth === null) return false;
            if (preg_match('#^\{(.+)\}$#', $pat, $m)) {
                $params[$m[1]] = $pth;
                continue;
            }
            if ($pat !== $pth) return false;
        }
        return true;
    }
}