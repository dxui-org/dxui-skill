# app.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-errappnotrunning"></a>
## ErrAppNotRunning

Source: `app.go:27`

```text
ErrAppNotRunning reports an Update attempted outside App.Run.
```

```go
var // ErrAppNotRunning reports an Update attempted outside App.Run.
ErrAppNotRunning = errors.New("dxui: app is not running")
```

<a id="api-errappclosed"></a>
## ErrAppClosed

Source: `app.go:29`

```text
ErrAppClosed reports an operation submitted after shutdown was requested.
```

```go
var // ErrAppClosed reports an operation submitted after shutdown was requested.
ErrAppClosed = errors.New("dxui: app is closing")
```

<a id="api-runtimediagnostics"></a>
## RuntimeDiagnostics

Source: `app.go:41`

```text
RuntimeDiagnostics is a backend-neutral snapshot of the running or most
recently stopped native runtime.
```

```go
type RuntimeDiagnostics struct {
	SDLVersion             string
	RendererName           string
	LogicalSize            Size
	PixelSize              Size
	PixelDensity           float32
	DisplayScale           float32
	FrameCount             uint64
	WindowCreates          uint64
	RendererCreateAttempts uint64
	RendererCreates        uint64
	ExposeEvents           uint64
	ResizeEvents           uint64
	ScaleEvents            uint64
	NoopViewportEvents     uint64
	RendererResetEvents    uint64
	BuildCount             uint64
	LayoutCount            uint64
	PaintCount             uint64
	SoftwareFallback       bool
	CountersEnabled        bool
	EventCount             uint64
	ReconcileCount         uint64
	PaintNodeCount         uint64
	TextureCreates         uint64
	TextureDestroys        uint64
	CacheBytes             uint64
	CacheBudgetBytes       uint64
	CacheEntries           uint64
	FontResources          uint64
	ImageResources         uint64
	RendererResources      uint64
	Goroutines             int
	GoHeapBytes            uint64
	GoHeapObjects          uint64
	GoTotalAllocBytes      uint64
	GoMallocs              uint64
	EventToPresent         TimingSummary
	FrameTime              TimingSummary
}
```

<a id="api-timingsummary"></a>
## TimingSummary

Source: `app.go:83`

```text
TimingSummary reports a bounded percentile distribution in nanoseconds.
```

```go
type TimingSummary struct {
	Count, Samples      uint64
	P50NS, P95NS, P99NS int64
}
```

<a id="api-app"></a>
## App

Source: `app.go:90`

```text
App owns one application runtime, one main window and any child windows. An
App is single-use: Run may be called exactly once.
```

```go
type App struct {
}
```

<a id="api-layoutcontext"></a>
## LayoutContext

Source: `app.go:152`

```text
LayoutContext is the logical space available to the root builder. It
contains no backend values. A constraint-aware build runs once initially
and once for the final resize/scale event in each drained event batch.
```

```go
type LayoutContext struct{ Width, Height float32 }
```

<a id="api-newapp"></a>
## NewApp

Source: `app.go:155`

```text
NewApp creates an application configuration without loading SDL.
```

```go
func NewApp(options AppOptions) *App
```

<a id="api-app-runresponsive"></a>
## App.RunResponsive

Source: `app.go:181`

```text
RunResponsive is Run with a root builder that may choose a different view
structure from the current logical window size. Measuring a result never
invokes the builder again; only a later coalesced viewport event can do so.
```

```go
func (a *App) RunResponsive(root func(LayoutContext) View) error
```

<a id="api-app-run"></a>
## App.Run

Source: `app.go:206`

```text
Run creates the native window, builds root, and owns the process main thread
until the app closes. Call it directly from main, before moving UI work to
other goroutines. Run is blocking and may be called only once, including
after a startup or runtime error. A nil root is rejected before the App is
consumed. Startup, build, renderer, callback, and event-loop failures are
returned; OnError also observes runtime failures when configured.
```

```go
func (a *App) Run(root func() View) (runErr error)
```

<a id="api-app-settheme"></a>
## App.SetTheme

Source: `app.go:411`

```text
SetTheme validates and copies a complete Primitive -> Semantic -> Component
theme atomically. Equal themes are a no-op. A relevant metric-token change
schedules layout; visual-only resolved changes schedule display/paint only.
While Run is active, call SetTheme from a UI callback or inside Update.
```

```go
func (a *App) SetTheme(source Theme) error
```

<a id="api-app-setclipboardtext"></a>
## App.SetClipboardText

Source: `app.go:499`

```text
SetClipboardText writes UTF-8 text to the system clipboard. While Run is
active, call it from a UI callback or inside Update so the native operation
remains on the UI thread. Invalid UTF-8 is normalized to replacement runes.
```

```go
func (a *App) SetClipboardText(value string) error
```

<a id="api-app-close"></a>
## App.Close

Source: `app.go:529`

```text
Close requests application shutdown and safely wakes a blocked event wait.
It may be called from callbacks or any goroutine. Repeated calls and calls
made before Run are no-ops.
```

```go
func (a *App) Close()
```

<a id="api-app-update"></a>
## App.Update

Source: `app.go:548`

```text
Update queues a state update for FIFO execution on the UI thread, then
rebuilds the root once after the batch. It never executes update on the
caller's goroutine and is safe to call from any goroutine.
```

```go
func (a *App) Update(update func()) error
```

<a id="api-app-invalidate"></a>
## App.Invalidate

Source: `app.go:574`

```text
Invalidate requests a rebuild of the main window only. It is safe from any
goroutine; child windows use Window.Invalidate.
```

```go
func (a *App) Invalidate() error
```

<a id="api-app-diagnostics"></a>
## App.Diagnostics

Source: `app.go:597`

```text
Diagnostics returns a race-safe, SDL-free runtime snapshot.
```

```go
func (a *App) Diagnostics() RuntimeDiagnostics
```
