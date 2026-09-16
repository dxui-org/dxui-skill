# view.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-view"></a>
## View

Source: `view.go:42`

```text
View is an immutable description. Its representation is deliberately
private and never contains backend or SDL handles. The zero value is invalid
as a root or child; a failed tree update leaves the last valid view visible.
```

```go
type View struct{}
```

<a id="api-view-withkey"></a>
## View.WithKey

Source: `view.go:47`

```text
WithKey returns an independent description whose sibling-local key is key.
The receiver and any descriptions that share its node are unchanged. This
does not add a container or retained identity level.
```

```go
func (view View) WithKey(key string) View
```

<a id="api-view-withstyle"></a>
## View.WithStyle

Source: `view.go:55`

```text
WithStyle returns an independent description whose complete local Style is
style. Replacement is intentional: zero values, nil slices, and explicit
empty slices keep their normal Style meanings. This does not add a container
or retained identity level.
```

```go
func (view View) WithStyle(style Style) View
```

<a id="api-box"></a>
## Box

Source: `view.go:231`

```text
Box creates a single-line flex description. Direction defaults to Vertical.
Zero children are valid; a zero View among the supplied children is rejected
transactionally.
```

```go
func Box(props BoxProps, children ...View) View
```

<a id="api-scroll"></a>
## Scroll

Source: `view.go:241`

```text
Scroll creates a clipped, one-child scrolling viewport.
```

```go
func Scroll(props ScrollProps, child View) View
```

<a id="api-virtuallist"></a>
## VirtualList

Source: `view.go:249`

```text
VirtualList creates a vertical fixed-row virtualized viewport. The runtime
builds only the visible rows plus the configured bounded overscan.
```

```go
func VirtualList(props VirtualListProps) View
```

<a id="api-select"></a>
## Select

Source: `view.go:256`

```text
Select creates a controlled custom popup Select. Options are copied.
```

```go
func Select(props SelectProps) View
```

<a id="api-popover"></a>
## Popover

Source: `view.go:273`

```text
Popover creates a controlled interactive overlay around one anchor and one
content view. The content remains retained but is painted only in the
window-level overlay layer while Open is true.
```

```go
func Popover(props PopoverProps, anchor, content View) View
```

<a id="api-tooltip"></a>
## Tooltip

Source: `view.go:282`

```text
Tooltip creates a delayed, non-interactive overlay around one anchor and
one content view.
```

```go
func Tooltip(props TooltipProps, anchor, content View) View
```

<a id="api-tabs"></a>
## Tabs

Source: `view.go:300`

```text
Tabs creates a controlled horizontal tab selector. Items are copied.
```

```go
func Tabs(props TabsProps) View
```

<a id="api-menu"></a>
## Menu

Source: `view.go:314`

```text
Menu creates an inline vertical or horizontal action list with an optional
controlled selected Value. Items are copied. Vertical is the zero value.
```

```go
func Menu(props MenuProps) View
```

<a id="api-text"></a>
## Text

Source: `view.go:327`

```text
Text creates a text description.
```

```go
func Text(props TextProps) View
```

<a id="api-label"></a>
## Label

Source: `view.go:335`

```text
Label creates text with the default text style.
```

```go
func Label(value string) View
```

<a id="api-button"></a>
## Button

Source: `view.go:338`

```text
Button creates a semantic button description.
```

```go
func Button(props ButtonProps, child View) View
```

<a id="api-textbutton"></a>
## TextButton

Source: `view.go:348`

```text
TextButton creates a Button whose text is centered in its content box.
Use Button directly when the content is not a simple label.
```

```go
func TextButton(props ButtonProps, label string) View
```

<a id="api-buttongroup"></a>
## ButtonGroup

Source: `view.go:359`

```text
ButtonGroup creates a non-focusable horizontal or vertical group containing
only Button views. Horizontal is the zero-value orientation.
```

```go
func ButtonGroup(props ButtonGroupProps, buttons ...View) View
```

<a id="api-inputgroup"></a>
## InputGroup

Source: `view.go:385`

```text
InputGroup creates one horizontal visual control from a required Input and
optional prefix/suffix views. The supplied Input keeps its own identity and
editing state; the group suppresses only the Input's internal surface paint.
```

```go
func InputGroup(props InputGroupProps, content InputGroupContent) View
```

<a id="api-badge"></a>
## Badge

Source: `view.go:422`

```text
Badge creates a compact, non-interactive one-child label.
```

```go
func Badge(props BadgeProps, child View) View
```

<a id="api-progressbar"></a>
## ProgressBar

Source: `view.go:432`

```text
ProgressBar creates a deterministic, non-interactive progress indicator.
```

```go
func ProgressBar(props ProgressBarProps) View
```

<a id="api-toggleswitch"></a>
## ToggleSwitch

Source: `view.go:439`

```text
ToggleSwitch creates a controlled semantic switch description.
```

```go
func ToggleSwitch(props ToggleSwitchProps) View
```

<a id="api-slider"></a>
## Slider

Source: `view.go:446`

```text
Slider creates a controlled single-value horizontal slider description.
```

```go
func Slider(props SliderProps) View
```

<a id="api-checkbox"></a>
## Checkbox

Source: `view.go:453`

```text
Checkbox creates a controlled semantic checkbox with one label child.
```

```go
func Checkbox(props CheckboxProps, label View) View
```

<a id="api-radio"></a>
## Radio

Source: `view.go:461`

```text
Radio creates a controlled semantic radio button with one label child.
```

```go
func Radio(props RadioProps, label View) View
```

<a id="api-icon"></a>
## Icon

Source: `view.go:485`

```text
Icon creates a lightweight vector icon description.
```

```go
func Icon(props IconProps) View
```

<a id="api-image"></a>
## Image

Source: `view.go:496`

```text
Image creates a guarded raster image description.
```

```go
func Image(props ImageProps) View
```

<a id="api-avatar"></a>
## Avatar

Source: `view.go:503`

```text
Avatar creates a centered cover image with circular or square clipping.
```

```go
func Avatar(props AvatarProps) View
```

<a id="api-input"></a>
## Input

Source: `view.go:534`

```text
Input creates a controlled, single-line input description.
```

```go
func Input(props InputProps) View
```

<a id="api-textarea"></a>
## Textarea

Source: `view.go:544`

```text
Textarea creates a controlled multiline text editor description.
```

```go
func Textarea(props TextareaProps) View
```
