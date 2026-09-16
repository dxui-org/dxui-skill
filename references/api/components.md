# components.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-scrollaxis"></a>
## ScrollAxis

Source: `components.go:12`

```text
ScrollAxis selects the axes whose content is measured without a maximum
and whose retained offset may change.
```

```go
type ScrollAxis uint8
```

<a id="api-scrollvertical"></a>
## ScrollVertical

Source: `components.go:15`

```go
const (
	ScrollVertical ScrollAxis = iota
	ScrollHorizontal
	ScrollBoth
)
```

<a id="api-scrollhorizontal"></a>
## ScrollHorizontal

Source: `components.go:16`

See the preceding constant block for the exact value and type.

<a id="api-scrollboth"></a>
## ScrollBoth

Source: `components.go:17`

See the preceding constant block for the exact value and type.

<a id="api-scrollbarpolicy"></a>
## ScrollbarPolicy

Source: `components.go:22`

```text
ScrollbarPolicy controls the overlay scrollbar. Hidden suppresses scrollbar
paint and pointer interaction without disabling wheel/trackpad scrolling.
```

```go
type ScrollbarPolicy uint8
```

<a id="api-scrollbarauto"></a>
## ScrollbarAuto

Source: `components.go:25`

```go
const (
	ScrollbarAuto ScrollbarPolicy = iota
	ScrollbarAlways
	ScrollbarHidden
)
```

<a id="api-scrollbaralways"></a>
## ScrollbarAlways

Source: `components.go:26`

See the preceding constant block for the exact value and type.

<a id="api-scrollbarhidden"></a>
## ScrollbarHidden

Source: `components.go:27`

See the preceding constant block for the exact value and type.

<a id="api-scrollprops"></a>
## ScrollProps

Source: `components.go:36`

```text
ScrollProps configures a one-child clipped viewport. Offset is authoritative
when set. Otherwise InitialOffset is used only when the view is first
mounted; later positions are preserved while the view keeps its identity.
OnScroll reports the complete offset. Without Offset, movement updates
retained state even with a nil callback; with Offset it only proposes a
change. Scroll has no Disabled or ReadOnly property.
```

```go
type ScrollProps struct {
	Key           string
	Style         Style
	Token         ComponentToken
	States        StateStyles
	Pointer       PointerBehavior
	Axis          ScrollAxis
	InitialOffset Option[Point]
	Offset        Option[Point]
	Scrollbar     ScrollbarPolicy
	// OnScroll reports movement. Nil still scrolls internally when Offset is unset; a set Offset stays authoritative.
	OnScroll func(Point)
}
```

<a id="api-virtuallistprops"></a>
## VirtualListProps

Source: `components.go:54`

```text
VirtualListProps configures a vertical, fixed-row-height virtual list.
Count and Version identify one immutable data snapshot; increment Version
whenever row keys or content may have changed. ItemKey and Build run on the
UI thread and must be deterministic and side-effect free for that snapshot.
```

```go
type VirtualListProps struct {
	Key           string
	Style         Style
	Token         ComponentToken
	States        StateStyles
	Pointer       PointerBehavior
	Count         int
	Version       uint64
	RowHeight     float32
	Overscan      int
	InitialOffset Option[Point]
	Offset        Option[Point]
	Scrollbar     ScrollbarPolicy
	ItemKey       func(index int) string
	Build         func(index int) View
	OnScroll      func(Point)
}
```

<a id="api-textwrap"></a>
## TextWrap

Source: `components.go:73`

```text
TextWrap selects the MVP simple wrapping policy.
```

```go
type TextWrap uint8
```

<a id="api-textnowrap"></a>
## TextNoWrap

Source: `components.go:76`

```go
const (
	TextNoWrap TextWrap = iota
	TextWrapWords
)
```

<a id="api-textwrapwords"></a>
## TextWrapWords

Source: `components.go:77`

See the preceding constant block for the exact value and type.

<a id="api-textprops"></a>
## TextProps

Source: `components.go:83`

```text
TextProps configures simple left-to-right text. Invalid UTF-8 is normalized
to U+FFFD when Text is constructed. TextWrapWords collapses whitespace and
wraps only at word boundaries; it is not Unicode line-break conformance.
```

```go
type TextProps struct {
	Key      string
	Style    Style
	Token    ComponentToken
	States   StateStyles
	Pointer  PointerBehavior
	Value    string
	Wrap     TextWrap
	MaxLines int
}
```

<a id="api-buttonprops"></a>
## ButtonProps

Source: `components.go:95`

```text
ButtonProps configures a semantic button.
```

```go
type ButtonProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Variant ButtonVariant
	Tone    ButtonTone
	Size    ButtonSize
	// Disabled removes focus and activation and suppresses Hover, Pressed, and Focus styles.
	Disabled bool
	// OnPress runs on activation. Nil preserves focus and interaction visuals but emits no action.
	OnPress func()
}
```

<a id="api-buttongrouporientation"></a>
## ButtonGroupOrientation

Source: `components.go:111`

```text
ButtonGroupOrientation selects the main axis used to arrange buttons.
```

```go
type ButtonGroupOrientation uint8
```

<a id="api-buttongrouphorizontal"></a>
## ButtonGroupHorizontal

Source: `components.go:114`

```go
const (
	ButtonGroupHorizontal ButtonGroupOrientation = iota
	ButtonGroupVertical
)
```

<a id="api-buttongroupvertical"></a>
## ButtonGroupVertical

Source: `components.go:115`

See the preceding constant block for the exact value and type.

<a id="api-buttongroupprops"></a>
## ButtonGroupProps

Source: `components.go:120`

```text
ButtonGroupProps configures a non-focusable connected container of Button
views.
```

```go
type ButtonGroupProps struct {
	Key         string
	Style       Style
	Token       ComponentToken
	States      StateStyles
	Pointer     PointerBehavior
	Orientation ButtonGroupOrientation
	// Dividers enables one themed border between adjacent Buttons.
	Dividers bool
}
```

<a id="api-inputgroupprops"></a>
## InputGroupProps

Source: `components.go:133`

```text
InputGroupProps configures the non-focusable visual container around one
Input and its optional leading and trailing content.
```

```go
type InputGroupProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
}
```

<a id="api-inputgroupcontent"></a>
## InputGroupContent

Source: `components.go:144`

```text
InputGroupContent identifies the required Input and optional adornments.
Prefix and Suffix may contain passive views or Buttons; other focusable
controls and nested text editors are rejected.
```

```go
type InputGroupContent struct {
	Input  View
	Prefix Option[View]
	Suffix Option[View]
}
```

<a id="api-badgeprops"></a>
## BadgeProps

Source: `components.go:152`

```text
BadgeProps configures a compact, non-interactive label around one arbitrary
child. The child inherits the Badge text/icon tint unless locally overridden.
```

```go
type BadgeProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
}
```

<a id="api-progressbarprops"></a>
## ProgressBarProps

Source: `components.go:163`

```text
ProgressBarProps configures a deterministic, non-interactive progress
indicator. Value is clamped to [0,1] for painting. NaN and negative
infinity paint empty; positive infinity paints complete.
```

```go
type ProgressBarProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Value   float32
}
```

<a id="api-pathverb"></a>
## PathVerb

Source: `components.go:174`

```text
PathVerb identifies one command in dxui's deliberately small vector icon
format. It is not an SVG parser or a general scene graph.
```

```go
type PathVerb = icondata.PathVerb
```

<a id="api-pathmove"></a>
## PathMove

Source: `components.go:177`

```go
const (
	PathMove  = icondata.PathMove
	PathLine  = icondata.PathLine
	PathQuad  = icondata.PathQuad
	PathCubic = icondata.PathCubic
	PathClose = icondata.PathClose
)
```

<a id="api-pathline"></a>
## PathLine

Source: `components.go:178`

See the preceding constant block for the exact value and type.

<a id="api-pathquad"></a>
## PathQuad

Source: `components.go:179`

See the preceding constant block for the exact value and type.

<a id="api-pathcubic"></a>
## PathCubic

Source: `components.go:180`

See the preceding constant block for the exact value and type.

<a id="api-pathclose"></a>
## PathClose

Source: `components.go:181`

See the preceding constant block for the exact value and type.

<a id="api-pathcommand"></a>
## PathCommand

Source: `components.go:186`

```text
PathCommand stores up to three points. Move/Line use Points[0], Quad uses
Points[0:2], and Cubic uses all three points.
```

```go
type PathCommand = icondata.PathCommand
```

<a id="api-rect"></a>
## Rect

Source: `components.go:189`

```text
Rect is a rectangle in logical units.
```

```go
type Rect = icondata.Rect
```

<a id="api-icondata"></a>
## IconData

Source: `components.go:192`

```text
IconData is immutable dxui path data in ViewBox coordinates.
```

```go
type IconData = icondata.Data
```

<a id="api-iconstrokewidth"></a>
## IconStrokeWidth

Source: `components.go:197`

```text
IconStrokeWidth is a stroke width in icon view-box units. Zero selects the
Lucide default of 2. It affects immutable stroked resources and is ignored
by legacy filled IconData.
```

```go
type IconStrokeWidth float32
```

<a id="api-iconprops"></a>
## IconProps

Source: `components.go:201`

```text
IconProps configures a vector icon. Size is measured in logical units; zero
uses the current component theme default.
```

```go
type IconProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Data    IconData
	Size    float32
	Color   ColorValue
	// StrokeWidth uses icon view-box units and defaults to 2. Values must be
	// finite and non-negative; zero means the default rather than no stroke.
	StrokeWidth IconStrokeWidth
}
```

<a id="api-toggleswitchprops"></a>
## ToggleSwitchProps

Source: `components.go:216`

```text
ToggleSwitchProps configures a controlled switch.
```

```go
type ToggleSwitchProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	// Checked is authoritative. Disabled cancels interaction and removes the focus stop.
	Checked, Disabled bool
	// OnChange proposes Checked. Nil preserves focus/press visuals without changing Checked.
	OnChange func(bool)
}
```

<a id="api-sliderprops"></a>
## SliderProps

Source: `components.go:232`

```text
SliderProps configures a controlled single-value horizontal slider. Value
is authoritative; OnChange receives a clamped, step-aligned proposal. Zero
Min and Max select the default 0..100 range. Step defaults to 1 when it is
non-positive or non-finite. Other invalid ranges are inert.
```

```go
type SliderProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Value   float32
	Min     float32
	Max     float32
	Step    float32
	// Disabled cancels dragging and removes focus and pointer interaction.
	Disabled bool
	// OnChange proposes Value. Nil preserves focus and drag visuals without changing Value.
	OnChange func(float32)
}
```

<a id="api-checkboxprops"></a>
## CheckboxProps

Source: `components.go:249`

```text
CheckboxProps configures a controlled two-state checkbox.
```

```go
type CheckboxProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	// Checked is authoritative. Disabled cancels interaction and removes the focus stop.
	Checked, Disabled bool
	// OnChange proposes Checked. Nil preserves focus/press visuals without changing Checked.
	OnChange func(bool)
}
```

<a id="api-radioprops"></a>
## RadioProps

Source: `components.go:263`

```text
RadioProps configures a controlled radio button. Selected is authoritative;
OnSelect is called only when an enabled, unselected Radio is activated.
```

```go
type RadioProps struct {
	Key      string
	Style    Style
	Token    ComponentToken
	States   StateStyles
	Pointer  PointerBehavior
	Selected bool
	// Disabled cancels interaction and removes the focus stop.
	Disabled bool
	// OnSelect proposes selection of an unselected Radio. Nil preserves focus and press visuals.
	OnSelect func()
}
```

<a id="api-imagesource"></a>
## ImageSource

Source: `components.go:284`

```text
ImageSource is an immutable, comparable handle to application image data.
```

```go
type ImageSource struct{}
```

<a id="api-imagebytes"></a>
## ImageBytes

Source: `components.go:287`

```text
ImageBytes copies encoded PNG, JPEG, or GIF bytes immediately.
```

```go
func ImageBytes(data []byte) ImageSource
```

<a id="api-imagefile"></a>
## ImageFile

Source: `components.go:292`

```text
ImageFile records a path that is read by the image engine on demand.
```

```go
func ImageFile(path string) ImageSource
```

<a id="api-imagefromgo"></a>
## ImageFromGo

Source: `components.go:295`

```text
ImageFromGo records an immutable-by-contract Go image source.
```

```go
func ImageFromGo(value image.Image) ImageSource
```

<a id="api-imagefit"></a>
## ImageFit

Source: `components.go:298`

```text
ImageFit selects the supported destination fitting policy.
```

```go
type ImageFit uint8
```

<a id="api-imagecontain"></a>
## ImageContain

Source: `components.go:301`

```go
const (
	ImageContain ImageFit = iota
	ImageCover
	ImageFill
	ImageNone
)
```

<a id="api-imagecover"></a>
## ImageCover

Source: `components.go:302`

See the preceding constant block for the exact value and type.

<a id="api-imagefill"></a>
## ImageFill

Source: `components.go:303`

See the preceding constant block for the exact value and type.

<a id="api-imagenone"></a>
## ImageNone

Source: `components.go:304`

See the preceding constant block for the exact value and type.

<a id="api-imageprops"></a>
## ImageProps

Source: `components.go:309`

```text
ImageProps configures a decoded raster image. Alignment components are in
[0,1].
```

```go
type ImageProps struct {
	Key       string
	Style     Style
	Token     ComponentToken
	States    StateStyles
	Pointer   PointerBehavior
	Source    ImageSource
	Fit       ImageFit
	Alignment Point
	MaxPixels int64
	// OnLoad and OnError are optional notifications; nil does not stop decoding.
	OnLoad  func(Size)
	OnError func(error)
}
```

<a id="api-avatarshape"></a>
## AvatarShape

Source: `components.go:325`

```text
AvatarShape selects the fixed Avatar clipping shape.
```

```go
type AvatarShape uint8
```

<a id="api-avatarcircle"></a>
## AvatarCircle

Source: `components.go:328`

```go
const (
	AvatarCircle AvatarShape = iota
	AvatarSquare
)
```

<a id="api-avatarsquare"></a>
## AvatarSquare

Source: `components.go:329`

See the preceding constant block for the exact value and type.

<a id="api-avatarprops"></a>
## AvatarProps

Source: `components.go:335`

```text
AvatarProps configures a square, centered cover image. Size is measured in
logical units; zero uses the current component theme default. Explicit Style
width and height take precedence.
```

```go
type AvatarProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Source  ImageSource
	Shape   AvatarShape
	Size    float32
	// OnLoad and OnError are optional notifications; nil does not stop decoding.
	OnLoad  func(Size)
	OnError func(error)
}
```

<a id="api-textrange"></a>
## TextRange

Source: `components.go:350`

```text
TextRange uses Unicode code-point (rune) offsets, never UTF-8 byte offsets.
```

```go
type TextRange struct{ Start, End int }
```

<a id="api-inputprops"></a>
## InputProps

Source: `components.go:359`

```text
InputProps configures a controlled single-line input. OnChange receives the
complete proposed value after committed text, paste, cut, deletion, undo, or
redo. The application accepts the edit by returning that value from the next
build; leaving Value unchanged rejects it. IME composition does not call
OnChange. Selection and TextRange use rune indices. A nil OnChange makes the
input read-only by behavior, without Disabled styling. ReadOnly also blocks
pre-edit; focus, selection, non-password copy, and OnSubmit remain available.
```

```go
type InputProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Value   string
	// OnChange proposes Value. Nil blocks editing and pre-edit, but preserves selection and copy.
	OnChange  func(string)
	Selection Option[TextRange]
	// OnSelectionChange reports rune selection. Nil retains internal selection; Selection, when set, wins on rebuild.
	OnSelectionChange func(TextRange)
	Placeholder       string
	Password          bool
	// ShowPasswordToggle adds an internal trailing visibility button only when
	// Password is also true. Visibility is temporary state owned by the Input.
	ShowPasswordToggle bool
	// Disabled removes focus, stops native text input, and cancels composition, drag, and press.
	Disabled bool
	// ReadOnly blocks edits and pre-edit while allowing focus, navigation, selection, and non-password copy.
	ReadOnly bool
	// OnSubmit handles Enter independently of OnChange and ReadOnly. Nil emits no submit; Disabled blocks it.
	OnSubmit func()
}
```

<a id="api-textareaprops"></a>
## TextareaProps

Source: `components.go:389`

```text
TextareaProps configures a controlled multiline editor and follows the same
controlled Value and rune-indexed selection contract as Input. TextWrapWords
is a simple LTR/CJK word-wrap policy, not full Unicode line breaking. A nil
OnChange preserves navigation, selection, copy, and scrolling without edits
or pre-edit; it does not imply Disabled styling.
```

```go
type TextareaProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Value   string
	// OnChange proposes Value. Nil blocks editing and pre-edit, but preserves selection and copy.
	OnChange  func(string)
	Selection Option[TextRange]
	// OnSelectionChange reports rune selection. Nil retains internal selection; Selection, when set, wins on rebuild.
	OnSelectionChange func(TextRange)
	Placeholder       string
	// Disabled removes focus, stops native text input, and cancels composition, drag, and press.
	Disabled bool
	// ReadOnly blocks edits and pre-edit while allowing focus, navigation, selection, and non-password copy.
	ReadOnly bool
	Wrap     TextWrap
}
```

<a id="api-selectoption"></a>
## SelectOption

Source: `components.go:412`

```text
SelectOption is one immutable entry in a Select. Value must be non-empty and
unique within the Select; it is both the controlled application value and
the stable identity used when options reorder.
```

```go
type SelectOption struct {
	Value    string
	Label    string
	Disabled bool
}
```

<a id="api-selectprops"></a>
## SelectProps

Source: `components.go:422`

```text
SelectProps configures a controlled custom popup Select. Value is
authoritative; an empty or unmatched Value displays Placeholder.
```

```go
type SelectProps struct {
	Key         string
	Style       Style
	Token       ComponentToken
	States      StateStyles
	Pointer     PointerBehavior
	Value       string
	Options     []SelectOption
	Placeholder string
	// Disabled closes the popup, cancels interaction, and removes the focus stop.
	Disabled bool
	// OnChange proposes Value. Nil still allows popup browsing, navigation, and dismissal.
	OnChange func(string)
}
```

<a id="api-overlayplacement"></a>
## OverlayPlacement

Source: `components.go:440`

```text
OverlayPlacement selects the preferred side and alignment of a window-level
overlay. Placement automatically flips to the opposite side when it has
more usable room and the preferred side cannot fit the content.
```

```go
type OverlayPlacement uint8
```

<a id="api-overlaybottomstart"></a>
## OverlayBottomStart

Source: `components.go:443`

```go
const (
	OverlayBottomStart OverlayPlacement = iota
	OverlayBottom
	OverlayBottomEnd
	OverlayTopStart
	OverlayTop
	OverlayTopEnd
	OverlayLeft
	OverlayRight
)
```

<a id="api-overlaybottom"></a>
## OverlayBottom

Source: `components.go:444`

See the preceding constant block for the exact value and type.

<a id="api-overlaybottomend"></a>
## OverlayBottomEnd

Source: `components.go:445`

See the preceding constant block for the exact value and type.

<a id="api-overlaytopstart"></a>
## OverlayTopStart

Source: `components.go:446`

See the preceding constant block for the exact value and type.

<a id="api-overlaytop"></a>
## OverlayTop

Source: `components.go:447`

See the preceding constant block for the exact value and type.

<a id="api-overlaytopend"></a>
## OverlayTopEnd

Source: `components.go:448`

See the preceding constant block for the exact value and type.

<a id="api-overlayleft"></a>
## OverlayLeft

Source: `components.go:449`

See the preceding constant block for the exact value and type.

<a id="api-overlayright"></a>
## OverlayRight

Source: `components.go:450`

See the preceding constant block for the exact value and type.

<a id="api-popoverprops"></a>
## PopoverProps

Source: `components.go:458`

```text
PopoverProps configures a controlled, interactive window-level overlay.
Open is authoritative. Anchor activation, Escape, and an outside primary
click submit the proposed state through OnOpenChange. Nil leaves Open
unchanged and preserves open-content interaction. There is no Disabled or
ReadOnly property; an anchor child does not disable the Popover host.
```

```go
type PopoverProps struct {
	Key       string
	Style     Style
	Token     ComponentToken
	States    StateStyles
	Pointer   PointerBehavior
	Open      bool
	Placement OverlayPlacement
	Offset    MetricValue
	// OnOpenChange proposes Open. Nil leaves Open unchanged; open content remains interactive.
	OnOpenChange func(bool)
}
```

<a id="api-tooltipprops"></a>
## TooltipProps

Source: `components.go:474`

```text
TooltipProps configures a non-interactive window-level hint. Hovering or
keyboard-focusing the anchor starts Delay; leaving both closes it. A zero
Delay selects the built-in 500 ms default.
```

```go
type TooltipProps struct {
	Key       string
	Style     Style
	Token     ComponentToken
	States    StateStyles
	Pointer   PointerBehavior
	Placement OverlayPlacement
	Offset    MetricValue
	Delay     time.Duration
	Disabled  bool
}
```

<a id="api-tabitem"></a>
## TabItem

Source: `components.go:488`

```text
TabItem is one immutable label in Tabs. Value must be non-empty and unique
within the component.
```

```go
type TabItem struct {
	Value    string
	Label    string
	Disabled bool
}
```

<a id="api-tabsprops"></a>
## TabsProps

Source: `components.go:497`

```text
TabsProps configures a controlled horizontal tab selector. Value is
authoritative; Tabs renders only the selector and applications render the
corresponding content separately.
```

```go
type TabsProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior
	Value   string
	Items   []TabItem
	// Disabled cancels interaction and removes the focus stop.
	Disabled bool
	// OnChange proposes a different Value. Nil retains active-item navigation and press visuals.
	OnChange func(string)
}
```

<a id="api-menuorientation"></a>
## MenuOrientation

Source: `components.go:512`

```text
MenuOrientation selects the axis used to arrange Menu items.
```

```go
type MenuOrientation uint8
```

<a id="api-menuvertical"></a>
## MenuVertical

Source: `components.go:515`

```go
const (
	MenuVertical MenuOrientation = iota
	MenuHorizontal
)
```

<a id="api-menuhorizontal"></a>
## MenuHorizontal

Source: `components.go:516`

See the preceding constant block for the exact value and type.

<a id="api-menuitem"></a>
## MenuItem

Source: `components.go:521`

```text
MenuItem is one immutable action in a Menu. Value must be non-empty and
unique within the component.
```

```go
type MenuItem struct {
	Value    string
	Label    string
	Disabled bool
}
```

<a id="api-menuprops"></a>
## MenuProps

Source: `components.go:530`

```text
MenuProps configures an inline action list. Value optionally identifies the
application-controlled selected item. Activating an enabled item calls
OnAction with that item's Value, including when it is already selected.
```

```go
type MenuProps struct {
	Key         string
	Style       Style
	Token       ComponentToken
	States      StateStyles
	Pointer     PointerBehavior
	Orientation MenuOrientation
	Value       string
	Items       []MenuItem
	// Disabled cancels interaction and removes the focus stop.
	Disabled bool
	// OnAction invokes an enabled item, including the selected one. Nil retains navigation and visuals.
	OnAction func(string)
}
```
