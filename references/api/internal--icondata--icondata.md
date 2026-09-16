# internal/icondata/icondata.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-point"></a>
## Point

Source: `internal/icondata/icondata.go:12`

```text
Point is a position in icon view-box coordinates.
```

```go
type Point struct{ X, Y float32 }
```

<a id="api-rect"></a>
## Rect

Source: `internal/icondata/icondata.go:15`

```text
Rect is a rectangle in icon view-box coordinates.
```

```go
type Rect struct{ X, Y, Width, Height float32 }
```

<a id="api-pathverb"></a>
## PathVerb

Source: `internal/icondata/icondata.go:18`

```text
PathVerb identifies one vector path command.
```

```go
type PathVerb uint8
```

<a id="api-pathmove"></a>
## PathMove

Source: `internal/icondata/icondata.go:21`

```go
const (
	PathMove PathVerb = iota
	PathLine
	PathQuad
	PathCubic
	PathClose
)
```

<a id="api-pathline"></a>
## PathLine

Source: `internal/icondata/icondata.go:22`

See the preceding constant block for the exact value and type.

<a id="api-pathquad"></a>
## PathQuad

Source: `internal/icondata/icondata.go:23`

See the preceding constant block for the exact value and type.

<a id="api-pathcubic"></a>
## PathCubic

Source: `internal/icondata/icondata.go:24`

See the preceding constant block for the exact value and type.

<a id="api-pathclose"></a>
## PathClose

Source: `internal/icondata/icondata.go:25`

See the preceding constant block for the exact value and type.

<a id="api-pathcommand"></a>
## PathCommand

Source: `internal/icondata/icondata.go:29`

```text
PathCommand stores up to three points.
```

```go
type PathCommand struct {
	Verb   PathVerb
	Points [3]Point
}
```

<a id="api-paintmode"></a>
## PaintMode

Source: `internal/icondata/icondata.go:35`

```text
PaintMode identifies whether a packed path is filled or stroked.
```

```go
type PaintMode uint8
```

<a id="api-paintstroke"></a>
## PaintStroke

Source: `internal/icondata/icondata.go:38`

```go
const (
	PaintStroke PaintMode = iota
	PaintFill
)
```

<a id="api-paintfill"></a>
## PaintFill

Source: `internal/icondata/icondata.go:39`

See the preceding constant block for the exact value and type.

<a id="api-path"></a>
## Path

Source: `internal/icondata/icondata.go:43`

```text
Path is one decoded path with a single paint mode.
```

```go
type Path struct {
	Mode     PaintMode
	Commands []PathCommand
}
```

<a id="api-data"></a>
## Data

Source: `internal/icondata/icondata.go:51`

```text
Data is immutable when returned by Packed. Commands remains exported for
compatibility with application-authored filled icons; callers own that
slice and dxui copies it when constructing a View.
```

```go
type Data struct {
	ViewBox  Rect
	Commands []PathCommand
}
```

<a id="api-data-ispacked"></a>
## Data.IsPacked

Source: `internal/icondata/icondata.go:70`

```text
IsPacked reports whether data uses the immutable generated representation.
```

```go
func (data Data) IsPacked() bool
```

<a id="api-data-identity"></a>
## Data.Identity

Source: `internal/icondata/icondata.go:73`

```text
Identity returns a stable content identity without exposing packed bytes.
```

```go
func (data Data) Identity() uint64
```

<a id="api-data-paths"></a>
## Data.Paths

Source: `internal/icondata/icondata.go:99`

```text
Paths validates and decodes data. Legacy Commands form one filled path.
```

```go
func (data Data) Paths(maxCommands int) ([]Path, error)
```
