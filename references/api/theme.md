# theme.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-colorprimitivewhite"></a>
## ColorPrimitiveWhite

Source: `theme.go:4`

```go
const (
	ColorPrimitiveWhite              ColorToken = "primitive.white"
	ColorPrimitiveBlack              ColorToken = "primitive.black"
	ColorPrimitiveBlue               ColorToken = "primitive.blue"
	ColorPrimitiveGray               ColorToken = "primitive.gray"
	ColorSemanticSurface             ColorToken = "semantic.surface"
	ColorSemanticSurfaceHi           ColorToken = "semantic.surface.high"
	ColorSemanticText                ColorToken = "semantic.text"
	ColorSemanticAccent              ColorToken = "semantic.accent"
	ColorSemanticAccentHover         ColorToken = "semantic.accent.hover"
	ColorSemanticOnAccent            ColorToken = "semantic.on-accent"
	ColorSemanticFocusRing           ColorToken = "semantic.focus-ring"
	ColorSemanticDanger              ColorToken = "semantic.danger"
	ColorSemanticSuccess             ColorToken = "semantic.success"
	ColorSemanticInfo                ColorToken = "semantic.info"
	ColorSemanticWarn                ColorToken = "semantic.warn"
	ColorSemanticBorder              ColorToken = "semantic.border"
	ColorSemanticShadow              ColorToken = "semantic.shadow"
	ColorSemanticScrollTrack         ColorToken = "semantic.scroll-track"
	ColorSemanticScrollThumb         ColorToken = "semantic.scroll-thumb"
	ColorSemanticScrollThumbHover    ColorToken = "semantic.scroll-thumb-hover"
	ColorSemanticScrollThumbActive   ColorToken = "semantic.scroll-thumb-active"
	ColorSemanticScrollThumbDisabled ColorToken = "semantic.scroll-thumb-disabled"
	ColorSemanticSelectHover         ColorToken = "semantic.select-hover"
	ColorSemanticSelectSelected      ColorToken = "semantic.select-selected"
	ColorSemanticSelectDisabled      ColorToken = "semantic.select-disabled"
	ColorSemanticSliderTrack         ColorToken = "semantic.slider-track"
	ColorSemanticSliderFill          ColorToken = "semantic.slider-fill"
	ColorSemanticSliderThumb         ColorToken = "semantic.slider-thumb"
	ColorSemanticSliderThumbBorder   ColorToken = "semantic.slider-thumb-border"
	ColorSemanticProgressTrack       ColorToken = "semantic.progress-track"
	ColorSemanticProgressFill        ColorToken = "semantic.progress-fill"
	ColorSemanticTabsHover           ColorToken = "semantic.tabs-hover"
	ColorSemanticTabsPressed         ColorToken = "semantic.tabs-pressed"
	ColorSemanticTabsSelected        ColorToken = "semantic.tabs-selected"
	ColorSemanticTabsDisabled        ColorToken = "semantic.tabs-disabled"
	ColorSemanticTabsIndicator       ColorToken = "semantic.tabs-indicator"
	ColorSemanticMenuHover           ColorToken = "semantic.menu-hover"
	ColorSemanticMenuActive          ColorToken = "semantic.menu-active"
	ColorSemanticMenuSelected        ColorToken = "semantic.menu-selected"
	ColorSemanticMenuPressed         ColorToken = "semantic.menu-pressed"
	ColorSemanticMenuDisabled        ColorToken = "semantic.menu-disabled"

	MetricPrimitive0                      MetricToken = "primitive.0"
	MetricPrimitive1                      MetricToken = "primitive.1"
	MetricPrimitive2                      MetricToken = "primitive.2"
	MetricSemanticRadius                  MetricToken = "semantic.radius"
	MetricSemanticBorder                  MetricToken = "semantic.border-width"
	MetricSemanticShadow                  MetricToken = "semantic.shadow-blur"
	MetricSemanticTextSize                MetricToken = "semantic.text-size"
	MetricSemanticLineHeight              MetricToken = "semantic.line-height"
	MetricSemanticControlHeight           MetricToken = "semantic.control-height"
	MetricComponentButtonPaddingX         MetricToken = "component.button.padding-x"
	MetricComponentButtonPaddingY         MetricToken = "component.button.padding-y"
	MetricComponentButtonGroupBorderWidth MetricToken = "component.button-group.border-width"
	MetricComponentButtonGroupRadius      MetricToken = "component.button-group.radius"
	MetricComponentBadgePaddingX          MetricToken = "component.badge.padding-x"
	MetricComponentBadgePaddingY          MetricToken = "component.badge.padding-y"
	MetricComponentBadgeMinHeight         MetricToken = "component.badge.min-height"
	MetricComponentBadgeRadius            MetricToken = "component.badge.radius"
	MetricComponentInputPaddingX          MetricToken = "component.input.padding-x"
	MetricComponentInputPaddingY          MetricToken = "component.input.padding-y"
	MetricComponentInputGroupPaddingX     MetricToken = "component.input-group.padding-x"
	MetricComponentInputGroupGap          MetricToken = "component.input-group.gap"
	MetricComponentTextareaMinHeight      MetricToken = "component.textarea.min-height"
	MetricComponentToggleWidth            MetricToken = "component.toggle.width"
	MetricComponentToggleHeight           MetricToken = "component.toggle.height"
	MetricComponentToggleKnobInset        MetricToken = "component.toggle.knob-inset"
	MetricComponentSliderWidth            MetricToken = "component.slider.width"
	MetricComponentSliderHeight           MetricToken = "component.slider.height"
	MetricComponentSliderTrackHeight      MetricToken = "component.slider.track-height"
	MetricComponentSliderThumbSize        MetricToken = "component.slider.thumb-size"
	MetricComponentProgressBarWidth       MetricToken = "component.progress-bar.width"
	MetricComponentProgressBarHeight      MetricToken = "component.progress-bar.height"
	MetricComponentProgressBarTrackHeight MetricToken = "component.progress-bar.track-height"
	MetricComponentProgressBarRadius      MetricToken = "component.progress-bar.radius"
	MetricComponentCheckboxSize           MetricToken = "component.checkbox.size"
	MetricComponentCheckboxGap            MetricToken = "component.checkbox.gap"
	MetricComponentRadioSize              MetricToken = "component.radio.size"
	MetricComponentRadioGap               MetricToken = "component.radio.gap"
	MetricComponentIconSize               MetricToken = "component.icon.size"
	MetricComponentAvatarSize             MetricToken = "component.avatar.size"
	MetricComponentScrollThickness        MetricToken = "component.scroll.thickness"
	MetricComponentScrollMinThumb         MetricToken = "component.scroll.min-thumb"
	MetricComponentScrollInset            MetricToken = "component.scroll.inset"
	MetricComponentSelectPaddingX         MetricToken = "component.select.padding-x"
	MetricComponentSelectPaddingY         MetricToken = "component.select.padding-y"
	MetricComponentSelectItemHeight       MetricToken = "component.select.item-height"
	MetricComponentSelectMaxHeight        MetricToken = "component.select.max-height"
	MetricComponentSelectGap              MetricToken = "component.select.gap"
	MetricComponentPopoverPaddingX        MetricToken = "component.popover.padding-x"
	MetricComponentPopoverPaddingY        MetricToken = "component.popover.padding-y"
	MetricComponentPopoverGap             MetricToken = "component.popover.gap"
	MetricComponentTooltipPaddingX        MetricToken = "component.tooltip.padding-x"
	MetricComponentTooltipPaddingY        MetricToken = "component.tooltip.padding-y"
	MetricComponentTooltipGap             MetricToken = "component.tooltip.gap"
	MetricComponentTabsHeight             MetricToken = "component.tabs.height"
	MetricComponentTabsGap                MetricToken = "component.tabs.gap"
	MetricComponentTabsPaddingX           MetricToken = "component.tabs.padding-x"
	MetricComponentTabsPaddingY           MetricToken = "component.tabs.padding-y"
	MetricComponentTabsIndicator          MetricToken = "component.tabs.indicator-height"
	MetricComponentTabsIndicatorInset     MetricToken = "component.tabs.indicator-inset"
	MetricComponentMenuItemHeight         MetricToken = "component.menu.item-height"
	MetricComponentMenuGap                MetricToken = "component.menu.gap"
	MetricComponentMenuPaddingX           MetricToken = "component.menu.padding-x"
	MetricComponentMenuPaddingY           MetricToken = "component.menu.padding-y"

	ComponentPanel           ComponentToken = "panel"
	ComponentText            ComponentToken = "text"
	ComponentButton          ComponentToken = "button"
	ComponentButtonSecondary ComponentToken = "button.secondary"
	ComponentButtonDanger    ComponentToken = "button.danger"
	ComponentButtonGhost     ComponentToken = "button.ghost"
	ComponentButtonGroup     ComponentToken = "button-group"
	ComponentBadge           ComponentToken = "badge"
	ComponentInput           ComponentToken = "input"
	ComponentInputGroup      ComponentToken = "input-group"
	ComponentToggleSwitch    ComponentToken = "toggle-switch"
	ComponentSlider          ComponentToken = "slider"
	ComponentProgressBar     ComponentToken = "progress-bar"
	ComponentCheckbox        ComponentToken = "checkbox"
	ComponentRadio           ComponentToken = "radio"
	ComponentIcon            ComponentToken = "icon"
	ComponentImage           ComponentToken = "image"
	ComponentAvatar          ComponentToken = "avatar"
	ComponentScroll          ComponentToken = "scroll"
	ComponentSelect          ComponentToken = "select"
	ComponentTabs            ComponentToken = "tabs"
	ComponentMenu            ComponentToken = "menu"
	ComponentPopover         ComponentToken = "popover"
	ComponentTooltip         ComponentToken = "tooltip"
)
```

<a id="api-colorprimitiveblack"></a>
## ColorPrimitiveBlack

Source: `theme.go:5`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitiveblue"></a>
## ColorPrimitiveBlue

Source: `theme.go:6`

See the preceding constant block for the exact value and type.

<a id="api-colorprimitivegray"></a>
## ColorPrimitiveGray

Source: `theme.go:7`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsurface"></a>
## ColorSemanticSurface

Source: `theme.go:8`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsurfacehi"></a>
## ColorSemanticSurfaceHi

Source: `theme.go:9`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictext"></a>
## ColorSemanticText

Source: `theme.go:10`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticaccent"></a>
## ColorSemanticAccent

Source: `theme.go:11`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticaccenthover"></a>
## ColorSemanticAccentHover

Source: `theme.go:12`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticonaccent"></a>
## ColorSemanticOnAccent

Source: `theme.go:13`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticfocusring"></a>
## ColorSemanticFocusRing

Source: `theme.go:14`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticdanger"></a>
## ColorSemanticDanger

Source: `theme.go:15`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsuccess"></a>
## ColorSemanticSuccess

Source: `theme.go:16`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticinfo"></a>
## ColorSemanticInfo

Source: `theme.go:17`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticwarn"></a>
## ColorSemanticWarn

Source: `theme.go:18`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticborder"></a>
## ColorSemanticBorder

Source: `theme.go:19`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticshadow"></a>
## ColorSemanticShadow

Source: `theme.go:20`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticscrolltrack"></a>
## ColorSemanticScrollTrack

Source: `theme.go:21`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticscrollthumb"></a>
## ColorSemanticScrollThumb

Source: `theme.go:22`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticscrollthumbhover"></a>
## ColorSemanticScrollThumbHover

Source: `theme.go:23`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticscrollthumbactive"></a>
## ColorSemanticScrollThumbActive

Source: `theme.go:24`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticscrollthumbdisabled"></a>
## ColorSemanticScrollThumbDisabled

Source: `theme.go:25`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticselecthover"></a>
## ColorSemanticSelectHover

Source: `theme.go:26`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticselectselected"></a>
## ColorSemanticSelectSelected

Source: `theme.go:27`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticselectdisabled"></a>
## ColorSemanticSelectDisabled

Source: `theme.go:28`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticslidertrack"></a>
## ColorSemanticSliderTrack

Source: `theme.go:29`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsliderfill"></a>
## ColorSemanticSliderFill

Source: `theme.go:30`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsliderthumb"></a>
## ColorSemanticSliderThumb

Source: `theme.go:31`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticsliderthumbborder"></a>
## ColorSemanticSliderThumbBorder

Source: `theme.go:32`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticprogresstrack"></a>
## ColorSemanticProgressTrack

Source: `theme.go:33`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticprogressfill"></a>
## ColorSemanticProgressFill

Source: `theme.go:34`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictabshover"></a>
## ColorSemanticTabsHover

Source: `theme.go:35`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictabspressed"></a>
## ColorSemanticTabsPressed

Source: `theme.go:36`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictabsselected"></a>
## ColorSemanticTabsSelected

Source: `theme.go:37`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictabsdisabled"></a>
## ColorSemanticTabsDisabled

Source: `theme.go:38`

See the preceding constant block for the exact value and type.

<a id="api-colorsemantictabsindicator"></a>
## ColorSemanticTabsIndicator

Source: `theme.go:39`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticmenuhover"></a>
## ColorSemanticMenuHover

Source: `theme.go:40`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticmenuactive"></a>
## ColorSemanticMenuActive

Source: `theme.go:41`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticmenuselected"></a>
## ColorSemanticMenuSelected

Source: `theme.go:42`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticmenupressed"></a>
## ColorSemanticMenuPressed

Source: `theme.go:43`

See the preceding constant block for the exact value and type.

<a id="api-colorsemanticmenudisabled"></a>
## ColorSemanticMenuDisabled

Source: `theme.go:44`

See the preceding constant block for the exact value and type.

<a id="api-metricprimitive0"></a>
## MetricPrimitive0

Source: `theme.go:46`

See the preceding constant block for the exact value and type.

<a id="api-metricprimitive1"></a>
## MetricPrimitive1

Source: `theme.go:47`

See the preceding constant block for the exact value and type.

<a id="api-metricprimitive2"></a>
## MetricPrimitive2

Source: `theme.go:48`

See the preceding constant block for the exact value and type.

<a id="api-metricsemanticradius"></a>
## MetricSemanticRadius

Source: `theme.go:49`

See the preceding constant block for the exact value and type.

<a id="api-metricsemanticborder"></a>
## MetricSemanticBorder

Source: `theme.go:50`

See the preceding constant block for the exact value and type.

<a id="api-metricsemanticshadow"></a>
## MetricSemanticShadow

Source: `theme.go:51`

See the preceding constant block for the exact value and type.

<a id="api-metricsemantictextsize"></a>
## MetricSemanticTextSize

Source: `theme.go:52`

See the preceding constant block for the exact value and type.

<a id="api-metricsemanticlineheight"></a>
## MetricSemanticLineHeight

Source: `theme.go:53`

See the preceding constant block for the exact value and type.

<a id="api-metricsemanticcontrolheight"></a>
## MetricSemanticControlHeight

Source: `theme.go:54`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbuttonpaddingx"></a>
## MetricComponentButtonPaddingX

Source: `theme.go:55`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbuttonpaddingy"></a>
## MetricComponentButtonPaddingY

Source: `theme.go:56`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbuttongroupborderwidth"></a>
## MetricComponentButtonGroupBorderWidth

Source: `theme.go:57`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbuttongroupradius"></a>
## MetricComponentButtonGroupRadius

Source: `theme.go:58`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbadgepaddingx"></a>
## MetricComponentBadgePaddingX

Source: `theme.go:59`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbadgepaddingy"></a>
## MetricComponentBadgePaddingY

Source: `theme.go:60`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbadgeminheight"></a>
## MetricComponentBadgeMinHeight

Source: `theme.go:61`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentbadgeradius"></a>
## MetricComponentBadgeRadius

Source: `theme.go:62`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentinputpaddingx"></a>
## MetricComponentInputPaddingX

Source: `theme.go:63`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentinputpaddingy"></a>
## MetricComponentInputPaddingY

Source: `theme.go:64`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentinputgrouppaddingx"></a>
## MetricComponentInputGroupPaddingX

Source: `theme.go:65`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentinputgroupgap"></a>
## MetricComponentInputGroupGap

Source: `theme.go:66`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttextareaminheight"></a>
## MetricComponentTextareaMinHeight

Source: `theme.go:67`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttogglewidth"></a>
## MetricComponentToggleWidth

Source: `theme.go:68`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttoggleheight"></a>
## MetricComponentToggleHeight

Source: `theme.go:69`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttoggleknobinset"></a>
## MetricComponentToggleKnobInset

Source: `theme.go:70`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentsliderwidth"></a>
## MetricComponentSliderWidth

Source: `theme.go:71`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentsliderheight"></a>
## MetricComponentSliderHeight

Source: `theme.go:72`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentslidertrackheight"></a>
## MetricComponentSliderTrackHeight

Source: `theme.go:73`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentsliderthumbsize"></a>
## MetricComponentSliderThumbSize

Source: `theme.go:74`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentprogressbarwidth"></a>
## MetricComponentProgressBarWidth

Source: `theme.go:75`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentprogressbarheight"></a>
## MetricComponentProgressBarHeight

Source: `theme.go:76`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentprogressbartrackheight"></a>
## MetricComponentProgressBarTrackHeight

Source: `theme.go:77`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentprogressbarradius"></a>
## MetricComponentProgressBarRadius

Source: `theme.go:78`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentcheckboxsize"></a>
## MetricComponentCheckboxSize

Source: `theme.go:79`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentcheckboxgap"></a>
## MetricComponentCheckboxGap

Source: `theme.go:80`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentradiosize"></a>
## MetricComponentRadioSize

Source: `theme.go:81`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentradiogap"></a>
## MetricComponentRadioGap

Source: `theme.go:82`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenticonsize"></a>
## MetricComponentIconSize

Source: `theme.go:83`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentavatarsize"></a>
## MetricComponentAvatarSize

Source: `theme.go:84`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentscrollthickness"></a>
## MetricComponentScrollThickness

Source: `theme.go:85`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentscrollminthumb"></a>
## MetricComponentScrollMinThumb

Source: `theme.go:86`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentscrollinset"></a>
## MetricComponentScrollInset

Source: `theme.go:87`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentselectpaddingx"></a>
## MetricComponentSelectPaddingX

Source: `theme.go:88`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentselectpaddingy"></a>
## MetricComponentSelectPaddingY

Source: `theme.go:89`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentselectitemheight"></a>
## MetricComponentSelectItemHeight

Source: `theme.go:90`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentselectmaxheight"></a>
## MetricComponentSelectMaxHeight

Source: `theme.go:91`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentselectgap"></a>
## MetricComponentSelectGap

Source: `theme.go:92`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentpopoverpaddingx"></a>
## MetricComponentPopoverPaddingX

Source: `theme.go:93`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentpopoverpaddingy"></a>
## MetricComponentPopoverPaddingY

Source: `theme.go:94`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentpopovergap"></a>
## MetricComponentPopoverGap

Source: `theme.go:95`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttooltippaddingx"></a>
## MetricComponentTooltipPaddingX

Source: `theme.go:96`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttooltippaddingy"></a>
## MetricComponentTooltipPaddingY

Source: `theme.go:97`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttooltipgap"></a>
## MetricComponentTooltipGap

Source: `theme.go:98`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabsheight"></a>
## MetricComponentTabsHeight

Source: `theme.go:99`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabsgap"></a>
## MetricComponentTabsGap

Source: `theme.go:100`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabspaddingx"></a>
## MetricComponentTabsPaddingX

Source: `theme.go:101`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabspaddingy"></a>
## MetricComponentTabsPaddingY

Source: `theme.go:102`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabsindicator"></a>
## MetricComponentTabsIndicator

Source: `theme.go:103`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponenttabsindicatorinset"></a>
## MetricComponentTabsIndicatorInset

Source: `theme.go:104`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentmenuitemheight"></a>
## MetricComponentMenuItemHeight

Source: `theme.go:105`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentmenugap"></a>
## MetricComponentMenuGap

Source: `theme.go:106`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentmenupaddingx"></a>
## MetricComponentMenuPaddingX

Source: `theme.go:107`

See the preceding constant block for the exact value and type.

<a id="api-metriccomponentmenupaddingy"></a>
## MetricComponentMenuPaddingY

Source: `theme.go:108`

See the preceding constant block for the exact value and type.

<a id="api-componentpanel"></a>
## ComponentPanel

Source: `theme.go:110`

See the preceding constant block for the exact value and type.

<a id="api-componenttext"></a>
## ComponentText

Source: `theme.go:111`

See the preceding constant block for the exact value and type.

<a id="api-componentbutton"></a>
## ComponentButton

Source: `theme.go:112`

See the preceding constant block for the exact value and type.

<a id="api-componentbuttonsecondary"></a>
## ComponentButtonSecondary

Source: `theme.go:113`

See the preceding constant block for the exact value and type.

<a id="api-componentbuttondanger"></a>
## ComponentButtonDanger

Source: `theme.go:114`

See the preceding constant block for the exact value and type.

<a id="api-componentbuttonghost"></a>
## ComponentButtonGhost

Source: `theme.go:115`

See the preceding constant block for the exact value and type.

<a id="api-componentbuttongroup"></a>
## ComponentButtonGroup

Source: `theme.go:116`

See the preceding constant block for the exact value and type.

<a id="api-componentbadge"></a>
## ComponentBadge

Source: `theme.go:117`

See the preceding constant block for the exact value and type.

<a id="api-componentinput"></a>
## ComponentInput

Source: `theme.go:118`

See the preceding constant block for the exact value and type.

<a id="api-componentinputgroup"></a>
## ComponentInputGroup

Source: `theme.go:119`

See the preceding constant block for the exact value and type.

<a id="api-componenttoggleswitch"></a>
## ComponentToggleSwitch

Source: `theme.go:120`

See the preceding constant block for the exact value and type.

<a id="api-componentslider"></a>
## ComponentSlider

Source: `theme.go:121`

See the preceding constant block for the exact value and type.

<a id="api-componentprogressbar"></a>
## ComponentProgressBar

Source: `theme.go:122`

See the preceding constant block for the exact value and type.

<a id="api-componentcheckbox"></a>
## ComponentCheckbox

Source: `theme.go:123`

See the preceding constant block for the exact value and type.

<a id="api-componentradio"></a>
## ComponentRadio

Source: `theme.go:124`

See the preceding constant block for the exact value and type.

<a id="api-componenticon"></a>
## ComponentIcon

Source: `theme.go:125`

See the preceding constant block for the exact value and type.

<a id="api-componentimage"></a>
## ComponentImage

Source: `theme.go:126`

See the preceding constant block for the exact value and type.

<a id="api-componentavatar"></a>
## ComponentAvatar

Source: `theme.go:127`

See the preceding constant block for the exact value and type.

<a id="api-componentscroll"></a>
## ComponentScroll

Source: `theme.go:128`

See the preceding constant block for the exact value and type.

<a id="api-componentselect"></a>
## ComponentSelect

Source: `theme.go:129`

See the preceding constant block for the exact value and type.

<a id="api-componenttabs"></a>
## ComponentTabs

Source: `theme.go:130`

See the preceding constant block for the exact value and type.

<a id="api-componentmenu"></a>
## ComponentMenu

Source: `theme.go:131`

See the preceding constant block for the exact value and type.

<a id="api-componentpopover"></a>
## ComponentPopover

Source: `theme.go:132`

See the preceding constant block for the exact value and type.

<a id="api-componenttooltip"></a>
## ComponentTooltip

Source: `theme.go:133`

See the preceding constant block for the exact value and type.

<a id="api-lighttheme"></a>
## LightTheme

Source: `theme.go:138`

```text
LightTheme returns an independent, mutable-by-the-caller light theme value.
App.SetTheme copies it before use.
```

```go
func LightTheme() Theme
```

<a id="api-darktheme"></a>
## DarkTheme

Source: `theme.go:143`

```text
DarkTheme returns an independent, mutable-by-the-caller dark theme value.
```

```go
func DarkTheme() Theme
```
