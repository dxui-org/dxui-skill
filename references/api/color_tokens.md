# color_tokens.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-colortokennamespace"></a>
## colorTokenNamespace

Source: `color_tokens.go:5`

```text
colorTokenNamespace provides discoverable, typed color tokens without
exposing stringly-typed names to applications.
```

```go
type colorTokenNamespace struct {
	Primitive primitiveColorTokens
	Semantic  semanticColorTokens
}
```

<a id="api-primitivecolortokens"></a>
## primitiveColorTokens

Source: `color_tokens.go:10`

```go
type primitiveColorTokens struct {
	White, Black                                                                                                                      ColorToken
	Red50, Red100, Red200, Red300, Red400, Red500, Red600, Red700, Red800, Red900, Red950                                             ColorToken
	Orange50, Orange100, Orange200, Orange300, Orange400, Orange500, Orange600, Orange700, Orange800, Orange900, Orange950            ColorToken
	Amber50, Amber100, Amber200, Amber300, Amber400, Amber500, Amber600, Amber700, Amber800, Amber900, Amber950                       ColorToken
	Yellow50, Yellow100, Yellow200, Yellow300, Yellow400, Yellow500, Yellow600, Yellow700, Yellow800, Yellow900, Yellow950            ColorToken
	Lime50, Lime100, Lime200, Lime300, Lime400, Lime500, Lime600, Lime700, Lime800, Lime900, Lime950                                  ColorToken
	Green50, Green100, Green200, Green300, Green400, Green500, Green600, Green700, Green800, Green900, Green950                       ColorToken
	Emerald50, Emerald100, Emerald200, Emerald300, Emerald400, Emerald500, Emerald600, Emerald700, Emerald800, Emerald900, Emerald950 ColorToken
	Teal50, Teal100, Teal200, Teal300, Teal400, Teal500, Teal600, Teal700, Teal800, Teal900, Teal950                                  ColorToken
	Cyan50, Cyan100, Cyan200, Cyan300, Cyan400, Cyan500, Cyan600, Cyan700, Cyan800, Cyan900, Cyan950                                  ColorToken
	Sky50, Sky100, Sky200, Sky300, Sky400, Sky500, Sky600, Sky700, Sky800, Sky900, Sky950                                             ColorToken
	Blue50, Blue100, Blue200, Blue300, Blue400, Blue500, Blue600, Blue700, Blue800, Blue900, Blue950                                  ColorToken
	Indigo50, Indigo100, Indigo200, Indigo300, Indigo400, Indigo500, Indigo600, Indigo700, Indigo800, Indigo900, Indigo950            ColorToken
	Violet50, Violet100, Violet200, Violet300, Violet400, Violet500, Violet600, Violet700, Violet800, Violet900, Violet950            ColorToken
	Purple50, Purple100, Purple200, Purple300, Purple400, Purple500, Purple600, Purple700, Purple800, Purple900, Purple950            ColorToken
	Fuchsia50, Fuchsia100, Fuchsia200, Fuchsia300, Fuchsia400, Fuchsia500, Fuchsia600, Fuchsia700, Fuchsia800, Fuchsia900, Fuchsia950 ColorToken
	Pink50, Pink100, Pink200, Pink300, Pink400, Pink500, Pink600, Pink700, Pink800, Pink900, Pink950                                  ColorToken
	Rose50, Rose100, Rose200, Rose300, Rose400, Rose500, Rose600, Rose700, Rose800, Rose900, Rose950                                  ColorToken
	Slate50, Slate100, Slate200, Slate300, Slate400, Slate500, Slate600, Slate700, Slate800, Slate900, Slate950                       ColorToken
	Gray50, Gray100, Gray200, Gray300, Gray400, Gray500, Gray600, Gray700, Gray800, Gray900, Gray950                                  ColorToken
	Zinc50, Zinc100, Zinc200, Zinc300, Zinc400, Zinc500, Zinc600, Zinc700, Zinc800, Zinc900, Zinc950                                  ColorToken
	Neutral50, Neutral100, Neutral200, Neutral300, Neutral400, Neutral500, Neutral600, Neutral700, Neutral800, Neutral900, Neutral950 ColorToken
	Stone50, Stone100, Stone200, Stone300, Stone400, Stone500, Stone600, Stone700, Stone800, Stone900, Stone950                       ColorToken
	Taupe50, Taupe100, Taupe200, Taupe300, Taupe400, Taupe500, Taupe600, Taupe700, Taupe800, Taupe900, Taupe950                       ColorToken
	Mauve50, Mauve100, Mauve200, Mauve300, Mauve400, Mauve500, Mauve600, Mauve700, Mauve800, Mauve900, Mauve950                       ColorToken
	Mist50, Mist100, Mist200, Mist300, Mist400, Mist500, Mist600, Mist700, Mist800, Mist900, Mist950                                  ColorToken
	Olive50, Olive100, Olive200, Olive300, Olive400, Olive500, Olive600, Olive700, Olive800, Olive900, Olive950                       ColorToken
}
```

<a id="api-semanticcolortokens"></a>
## semanticColorTokens

Source: `color_tokens.go:40`

```go
type semanticColorTokens struct {
	Surface, SurfaceHigh, Text, Accent, AccentHover, OnAccent, FocusRing, Danger, Success, Info, Warn, Border, Shadow ColorToken
}
```

<a id="api-color"></a>
## Color

Source: `color_tokens.go:45`

```text
Color is the public color-token namespace.
```

```go
var Color colorTokenNamespace
```

<a id="api-colorprimitivepalettewhite"></a>
## ColorPrimitivePaletteWhite

Source: `color_tokens.go:86`

```go
const (
	ColorPrimitivePaletteWhite ColorToken = "primitive.palette.white"
	ColorPrimitivePaletteBlack ColorToken = "primitive.palette.black"
	ColorPrimitiveRed50        ColorToken = "primitive.red.50"
	ColorPrimitiveRed100       ColorToken = "primitive.red.100"
	ColorPrimitiveRed200       ColorToken = "primitive.red.200"
	ColorPrimitiveRed300       ColorToken = "primitive.red.300"
	ColorPrimitiveRed400       ColorToken = "primitive.red.400"
	ColorPrimitiveRed500       ColorToken = "primitive.red.500"
	ColorPrimitiveRed600       ColorToken = "primitive.red.600"
	ColorPrimitiveRed700       ColorToken = "primitive.red.700"
	ColorPrimitiveRed800       ColorToken = "primitive.red.800"
	ColorPrimitiveRed900       ColorToken = "primitive.red.900"
	ColorPrimitiveRed950       ColorToken = "primitive.red.950"
	ColorPrimitiveOrange50     ColorToken = "primitive.orange.50"
	ColorPrimitiveOrange100    ColorToken = "primitive.orange.100"
	ColorPrimitiveOrange200    ColorToken = "primitive.orange.200"
	ColorPrimitiveOrange300    ColorToken = "primitive.orange.300"
	ColorPrimitiveOrange400    ColorToken = "primitive.orange.400"
	ColorPrimitiveOrange500    ColorToken = "primitive.orange.500"
	ColorPrimitiveOrange600    ColorToken = "primitive.orange.600"
	ColorPrimitiveOrange700    ColorToken = "primitive.orange.700"
	ColorPrimitiveOrange800    ColorToken = "primitive.orange.800"
	ColorPrimitiveOrange900    ColorToken = "primitive.orange.900"
	ColorPrimitiveOrange950    ColorToken = "primitive.orange.950"
	ColorPrimitiveAmber50      ColorToken = "primitive.amber.50"
	ColorPrimitiveAmber100     ColorToken = "primitive.amber.100"
	ColorPrimitiveAmber200     ColorToken = "primitive.amber.200"
	ColorPrimitiveAmber300     ColorToken = "primitive.amber.300"
	ColorPrimitiveAmber400     ColorToken = "primitive.amber.400"
	ColorPrimitiveAmber500     ColorToken = "primitive.amber.500"
	ColorPrimitiveAmber600     ColorToken = "primitive.amber.600"
	ColorPrimitiveAmber700     ColorToken = "primitive.amber.700"
	ColorPrimitiveAmber800     ColorToken = "primitive.amber.800"
	ColorPrimitiveAmber900     ColorToken = "primitive.amber.900"
	ColorPrimitiveAmber950     ColorToken = "primitive.amber.950"
	ColorPrimitiveYellow50     ColorToken = "primitive.yellow.50"
	ColorPrimitiveYellow100    ColorToken = "primitive.yellow.100"
	ColorPrimitiveYellow200    ColorToken = "primitive.yellow.200"
	ColorPrimitiveYellow300    ColorToken = "primitive.yellow.300"
	ColorPrimitiveYellow400    ColorToken = "primitive.yellow.400"
	ColorPrimitiveYellow500    ColorToken = "primitive.yellow.500"
	ColorPrimitiveYellow600    ColorToken = "primitive.yellow.600"
	ColorPrimitiveYellow700    ColorToken = "primitive.yellow.700"
	ColorPrimitiveYellow800    ColorToken = "primitive.yellow.800"
	ColorPrimitiveYellow900    ColorToken = "primitive.yellow.900"
	ColorPrimitiveYellow950    ColorToken = "primitive.yellow.950"
	ColorPrimitiveLime50       ColorToken = "primitive.lime.50"
	ColorPrimitiveLime100      ColorToken = "primitive.lime.100"
	ColorPrimitiveLime200      ColorToken = "primitive.lime.200"
	ColorPrimitiveLime300      ColorToken = "primitive.lime.300"
	ColorPrimitiveLime400      ColorToken = "primitive.lime.400"
	ColorPrimitiveLime500      ColorToken = "primitive.lime.500"
	ColorPrimitiveLime600      ColorToken = "primitive.lime.600"
	ColorPrimitiveLime700      ColorToken = "primitive.lime.700"
	ColorPrimitiveLime800      ColorToken = "primitive.lime.800"
	ColorPrimitiveLime900      ColorToken = "primitive.lime.900"
	ColorPrimitiveLime950      ColorToken = "primitive.lime.950"
	ColorPrimitiveGreen50      ColorToken = "primitive.green.50"
	ColorPrimitiveGreen100     ColorToken = "primitive.green.100"
	ColorPrimitiveGreen200     ColorToken = "primitive.green.200"
	ColorPrimitiveGreen300     ColorToken = "primitive.green.300"
	ColorPrimitiveGreen400     ColorToken = "primitive.green.400"
	ColorPrimitiveGreen500     ColorToken = "primitive.green.500"
	ColorPrimitiveGreen600     ColorToken = "primitive.green.600"
	ColorPrimitiveGreen700     ColorToken = "primitive.green.700"
	ColorPrimitiveGreen800     ColorToken = "primitive.green.800"
	ColorPrimitiveGreen900     ColorToken = "primitive.green.900"
	ColorPrimitiveGreen950     ColorToken = "primitive.green.950"
	ColorPrimitiveEmerald50    ColorToken = "primitive.emerald.50"
	ColorPrimitiveEmerald100   ColorToken = "primitive.emerald.100"
	ColorPrimitiveEmerald200   ColorToken = "primitive.emerald.200"
	ColorPrimitiveEmerald300   ColorToken = "primitive.emerald.300"
	ColorPrimitiveEmerald400   ColorToken = "primitive.emerald.400"
	ColorPrimitiveEmerald500   ColorToken = "primitive.emerald.500"
	ColorPrimitiveEmerald600   ColorToken = "primitive.emerald.600"
	ColorPrimitiveEmerald700   ColorToken = "primitive.emerald.700"
	ColorPrimitiveEmerald800   ColorToken = "primitive.emerald.800"
	ColorPrimitiveEmerald900   ColorToken = "primitive.emerald.900"
	ColorPrimitiveEmerald950   ColorToken = "primitive.emerald.950"
	ColorPrimitiveTeal50       ColorToken = "primitive.teal.50"
	ColorPrimitiveTeal100      ColorToken = "primitive.teal.100"
	ColorPrimitiveTeal200      ColorToken = "primitive.teal.200"
	ColorPrimitiveTeal300      ColorToken = "primitive.teal.300"
	ColorPrimitiveTeal400      ColorToken = "primitive.teal.400"
	ColorPrimitiveTeal500      ColorToken = "primitive.teal.500"
	ColorPrimitiveTeal600      ColorToken = "primitive.teal.600"
	ColorPrimitiveTeal700      ColorToken = "primitive.teal.700"
	ColorPrimitiveTeal800      ColorToken = "primitive.teal.800"
	ColorPrimitiveTeal900      ColorToken = "primitive.teal.900"
	ColorPrimitiveTeal950      ColorToken = "primitive.teal.950"
	ColorPrimitiveCyan50       ColorToken = "primitive.cyan.50"
	ColorPrimitiveCyan100      ColorToken = "primitive.cyan.100"
	ColorPrimitiveCyan200      ColorToken = "primitive.cyan.200"
	ColorPrimitiveCyan300      ColorToken = "primitive.cyan.300"
	ColorPrimitiveCyan400      ColorToken = "primitive.cyan.400"
	ColorPrimitiveCyan500      ColorToken = "primitive.cyan.500"
	ColorPrimitiveCyan600      ColorToken = "primitive.cyan.600"
	ColorPrimitiveCyan700      ColorToken = "primitive.cyan.700"
	ColorPrimitiveCyan800      ColorToken = "primitive.cyan.800"
	ColorPrimitiveCyan900      ColorToken = "primitive.cyan.900"
	ColorPrimitiveCyan950      ColorToken = "primitive.cyan.950"
	ColorPrimitiveSky50        ColorToken = "primitive.sky.50"
	ColorPrimitiveSky100       ColorToken = "primitive.sky.100"
	ColorPrimitiveSky200       ColorToken = "primitive.sky.200"
	ColorPrimitiveSky300       ColorToken = "primitive.sky.300"
	ColorPrimitiveSky400       ColorToken = "primitive.sky.400"
	ColorPrimitiveSky500       ColorToken = "primitive.sky.500"
	ColorPrimitiveSky600       ColorToken = "primitive.sky.600"
	ColorPrimitiveSky700       ColorToken = "primitive.sky.700"
	ColorPrimitiveSky800       ColorToken = "primitive.sky.800"
	ColorPrimitiveSky900       ColorToken = "primitive.sky.900"
	ColorPrimitiveSky950       ColorToken = "primitive.sky.950"
	ColorPrimitiveBlue50       ColorToken = "primitive.blue.50"
	ColorPrimitiveBlue100      ColorToken = "primitive.blue.100"
	ColorPrimitiveBlue200      ColorToken = "primitive.blue.200"
	ColorPrimitiveBlue300      ColorToken = "primitive.blue.300"
	ColorPrimitiveBlue400      ColorToken = "primitive.blue.400"
	ColorPrimitiveBlue500      ColorToken = "primitive.blue.500"
	ColorPrimitiveBlue600      ColorToken = "primitive.blue.600"
	ColorPrimitiveBlue700      ColorToken = "primitive.blue.700"
	ColorPrimitiveBlue800      ColorToken = "primitive.blue.800"
	ColorPrimitiveBlue900      ColorToken = "primitive.blue.900"
	ColorPrimitiveBlue950      ColorToken = "primitive.blue.950"
	ColorPrimitiveIndigo50     ColorToken = "primitive.indigo.50"
	ColorPrimitiveIndigo100    ColorToken = "primitive.indigo.100"
	ColorPrimitiveIndigo200    ColorToken = "primitive.indigo.200"
	ColorPrimitiveIndigo300    ColorToken = "primitive.indigo.300"
	ColorPrimitiveIndigo400    ColorToken = "primitive.indigo.400"
	ColorPrimitiveIndigo500    ColorToken = "primitive.indigo.500"
	ColorPrimitiveIndigo600    ColorToken = "primitive.indigo.600"
	ColorPrimitiveIndigo700    ColorToken = "primitive.indigo.700"
	ColorPrimitiveIndigo800    ColorToken = "primitive.indigo.800"
	ColorPrimitiveIndigo900    ColorToken = "primitive.indigo.900"
	ColorPrimitiveIndigo950    ColorToken = "primitive.indigo.950"
	ColorPrimitiveViolet50     ColorToken = "primitive.violet.50"
	ColorPrimitiveViolet100    ColorToken = "primitive.violet.100"
	ColorPrimitiveViolet200    ColorToken = "primitive.violet.200"
	ColorPrimitiveViolet300    ColorToken = "primitive.violet.300"
	ColorPrimitiveViolet400    ColorToken = "primitive.violet.400"
	ColorPrimitiveViolet500    ColorToken = "primitive.violet.500"
	ColorPrimitiveViolet600    ColorToken = "primitive.violet.600"
	ColorPrimitiveViolet700    ColorToken = "primitive.violet.700"
	ColorPrimitiveViolet800    ColorToken = "primitive.violet.800"
	ColorPrimitiveViolet900    ColorToken = "primitive.violet.900"
	ColorPrimitiveViolet950    ColorToken = "primitive.violet.950"
	ColorPrimitivePurple50     ColorToken = "primitive.purple.50"
	ColorPrimitivePurple100    ColorToken = "primitive.purple.100"
	ColorPrimitivePurple200    ColorToken = "primitive.purple.200"
	ColorPrimitivePurple300    ColorToken = "primitive.purple.300"
	ColorPrimitivePurple400    ColorToken = "primitive.purple.400"
	ColorPrimitivePurple500    ColorToken = "primitive.purple.500"
	ColorPrimitivePurple600    ColorToken = "primitive.purple.600"
	ColorPrimitivePurple700    ColorToken = "primitive.purple.700"
	ColorPrimitivePurple800    ColorToken = "primitive.purple.800"
	ColorPrimitivePurple900    ColorToken = "primitive.purple.900"
	ColorPrimitivePurple950    ColorToken = "primitive.purple.950"
	ColorPrimitiveFuchsia50    ColorToken = "primitive.fuchsia.50"
	ColorPrimitiveFuchsia100   ColorToken = "primitive.fuchsia.100"
	ColorPrimitiveFuchsia200   ColorToken = "primitive.fuchsia.200"
	ColorPrimitiveFuchsia300   ColorToken = "primitive.fuchsia.300"
	ColorPrimitiveFuchsia400   ColorToken = "primitive.fuchsia.400"
	ColorPrimitiveFuchsia500   ColorToken = "primitive.fuchsia.500"
	ColorPrimitiveFuchsia600   ColorToken = "primitive.fuchsia.600"
	ColorPrimitiveFuchsia700   ColorToken = "primitive.fuchsia.700"
	ColorPrimitiveFuchsia800   ColorToken = "primitive.fuchsia.800"
	ColorPrimitiveFuchsia900   ColorToken = "primitive.fuchsia.900"
	ColorPrimitiveFuchsia950   ColorToken = "primitive.fuchsia.950"
	ColorPrimitivePink50       ColorToken = "primitive.pink.50"
	ColorPrimitivePink100      ColorToken = "primitive.pink.100"
	ColorPrimitivePink200      ColorToken = "primitive.pink.200"
	ColorPrimitivePink300      ColorToken = "primitive.pink.300"
	ColorPrimitivePink400      ColorToken = "primitive.pink.400"
	ColorPrimitivePink500      ColorToken = "primitive.pink.500"
	ColorPrimitivePink600      ColorToken = "primitive.pink.600"
	ColorPrimitivePink700      ColorToken = "primitive.pink.700"
	ColorPrimitivePink800      ColorToken = "primitive.pink.800"
	ColorPrimitivePink900      ColorToken = "primitive.pink.900"
	ColorPrimitivePink950      ColorToken = "primitive.pink.950"
	ColorPrimitiveRose50       ColorToken = "primitive.rose.50"
	ColorPrimitiveRose100      ColorToken = "primitive.rose.100"
	ColorPrimitiveRose200      ColorToken = "primitive.rose.200"
	ColorPrimitiveRose300      ColorToken = "primitive.rose.300"
	ColorPrimitiveRose400      ColorToken = "primitive.rose.400"
	ColorPrimitiveRose500      ColorToken = "primitive.rose.500"
	ColorPrimitiveRose600      ColorToken = "primitive.rose.600"
	ColorPrimitiveRose700      ColorToken = "primitive.rose.700"
	ColorPrimitiveRose800      ColorToken = "primitive.rose.800"
	ColorPrimitiveRose900      ColorToken = "primitive.rose.900"
	ColorPrimitiveRose950      ColorToken = "primitive.rose.950"
	ColorPrimitiveSlate50      ColorToken = "primitive.slate.50"
	ColorPrimitiveSlate100     ColorToken = "primitive.slate.100"
	ColorPrimitiveSlate200     ColorToken = "primitive.slate.200"
	ColorPrimitiveSlate300     ColorToken = "primitive.slate.300"
	ColorPrimitiveSlate400     ColorToken = "primitive.slate.400"
	ColorPrimitiveSlate500     ColorToken = "primitive.slate.500"
	ColorPrimitiveSlate600     ColorToken = "primitive.slate.600"
	ColorPrimitiveSlate700     ColorToken = "primitive.slate.700"
	ColorPrimitiveSlate800     ColorToken = "primitive.slate.800"
	ColorPrimitiveSlate900     ColorToken = "primitive.slate.900"
	ColorPrimitiveSlate950     ColorToken = "primitive.slate.950"
	ColorPrimitiveGray50       ColorToken = "primitive.gray.50"
	ColorPrimitiveGray100      ColorToken = "primitive.gray.100"
	ColorPrimitiveGray200      ColorToken = "primitive.gray.200"
	ColorPrimitiveGray300      ColorToken = "primitive.gray.300"
	ColorPrimitiveGray400      ColorToken = "primitive.gray.400"
	ColorPrimitiveGray500      ColorToken = "primitive.gray.500"
	ColorPrimitiveGray600      ColorToken = "primitive.gray.600"
	ColorPrimitiveGray700      ColorToken = "primitive.gray.700"
	ColorPrimitiveGray800      ColorToken = "primitive.gray.800"
	ColorPrimitiveGray900      ColorToken = "primitive.gray.900"
	ColorPrimitiveGray950      ColorToken = "primitive.gray.950"
	ColorPrimitiveZinc50       ColorToken = "primitive.zinc.50"
	ColorPrimitiveZinc100      ColorToken = "primitive.zinc.100"
	ColorPrimitiveZinc200      ColorToken = "primitive.zinc.200"
	ColorPrimitiveZinc300      ColorToken = "primitive.zinc.300"
	ColorPrimitiveZinc400      ColorToken = "primitive.zinc.400"
	ColorPrimitiveZinc500      ColorToken = "primitive.zinc.500"
	ColorPrimitiveZinc600      ColorToken = "primitive.zinc.600"
	ColorPrimitiveZinc700      ColorToken = "primitive.zinc.700"
	ColorPrimitiveZinc800      ColorToken = "primitive.zinc.800"
	ColorPrimitiveZinc900      ColorToken = "primitive.zinc.900"
	ColorPrimitiveZinc950      ColorToken = "primitive.zinc.950"
	ColorPrimitiveNeutral50    ColorToken = "primitive.neutral.50"
	ColorPrimitiveNeutral100   ColorToken = "primitive.neutral.100"
	ColorPrimitiveNeutral200   ColorToken = "primitive.neutral.200"
	ColorPrimitiveNeutral300   ColorToken = "primitive.neutral.300"
	ColorPrimitiveNeutral400   ColorToken = "primitive.neutral.400"
	ColorPrimitiveNeutral500   ColorToken = "primitive.neutral.500"
	ColorPrimitiveNeutral600   ColorToken = "primitive.neutral.600"
	ColorPrimitiveNeutral700   ColorToken = "primitive.neutral.700"
	ColorPrimitiveNeutral800   ColorToken = "primitive.neutral.800"
	ColorPrimitiveNeutral900   ColorToken = "primitive.neutral.900"
	ColorPrimitiveNeutral950   ColorToken = "primitive.neutral.950"
	ColorPrimitiveStone50      ColorToken = "primitive.stone.50"
	ColorPrimitiveStone100     ColorToken = "primitive.stone.100"
	ColorPrimitiveStone200     ColorToken = "primitive.stone.200"
	ColorPrimitiveStone300     ColorToken = "primitive.stone.300"
	ColorPrimitiveStone400     ColorToken = "primitive.stone.400"
	ColorPrimitiveStone500     ColorToken = "primitive.stone.500"
	ColorPrimitiveStone600     ColorToken = "primitive.stone.600"
	ColorPrimitiveStone700     ColorToken = "primitive.stone.700"
	ColorPrimitiveStone800     ColorToken = "primitive.stone.800"
	ColorPrimitiveStone900     ColorToken = "primitive.stone.900"
	ColorPrimitiveStone950     ColorToken = "primitive.stone.950"
	ColorPrimitiveTaupe50      ColorToken = "primitive.taupe.50"
	ColorPrimitiveTaupe100     ColorToken = "primitive.taupe.100"
	ColorPrimitiveTaupe200     ColorToken = "primitive.taupe.200"
	ColorPrimitiveTaupe300     ColorToken = "primitive.taupe.300"
	ColorPrimitiveTaupe400     ColorToken = "primitive.taupe.400"
	ColorPrimitiveTaupe500     ColorToken = "primitive.taupe.500"
	ColorPrimitiveTaupe600     ColorToken = "primitive.taupe.600"
	ColorPrimitiveTaupe700     ColorToken = "primitive.taupe.700"
	ColorPrimitiveTaupe800     ColorToken = "primitive.taupe.800"
	ColorPrimitiveTaupe900     ColorToken = "primitive.taupe.900"
	ColorPrimitiveTaupe950     ColorToken = "primitive.taupe.950"
	ColorPrimitiveMauve50      ColorToken = "primitive.mauve.50"
	ColorPrimitiveMauve100     ColorToken = "primitive.mauve.100"
	ColorPrimitiveMauve200     ColorToken = "primitive.mauve.200"
	ColorPrimitiveMauve300     ColorToken = "primitive.mauve.300"
	ColorPrimitiveMauve400     ColorToken = "primitive.mauve.400"
	ColorPrimitiveMauve500     ColorToken = "primitive.mauve.500"
	ColorPrimitiveMauve600     ColorToken = "primitive.mauve.600"
	ColorPrimitiveMauve700     ColorToken = "primitive.mauve.700"
	ColorPrimitiveMauve800     ColorToken = "primitive.mauve.800"
	ColorPrimitiveMauve900     ColorToken = "primitive.mauve.900"
	ColorPrimitiveMauve950     ColorToken = "primitive.mauve.950"
	ColorPrimitiveMist50       ColorToken = "primitive.mist.50"
	ColorPrimitiveMist100      ColorToken = "primitive.mist.100"
	ColorPrimitiveMist200      ColorToken = "primitive.mist.200"
	ColorPrimitiveMist300      ColorToken = "primitive.mist.300"
	ColorPrimitiveMist400      ColorToken = "primitive.mist.400"
	ColorPrimitiveMist500      ColorToken = "primitive.mist.500"
	ColorPrimitiveMist600      ColorToken = "primitive.mist.600"
	ColorPrimitiveMist700      ColorToken = "primitive.mist.700"
	ColorPrimitiveMist800      ColorToken = "primitive.mist.800"
	ColorPrimitiveMist900      ColorToken = "primitive.mist.900"
	ColorPrimitiveMist950      ColorToken = "primitive.mist.950"
	ColorPrimitiveOlive50      ColorToken = "primitive.olive.50"
	ColorPrimitiveOlive100     ColorToken = "primitive.olive.100"
	ColorPrimitiveOlive200     ColorToken = "primitive.olive.200"
	ColorPrimitiveOlive300     ColorToken = "primitive.olive.300"
	ColorPrimitiveOlive400     ColorToken = "primitive.olive.400"
	ColorPrimitiveOlive500     ColorToken = "primitive.olive.500"
	ColorPrimitiveOlive600     ColorToken = "primitive.olive.600"
	ColorPrimitiveOlive700     ColorToken = "primitive.olive.700"
	ColorPrimitiveOlive800     ColorToken = "primitive.olive.800"
	ColorPrimitiveOlive900     ColorToken = "primitive.olive.900"
	ColorPrimitiveOlive950     ColorToken = "primitive.olive.950"
)
```

<a id="api-colorprimitivepaletteblack"></a>
## ColorPrimitivePaletteBlack

Source: `color_tokens.go:87`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered50"></a>
## ColorPrimitiveRed50

Source: `color_tokens.go:88`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered100"></a>
## ColorPrimitiveRed100

Source: `color_tokens.go:89`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered200"></a>
## ColorPrimitiveRed200

Source: `color_tokens.go:90`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered300"></a>
## ColorPrimitiveRed300

Source: `color_tokens.go:91`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered400"></a>
## ColorPrimitiveRed400

Source: `color_tokens.go:92`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered500"></a>
## ColorPrimitiveRed500

Source: `color_tokens.go:93`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered600"></a>
## ColorPrimitiveRed600

Source: `color_tokens.go:94`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered700"></a>
## ColorPrimitiveRed700

Source: `color_tokens.go:95`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered800"></a>
## ColorPrimitiveRed800

Source: `color_tokens.go:96`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered900"></a>
## ColorPrimitiveRed900

Source: `color_tokens.go:97`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivered950"></a>
## ColorPrimitiveRed950

Source: `color_tokens.go:98`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange50"></a>
## ColorPrimitiveOrange50

Source: `color_tokens.go:99`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange100"></a>
## ColorPrimitiveOrange100

Source: `color_tokens.go:100`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange200"></a>
## ColorPrimitiveOrange200

Source: `color_tokens.go:101`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange300"></a>
## ColorPrimitiveOrange300

Source: `color_tokens.go:102`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange400"></a>
## ColorPrimitiveOrange400

Source: `color_tokens.go:103`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange500"></a>
## ColorPrimitiveOrange500

Source: `color_tokens.go:104`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange600"></a>
## ColorPrimitiveOrange600

Source: `color_tokens.go:105`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange700"></a>
## ColorPrimitiveOrange700

Source: `color_tokens.go:106`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange800"></a>
## ColorPrimitiveOrange800

Source: `color_tokens.go:107`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange900"></a>
## ColorPrimitiveOrange900

Source: `color_tokens.go:108`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveorange950"></a>
## ColorPrimitiveOrange950

Source: `color_tokens.go:109`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber50"></a>
## ColorPrimitiveAmber50

Source: `color_tokens.go:110`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber100"></a>
## ColorPrimitiveAmber100

Source: `color_tokens.go:111`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber200"></a>
## ColorPrimitiveAmber200

Source: `color_tokens.go:112`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber300"></a>
## ColorPrimitiveAmber300

Source: `color_tokens.go:113`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber400"></a>
## ColorPrimitiveAmber400

Source: `color_tokens.go:114`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber500"></a>
## ColorPrimitiveAmber500

Source: `color_tokens.go:115`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber600"></a>
## ColorPrimitiveAmber600

Source: `color_tokens.go:116`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber700"></a>
## ColorPrimitiveAmber700

Source: `color_tokens.go:117`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber800"></a>
## ColorPrimitiveAmber800

Source: `color_tokens.go:118`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber900"></a>
## ColorPrimitiveAmber900

Source: `color_tokens.go:119`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveamber950"></a>
## ColorPrimitiveAmber950

Source: `color_tokens.go:120`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow50"></a>
## ColorPrimitiveYellow50

Source: `color_tokens.go:121`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow100"></a>
## ColorPrimitiveYellow100

Source: `color_tokens.go:122`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow200"></a>
## ColorPrimitiveYellow200

Source: `color_tokens.go:123`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow300"></a>
## ColorPrimitiveYellow300

Source: `color_tokens.go:124`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow400"></a>
## ColorPrimitiveYellow400

Source: `color_tokens.go:125`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow500"></a>
## ColorPrimitiveYellow500

Source: `color_tokens.go:126`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow600"></a>
## ColorPrimitiveYellow600

Source: `color_tokens.go:127`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow700"></a>
## ColorPrimitiveYellow700

Source: `color_tokens.go:128`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow800"></a>
## ColorPrimitiveYellow800

Source: `color_tokens.go:129`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow900"></a>
## ColorPrimitiveYellow900

Source: `color_tokens.go:130`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveyellow950"></a>
## ColorPrimitiveYellow950

Source: `color_tokens.go:131`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime50"></a>
## ColorPrimitiveLime50

Source: `color_tokens.go:132`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime100"></a>
## ColorPrimitiveLime100

Source: `color_tokens.go:133`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime200"></a>
## ColorPrimitiveLime200

Source: `color_tokens.go:134`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime300"></a>
## ColorPrimitiveLime300

Source: `color_tokens.go:135`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime400"></a>
## ColorPrimitiveLime400

Source: `color_tokens.go:136`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime500"></a>
## ColorPrimitiveLime500

Source: `color_tokens.go:137`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime600"></a>
## ColorPrimitiveLime600

Source: `color_tokens.go:138`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime700"></a>
## ColorPrimitiveLime700

Source: `color_tokens.go:139`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime800"></a>
## ColorPrimitiveLime800

Source: `color_tokens.go:140`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime900"></a>
## ColorPrimitiveLime900

Source: `color_tokens.go:141`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivelime950"></a>
## ColorPrimitiveLime950

Source: `color_tokens.go:142`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen50"></a>
## ColorPrimitiveGreen50

Source: `color_tokens.go:143`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen100"></a>
## ColorPrimitiveGreen100

Source: `color_tokens.go:144`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen200"></a>
## ColorPrimitiveGreen200

Source: `color_tokens.go:145`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen300"></a>
## ColorPrimitiveGreen300

Source: `color_tokens.go:146`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen400"></a>
## ColorPrimitiveGreen400

Source: `color_tokens.go:147`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen500"></a>
## ColorPrimitiveGreen500

Source: `color_tokens.go:148`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen600"></a>
## ColorPrimitiveGreen600

Source: `color_tokens.go:149`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen700"></a>
## ColorPrimitiveGreen700

Source: `color_tokens.go:150`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen800"></a>
## ColorPrimitiveGreen800

Source: `color_tokens.go:151`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen900"></a>
## ColorPrimitiveGreen900

Source: `color_tokens.go:152`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegreen950"></a>
## ColorPrimitiveGreen950

Source: `color_tokens.go:153`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald50"></a>
## ColorPrimitiveEmerald50

Source: `color_tokens.go:154`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald100"></a>
## ColorPrimitiveEmerald100

Source: `color_tokens.go:155`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald200"></a>
## ColorPrimitiveEmerald200

Source: `color_tokens.go:156`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald300"></a>
## ColorPrimitiveEmerald300

Source: `color_tokens.go:157`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald400"></a>
## ColorPrimitiveEmerald400

Source: `color_tokens.go:158`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald500"></a>
## ColorPrimitiveEmerald500

Source: `color_tokens.go:159`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald600"></a>
## ColorPrimitiveEmerald600

Source: `color_tokens.go:160`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald700"></a>
## ColorPrimitiveEmerald700

Source: `color_tokens.go:161`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald800"></a>
## ColorPrimitiveEmerald800

Source: `color_tokens.go:162`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald900"></a>
## ColorPrimitiveEmerald900

Source: `color_tokens.go:163`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveemerald950"></a>
## ColorPrimitiveEmerald950

Source: `color_tokens.go:164`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal50"></a>
## ColorPrimitiveTeal50

Source: `color_tokens.go:165`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal100"></a>
## ColorPrimitiveTeal100

Source: `color_tokens.go:166`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal200"></a>
## ColorPrimitiveTeal200

Source: `color_tokens.go:167`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal300"></a>
## ColorPrimitiveTeal300

Source: `color_tokens.go:168`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal400"></a>
## ColorPrimitiveTeal400

Source: `color_tokens.go:169`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal500"></a>
## ColorPrimitiveTeal500

Source: `color_tokens.go:170`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal600"></a>
## ColorPrimitiveTeal600

Source: `color_tokens.go:171`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal700"></a>
## ColorPrimitiveTeal700

Source: `color_tokens.go:172`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal800"></a>
## ColorPrimitiveTeal800

Source: `color_tokens.go:173`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal900"></a>
## ColorPrimitiveTeal900

Source: `color_tokens.go:174`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveteal950"></a>
## ColorPrimitiveTeal950

Source: `color_tokens.go:175`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan50"></a>
## ColorPrimitiveCyan50

Source: `color_tokens.go:176`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan100"></a>
## ColorPrimitiveCyan100

Source: `color_tokens.go:177`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan200"></a>
## ColorPrimitiveCyan200

Source: `color_tokens.go:178`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan300"></a>
## ColorPrimitiveCyan300

Source: `color_tokens.go:179`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan400"></a>
## ColorPrimitiveCyan400

Source: `color_tokens.go:180`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan500"></a>
## ColorPrimitiveCyan500

Source: `color_tokens.go:181`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan600"></a>
## ColorPrimitiveCyan600

Source: `color_tokens.go:182`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan700"></a>
## ColorPrimitiveCyan700

Source: `color_tokens.go:183`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan800"></a>
## ColorPrimitiveCyan800

Source: `color_tokens.go:184`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan900"></a>
## ColorPrimitiveCyan900

Source: `color_tokens.go:185`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivecyan950"></a>
## ColorPrimitiveCyan950

Source: `color_tokens.go:186`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky50"></a>
## ColorPrimitiveSky50

Source: `color_tokens.go:187`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky100"></a>
## ColorPrimitiveSky100

Source: `color_tokens.go:188`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky200"></a>
## ColorPrimitiveSky200

Source: `color_tokens.go:189`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky300"></a>
## ColorPrimitiveSky300

Source: `color_tokens.go:190`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky400"></a>
## ColorPrimitiveSky400

Source: `color_tokens.go:191`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky500"></a>
## ColorPrimitiveSky500

Source: `color_tokens.go:192`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky600"></a>
## ColorPrimitiveSky600

Source: `color_tokens.go:193`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky700"></a>
## ColorPrimitiveSky700

Source: `color_tokens.go:194`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky800"></a>
## ColorPrimitiveSky800

Source: `color_tokens.go:195`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky900"></a>
## ColorPrimitiveSky900

Source: `color_tokens.go:196`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivesky950"></a>
## ColorPrimitiveSky950

Source: `color_tokens.go:197`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue50"></a>
## ColorPrimitiveBlue50

Source: `color_tokens.go:198`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue100"></a>
## ColorPrimitiveBlue100

Source: `color_tokens.go:199`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue200"></a>
## ColorPrimitiveBlue200

Source: `color_tokens.go:200`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue300"></a>
## ColorPrimitiveBlue300

Source: `color_tokens.go:201`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue400"></a>
## ColorPrimitiveBlue400

Source: `color_tokens.go:202`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue500"></a>
## ColorPrimitiveBlue500

Source: `color_tokens.go:203`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue600"></a>
## ColorPrimitiveBlue600

Source: `color_tokens.go:204`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue700"></a>
## ColorPrimitiveBlue700

Source: `color_tokens.go:205`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue800"></a>
## ColorPrimitiveBlue800

Source: `color_tokens.go:206`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue900"></a>
## ColorPrimitiveBlue900

Source: `color_tokens.go:207`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue950"></a>
## ColorPrimitiveBlue950

Source: `color_tokens.go:208`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo50"></a>
## ColorPrimitiveIndigo50

Source: `color_tokens.go:209`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo100"></a>
## ColorPrimitiveIndigo100

Source: `color_tokens.go:210`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo200"></a>
## ColorPrimitiveIndigo200

Source: `color_tokens.go:211`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo300"></a>
## ColorPrimitiveIndigo300

Source: `color_tokens.go:212`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo400"></a>
## ColorPrimitiveIndigo400

Source: `color_tokens.go:213`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo500"></a>
## ColorPrimitiveIndigo500

Source: `color_tokens.go:214`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo600"></a>
## ColorPrimitiveIndigo600

Source: `color_tokens.go:215`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo700"></a>
## ColorPrimitiveIndigo700

Source: `color_tokens.go:216`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo800"></a>
## ColorPrimitiveIndigo800

Source: `color_tokens.go:217`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo900"></a>
## ColorPrimitiveIndigo900

Source: `color_tokens.go:218`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveindigo950"></a>
## ColorPrimitiveIndigo950

Source: `color_tokens.go:219`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet50"></a>
## ColorPrimitiveViolet50

Source: `color_tokens.go:220`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet100"></a>
## ColorPrimitiveViolet100

Source: `color_tokens.go:221`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet200"></a>
## ColorPrimitiveViolet200

Source: `color_tokens.go:222`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet300"></a>
## ColorPrimitiveViolet300

Source: `color_tokens.go:223`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet400"></a>
## ColorPrimitiveViolet400

Source: `color_tokens.go:224`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet500"></a>
## ColorPrimitiveViolet500

Source: `color_tokens.go:225`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet600"></a>
## ColorPrimitiveViolet600

Source: `color_tokens.go:226`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet700"></a>
## ColorPrimitiveViolet700

Source: `color_tokens.go:227`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet800"></a>
## ColorPrimitiveViolet800

Source: `color_tokens.go:228`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet900"></a>
## ColorPrimitiveViolet900

Source: `color_tokens.go:229`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveviolet950"></a>
## ColorPrimitiveViolet950

Source: `color_tokens.go:230`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple50"></a>
## ColorPrimitivePurple50

Source: `color_tokens.go:231`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple100"></a>
## ColorPrimitivePurple100

Source: `color_tokens.go:232`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple200"></a>
## ColorPrimitivePurple200

Source: `color_tokens.go:233`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple300"></a>
## ColorPrimitivePurple300

Source: `color_tokens.go:234`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple400"></a>
## ColorPrimitivePurple400

Source: `color_tokens.go:235`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple500"></a>
## ColorPrimitivePurple500

Source: `color_tokens.go:236`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple600"></a>
## ColorPrimitivePurple600

Source: `color_tokens.go:237`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple700"></a>
## ColorPrimitivePurple700

Source: `color_tokens.go:238`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple800"></a>
## ColorPrimitivePurple800

Source: `color_tokens.go:239`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple900"></a>
## ColorPrimitivePurple900

Source: `color_tokens.go:240`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepurple950"></a>
## ColorPrimitivePurple950

Source: `color_tokens.go:241`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia50"></a>
## ColorPrimitiveFuchsia50

Source: `color_tokens.go:242`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia100"></a>
## ColorPrimitiveFuchsia100

Source: `color_tokens.go:243`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia200"></a>
## ColorPrimitiveFuchsia200

Source: `color_tokens.go:244`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia300"></a>
## ColorPrimitiveFuchsia300

Source: `color_tokens.go:245`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia400"></a>
## ColorPrimitiveFuchsia400

Source: `color_tokens.go:246`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia500"></a>
## ColorPrimitiveFuchsia500

Source: `color_tokens.go:247`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia600"></a>
## ColorPrimitiveFuchsia600

Source: `color_tokens.go:248`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia700"></a>
## ColorPrimitiveFuchsia700

Source: `color_tokens.go:249`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia800"></a>
## ColorPrimitiveFuchsia800

Source: `color_tokens.go:250`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia900"></a>
## ColorPrimitiveFuchsia900

Source: `color_tokens.go:251`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivefuchsia950"></a>
## ColorPrimitiveFuchsia950

Source: `color_tokens.go:252`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink50"></a>
## ColorPrimitivePink50

Source: `color_tokens.go:253`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink100"></a>
## ColorPrimitivePink100

Source: `color_tokens.go:254`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink200"></a>
## ColorPrimitivePink200

Source: `color_tokens.go:255`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink300"></a>
## ColorPrimitivePink300

Source: `color_tokens.go:256`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink400"></a>
## ColorPrimitivePink400

Source: `color_tokens.go:257`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink500"></a>
## ColorPrimitivePink500

Source: `color_tokens.go:258`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink600"></a>
## ColorPrimitivePink600

Source: `color_tokens.go:259`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink700"></a>
## ColorPrimitivePink700

Source: `color_tokens.go:260`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink800"></a>
## ColorPrimitivePink800

Source: `color_tokens.go:261`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink900"></a>
## ColorPrimitivePink900

Source: `color_tokens.go:262`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivepink950"></a>
## ColorPrimitivePink950

Source: `color_tokens.go:263`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose50"></a>
## ColorPrimitiveRose50

Source: `color_tokens.go:264`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose100"></a>
## ColorPrimitiveRose100

Source: `color_tokens.go:265`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose200"></a>
## ColorPrimitiveRose200

Source: `color_tokens.go:266`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose300"></a>
## ColorPrimitiveRose300

Source: `color_tokens.go:267`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose400"></a>
## ColorPrimitiveRose400

Source: `color_tokens.go:268`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose500"></a>
## ColorPrimitiveRose500

Source: `color_tokens.go:269`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose600"></a>
## ColorPrimitiveRose600

Source: `color_tokens.go:270`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose700"></a>
## ColorPrimitiveRose700

Source: `color_tokens.go:271`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose800"></a>
## ColorPrimitiveRose800

Source: `color_tokens.go:272`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose900"></a>
## ColorPrimitiveRose900

Source: `color_tokens.go:273`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiverose950"></a>
## ColorPrimitiveRose950

Source: `color_tokens.go:274`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate50"></a>
## ColorPrimitiveSlate50

Source: `color_tokens.go:275`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate100"></a>
## ColorPrimitiveSlate100

Source: `color_tokens.go:276`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate200"></a>
## ColorPrimitiveSlate200

Source: `color_tokens.go:277`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate300"></a>
## ColorPrimitiveSlate300

Source: `color_tokens.go:278`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate400"></a>
## ColorPrimitiveSlate400

Source: `color_tokens.go:279`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate500"></a>
## ColorPrimitiveSlate500

Source: `color_tokens.go:280`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate600"></a>
## ColorPrimitiveSlate600

Source: `color_tokens.go:281`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate700"></a>
## ColorPrimitiveSlate700

Source: `color_tokens.go:282`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate800"></a>
## ColorPrimitiveSlate800

Source: `color_tokens.go:283`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate900"></a>
## ColorPrimitiveSlate900

Source: `color_tokens.go:284`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveslate950"></a>
## ColorPrimitiveSlate950

Source: `color_tokens.go:285`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray50"></a>
## ColorPrimitiveGray50

Source: `color_tokens.go:286`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray100"></a>
## ColorPrimitiveGray100

Source: `color_tokens.go:287`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray200"></a>
## ColorPrimitiveGray200

Source: `color_tokens.go:288`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray300"></a>
## ColorPrimitiveGray300

Source: `color_tokens.go:289`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray400"></a>
## ColorPrimitiveGray400

Source: `color_tokens.go:290`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray500"></a>
## ColorPrimitiveGray500

Source: `color_tokens.go:291`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray600"></a>
## ColorPrimitiveGray600

Source: `color_tokens.go:292`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray700"></a>
## ColorPrimitiveGray700

Source: `color_tokens.go:293`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray800"></a>
## ColorPrimitiveGray800

Source: `color_tokens.go:294`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray900"></a>
## ColorPrimitiveGray900

Source: `color_tokens.go:295`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray950"></a>
## ColorPrimitiveGray950

Source: `color_tokens.go:296`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc50"></a>
## ColorPrimitiveZinc50

Source: `color_tokens.go:297`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc100"></a>
## ColorPrimitiveZinc100

Source: `color_tokens.go:298`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc200"></a>
## ColorPrimitiveZinc200

Source: `color_tokens.go:299`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc300"></a>
## ColorPrimitiveZinc300

Source: `color_tokens.go:300`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc400"></a>
## ColorPrimitiveZinc400

Source: `color_tokens.go:301`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc500"></a>
## ColorPrimitiveZinc500

Source: `color_tokens.go:302`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc600"></a>
## ColorPrimitiveZinc600

Source: `color_tokens.go:303`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc700"></a>
## ColorPrimitiveZinc700

Source: `color_tokens.go:304`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc800"></a>
## ColorPrimitiveZinc800

Source: `color_tokens.go:305`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc900"></a>
## ColorPrimitiveZinc900

Source: `color_tokens.go:306`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivezinc950"></a>
## ColorPrimitiveZinc950

Source: `color_tokens.go:307`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral50"></a>
## ColorPrimitiveNeutral50

Source: `color_tokens.go:308`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral100"></a>
## ColorPrimitiveNeutral100

Source: `color_tokens.go:309`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral200"></a>
## ColorPrimitiveNeutral200

Source: `color_tokens.go:310`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral300"></a>
## ColorPrimitiveNeutral300

Source: `color_tokens.go:311`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral400"></a>
## ColorPrimitiveNeutral400

Source: `color_tokens.go:312`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral500"></a>
## ColorPrimitiveNeutral500

Source: `color_tokens.go:313`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral600"></a>
## ColorPrimitiveNeutral600

Source: `color_tokens.go:314`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral700"></a>
## ColorPrimitiveNeutral700

Source: `color_tokens.go:315`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral800"></a>
## ColorPrimitiveNeutral800

Source: `color_tokens.go:316`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral900"></a>
## ColorPrimitiveNeutral900

Source: `color_tokens.go:317`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveneutral950"></a>
## ColorPrimitiveNeutral950

Source: `color_tokens.go:318`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone50"></a>
## ColorPrimitiveStone50

Source: `color_tokens.go:319`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone100"></a>
## ColorPrimitiveStone100

Source: `color_tokens.go:320`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone200"></a>
## ColorPrimitiveStone200

Source: `color_tokens.go:321`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone300"></a>
## ColorPrimitiveStone300

Source: `color_tokens.go:322`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone400"></a>
## ColorPrimitiveStone400

Source: `color_tokens.go:323`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone500"></a>
## ColorPrimitiveStone500

Source: `color_tokens.go:324`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone600"></a>
## ColorPrimitiveStone600

Source: `color_tokens.go:325`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone700"></a>
## ColorPrimitiveStone700

Source: `color_tokens.go:326`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone800"></a>
## ColorPrimitiveStone800

Source: `color_tokens.go:327`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone900"></a>
## ColorPrimitiveStone900

Source: `color_tokens.go:328`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivestone950"></a>
## ColorPrimitiveStone950

Source: `color_tokens.go:329`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe50"></a>
## ColorPrimitiveTaupe50

Source: `color_tokens.go:330`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe100"></a>
## ColorPrimitiveTaupe100

Source: `color_tokens.go:331`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe200"></a>
## ColorPrimitiveTaupe200

Source: `color_tokens.go:332`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe300"></a>
## ColorPrimitiveTaupe300

Source: `color_tokens.go:333`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe400"></a>
## ColorPrimitiveTaupe400

Source: `color_tokens.go:334`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe500"></a>
## ColorPrimitiveTaupe500

Source: `color_tokens.go:335`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe600"></a>
## ColorPrimitiveTaupe600

Source: `color_tokens.go:336`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe700"></a>
## ColorPrimitiveTaupe700

Source: `color_tokens.go:337`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe800"></a>
## ColorPrimitiveTaupe800

Source: `color_tokens.go:338`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe900"></a>
## ColorPrimitiveTaupe900

Source: `color_tokens.go:339`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivetaupe950"></a>
## ColorPrimitiveTaupe950

Source: `color_tokens.go:340`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve50"></a>
## ColorPrimitiveMauve50

Source: `color_tokens.go:341`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve100"></a>
## ColorPrimitiveMauve100

Source: `color_tokens.go:342`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve200"></a>
## ColorPrimitiveMauve200

Source: `color_tokens.go:343`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve300"></a>
## ColorPrimitiveMauve300

Source: `color_tokens.go:344`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve400"></a>
## ColorPrimitiveMauve400

Source: `color_tokens.go:345`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve500"></a>
## ColorPrimitiveMauve500

Source: `color_tokens.go:346`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve600"></a>
## ColorPrimitiveMauve600

Source: `color_tokens.go:347`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve700"></a>
## ColorPrimitiveMauve700

Source: `color_tokens.go:348`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve800"></a>
## ColorPrimitiveMauve800

Source: `color_tokens.go:349`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve900"></a>
## ColorPrimitiveMauve900

Source: `color_tokens.go:350`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemauve950"></a>
## ColorPrimitiveMauve950

Source: `color_tokens.go:351`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist50"></a>
## ColorPrimitiveMist50

Source: `color_tokens.go:352`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist100"></a>
## ColorPrimitiveMist100

Source: `color_tokens.go:353`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist200"></a>
## ColorPrimitiveMist200

Source: `color_tokens.go:354`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist300"></a>
## ColorPrimitiveMist300

Source: `color_tokens.go:355`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist400"></a>
## ColorPrimitiveMist400

Source: `color_tokens.go:356`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist500"></a>
## ColorPrimitiveMist500

Source: `color_tokens.go:357`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist600"></a>
## ColorPrimitiveMist600

Source: `color_tokens.go:358`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist700"></a>
## ColorPrimitiveMist700

Source: `color_tokens.go:359`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist800"></a>
## ColorPrimitiveMist800

Source: `color_tokens.go:360`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist900"></a>
## ColorPrimitiveMist900

Source: `color_tokens.go:361`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivemist950"></a>
## ColorPrimitiveMist950

Source: `color_tokens.go:362`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive50"></a>
## ColorPrimitiveOlive50

Source: `color_tokens.go:363`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive100"></a>
## ColorPrimitiveOlive100

Source: `color_tokens.go:364`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive200"></a>
## ColorPrimitiveOlive200

Source: `color_tokens.go:365`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive300"></a>
## ColorPrimitiveOlive300

Source: `color_tokens.go:366`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive400"></a>
## ColorPrimitiveOlive400

Source: `color_tokens.go:367`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive500"></a>
## ColorPrimitiveOlive500

Source: `color_tokens.go:368`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive600"></a>
## ColorPrimitiveOlive600

Source: `color_tokens.go:369`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive700"></a>
## ColorPrimitiveOlive700

Source: `color_tokens.go:370`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive800"></a>
## ColorPrimitiveOlive800

Source: `color_tokens.go:371`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive900"></a>
## ColorPrimitiveOlive900

Source: `color_tokens.go:372`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveolive950"></a>
## ColorPrimitiveOlive950

Source: `color_tokens.go:373`

See the preceding constant block for the exact value and type.
