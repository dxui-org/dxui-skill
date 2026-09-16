# window.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-errwindowclosed"></a>
## ErrWindowClosed

Source: `window.go:15`

```text
ErrWindowClosed reports an operation on a child window after close.
```

```go
var // ErrWindowClosed reports an operation on a child window after close.
ErrWindowClosed = errors.New("dxui: window is closed")
```

<a id="api-errwindownotrunning"></a>
## ErrWindowNotRunning

Source: `window.go:17`

```text
ErrWindowNotRunning reports child-window creation outside App.Run.
```

```go
var // ErrWindowNotRunning reports child-window creation outside App.Run.
ErrWindowNotRunning = errors.New("dxui: window runtime is not running")
```

<a id="api-window"></a>
## Window

Source: `window.go:23`

```text
Window is an opaque, concurrency-safe handle to a child native window.
Component construction remains on the root dxui API; a Window only owns
window-level lifecycle and scheduling operations.
```

```go
type Window struct {
}
```

<a id="api-app-createwindow"></a>
## App.CreateWindow

Source: `window.go:49`

```text
CreateWindow creates a hidden native child window and prepares its complete
first frame. It must be called from a UI callback or App.Update closure.
Failure releases every partially created child resource and leaves existing
windows unchanged.
```

```go
func (a *App) CreateWindow(options WindowOptions, root func() View) (*Window, error)
```

<a id="api-window-update"></a>
## Window.Update

Source: `window.go:167`

```text
Update queues a child-window state mutation and rebuilds only that window.
```

```go
func (w *Window) Update(update func()) error
```

<a id="api-window-invalidate"></a>
## Window.Invalidate

Source: `window.go:187`

```text
Invalidate requests a rebuild of only this child window.
```

```go
func (w *Window) Invalidate() error
```

<a id="api-window-settitle"></a>
## Window.SetTitle

Source: `window.go:191`

```text
SetTitle changes the native title on the UI thread. It may be called from a
UI callback or App.Update closure and does not rebuild the root.
```

```go
func (w *Window) SetTitle(title string) error
```

<a id="api-window-setsize"></a>
## Window.SetSize

Source: `window.go:207`

```text
SetSize requests a new positive logical client size. The resulting native
viewport event drives layout; it is not presented speculatively.
```

```go
func (w *Window) SetSize(width, height float32) error
```

<a id="api-window-title"></a>
## Window.Title

Source: `window.go:234`

```text
Title returns the last successfully configured title.
```

```go
func (w *Window) Title() string
```

<a id="api-window-size"></a>
## Window.Size

Source: `window.go:245`

```text
Size returns the latest known logical client size. Native resize events and
successful SetSize calls update this snapshot.
```

```go
func (w *Window) Size() Size
```

<a id="api-window-maximize"></a>
## Window.Maximize

Source: `window.go:255`

```text
Maximize requests the platform's maximized window state.
```

```go
func (w *Window) Maximize() error
```

<a id="api-window-unmaximize"></a>
## Window.Unmaximize

Source: `window.go:267`

```text
Unmaximize restores a maximized window to its normal state.
```

```go
func (w *Window) Unmaximize() error
```

<a id="api-window-minimize"></a>
## Window.Minimize

Source: `window.go:270`

```text
Minimize requests the platform's minimized window state.
```

```go
func (w *Window) Minimize() error
```

<a id="api-window-unminimize"></a>
## Window.Unminimize

Source: `window.go:282`

```text
Unminimize restores a minimized window to its normal state.
```

```go
func (w *Window) Unminimize() error
```

<a id="api-window-ismaximized"></a>
## Window.IsMaximized

Source: `window.go:295`

```text
IsMaximized reports the latest state confirmed by native window events.
```

```go
func (w *Window) IsMaximized() bool
```

<a id="api-window-isminimized"></a>
## Window.IsMinimized

Source: `window.go:305`

```text
IsMinimized reports the latest state confirmed by native window events.
```

```go
func (w *Window) IsMinimized() bool
```

<a id="api-app-title"></a>
## App.Title

Source: `window.go:345`

```text
Main-window counterparts preserve App as the main lifecycle handle.
```

```go
func (a *App) Title() string
```

<a id="api-app-size"></a>
## App.Size

Source: `window.go:355`

```go
func (a *App) Size() Size
```

<a id="api-app-settitle"></a>
## App.SetTitle

Source: `window.go:365`

```go
func (a *App) SetTitle(title string) error
```

<a id="api-app-setsize"></a>
## App.SetSize

Source: `window.go:372`

```go
func (a *App) SetSize(width, height float32) error
```

<a id="api-app-maximize"></a>
## App.Maximize

Source: `window.go:379`

```go
func (a *App) Maximize() error
```

<a id="api-app-unmaximize"></a>
## App.Unmaximize

Source: `window.go:386`

```go
func (a *App) Unmaximize() error
```

<a id="api-app-minimize"></a>
## App.Minimize

Source: `window.go:393`

```go
func (a *App) Minimize() error
```

<a id="api-app-unminimize"></a>
## App.Unminimize

Source: `window.go:400`

```go
func (a *App) Unminimize() error
```

<a id="api-app-ismaximized"></a>
## App.IsMaximized

Source: `window.go:407`

```go
func (a *App) IsMaximized() bool
```

<a id="api-app-isminimized"></a>
## App.IsMinimized

Source: `window.go:413`

```go
func (a *App) IsMinimized() bool
```

<a id="api-window-close"></a>
## Window.Close

Source: `window.go:434`

```text
Close closes this child window without affecting its owner or siblings.
Repeated calls are no-ops.
```

```go
func (w *Window) Close()
```

<a id="api-window-diagnostics"></a>
## Window.Diagnostics

Source: `window.go:455`

```text
Diagnostics returns this window's backend-neutral counters.
```

```go
func (w *Window) Diagnostics() RuntimeDiagnostics
```

<a id="api-window-closed"></a>
## Window.Closed

Source: `window.go:463`

```text
Closed reports whether close has been requested or completed.
```

```go
func (w *Window) Closed() bool
```
