# font.go

Exact source declarations and comments. Private fields and function bodies are omitted.

<a id="api-fontfamily"></a>
## FontFamily

Source: `font.go:17`

```text
FontFamily is an application-visible family name used for deterministic
ordered fallback. It is not an operating-system font handle.
```

```go
type FontFamily string
```

<a id="api-fontfamilydefault"></a>
## FontFamilyDefault

Source: `font.go:22`

```text
FontFamilyDefault is dxui's embedded, BSD-licensed Go Regular font. It
covers the MVP Latin samples but not CJK.
```

```go
const (
	// FontFamilyDefault is dxui's embedded, BSD-licensed Go Regular font. It
	// covers the MVP Latin samples but not CJK.
	FontFamilyDefault FontFamily = internaltext.BuiltinFamily
	// FontFamilySystemSans resolves one fixed candidate list per operating
	// system; it is never searched by fuzzy display name.
	FontFamilySystemSans FontFamily = "system-ui"
	// FontFamilySystemMono is the deterministic system monospace family.
	FontFamilySystemMono FontFamily = "system-monospace"
	// FontFamilySystemCJK is the deterministic system CJK fallback family.
	FontFamilySystemCJK FontFamily = "system-cjk"
)
```

<a id="api-fontfamilysystemsans"></a>
## FontFamilySystemSans

Source: `font.go:25`

```text
FontFamilySystemSans resolves one fixed candidate list per operating
system; it is never searched by fuzzy display name.
```

See the preceding constant block for the exact value and type.

<a id="api-fontfamilysystemmono"></a>
## FontFamilySystemMono

Source: `font.go:27`

```text
FontFamilySystemMono is the deterministic system monospace family.
```

See the preceding constant block for the exact value and type.

<a id="api-fontfamilysystemcjk"></a>
## FontFamilySystemCJK

Source: `font.go:29`

```text
FontFamilySystemCJK is the deterministic system CJK fallback family.
```

See the preceding constant block for the exact value and type.

<a id="api-font"></a>
## Font

Source: `font.go:52`

```text
Font registers one TTF/OTF/TTC face. A FontBytes value owns its copied bytes
for as long as that value or an App configured with it remains reachable.
FontFile handles and all parsed faces live only from App.Run text startup until
renderer teardown completes. The file is not copied into the Go heap.
FaceIndex selects a collection face and is zero
for ordinary fonts.
```

```go
type Font struct {
	Family    FontFamily
	Weight    FontWeight
	Slant     FontSlant
	FaceIndex int
}
```

<a id="api-fontbytes"></a>
## FontBytes

Source: `font.go:61`

```text
FontBytes creates an application-owned font from a defensive copy of data.
```

```go
func FontBytes(family FontFamily, data []byte) Font
```

<a id="api-fontfile"></a>
## FontFile

Source: `font.go:67`

```text
FontFile creates a font loaded from the exact path during App.Run startup.
dxui does not search or copy the file into an application package.
```

```go
func FontFile(family FontFamily, path string) Font
```

<a id="api-systemfont"></a>
## SystemFont

Source: `font.go:74`

```text
SystemFont requests one of the documented generic system families. The
resolver tests a fixed path list for the current OS and returns a startup
error when none exists; it never depends on fontconfig or fuzzy name search.
```

```go
func SystemFont(family FontFamily) Font
```
