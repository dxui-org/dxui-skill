# icon/catalog/catalog_generated.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-entry"></a>
## Entry

Source: `icon/catalog/catalog_generated.go:11`

```text
Entry maps a Lucide kebab-case name and Go constructor name to its lazy icon constructor.
```

```go
type Entry struct {
	Name   string
	GoName string
	Icon   func() dxui.IconData
}
```

<a id="api-icons"></a>
## Icons

Source: `icon/catalog/catalog_generated.go:18`

```text
Icons contains all canonical icons and aliases. Importing catalog intentionally makes the full library reachable.
```

```go
var Icons []Entry
```
