# button.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-buttonvariant"></a>
## ButtonVariant

Source: `button.go:10`

```text
ButtonVariant selects a Button's surface and border recipe.
```

```go
type ButtonVariant uint8
```

<a id="api-buttonfilled"></a>
## ButtonFilled

Source: `button.go:13`

```go
const (
	ButtonFilled ButtonVariant = iota // Filled is the compatible default.
	ButtonSoft
	ButtonOutline
	ButtonDashed
	ButtonGhost
	ButtonLink // Link is an action, with compact spacing; it never navigates.
)
```

<a id="api-buttonsoft"></a>
## ButtonSoft

Source: `button.go:14`

See the preceding constant block for the exact value and type.

<a id="api-buttonoutline"></a>
## ButtonOutline

Source: `button.go:15`

See the preceding constant block for the exact value and type.

<a id="api-buttondashed"></a>
## ButtonDashed

Source: `button.go:16`

See the preceding constant block for the exact value and type.

<a id="api-buttonghost"></a>
## ButtonGhost

Source: `button.go:17`

See the preceding constant block for the exact value and type.

<a id="api-buttonlink"></a>
## ButtonLink

Source: `button.go:18`

See the preceding constant block for the exact value and type.

<a id="api-buttontone"></a>
## ButtonTone

Source: `button.go:22`

```text
ButtonTone selects semantic colors independently of the surface recipe.
```

```go
type ButtonTone uint8
```

<a id="api-buttonprimary"></a>
## ButtonPrimary

Source: `button.go:25`

```go
const (
	ButtonPrimary ButtonTone = iota
	ButtonSecondary
	ButtonSuccess
	ButtonInfo
	ButtonWarn
	ButtonDanger
)
```

<a id="api-buttonsecondary"></a>
## ButtonSecondary

Source: `button.go:26`

See the preceding constant block for the exact value and type.

<a id="api-buttonsuccess"></a>
## ButtonSuccess

Source: `button.go:27`

See the preceding constant block for the exact value and type.

<a id="api-buttoninfo"></a>
## ButtonInfo

Source: `button.go:28`

See the preceding constant block for the exact value and type.

<a id="api-buttonwarn"></a>
## ButtonWarn

Source: `button.go:29`

See the preceding constant block for the exact value and type.

<a id="api-buttondanger"></a>
## ButtonDanger

Source: `button.go:30`

See the preceding constant block for the exact value and type.

<a id="api-buttondefault"></a>
## ButtonDefault

Source: `button.go:34`

```text
ButtonDefault is an alias for the zero-value Primary tone.
```

```go
// ButtonDefault is an alias for the zero-value Primary tone.
const ButtonDefault = ButtonPrimary
```

<a id="api-buttonsize"></a>
## ButtonSize

Source: `button.go:37`

```text
ButtonSize selects overridable padding, minimum height, and inherited text metrics.
```

```go
type ButtonSize uint8
```

<a id="api-buttonnormal"></a>
## ButtonNormal

Source: `button.go:40`

```go
const (
	ButtonNormal ButtonSize = iota
	ButtonSmall
	ButtonLarge
)
```

<a id="api-buttonsmall"></a>
## ButtonSmall

Source: `button.go:41`

See the preceding constant block for the exact value and type.

<a id="api-buttonlarge"></a>
## ButtonLarge

Source: `button.go:42`

See the preceding constant block for the exact value and type.
