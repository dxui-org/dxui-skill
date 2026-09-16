# dxui.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-option"></a>
## Option

Source: `dxui.go:16`

```text
Option distinguishes an explicitly supplied zero value from an unset value.
```

```go
type Option[T any] struct {
}
```

<a id="api-some"></a>
## Some

Source: `dxui.go:22`

```text
Some creates a set option.
```

```go
func Some[T any](value T) Option[T]
```

<a id="api-point"></a>
## Point

Source: `dxui.go:27`

```text
Point is a position or offset in logical units.
```

```go
type Point = icondata.Point
```

<a id="api-size"></a>
## Size

Source: `dxui.go:30`

```text
Size is a width and height in logical units.
```

```go
type Size struct{ Width, Height float32 }
```

<a id="api-rgbacolor"></a>
## RGBAColor

Source: `dxui.go:35`

```text
RGBAColor is an 8-bit non-premultiplied RGBA color.

The former Color type name is now the discoverable color-token namespace.
```

```go
type RGBAColor struct{ R, G, B, A uint8 }
```

<a id="api-rgba"></a>
## RGBA

Source: `dxui.go:38`

```text
RGBA creates an 8-bit non-premultiplied color.
```

```go
func RGBA(r, g, b, a uint8) RGBAColor
```

<a id="api-rendererpreference"></a>
## RendererPreference

Source: `dxui.go:41`

```text
RendererPreference selects the preferred renderer creation policy.
```

```go
type RendererPreference uint8
```

<a id="api-rendererauto"></a>
## RendererAuto

Source: `dxui.go:44`

```go
const (
	RendererAuto RendererPreference = iota
	RendererSoftware
)
```

<a id="api-renderersoftware"></a>
## RendererSoftware

Source: `dxui.go:45`

See the preceding constant block for the exact value and type.

<a id="api-cachebudgets"></a>
## CacheBudgets

Source: `dxui.go:56`

```text
CacheBudgets bounds CPU and renderer-owned text, icon, and image resources. Zero
selects defaults: FontBytes 32 MiB, TextSourceBytes 2 MiB, GlyphBytes 2 MiB,
TextMeasureBytes 1 MiB, ImageBytes 2 MiB, and ShadowBytes 2 MiB. ImageBytes
bounds inactive reusable CPU pixels and renderer textures. Unique images in
the committed display are working-set resources charged at four bytes per
source pixel until that display releases them. A negative cache budget
disables that cache; negative FontBytes or TextSourceBytes permits no
application fonts or retained text/icon masks respectively.
```

```go
type CacheBudgets struct {
	FontBytes        int
	TextSourceBytes  int
	GlyphBytes       int
	TextMeasureBytes int
	ImageBytes       int
	ShadowBytes      int
}
```

<a id="api-appoptions"></a>
## AppOptions

Source: `dxui.go:69`

```text
AppOptions configures an App's main window and shared runtime. Its
zero value selects documented window, renderer, cache, font, and theme
defaults; invalid dimensions, renderer values, fonts, or themes are reported
by App.Run before native event processing begins.
```

```go
type AppOptions struct {
	Title               string
	Width, Height       float32
	MinWidth, MinHeight float32
	Renderer            RendererPreference
	Background          RGBAColor
	Caches              CacheBudgets
	Fonts               []Font
	DefaultFont         FontFamily
	// DisableSystemFontFallback prevents lazy deterministic system-CJK font
	// loading. The zero value enables fallback after all application fonts and
	// dxui's built-in Latin font.
	DisableSystemFontFallback bool
	Theme                     Theme
	Shortcuts                 []Shortcut
	// OnCloseRequest handles a native window-close request on the UI thread.
	// A nil callback closes the App. A non-nil callback must call Close when it
	// accepts the request.
	OnCloseRequest func(*App)
	// OnError observes recoverable build and callback failures on the UI
	// thread. When nil, the failure terminates Run and is returned.
	OnError func(error)
	// OnShown runs once on the UI thread after the complete first frame was
	// presented and the native window was shown successfully. It is not called
	// after startup failure or on later builds/presents.
	OnShown func(*App)
	// Diagnostics enables bounded event/timing/resource counters.
	// It is false by default so release event and render paths avoid the work.
	Diagnostics bool
}
```

<a id="api-windowoptions"></a>
## WindowOptions

Source: `dxui.go:103`

```text
WindowOptions configures an independent native child window. Theme, fonts,
renderer preference, cache budgets and App shortcuts are inherited from the
owning App. Callbacks execute on the App UI thread.
```

```go
type WindowOptions struct {
	Title               string
	Width, Height       float32
	MinWidth, MinHeight float32
	Background          RGBAColor
	Shortcuts           []Shortcut
	// OnCloseRequest may reject a native close request by returning without
	// calling Window.Close. A nil callback accepts the request.
	OnCloseRequest func(*Window)
	// OnShown runs once after the complete first frame is presented and the
	// hidden native window has been shown successfully.
	OnShown func(*Window)
}
```

<a id="api-shortcutkey"></a>
## ShortcutKey

Source: `dxui.go:118`

```text
ShortcutKey is a backend-neutral semantic key used by an App shortcut.
```

```go
type ShortcutKey uint8
```

<a id="api-keyenter"></a>
## KeyEnter

Source: `dxui.go:121`

```go
const (
	KeyEnter ShortcutKey = iota + 1
	KeyBackspace
	Key0
	Key1
	Key2
	Key3
	Key4
	Key5
	Key6
	Key7
	Key8
	Key9
	KeyPlus
	KeyMinus
	KeyMultiply
	KeyDivide
	KeyDecimal
	KeyEquals
)
```

<a id="api-keybackspace"></a>
## KeyBackspace

Source: `dxui.go:122`

See the preceding constant block for the exact value and type.

<a id="api-key0"></a>
## Key0

Source: `dxui.go:123`

See the preceding constant block for the exact value and type.

<a id="api-key1"></a>
## Key1

Source: `dxui.go:124`

See the preceding constant block for the exact value and type.

<a id="api-key2"></a>
## Key2

Source: `dxui.go:125`

See the preceding constant block for the exact value and type.

<a id="api-key3"></a>
## Key3

Source: `dxui.go:126`

See the preceding constant block for the exact value and type.

<a id="api-key4"></a>
## Key4

Source: `dxui.go:127`

See the preceding constant block for the exact value and type.

<a id="api-key5"></a>
## Key5

Source: `dxui.go:128`

See the preceding constant block for the exact value and type.

<a id="api-key6"></a>
## Key6

Source: `dxui.go:129`

See the preceding constant block for the exact value and type.

<a id="api-key7"></a>
## Key7

Source: `dxui.go:130`

See the preceding constant block for the exact value and type.

<a id="api-key8"></a>
## Key8

Source: `dxui.go:131`

See the preceding constant block for the exact value and type.

<a id="api-key9"></a>
## Key9

Source: `dxui.go:132`

See the preceding constant block for the exact value and type.

<a id="api-keyplus"></a>
## KeyPlus

Source: `dxui.go:133`

See the preceding constant block for the exact value and type.

<a id="api-keyminus"></a>
## KeyMinus

Source: `dxui.go:134`

See the preceding constant block for the exact value and type.

<a id="api-keymultiply"></a>
## KeyMultiply

Source: `dxui.go:135`

See the preceding constant block for the exact value and type.

<a id="api-keydivide"></a>
## KeyDivide

Source: `dxui.go:136`

See the preceding constant block for the exact value and type.

<a id="api-keydecimal"></a>
## KeyDecimal

Source: `dxui.go:137`

See the preceding constant block for the exact value and type.

<a id="api-keyequals"></a>
## KeyEquals

Source: `dxui.go:138`

See the preceding constant block for the exact value and type.

<a id="api-shortcutmodifiers"></a>
## ShortcutModifiers

Source: `dxui.go:143`

```text
ShortcutModifiers are matched exactly. Primary substitutes for Command on
macOS and Control elsewhere; callers do not also set that physical field.
```

```go
type ShortcutModifiers struct{ Shift, Control, Alt, Super, Primary bool }
```

<a id="api-shortcut"></a>
## Shortcut

Source: `dxui.go:148`

```text
Shortcut binds one application-window key chord to a semantic action.
Focused editors and built-in control keys have priority. Repeat enables
repeated key-down activation; otherwise native repeat is consumed silently.
```

```go
type Shortcut struct {
	Key       ShortcutKey
	Modifiers ShortcutModifiers
	Repeat    bool
	OnPress   func()
}
```
