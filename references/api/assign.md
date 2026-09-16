# assign.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-assign"></a>
## Assign

Source: `assign.go:6`

```text
Assign returns a callback that stores its argument in target. It is intended
for simple controlled UI callbacks. Assign panics when target is nil; it does
not schedule work or replace App.Update for cross-goroutine mutation.
```

```go
func Assign[T any](target *T) func(T)
```
