# style.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-length"></a>
## Length

Source: `style.go:13`

```text
Length is an opaque automatic, logical-pixel, or percentage length. Its zero
value means automatic sizing; use Px or Percent for an explicit value.
```

```go
type Length struct {
}
```

<a id="api-px"></a>
## Px

Source: `style.go:19`

```text
Px creates a logical-pixel length.
```

```go
func Px(value float32) Length
```

<a id="api-percent"></a>
## Percent

Source: `style.go:22`

```text
Percent creates a percentage length in the range 0..100.
```

```go
func Percent(value float32) Length
```

<a id="api-fill"></a>
## Fill

Source: `style.go:26`

```text
Fill is the common full-available-axis length. It is equivalent to
Percent(100) and remains subject to the parent's definite-size rules.
```

```go
func Fill() Length
```

<a id="api-metrictoken"></a>
## MetricToken

Source: `style.go:29`

```text
MetricToken names a theme metric.
```

```go
type MetricToken string
```

<a id="api-colortoken"></a>
## ColorToken

Source: `style.go:32`

```text
ColorToken names a theme color.
```

```go
type ColorToken string
```

<a id="api-metricvalue"></a>
## MetricValue

Source: `style.go:35`

```text
MetricValue is either a literal logical-unit metric or a theme token.
```

```go
type MetricValue struct {
}
```

<a id="api-metric"></a>
## Metric

Source: `style.go:43`

```text
Metric creates a literal metric.
```

```go
func Metric(value float32) MetricValue
```

<a id="api-noshrink"></a>
## NoShrink

Source: `style.go:47`

```text
NoShrink explicitly disables flex shrinking. It is equivalent to Some(0)
and is distinct from an unset Shrink, whose default is one.
```

```go
func NoShrink() Option[float32]
```

<a id="api-padding"></a>
## Padding

Source: `style.go:51`

```text
Padding applies one literal logical-unit metric to every edge. The returned
metrics are explicitly set, including when value is zero.
```

```go
func Padding(value float32) EdgeValues
```

<a id="api-paddingxy"></a>
## PaddingXY

Source: `style.go:55`

```text
PaddingXY applies literal logical-unit metrics to the horizontal and vertical
edges. The returned metrics are explicitly set, including zero values.
```

```go
func PaddingXY(horizontal, vertical float32) EdgeValues
```

<a id="api-margin"></a>
## Margin

Source: `style.go:64`

```text
Margin applies one literal logical-unit metric to every edge, like Padding.
The returned metrics are explicitly set, including when value is zero.
```

```go
func Margin(value float32) EdgeValues
```

<a id="api-marginxy"></a>
## MarginXY

Source: `style.go:68`

```text
MarginXY applies literal logical-unit metrics to the horizontal and vertical
edges, like PaddingXY. The returned metrics are explicitly set, including zero values.
```

```go
func MarginXY(horizontal, vertical float32) EdgeValues
```

<a id="api-round"></a>
## Round

Source: `style.go:72`

```text
Round applies one literal logical-unit radius to every corner. The returned
metrics are explicitly set, including when value is zero.
```

```go
func Round(value float32) CornerValues
```

<a id="api-tokenmetric"></a>
## TokenMetric

Source: `style.go:75`

```text
TokenMetric creates a token-backed metric.
```

```go
func TokenMetric(token MetricToken) MetricValue
```

<a id="api-colorvalue"></a>
## ColorValue

Source: `style.go:80`

```text
ColorValue is either a literal color or a theme token.
```

```go
type ColorValue struct {
}
```

<a id="api-colorrgba"></a>
## ColorRGBA

Source: `style.go:89`

```text
ColorRGBA creates an explicitly set literal paint color from RGBA channels,
including transparent zero. Use RGBA for raw RGBAColor data instead.
```

```go
func ColorRGBA(r, g, b, a uint8) ColorValue
```

<a id="api-literalcolor"></a>
## LiteralColor

Source: `style.go:93`

```text
LiteralColor wraps existing raw RGBA data as a literal paint color.
Use ColorRGBA when supplying channels directly.
```

```go
func LiteralColor(value RGBAColor) ColorValue
```

<a id="api-tokencolor"></a>
## TokenColor

Source: `style.go:96`

```text
TokenColor creates a token-backed paint color.
```

```go
func TokenColor(token ColorToken) ColorValue
```

<a id="api-edgevalues"></a>
## EdgeValues

Source: `style.go:102`

```text
EdgeValues contains metrics in top, right, bottom, left order. Its zero-value
fields are unset.
```

```go
type EdgeValues struct{ Top, Right, Bottom, Left MetricValue }
```

<a id="api-edges"></a>
## Edges

Source: `style.go:105`

```text
Edges creates explicit logical-unit edges in top, right, bottom, left order.
```

```go
func Edges(top, right, bottom, left float32) EdgeValues
```

<a id="api-uniformedges"></a>
## UniformEdges

Source: `style.go:115`

```text
UniformEdges applies one metric to every edge.
```

```go
func UniformEdges(value MetricValue) EdgeValues
```

<a id="api-cornervalues"></a>
## CornerValues

Source: `style.go:121`

```text
CornerValues contains radii in top-left, top-right, bottom-right, bottom-left order.
Its zero-value fields are unset.
```

```go
type CornerValues struct{ TopLeft, TopRight, BottomRight, BottomLeft MetricValue }
```

<a id="api-corners"></a>
## Corners

Source: `style.go:125`

```text
Corners creates explicit logical-unit radii in top-left, top-right,
bottom-right, bottom-left order.
```

```go
func Corners(topLeft, topRight, bottomRight, bottomLeft float32) CornerValues
```

<a id="api-uniformcorners"></a>
## UniformCorners

Source: `style.go:135`

```text
UniformCorners applies one radius to every corner.
```

```go
func UniformCorners(value MetricValue) CornerValues
```

<a id="api-position"></a>
## Position

Source: `style.go:140`

```text
Position controls normal-flow versus absolute layout.
```

```go
type Position uint8
```

<a id="api-positionflow"></a>
## PositionFlow

Source: `style.go:143`

```go
const (
	PositionFlow Position = iota
	PositionAbsolute
)
```

<a id="api-positionabsolute"></a>
## PositionAbsolute

Source: `style.go:144`

See the preceding constant block for the exact value and type.

<a id="api-insets"></a>
## Insets

Source: `style.go:148`

```text
Insets contains absolute-position insets.
```

```go
type Insets struct{ Top, Right, Bottom, Left Length }
```

<a id="api-overflow"></a>
## Overflow

Source: `style.go:151`

```text
Overflow controls container clipping.
```

```go
type Overflow uint8
```

<a id="api-overflowvisible"></a>
## OverflowVisible

Source: `style.go:154`

```go
const (
	OverflowVisible Overflow = iota
	OverflowClip
)
```

<a id="api-overflowclip"></a>
## OverflowClip

Source: `style.go:155`

See the preceding constant block for the exact value and type.

<a id="api-align"></a>
## Align

Source: `style.go:159`

```text
Align controls cross-axis alignment.
```

```go
type Align uint8
```

<a id="api-alignstart"></a>
## AlignStart

Source: `style.go:162`

```go
const (
	AlignStart Align = iota
	AlignCenter
	AlignEnd
	AlignStretch
)
```

<a id="api-aligncenter"></a>
## AlignCenter

Source: `style.go:163`

See the preceding constant block for the exact value and type.

<a id="api-alignend"></a>
## AlignEnd

Source: `style.go:164`

See the preceding constant block for the exact value and type.

<a id="api-alignstretch"></a>
## AlignStretch

Source: `style.go:165`

See the preceding constant block for the exact value and type.

<a id="api-justify"></a>
## Justify

Source: `style.go:169`

```text
Justify controls main-axis alignment.
```

```go
type Justify uint8
```

<a id="api-justifystart"></a>
## JustifyStart

Source: `style.go:172`

```go
const (
	JustifyStart Justify = iota
	JustifyCenter
	JustifyEnd
	JustifySpaceBetween
)
```

<a id="api-justifycenter"></a>
## JustifyCenter

Source: `style.go:173`

See the preceding constant block for the exact value and type.

<a id="api-justifyend"></a>
## JustifyEnd

Source: `style.go:174`

See the preceding constant block for the exact value and type.

<a id="api-justifyspacebetween"></a>
## JustifySpaceBetween

Source: `style.go:175`

See the preceding constant block for the exact value and type.

<a id="api-style"></a>
## Style

Source: `style.go:182`

```text
Style contains the supported layout, paint, and typography controls. Box
is always single-line; there is intentionally no wrap or order
property. The zero value is safe and selects intrinsic sizing and theme
defaults.
```

```go
type Style struct {
	Width, Height       Length
	MinWidth, MinHeight Length
	MaxWidth, MaxHeight Length
	Margin, Padding     EdgeValues
	Position            Position
	Insets              Insets
	Grow                float32
	Shrink              Option[float32]
	Basis               Length
	AlignSelf           Option[Align]
	ZIndex              int
	Overflow            Overflow
	Background          ColorValue
	Border              Border
	Radius              CornerValues
	// Shadow is an explicitly requested list of outer shadows. A nil value
	// leaves a theme/state value unchanged; a non-nil empty slice removes it.
	Shadow     []Shadow
	Opacity    Option[float32]
	Visibility Visibility
	Text       TextStyle
	// Force is applied after component and interaction-state styles. It is for
	// deliberate paint overrides such as suppressing a focus ring; ordinary
	// base appearance belongs in the fields above so Hover/Pressed/Focus remain
	// visible. Force cannot affect layout.
	Force StylePatch
}
```

<a id="api-visibility"></a>
## Visibility

Source: `style.go:212`

```text
Visibility controls whether a node contributes display items.
```

```go
type Visibility uint8
```

<a id="api-visible"></a>
## Visible

Source: `style.go:215`

```go
const (
	Visible Visibility = iota
	Hidden
)
```

<a id="api-hidden"></a>
## Hidden

Source: `style.go:216`

See the preceding constant block for the exact value and type.

<a id="api-pointerbehavior"></a>
## PointerBehavior

Source: `style.go:220`

```text
PointerBehavior controls pointer participation for a view subtree.
```

```go
type PointerBehavior uint8
```

<a id="api-pointerauto"></a>
## PointerAuto

Source: `style.go:223`

```go
const (
	PointerAuto PointerBehavior = iota
	// PointerNone excludes the view and all descendants. It is intended for
	// decorative overlays that must not intercept content below them.
	PointerNone
)
```

<a id="api-pointernone"></a>
## PointerNone

Source: `style.go:226`

```text
PointerNone excludes the view and all descendants. It is intended for
decorative overlays that must not intercept content below them.
```

See the preceding constant block for the exact value and type.

<a id="api-borderpattern"></a>
## BorderPattern

Source: `style.go:230`

```text
BorderPattern selects how a border is painted. The zero value is solid.
```

```go
type BorderPattern uint8
```

<a id="api-bordersolid"></a>
## BorderSolid

Source: `style.go:233`

```go
const (
	BorderSolid BorderPattern = iota
	BorderDashed
)
```

<a id="api-borderdashed"></a>
## BorderDashed

Source: `style.go:234`

See the preceding constant block for the exact value and type.

<a id="api-bordersides"></a>
## BorderSides

Source: `style.go:238`

```text
BorderSides selects edges. Zero means all edges, not an absent border.
```

```go
type BorderSides uint8
```

<a id="api-bordertop"></a>
## BorderTop

Source: `style.go:241`

```go
const (
	BorderTop BorderSides = 1 << iota
	BorderRight
	BorderBottom
	BorderLeft
	BorderAll = BorderTop | BorderRight | BorderBottom | BorderLeft
)
```

<a id="api-borderright"></a>
## BorderRight

Source: `style.go:242`

See the preceding constant block for the exact value and type.

<a id="api-borderbottom"></a>
## BorderBottom

Source: `style.go:243`

See the preceding constant block for the exact value and type.

<a id="api-borderleft"></a>
## BorderLeft

Source: `style.go:244`

See the preceding constant block for the exact value and type.

<a id="api-borderall"></a>
## BorderAll

Source: `style.go:245`

See the preceding constant block for the exact value and type.

<a id="api-border"></a>
## Border

Source: `style.go:250`

```text
Border is a paint-only border drawn inside a view's layout bounds.
Each side owns the nearest half of its two adjacent corner arcs.
```

```go
type Border struct {
	Width   MetricValue
	Color   ColorValue
	Pattern BorderPattern
	// Sides defaults to all edges. In Style, a Width/Color assignment resets
	// Sides too; otherwise nonzero Sides changes only edge selection.
	// StylePatch.Border replaces the complete Border.
	Sides BorderSides
}
```

<a id="api-noborder"></a>
## NoBorder

Source: `style.go:262`

```text
NoBorder explicitly clears the border width. In ordinary Style, later state
patches may restore a border; Style.Force is applied after those patches.
```

```go
func NoBorder() Border
```

<a id="api-stroke"></a>
## Stroke

Source: `style.go:265`

```text
Stroke creates a solid border with a literal logical-unit width.
```

```go
func Stroke(width float32, color ColorValue) Border
```

<a id="api-shadow"></a>
## Shadow

Source: `style.go:271`

```text
Shadow is an outer paint-only shadow. MVP shadows support finite,
non-negative blur/spread and are rendered by a bounded approximation.
```

```go
type Shadow struct {
	OffsetX, OffsetY MetricValue
	Blur, Spread     MetricValue
	Color            ColorValue
}
```

<a id="api-fontweight"></a>
## FontWeight

Source: `style.go:278`

```text
FontWeight selects the nearest registered face weight in a family.
```

```go
type FontWeight uint16
```

<a id="api-weightregular"></a>
## WeightRegular

Source: `style.go:281`

```go
const (
	WeightRegular FontWeight = 400
	WeightMedium  FontWeight = 500
	WeightBold    FontWeight = 700
)
```

<a id="api-weightmedium"></a>
## WeightMedium

Source: `style.go:282`

See the preceding constant block for the exact value and type.

<a id="api-weightbold"></a>
## WeightBold

Source: `style.go:283`

See the preceding constant block for the exact value and type.

<a id="api-fontslant"></a>
## FontSlant

Source: `style.go:287`

```text
FontSlant selects a registered normal or italic face.
```

```go
type FontSlant uint8
```

<a id="api-slantnormal"></a>
## SlantNormal

Source: `style.go:290`

```go
const (
	SlantNormal FontSlant = iota
	SlantItalic
)
```

<a id="api-slantitalic"></a>
## SlantItalic

Source: `style.go:291`

See the preceding constant block for the exact value and type.

<a id="api-textalign"></a>
## TextAlign

Source: `style.go:295`

```text
TextAlign is horizontal alignment within a Text node's content box.
```

```go
type TextAlign uint8
```

<a id="api-textstart"></a>
## TextStart

Source: `style.go:298`

```go
const (
	TextStart TextAlign = iota
	TextCenter
	TextEnd
)
```

<a id="api-textcenter"></a>
## TextCenter

Source: `style.go:299`

See the preceding constant block for the exact value and type.

<a id="api-textend"></a>
## TextEnd

Source: `style.go:300`

See the preceding constant block for the exact value and type.

<a id="api-textstyle"></a>
## TextStyle

Source: `style.go:309`

```text
TextStyle contains the simple-LTR/CJK MVP text inputs. Families are tried in
order before the App default and built-in Latin fallback. Size is a font
size in logical units; zero uses the current theme's default. LineHeight is
a logical-unit line height; zero uses the current theme's default.
Arabic/Indic shaping, bidi/RTL, color emoji, and vertical text are not
supported by this API.
```

```go
type TextStyle struct {
	Families   []FontFamily
	Size       float32
	LineHeight float32
	Weight     FontWeight
	Slant      FontSlant
	Color      ColorValue
	Align      TextAlign
}
```

<a id="api-componenttoken"></a>
## ComponentToken

Source: `style.go:320`

```text
ComponentToken names a component-level theme entry.
```

```go
type ComponentToken string
```

<a id="api-primitivetokens"></a>
## PrimitiveTokens

Source: `style.go:323`

```text
PrimitiveTokens are the literal foundation of a theme.
```

```go
type PrimitiveTokens struct {
	Colors  map[ColorToken]RGBAColor
	Metrics map[MetricToken]float32
}
```

<a id="api-semantictokens"></a>
## SemanticTokens

Source: `style.go:330`

```text
SemanticTokens map product meaning onto primitive or earlier semantic
tokens. A literal ColorValue/MetricValue is also accepted.
```

```go
type SemanticTokens struct {
	Colors  map[ColorToken]ColorValue
	Metrics map[MetricToken]MetricValue
}
```

<a id="api-stylepatch"></a>
## StylePatch

Source: `style.go:337`

```text
StylePatch is an explicitly optional paint-only override. State styles are
intentionally paint-only in MVP, so interaction never moves layout.
```

```go
type StylePatch struct {
	Background Option[ColorValue]
	Border     Option[Border]
	Radius     Option[CornerValues]
	Shadow     Option[[]Shadow]
	Opacity    Option[float32]
	Visibility Option[Visibility]
	TextColor  Option[ColorValue]
}
```

<a id="api-statestyles"></a>
## StateStyles

Source: `style.go:348`

```text
StateStyles contains the deterministic MVP visual-state cascade.
```

```go
type StateStyles struct {
	Default  StylePatch
	Hover    StylePatch
	Focus    StylePatch
	Disabled StylePatch
	Pressed  StylePatch
	Checked  StylePatch
}
```

<a id="api-componenttheme"></a>
## ComponentTheme

Source: `style.go:358`

```text
ComponentTheme supplies semantic-token-backed defaults for one component.
```

```go
type ComponentTheme struct {
	Base   StylePatch
	States StateStyles
}
```

<a id="api-theme"></a>
## Theme

Source: `style.go:365`

```text
Theme is the public, type-safe Primitive -> Semantic -> Component token
structure. SetTheme validates and copies every map and slice atomically.
```

```go
type Theme struct {
	Primitive  PrimitiveTokens
	Semantic   SemanticTokens
	Components map[ComponentToken]ComponentTheme
}
```

<a id="api-direction"></a>
## Direction

Source: `style.go:384`

```text
Direction selects Box's main axis. Vertical is the zero value.
```

```go
type Direction uint8
```

<a id="api-vertical"></a>
## Vertical

Source: `style.go:388`

```text
Vertical lays out Box children from top to bottom and is the zero value.
```

```go
const (
	// Vertical lays out Box children from top to bottom and is the zero value.
	Vertical Direction = iota
	// Horizontal lays out Box children from left to right.
	Horizontal
)
```

<a id="api-horizontal"></a>
## Horizontal

Source: `style.go:390`

```text
Horizontal lays out Box children from left to right.
```

See the preceding constant block for the exact value and type.

<a id="api-boxprops"></a>
## BoxProps

Source: `style.go:395`

```text
BoxProps configures a Box. Gap is a fixed logical-unit spacing; zero means
no spacing between children.
```

```go
type BoxProps struct {
	Key     string
	Style   Style
	Token   ComponentToken
	States  StateStyles
	Pointer PointerBehavior

	Direction Direction
	Gap       float32
	Justify   Justify
	Align     Align
}
```
